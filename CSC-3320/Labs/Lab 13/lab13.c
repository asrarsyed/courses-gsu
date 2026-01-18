/*
  Program: 
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdbool.h>

// Function to calculate the sum of even numbers
void calculate_even_sum() {
    int sum = 0;
    for (int i = 2; i <= 1000; i += 2) {
        sum += i;
    }
    printf("Child 1: Sum of even numbers between 1 and 1000 is %d\n", sum);
    printf("DONE. MY PID IS %d. MY PARENT'S PID IS %d.\n\n", getpid(), getppid());
    exit(0);
}

// Function to calculate the sum of odd numbers
void calculate_odd_sum() {
    int sum = 0;
    for (int i = 1; i <= 1000; i += 2) {
        sum += i;
    }
    printf("Child 2: Sum of odd numbers between 1 and 1000 is %d\n", sum);
    printf("DONE. MY PID IS %d. MY PARENT'S PID IS %d.\n\n", getpid(), getppid());
    exit(0);
}

// Function to find and display prime numbers
void find_primes() {
    printf("Child 3: Prime numbers between 1 and 1000 are:\n");
    for (int num = 2; num <= 1000; ++num) {
        bool is_prime = true;
        for (int divisor = 2; divisor * divisor <= num; ++divisor) {
            if (num % divisor == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) {
            printf("%d ", num);
        }
    }
    printf("\n");
    printf("DONE. MY PID IS %d. MY PARENT'S PID IS %d.\n\n", getpid(), getppid());
    exit(0);
}

int main() {
    pid_t pid1, pid2, pid3;

    // Creating the first child process
    pid1 = fork();
    if (pid1 < 0) {
        perror("Failed to fork first child");
        exit(1);
    } else if (pid1 == 0) {
        calculate_even_sum();
    }

    // Creating the second child process
    pid2 = fork();
    if (pid2 < 0) {
        perror("Failed to fork second child");
        exit(1);
    } else if (pid2 == 0) {
        calculate_odd_sum();
    }

    // Creating the third child process
    pid3 = fork();
    if (pid3 < 0) {
        perror("Failed to fork third child");
        exit(1);
    } else if (pid3 == 0) {
        find_primes();
    }

    // Parent process waits for all children to finish
    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    // Parent process termination message
    printf("Parent: DONE. MY PID IS %d. MY PARENT'S PID IS %d.\n", getpid(), getppid());
    return 0;
}
