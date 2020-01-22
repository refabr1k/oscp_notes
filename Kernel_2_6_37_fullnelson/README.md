# Kernel 2.6.37 Full Nelson
source: `searchsploit -m exploits/linux/local/18411.c`

If encounter compilation errors like:
```c
' error: ‘CLONE_VM’ undeclared (first use in this function); did you mean ‘CLNEXT’'
```

Fix it by including the following statements in code:
```c
#define _GNU_SOURCE     
#include <sched.h>
```

Compile:
```bash
gcc 18411.c -o exploit
```
