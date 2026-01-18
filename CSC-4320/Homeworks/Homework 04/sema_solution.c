/*
  Requirments: Have a file called f.txt with a single zero
  To-Run: gcc sema_solution.c -o sema_solution -std=c99 -pthread
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/file.h>
#include <sys/wait.h>

#define FILENAME "f.txt"
#define LOCKFILE "f.lock"

int readLastNumber(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file for reading");
        exit(1);
    }
    
    int lastNum = 0;
    int num;
    
    // Read until the end of file, keeping track of the last number
    while (fscanf(file, "%d", &num) == 1) {
        lastNum = num;
    }
    
    fclose(file);
    return lastNum;
}

void appendNumber(const char *filename, int number) {
    FILE *file = fopen(filename, "a");
    if (file == NULL) {
        perror("Error opening file for appending");
        exit(1);
    }
    
    fprintf(file, "\n%d", number);
    fclose(file);
}

int main() {
    // Create 5 child processes
    for (int i = 0; i < 5; i++) {
        pid_t pid = fork();
        
        if (pid < 0) {
            // Fork failed
            perror("Fork failed");
            exit(1);
        } else if (pid == 0) {
            // Child process
            
            // Open lockfile for locking
            int lockfd = open(LOCKFILE, O_CREAT | O_RDWR, 0666);
            if (lockfd == -1) {
                perror("Error opening lock file");
                exit(1);
            }
            
            // Acquire exclusive lock (entering critical section)
            if (flock(lockfd, LOCK_EX) == -1) {
                perror("Error acquiring lock");
                close(lockfd);
                exit(1);
            }
            
            // Open file and read the last integer
            int lastNum = readLastNumber(FILENAME);
            
            // Output the number and process PID
            printf("Process PID: %d read number: %d\n", getpid(), lastNum);
            
            // Increment the number
            int newNum = lastNum + 1;
            
            // Open file in append mode and write the new number
            appendNumber(FILENAME, newNum);
            
            // Release lock (exiting critical section)
            flock(lockfd, LOCK_UN);
            close(lockfd);
            
            // Exit child process
            exit(0);
        }
    }
    
    // Parent process waits for all children to complete
    for (int i = 0; i < 5; i++) {
        wait(NULL);
    }
    
    printf("All child processes have finished.\n");
    return 0;
}