/*
  Program: Temperature Converter
           Converts a Celsius temperature to its equivalent Fahrenheit temperature!
*/

#include <stdio.h>

int main() {
    float userInput,formula;
    printf("Enter Celsius temperature: ");
    scanf("%f", &userInput);
    formula = (9.0 / 5.0) * userInput + 32;
    printf("Equivalent Fahrenheit temperature: %.2f\n", formula);

    return 0;
}
