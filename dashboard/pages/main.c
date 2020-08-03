#include <stdio.h>

int main(void) {
    printf("starting program...\n");
    
    printf("enter input: ");
    char buff[5];
    gets(buff);
    printf("your input was:\n%s", buff);
    
    return 0;
}