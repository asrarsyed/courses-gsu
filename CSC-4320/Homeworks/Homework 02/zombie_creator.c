#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;

    // Fork a child process
    pid = fork();

    if (pid < 0) {
        // Fork failed
        fprintf(stderr, "Fork failed\n");
        exit(1);
    }
    else if (pid == 0) {
        // Child process
        printf("Child process with PID: %d\n", getpid());
        exit(0);
    }
    else {
        // Parent process
        printf("Parent process with PID: %d\n", getpid());
        printf("Created child process with PID: %d\n", pid);
        // Sleep for 10 seconds to keep zombie around
        sleep(10);
    }

    return 0;
}
