/*
  Program: Develop a C program to manage student grades in a class (like lab 10).
           Maintain the student structures in a linked list (instead of a fixed-sized array)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char name[50];          // To store the student’s name
    int rollNo;             // To store a student’s unique roll number (within this class), e.g.: 1, 2, 3, ...
    float marks[5];         // To store an array of grades for five different subjects
    /* also declare your pointer members */
    float totalMarks;       // Total marks across 5 subjects
    float averageMarks;     // Average marks across 5 subjects
    struct Student *next;   // Pointer to the next student in the list
};

// Function to create a new student node and taking inputs
struct Student* createStudent() {
    struct Student *newStudent = (struct Student*) malloc(sizeof(struct Student));
    if (!newStudent) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    printf("\nEnter student's name: ");
    scanf("%s", newStudent->name);
    printf("Enter student's roll number: ");
    scanf("%d", &newStudent->rollNo);

    // Takes the marks input for 5 subjects
    printf("Enter grades for five subjects (0-100):\n");
    for (int i = 0; i < 5; i++) {
        while (1) {
            printf("Subject %d: ", i + 1);
            if (scanf("%f", &newStudent->marks[i]) != 1 || newStudent->marks[i] < 0 || newStudent->marks[i] > 100) {
                printf("Invalid grade. Please enter a number between 0 and 100.\n");
                while (getchar() != '\n'); // Clear input buffer
            } else {
                break;
            }
        }
    }
    newStudent->next = NULL; // Initialize the next pointer to NULL
    return newStudent;
}

// Function to add a student to the start of the linked list
struct Student* addStudent(struct Student *head) {
    struct Student *newStudent = createStudent();
    newStudent->next = head; // Link the new student to the previous head
    return newStudent;       // New student becomes the new head
}

// Function to calculate total and average marks for each student
void calculateGrades(struct Student *head) {
    struct Student *current = head;
    while (current != NULL) {
        current->totalMarks = 0.0;
        for (int i = 0; i < 5; i++) {
            current->totalMarks += current->marks[i]; // Sum up marks
        }
        current->averageMarks = current->totalMarks / 5; // Calculate average
        current = current->next;
    }
}

// Function to display each student's data and calculate class statistics
void displayStudentData(struct Student *head) {
    struct Student *current = head;
    float classTotal = 0.0;  // Sum of all students' average marks
    int studentCount = 0;    // Number of students
    float highestAverage = 0.0, lowestAverage = 100.0;
    struct Student *highestStudent = NULL, *lowestStudent = NULL;

    printf("\n%-10s %-15s %-36s %-15s %-15s\n", "Name", "Roll Number", "Marks", "Total Marks", "Average Marks");
    printf("---------------------------------------------------------------------------------------------\n");

    while (current != NULL) {
        studentCount++;
        classTotal += current->averageMarks;

        // Update highest and lowest averages
        if (current->averageMarks > highestAverage) {
            highestAverage = current->averageMarks;
            highestStudent = current;
        }
        if (current->averageMarks < lowestAverage) {
            lowestAverage = current->averageMarks;
            lowestStudent = current;
        }

        // Display each student's data
        printf("%-10s %-15d ", current->name, current->rollNo);
        for (int j = 0; j < 5; j++) {
            printf("%-5.1f ", current->marks[j]);
        }
        printf("\t%-15.1f %-15.1f\n", current->totalMarks, current->averageMarks);

        current = current->next;
    }

    // Display class statistics if there are students
    if (studentCount > 0) {
        printf("\nClass Average Marks: %.2f\n", classTotal / studentCount);
        printf("Highest Average: %s (%.2f)\n", highestStudent->name, highestStudent->averageMarks);
        printf("Lowest Average: %s (%.2f)\n", lowestStudent->name, lowestStudent->averageMarks);
    } else {
        printf("No students in the class.\n");
    }
}

// Free memory used by the linked list
void freeList(struct Student *head) {
    struct Student *temp;
    while (head != NULL) {
        temp = head;   // Store current head
        head = head->next; // Move to the next student
        free(temp);    // Free the previous head
    }
}

int main() {
    struct Student *head = NULL; // Initialize the list as empty
    char choice;

    // Loop to add students to the list
    while (1) {
        printf("Do you want to add a student? (y/n): ");
        scanf(" %c", &choice);
        if (choice == 'y' || choice == 'Y') {
            head = addStudent(head); // Add the student and update head
        } else {
            break; // Exit the loop if no more students to add
        }
    }

    // Calculate and display data
    calculateGrades(head);
    displayStudentData(head);

    // Free allocated memory
    freeList(head);

    return 0;
}