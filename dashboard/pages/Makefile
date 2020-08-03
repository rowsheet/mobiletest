
all:
	gcc -g -c hi.c -o hi.o
	gcc hi.o -o hi
	objdump -Sx hi.o >hi.asm

clean:
	rm hi.o hi hi.asm

alld:
	gcc -g -c hi.c -o hi.o
	gcc hi.o -o hi
	objdump -d hi.o >hi.asm

allt:
	gcc -g -c test.c -o test.o
	gcc test.o -o test
	objdump -Sx test.o >test.asm
	
allv:
	as var.asm -o var.o
	ld var.o -o var

cleanv:
	rm var.o var
