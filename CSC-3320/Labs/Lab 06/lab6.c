/*
  Program: Take user input of 10 and increment based on a random array of 100
*/

#include <stdio.h>
#include <stdlib.h>  // For rand() and srand()
#include <time.h>    // For time() to seed the random number generator

void genRandomArray(int randomArray[], int size) {
    srand(time(0)); 

    for (int i = 0; i < size; i++) {
        randomArray[i] = rand() % 10;
    }
}

int main() {
    int array[10];
    int randomArray[100];

    printf("Enter ten integers: ");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &array[i]);
    }

    genRandomArray(array, 100);

    for (int i = 0; i < 100; i++) {
        int index = randomArray[i];
        array[index] += 1;
    }

    printf("\nUpdated array: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", array[i]);
    }
    
    return 0;
}