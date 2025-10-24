#include <stdio.h>
#include <windows.h>
#include <unistd.h>
#include <string.h>

char *find() {
    FILE *out;
    char path[256];
    static char final[256];

    out = popen("where /r C:\\ \"organizer.py\"", "r");
    if(out == NULL) {
        return NULL;
    }
    
    fgets(path, 256, out);

    int index = 0;
    char let = ' ';
    int size = 0;
    while(1) {
        let = path[index];
        if(let == '\n') break;
        size += snprintf(final + size, sizeof(final) - size, "%c", path[index]);
        index++;
    }
    
    return final;
}

char *getPath() {
    FILE *out;
    char path[256];

    out = popen("cd", "r");

    if(out == NULL) return "";
    
    fgets(path, 256, out);
    
    int counter = 0;
    int size = 0;
    static char final_path[256] = "";
    for(int i = 0; i < strlen(path); i++) {
        if(counter < 3) {
            size += snprintf(final_path + size, sizeof(final_path) - size, "%c", path[i]); 
        } else break;
        if(path[i] == '\\') counter++;
    }

    return final_path;
}

int install() {
    printf("Installing organize.exe");
    if(system("cmd /C copy organize.exe C:\\Windows") == 0) return 1;
    return 0;
}

int copy(char *prog, char *path) {
    char command[256];
    printf("Copying files from %s to %s\n", prog, path);
    sprintf(command, "copy \"%s\" \"%s\"", prog, path);
    if(system(command) == 0) return 1;
    return 0;
}

int run() {
    char *path = getPath();
    char *prog = find();
    if(copy(prog, path)) {
        if(install()) {
            return 1;
        }
    }

    return 0;
}

int main() {
    if(run()) {
        printf("Installation successful.\n");
        return 0;
    } 
    printf("Something went wrong.\n");
    return 1;
}