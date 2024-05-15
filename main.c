#include <stdio.h>

#ifndef N
#error no defined size
#endif

int main(void)
{
    int a[N];
    a[0] = 123;
    printf("%d \n", a[0]);
    return 0;
}
