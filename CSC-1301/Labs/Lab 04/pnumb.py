# Prolog
# Section: 002
'''
  Purpose:
    Phone number breakdown

  Pre-conditions (input): 
       (Enter the 10-digit phone number)
  Post-conditions (output): 
      Breakdown of phone number (area code, prefix, line number)
'''

def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Breakdown of phone number to area code, prefix, and line number")
    print()

#  2.  Input the 10-digit phone number
    Phone_number = (input("Enter phone number? "))

#  3.  Breakdown the phone number
    area_code = Phone_number[0:3]
    prefix = Phone_number[3:6]
    line_number = Phone_number[6:10]

#  4. Output breakdown to area code, prefix, line number
    print()
    print("Phone number is converted to area code = ",area_code,", prefix = ",prefix,", line number = ",line_number)
    print()
    phone_str = '(%s) %s-%s' % (area_code, prefix, line_number)
    print(phone_str)
    print()
main()
# end of program file


'''
#Errors Found in ORIGINAL Program & Method to Fix

We can find Syntax Errors by running the Program 
------------------------------------------------

1st error is on the Original line 23 we recive is a indentation error.

        Phone_number = int(input ())
    IndentationError: unexpected indent

I fixed the first error by correcting the indentation i.e backspacing it to make it proper.end=

2nd error is on Original line 31, a syntax error caused by improper apostrophe(cause it wasn't typed in python)

        print(phone_str = ‘ (%s) %s-%s ’ % (area_code, prefix, line_number)
                          ^
    SyntaxError: invalid character '‘' (U+2018)

I fixed this error by correcting and replacing the apostrophes.

3rd error is on Original line 31, it is a Syntax error caused because the print statement bracket wasn't closed.

        print(phone_str = ' (%s) %s-%s ' % (area_code, prefix, line_number)
             ^
    SyntaxError: '(' was never closed

I fixed this error by adding the parentheses at the end.


The Semantic errors was due to incompletion of Code
---------------------------------------------------

So the Semantic error can be explained that the original code was incomplete.

When I checked my terminal and found that 3 problems existed, which were basically the 3 variables that were not defined.
    On the original line 31, "area_code", "prefix" and "line_number" are not defined.

We can fix this issue by adding the code to complete the program.


The Errors Found during writing the code
----------------------------------------

So a problem that occured for me was that the way I intended for the code to seperate the 10-digit phone number from input was
interfering with the int(input from the original code) - this showed up as a TypeError.

    Traceback (most recent call last):
     File "/Users/asrarsyed/Desktop/Fall CS 1301/CS Labs/Lab 4/pnumb.py", line 34, in <module>
       main()
     File "/Users/asrarsyed/Desktop/Fall CS 1301/CS Labs/Lab 4/pnumb.py", line 26, in main
       area_code = Phone_number[0:3]
    TypeError: 'int' object is not subscriptable

I fixed this error by removing the int from the line that took int(input).
'''
