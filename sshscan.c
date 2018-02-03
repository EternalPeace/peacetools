#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/select.h>
#include <sys/types.h>
#include <time.h>
#include <fcntl.h>
#include <signal.h>
#include <errno.h>
#include <string.h>
#include <linux/ip.h>
#include <linux/tcp.h>

#define INET_ADDR(o1,o2,o3,o4) (htonl((o1 << 24) | (o2 << 16) | (o3 << 8) | (o4 << 0)))

#define FALSE   0
#define TRUE    1
#define MAXSEND 1		//一次发送　ＳＳＨ探测次数

#define DEBUG 1
static uint32_t x, y, z, w;
typedef uint32_t ipv4_t;


void
rand_init (void)
{
  x = time (NULL);
  y = getpid () ^ getppid ();
  z = clock ();
  w = z ^ y;
}

uint32_t
rand_next (void)		//period 2^96-1
{
  uint32_t t = x;
  t ^= t << 11;
  t ^= t >> 8;
  x = y;
  y = z;
  z = w;
  w ^= w >> 19;
  w ^= t;
  return w;
}

get_random_ip (char *buffer)
{
  uint32_t tmp;
  uint8_t o1, o2, o3, o4;

  do
    {
      tmp = rand_next ();
      o1 = tmp & 0xff;
      o2 = (tmp >> 8) & 0xff;
      o3 = (tmp >> 16) & 0xff;
      o4 = (tmp >> 24) & 0xff;
    }
  while (o1 == 127 ||		// 127.0.0.0/8      - Loopback
	 (o1 == 0) ||		// 0.0.0.0/8        - Invalid address space
	 (o1 == 3) ||		// 3.0.0.0/8        - General Electric Company
	 (o1 == 15 || o1 == 16) ||	// 15.0.0.0/7       - Hewlett-Packard Company
	 (o1 == 56) ||		// 56.0.0.0/8       - US Postal Service
	 (o1 == 10) ||		// 10.0.0.0/8       - Internal network
	 (o1 == 192 && o2 == 168) ||	// 192.168.0.0/16   - Internal network
	 (o1 == 172 && o2 >= 16 && o2 < 32) ||	// 172.16.0.0/14    - Internal network
	 (o1 == 100 && o2 >= 64 && o2 < 127) ||	// 100.64.0.0/10    - IANA NAT reserved
	 (o1 == 169 && o2 > 254) ||	// 169.254.0.0/16   - IANA NAT reserved
	 (o1 == 198 && o2 >= 18 && o2 < 20) ||	// 198.18.0.0/15    - IANA Special use
	 (o1 >= 224) ||		// 224.*.*.*+       - Multicast
	 (o1 == 6 || o1 == 7 || o1 == 11 || o1 == 21 || o1 == 22 || o1 == 26 || o1 == 28 || o1 == 29 || o1 == 30 || o1 == 33 || o1 == 55 || o1 == 214 || o1 == 215)	// Department of Defense
    );

  sprintf (buffer, "%d.%d.%d.%d\0", o1, o2, o3, o4);

  return buffer;
}

void
main ()
{
  int i;
  char ip[100] = { 0 };//store ip 
  char shell[200]; //shell　cmd
  rand_init ();
  // while (TRUE) {
  for (i = 0; i <= MAXSEND; i++)
    {
      get_random_ip (ip);
      printf ("%s\n", ip);
    }

  //sprintf( shell, "ssh %s root@%s", ip  );
  sprintf (shell, "ls");
  system (shell);



  //wait to brust
//  }
  exit;
}
