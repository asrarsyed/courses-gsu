/*
  Program: Fibonacci
*/

#include <stdio.h>

void fill_fib(int fib_numbers[], int n) {
    if (n < 2) fib_numbers[n] = n;  // Base cases if result is 0 and 1
    else if (fib_numbers[n] == -1) {  // Only if not already calculated
        fill_fib(fib_numbers, n - 1);
        fill_fib(fib_numbers, n - 2);
        fib_numbers[n] = fib_numbers[n - 1] + fib_numbers[n - 2];
    }
}

int main() {
    int fib_numbers[40];
    for (int i = 0; i < 40; i++) fib_numbers[i] = -1;  // Mark as uncalculated
    fill_fib(fib_numbers, 39);

    for (int i = 0; i < 40; i++) printf("%d ", fib_numbers[i]);
    return 0;
}