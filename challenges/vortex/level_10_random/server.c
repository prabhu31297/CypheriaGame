#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 9010
#define FLAG "cypheria{suid_rooted}"

void generate_numbers(unsigned int seed, int *numbers, int count) {
    srand(seed);
    for (int i = 0; i < count; i++) numbers[i] = rand();
}

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    socklen_t addrlen = sizeof(address);
    int numbers[20];
    unsigned int seed = time(NULL) % 100000;
    char buffer[1024] = {0};

    generate_numbers(seed, numbers, 20);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;   // <-- fixed
    address.sin_port = htons(PORT);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 1);
    new_socket = accept(server_fd, (struct sockaddr *)&address, &addrlen);

    for (int i = 0; i < 20; i++) {
        char num[32];
        sprintf(num, "%d\n", numbers[i]);
        send(new_socket, num, strlen(num), 0);
    }

    read(new_socket, buffer, sizeof(buffer));
    unsigned int guess = (unsigned int)atoi(buffer);

    if (guess == seed) send(new_socket, FLAG, strlen(FLAG), 0);
    else send(new_socket, "Wrong seed!\n", 12, 0);

    close(new_socket);
    close(server_fd);
    return 0;
}