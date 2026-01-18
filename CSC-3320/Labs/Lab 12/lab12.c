/*
  Program: Practice File Management in a C program
*/

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 1 // Reading one byte at a time

void createFile(const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error creating file");
        exit(1);
    }
    for (int i = 32; i <= 126; i++) {
        fprintf(file, "%d\n", i); // Write integers followed by newline
    }
    fclose(file);
}

void displayFile(const char *filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        perror("Error opening file");
        exit(1);
    }

    char buffer[BUFFER_SIZE];   // For reading raw bytes
    char num_buffer[10];        // Buffer to store digits of a number
    int num_index = 0;          // Index for num_buffer

    while (read(fd, buffer, BUFFER_SIZE) > 0) {
        char ch = buffer[0];    // Current character

        if (isdigit(ch)) {
            num_buffer[num_index++] = ch; // Append digit to num_buffer
        } else if (ch == '\n' || ch == ' ') {
            if (num_index > 0) {
                num_buffer[num_index] = '\0'; // Null-terminate the number string
                int num = atoi(num_buffer);  // Convert to integer

                // Print integer as a string
                char num_str[10];
                int length = snprintf(num_str, sizeof(num_str), "%d", num);
                write(STDOUT_FILENO, num_str, length);
                write(STDOUT_FILENO, " ", 1);

                // Print binary encoding of the number
                write(STDOUT_FILENO, &num, sizeof(num));

                // Print newline
                write(STDOUT_FILENO, "\n", 1);

                num_index = 0; // Reset for next number
            }
        }
    }

    close(fd);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    const char *filename = argv[1];

    // Create the file and store the integers
    createFile(filename);

    // Reopen the file and process its content
    displayFile(filename);

    return 0;
}
