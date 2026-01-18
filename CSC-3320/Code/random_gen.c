#include<stdio.h>
#include<stdlib.h>

int main()
{

    srand(0);
    int random_number;
    
    // use % operation if random numbers to be in a range, e.g. 0-14
    random_number = rand() % 15;
    printf("%d ", random_number);
    printf("\n");
    return 0;
} 
