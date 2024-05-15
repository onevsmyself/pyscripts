#include <stdio.h>

#ifndef N
#error no defined size
#endif

int main(void)
{
    int a[N];
    a[0] = 123;
    a[N - 1] = a[0] + 53;
    printf("%d %d \n", a[0], a[N-1]);
    return 0;
}
