/*
  Program: Given a string s, write a function that returns true if it is a palindrome, or false otherwise.
  Limitations: Do not use extra memory space to store the characters of s.
*/

#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isPalindrome(char* s) {
    // Two pointers approach: left starts from beginning, right from end
    int left = 0;
    int right = strlen(s) - 1;
    
    while (left < right) {
        // Skip the non-alphanumeric characters from left
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        
        // Skip the non-alphanumeric characters from right
        while (left < right && !isalnum(s[right])) {
            right--;
        }
        
        // Compare characters after converting to lowercase
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}

int main() {
    // Test cases
    char str1[] = "A man, a plan, a canal – Panama";
    char str2[] = "22/02/2022";
    char str3[] = "Hello, World!";
    char str4[] = "race car";
    
    printf("Test 1: %s\n", isPalindrome(str1) ? "true" : "false"); // Should print true
    printf("Test 2: %s\n", isPalindrome(str2) ? "true" : "false"); // Should print true
    printf("Test 3: %s\n", isPalindrome(str3) ? "true" : "false"); // Should print false
    printf("Test 4: %s\n", isPalindrome(str4) ? "true" : "false"); // Should print true
    
    return 0;
}