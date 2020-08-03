
all:
	gcc -g -c hi.c -o hi.o
	gcc hi.o -o hi
	objdump -Sx hi.o >hi.asm

clean:
	rm hi.o hi hi.asm