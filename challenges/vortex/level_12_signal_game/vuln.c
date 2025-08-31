#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int bomb_disarmed = 0;

void the_secret_disarm_code(int sig) {
    if (sig == SIGUSR1) {
        bomb_disarmed = 1;
    }
}

int main() {
    signal(SIGUSR1, the_secret_disarm_code);
    int my_pid = getpid();

    printf("****************************************\n");
    printf("* !!! BOMB DEFUSAL !!!       *\n");
    printf("****************************************\n\n");
    printf("AGENT, THE CLOCK IS TICKING!\n");
    printf("You must send the secret disarm signal to this program (PID: %d)!\n", my_pid);
    printf("You have exactly 5 seconds... GO GO GO!\n");
    
    sleep(5);

    if (bomb_disarmed) {
        printf("\nWhew! You did it with milliseconds to spare!\n");
        printf("The bomb is defused. Here are the secret launch codes you recovered:\n");
        FILE *secret_plans = fopen("flag.txt", "r");
        char launch_codes[64];
        fgets(launch_codes, sizeof(launch_codes), secret_plans);
        fclose(secret_plans);
        printf("\nCODES: %s\n", launch_codes);
    } else {
        printf("\n..........................\n");
        printf("!!!!!!!!!! BOOM !!!!!!!!!!\n");
        printf("You were too slow! Mission failed.\n");
    }

    return 0;
}