#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void enter_the_magic_portal() {
    char magic_incantation[100];
    
 
    for (int i = 0; i < 30; i++) {
        putchar('*');
    }
    printf("\nYou stand at the entrance to a swirling vortex.\nSpeak your name to enter:\n");
    
    fgets(magic_incantation, sizeof(magic_incantation), stdin);
    
    printf(magic_incantation);
    
    printf("\nThe vortex closes!\n");
}

int main() {
    int ritual_active = 1;
    setuid(0);
    

    while (ritual_active) {
        printf("The ritual to open the vortex begins...\n");
        ritual_active = 0;
    }
    
    enter_the_magic_portal();
    
    return 0;
}