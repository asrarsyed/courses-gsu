/*
  Program: Print a One-Month Calendar
*/

#include <stdio.h>

void printCalendar(int numDays, int startDay) {
    int i;

    startDay--;
    printf("Sun Mon Tue Wed Thu Fri Sat\n");
    for (i = 0; i < startDay; i++) {
        printf("    ");
    }

    for (i = 1; i <= numDays; i++) {
        printf("%3d ", i);
        if ((i + startDay) % 7 == 0) {
            printf("\n");
        }
    }
}

int main() {
    int numDays, startDay;

    // Get user input for the number of days and starting day
    printf("Enter number of days in month: ");
    scanf("%d", &numDays);
    printf("Enter starting day of the week (1=Sun, 7=Sat): ");
    scanf("%d", &startDay);

    // Print the calendar
    printf("\nYour requested month's calendar is:\n\n");
    printCalendar(numDays, startDay);

    return 0;
}
