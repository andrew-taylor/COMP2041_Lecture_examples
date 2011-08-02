// Written by andrewt@cse.unsw.edu.au
// as a COMP2041 lecture example
// March 2011

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void
count_file(FILE *in) {
	int n_lines = 0, n_words = 0, n_chars = 0;
	int in_word = 0, c;
    while ((c = fgetc(in)) != EOF) {
    	n_chars++;
        if (c == '\n')
        	n_lines++;
        if (isspace(c))
        	in_word = 0;
        else if (!in_word) {
            in_word = 1;
            n_words++;
        }
    }
	printf("%6d %6d %6d", n_lines, n_words, n_chars);
}

int
main(int argc, char *argv[]) {
    if (argc == 1) 
        count_file(stdin);
    else
        for (int i = 1; i < argc; i++) {
            FILE *in = fopen(argv[i], "r");
            if (in == NULL) {
                fprintf(stderr, "wc: %s: ", argv[i]);
                perror("");
                return 1;
            }
            count_file(in);
			printf(" %s\n", argv[i]);
            fclose(in);
        }
    return 0;
}
