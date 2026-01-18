/*
  Program: Implement Banker’s Algorithm
  
  Requirments: create a .txt file and input the matrix
    6,4,7,3
    4,2,3,2
    2,5,3,3
    6,3,3,2
    5,6,7,5

  To-Run: gcc banker.c -o banker -std=c99
          ./banker max_input.txt 10 5 7 8
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUMBER_OF_CUSTOMERS 5
#define NUMBER_OF_RESOURCES 4

// Global data structures
int available[NUMBER_OF_RESOURCES]; /* the available amount of each resource */
int maximum[NUMBER_OF_CUSTOMERS][NUMBER_OF_RESOURCES]; /*the maximum demand of each customer */
int allocation[NUMBER_OF_CUSTOMERS][NUMBER_OF_RESOURCES] = {0}; /* the amount currently allocated to each customer */
int need[NUMBER_OF_CUSTOMERS][NUMBER_OF_RESOURCES]; /* the remaining need of each customer */

// Prints the current state of all matrices
void print_state() {
    printf("\n=== CURRENT STATE ===\n");

    printf("Available:\n");
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        printf("R%d: %d  ", i, available[i]);
    }
    printf("\n");

    printf("\nMaximum:\n");
    for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
        printf("C%d: ", i);
        for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
            printf("%d ", maximum[i][j]);
        }
        printf("\n");
    }

    printf("\nAllocation:\n");
    for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
        printf("C%d: ", i);
        for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
            printf("%d ", allocation[i][j]);
        }
        printf("\n");
    }

    printf("\nNeed:\n");
    for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
        printf("C%d: ", i);
        for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
            printf("%d ", need[i][j]);
        }
        printf("\n");
    }

    printf("=====================\n\n");
}

// Safety algorithm that checks if the system is in a safe state
int is_safe() {
    int work[NUMBER_OF_RESOURCES];
    int finish[NUMBER_OF_CUSTOMERS] = {0};

    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        work[i] = available[i];
    }

    int done_something;
    do {
        done_something = 0;
        for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
            if (!finish[i]) {
                int can_finish = 1;
                for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
                    if (need[i][j] > work[j]) {
                        can_finish = 0;
                        break;
                    }
                }
                if (can_finish) {
                    for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = 1;
                    done_something = 1;
                }
            }
        }
    } while (done_something);

    for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
        if (!finish[i]) {
            return 0; // Not safe
        }
    }
    return 1; // Safe
}

// Handles a resource request
int request_resources(int customer_num, int request[]) {
    // Check if request is valid
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        if (request[i] > need[customer_num][i]) return -1;
        if (request[i] > available[i]) return -1;
    }

    // Try allocation
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        available[i] -= request[i];
        allocation[customer_num][i] += request[i];
        need[customer_num][i] -= request[i];
    }

    if (!is_safe()) {
        // Rollback
        for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
            available[i] += request[i];
            allocation[customer_num][i] -= request[i];
            need[customer_num][i] += request[i];
        }
        return -1;
    }

    return 0; // Request successful
}

// Handles resource release
void release_resources(int customer_num, int release[]) {
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        if (release[i] <= allocation[customer_num][i]) {
            allocation[customer_num][i] -= release[i];
            available[i] += release[i];
            need[customer_num][i] += release[i];
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != NUMBER_OF_RESOURCES + 2) {
        printf("Usage: %s input_file R0 R1 R2 R3\n", argv[0]);
        return 1;
    }

    // Load available resources from command-line
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        available[i] = atoi(argv[i + 2]);
    }

    // Loads the maximum matrix from file
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Failed to open input file");
        return 1;
    }

    for (int i = 0; i < NUMBER_OF_CUSTOMERS; i++) {
        for (int j = 0; j < NUMBER_OF_RESOURCES; j++) {
            fscanf(file, "%d,", &maximum[i][j]);
            need[i][j] = maximum[i][j]; // initially all need = max
        }
    }
    fclose(file);

    printf("Banker's Algorithm ready.\nType 'RQ <cust> <r0> <r1> <r2> <r3>' to request.\n");
    printf("Type 'RL <cust> <r0> <r1> <r2> <r3>' to release.\nType '*' to show state, 'exit' to quit.\n");

    // Command loop
    char input[100];
    while (1) {
        printf("> ");
        fgets(input, sizeof(input), stdin);

        if (input[0] == '*') {
            print_state();
        } else if (strncmp(input, "RQ", 2) == 0) {
            int c, r[4];
            sscanf(input, "RQ %d %d %d %d %d", &c, &r[0], &r[1], &r[2], &r[3]);
            if (request_resources(c, r) == 0)
                printf("Request granted.\n");
            else
                printf("Request denied (invalid or unsafe).\n");
        } else if (strncmp(input, "RL", 2) == 0) {
            int c, r[4];
            sscanf(input, "RL %d %d %d %d %d", &c, &r[0], &r[1], &r[2], &r[3]);
            release_resources(c, r);
            printf("Resources released.\n");
        } else if (strncmp(input, "exit", 4) == 0) {
            break;
        } else {
            printf("Unknown command.\n");
        }
    }

    return 0;
}