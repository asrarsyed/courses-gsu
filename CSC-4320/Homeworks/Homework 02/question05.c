#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define FILENAME "f.txt"
#define NUM_ITERATIONS 200

void process_work(int pid) {
    FILE *file;
    int N;

    for (int i = 0; i < NUM_ITERATIONS; i++) {
        // Open the file for reading
        file = fopen(FILENAME, "r+");
        if (file == NULL) {
            perror("Error opening file");
            exit(1);
        }

        // Read the integer from the file
        fscanf(file, "%d", &N);
        fclose(file);

        // Output the current value and the process PID
        printf("Process %d: Current value: %d\n", pid, N);

        // Increment the value
        N++;

        // Open the file for writing (overwrite the current value)
        file = fopen(FILENAME, "w");
        if (file == NULL) {
            perror("Error opening file for writing");
            exit(1);
        }

        // Write the updated value back to the file
        fprintf(file, "%d", N);
        fclose(file);

        // Sleep for a short time to simulate work
        usleep(100000); // 100 ms
    }
}

int main() {
    pid_t pid;

    // Initialize the file with the value 0 if it doesn't exist
    FILE *file = fopen(FILENAME, "r");
    if (file == NULL) {
        file = fopen(FILENAME, "w");
        if (file == NULL) {
            perror("Error opening file to initialize");
            exit(1);
        }
        fprintf(file, "0");
        fclose(file);
    } else {
        fclose(file);
    }

    // Create three processes P1, P2, and P3
    for (int i = 1; i <= 3; i++) {
        pid = fork();

        if (pid < 0) {
            perror("Fork failed");
            exit(1);
        }

        if (pid == 0) {
            // In the child process (P1, P2, or P3)
            process_work(i);
            exit(0);  // Terminate the child process after work
        }
    }

    // Wait for all child processes to finish
    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    return 0;
}
