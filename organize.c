#include <stdio.h>
#include <windows.h>

int run(char *command) {
    
    if(system(command) == 0) return 1;
    return 0;
}

char *getDirectory() {
    FILE *fp;
    char buffer[256];

    fp = popen("dir organizer.py /s /b", "r");

    if(fp == NULL) {
        printf("Error on running command");
        return NULL;
    }

    fgets(buffer, 256, fp);
    char command[256];
    sprintf(command, "python %s", buffer);
    run(command);
}

int main() {
    if(getDirectory()) {
        return 0;
    } return 1;
}