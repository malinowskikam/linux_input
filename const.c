#include <stdio.h>
#include <linux/input.h>

int main() {
    printf("EV_KEY: %d\n", EV_KEY);
    printf("EV_ABS: %d\n", EV_ABS);
    
    return 0;
}