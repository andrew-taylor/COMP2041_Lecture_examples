# this is a comment with a : in it

game : main.o graphics.o world.o 
	$(CC) $(FLAGS) -o game main.o graphics.o world.o

CC=gcc-4.0

main.o : main.c graphics.h world.h
	gcc -c main.c

graphics.o : graphics.c world.h 
	gcc -c graphics.c

world.o : world.c world.h 
	gcc -c world.c

clean:
	rm -f game main.o graphics.o world.o

FLAGS=-O
