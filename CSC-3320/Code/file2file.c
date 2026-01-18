
/* 

File I/O:
This program copies the contents of a file to another file
*/



#include<stdio.h>

int main()
{

    FILE *fp1 = fopen("example.txt", "r");  // Open file for reading
    FILE *fp2 = fopen("dest_file.txt", "w");  // Open file for writing
    char c;
    if (fp1 != NULL) {
       while ((c = fgetc(fp1)) != EOF) {
           putchar(c);  // Output file content to the screen
           fputc(c, fp2); 
       }
    fclose(fp1);  // Close the file
    fclose(fp2);  // Close the file
    }
    
    return 0;
}

