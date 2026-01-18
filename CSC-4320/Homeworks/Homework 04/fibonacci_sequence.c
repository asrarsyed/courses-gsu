/*
  Author: Asrar Syed
  Program: Fibonacci Sequence: Question 2
  
  Requirments: None
  To-Run: gcc fibonacci_sequence.c -o fibonacci_sequence -std=c99 -pthread
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX 20

int fib[MAX];        // Array to store Fibonacci numbers
int computed = 0;  // Tracks computed numbers
pthread_mutex_t mutex;
pthread_cond_t cond;

// Child thread function to generate Fibonacci sequence
void *generate_fibonacci(void *param) {
    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i < MAX; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];

        // Lock before updating `computed`
        pthread_mutex_lock(&mutex);
        computed = i + 1; // Update computed count
        pthread_cond_signal(&cond); // Notify parent thread
        pthread_mutex_unlock(&mutex);
    }

    pthread_exit(0);
}

int main() {
    pthread_t thread;

    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond, NULL);

    // Create the child thread
    pthread_create(&thread, NULL, generate_fibonacci, NULL);

    // Parent thread prints numbers as they are computed
    for (int i = 0; i < MAX; i++) {
        pthread_mutex_lock(&mutex);
        while (computed <= i) { // Wait until number is computed
            pthread_cond_wait(&cond, &mutex);
        }
        printf("Fibonacci[%d] = %d\n", i, fib[i]);
        pthread_mutex_unlock(&mutex);
    }

    // Wait for child thread to finish
    pthread_join(thread, NULL);

    // Clean up after
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);

    return 0;
}