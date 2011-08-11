// written by andrewt@cse.unsw.edu.au

#include <stdio.h>
#include <stdlib.h>

int rprime(int x, int n);

int
rprime(int x, int n) {
    return x < n && (n % x == 0 || rprime(x+1, n));
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n",argv[0]);
        return 1;  // could also call exit
    }
    int number = atoi(argv[1]);
    printf("%d is %sprime\n", number, rprime(2, number) ? "" : "not ");
    return 0;
}
