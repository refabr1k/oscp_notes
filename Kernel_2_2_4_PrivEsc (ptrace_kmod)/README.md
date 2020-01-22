# Linux Kernel 2.2-4 PrivEsc (ptrace-kmod)

source: https://www.exploit-db.com/exploits/3

Works for 2.2.x and 2.4.x kernels.
```c
// include <linux/user.h> <---remove this
// add below 
#include <sys/user.h>
#include <sys/reg.h>
```
