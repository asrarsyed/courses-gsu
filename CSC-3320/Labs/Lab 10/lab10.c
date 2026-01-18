/*
  Program: Develop a C program to manage student grades in a class.
*/

#include <stdio.h>

struct Student {
    char name[50];     // To store the student’s name
    int rollNo;        // To store a student’s unique roll number (within this class), e.g.: 1, 2, 3, ...
    float marks[5];    // To store an array of grades for five different subjects
};

// Function to get the number of students in the class
int studentAmount() {
    int number;
    while (1) {
        printf("Enter the total number of students in the class (≤ 50): ");
        if (scanf("%d", &number) != 1 || number < 1 || number > 50) {
            while (getchar() != '\n'); // Clears the invalid input
                printf("Invalid input. Please enter an integer between 1 and 50.\n");
        } else {
            return number;
        }
    }
}

// Function to input student data
void inputStudentData(struct Student students[], int n) {
    for (int i = 0; i < n; i++) {
        printf("\nEnter name for student %d: ", i + 1);
        scanf("%s", students[i].name);
        printf("Enter the roll number for student %d: ", i + 1);
        scanf("%d", &students[i].rollNo);

        printf("Enter the grades (0-100) for five subjects for student %d:\n", i + 1);
        for (int j = 0; j < 5; j++) {
            while (1) {
                printf("Subject %d: ", j + 1);
                if (scanf("%f", &students[i].marks[j]) != 1 || students[i].marks[j] < 0 || students[i].marks[j] > 100) {
                    while (getchar() != '\n'); // Clear invalid input
                        printf("Invalid grade. Please enter a number between 0 and 100.\n");
                } else {
                    break;
                }
            }
        }
    }
}

// Function to calculate grades and display statistics
void calculateAndDisplay(struct Student students[], int n) {
    float classTotal = 0.0, highestAverage = 0.0, lowestAverage = 100.0;
    int highestIndex = 0, lowestIndex = 0;

    printf("\n%-10s %-15s %-36s %-15s %-15s\n", "Name", "Roll Number", "Marks", "Total Marks", "Average Marks");
    printf("---------------------------------------------------------------------------------------------\n");

    for (int i = 0; i < n; i++) {
        float totalMarks = 0.0, averageMarks = 0.0;
        
        // Calculate total and average marks for the student
        for (int j = 0; j < 5; j++) {
            totalMarks += students[i].marks[j];
        }
        averageMarks = totalMarks / 5;

        // Update class total for calculating class average
        classTotal += averageMarks;

        // Check for highest and lowest averages
        if (averageMarks > highestAverage) {
            highestAverage = averageMarks;
            highestIndex = i;
        }
        if (averageMarks < lowestAverage) {
            lowestAverage = averageMarks;
            lowestIndex = i;
        }

        // Displays the students information
        printf("%-10s %-15d ", students[i].name, students[i].rollNo);
        for (int j = 0; j < 5; j++) {
            printf("%-5.1f ", students[i].marks[j]);
        }
        printf("\t%-15.1f %-15.1f\n", totalMarks, averageMarks);
    }

    // Display the class average
    float classAverage = classTotal / n;
    printf("\nClass Average Marks: %.2f\n", classAverage);

    // Display students with highest and lowest average
    printf("Highest Average: %s (%.2f)\n", students[highestIndex].name, highestAverage);
    printf("Lowest Average: %s (%.2f)\n", students[lowestIndex].name, lowestAverage);
}

int main () {
    int n = studentAmount();
    struct Student students[n]; // Array of user_number of struct Student elements

    inputStudentData(students, n); // Gets the data for each student
    calculateAndDisplay(students, n); // Calculates the grades and displays

    return 0;
}