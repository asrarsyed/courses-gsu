/*
  Program: Reverse a range of elements in an array using pointers
*/

#include <stdio.h>

// Function to reverse the elements
void reverse(int arr[], int *beg, int *end) {
    while(beg < end) {
        int temp = *beg;
        *beg = *end;
        *end = temp;
        beg++;
        end--;
    }
}

// Function to rotate the array to the right by k steps
void rotate(int arr[], int n, int k) {
    if (k > 0 && k < n) {
        // Reverse the entire array
        reverse(arr, &arr[0], &arr[n - 1]);
        // Reverse the first k elements
        reverse(arr, &arr[0], &arr[k - 1]);
        // Reverse the remaining elements
        reverse(arr, &arr[k], &arr[n - 1]);
    }
}

int main() {
    int n, k;

    // Input for array size and elements
    printf("Size of array: ");
    scanf("%d", &n);

    int arr[n];
    printf("Given array (%d elements): ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Input for rotation steps
    printf("How many steps? ");
    scanf("%d", &k);
    
    // Rotate the array to the right by k steps
    rotate(arr, n, k);
    
    printf("\t");

    // Print the array
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));  // Using pointer to access elements
    }

    return 0;
}