/*
  Program: Create selection_sort method and sort an array and print it out
*/

#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selection_sort(int array[], int n) {
    if (n <= 1)
        return;

    int maxVal = 0;
    for (int i = 1; i < n; i++) {
        if (array[i] > array[maxVal]) {
            maxVal = i;
        }
    }

    swap(&array[maxVal], &array[n-1]);

    printf("After the next call: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    selection_sort(array, n - 1);
}

int main() {
    int n;

    printf("How many integers: ");
    scanf("%d", &n);

    int array[n];
    printf("\nEnter %d elements: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }
    
    selection_sort(array, n);

    printf("Sorted Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}