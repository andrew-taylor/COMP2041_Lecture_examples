// Written by andrewt@cse.unsw.edu.au
// as a COMP2041 lecture example
// July 2010

#include <stdio.h>
#include <stdlib.h>

void
output_file(FILE *in) {
    while (1) {
        int ch = fgetc(in);
        if (ch == EOF)
             break;
        if (fputc(ch, stdout) == EOF) {
            fprintf(stderr, "cat:");
            perror("");
            exit(1);
        }
    }
}

int
main(int argc, char *argv[]) {
    if (argc == 1) 
        output_file(stdin);
    else
        for (int i = 1; i < argc; i++) {
            FILE *in = fopen(argv[i], "r");
            if (in == NULL) {
                fprintf(stderr, "cat: %s: ", argv[i]);
                perror("");
                return 1;
            }
            output_file(in);
            fclose(in);
        }
    return 0;
}
