#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>
#include <openssl/bio.h>
#include <openssl/evp.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PORT 9022
#define ANCIENT_PASSWORD "super_secret_phrase"

void translate_ancient_runes(char *input, char *output) {
    BIO *b64, *bmem;
    int len;

    b64 = BIO_new(BIO_f_base64());
    BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    bmem = BIO_new_mem_buf(input, strlen(input));
    bmem = BIO_push(b64, bmem);

    len = BIO_read(bmem, output, strlen(input));
    output[len] = 0;

    BIO_free_all(bmem);
}

int main() {
    int magic_portal_fd, adventurer_fd;
    struct sockaddr_in addr;
    char submitted_scroll[1024] = {0};
    char spoken_incantation[1024] = {0};

    magic_portal_fd = socket(AF_INET, SOCK_STREAM, 0);
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY; 
    addr.sin_port = htons(PORT);

    bind(magic_portal_fd, (struct sockaddr *)&addr, sizeof(addr));
    listen(magic_portal_fd, 1);
    
    printf("The Ancient Guardian awakens and awaits a challenger on port %d...\n", PORT);
    adventurer_fd = accept(magic_portal_fd, NULL, NULL);

    char *welcome = "Halt! I am the Guardian. To pass, you must speak the ancient password.\nBut my old ears can only understand the language of runes (Base64).\nPresent your incantation now!\n> ";
    write(adventurer_fd, welcome, strlen(welcome));

    read(adventurer_fd, submitted_scroll, 1024);
    translate_ancient_runes(submitted_scroll, spoken_incantation);

    if (strcmp(spoken_incantation, ANCIENT_PASSWORD) == 0) {
        char *success = "Incredible! The runes are true! The path is open!\nYour reward is this sacred text:\n";
        write(adventurer_fd, success, strlen(success));
        
        FILE *f = fopen("flag.txt", "r");
        char treasure_map[64];
        fgets(treasure_map, sizeof(treasure_map), f);
        fclose(f);
        write(adventurer_fd, treasure_map, strlen(treasure_map));
    } else {
        char *msg = "Foolish mortal! Those are meaningless scribbles! Begone!\n";
        write(adventurer_fd, msg, strlen(msg));
    }

    close(adventurer_fd);
    close(magic_portal_fd);
    return 0;
}