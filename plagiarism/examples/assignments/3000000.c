// written by andrewt@cse.unsw.edu.au

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n",argv[0]);
        return 1;  // could also call exit
    }
    
    int number = atoi(argv[1]);
    int counter;
    for (counter = 2; counter < number; counter++) 
        if (number % counter == 0) {
            printf("%d is not prime\n", number);
            return 0;
        }
    printf("%d is prime\n", number);
    return 0;
}
