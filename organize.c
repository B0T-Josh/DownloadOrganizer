#include <stdio.h>
#include <windows.h>

int run() {
    if(system("python organizer.py") == 0) return 1;
    return 0;
}

int main() {
    if(run()) {
        return 0;
    } return 1;
}