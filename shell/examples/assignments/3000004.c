// written by 3000004@cse.unsw.edu.au (copied from 3000000.c and variable names changed)

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <possiblePrime>\n",argv[0]);
        return 1;  // could also call exit
    }
    
    int possiblePrime = atoi(argv[1]);
    int myCount;
    for (myCount = 2; myCount < possiblePrime; myCount++) 
        if (possiblePrime % myCount == 0) {
            printf("%d is not prime\n", possiblePrime);
            return 0;
        }
    printf("%d is prime\n", possiblePrime);
    return 0;
}
