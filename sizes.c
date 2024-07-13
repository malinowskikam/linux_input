#include <stdio.h>
#include <sys/time.h>
#include <linux/input.h>

int main() {
    printf("sizeof input_event: %lu\n", sizeof(struct input_event));
    
    printf("sizeof timeval: %lu\n", sizeof(struct timeval));
    printf("sizeof time_t: %lu\n", sizeof(time_t));
    printf("sizeof suseconds_t: %lu\n", sizeof(suseconds_t));
    
    return 0;
}