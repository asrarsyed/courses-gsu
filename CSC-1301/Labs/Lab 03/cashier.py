# Prolog
# Section: CSC 1301-002

'''
  Purpose: 
      calculate the change you are due when you buy an item in a store
  Pre-conditions (input): 
      money given to the cashier(cost of item)
  Post-conditions (output): 
      change user get back from the cashier(dollars, quarters, dimes, nickels and pennies)
      
'''
import math
def main():
    
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()

#  2.  Input amount of change from user
    cost = float(input("Cost of an item? "))
    amt = float(input("Amount of money given to the cashier? "))

#  3.  Calculate the change
    change = (amt-cost)*100
    if change < 0:
        print("Let me get the change")
    elif change == 0:
        print("Change not needed")
    else:
        dollar = change // 100
        change = change % 100
        quarter = change // 25
        change = change % 25
        dime = change // 10
        change = change % 10
        nickle = change // 5
        change = change % 5 
        pennies = round(change)    
#  4. Output resulting change and given cost of an item
    print()
    print(f"change is converted ", + dollar, "dollar", + quarter, "quarter", + dime, "dime", + nickle, "nickle", + pennies, "pennies")

main()
# end of program file

'''
Errors Found in ORIGINAL Program & Method to Fix - I CHANGED BOTH LINES 
---------------------------------------
We can find errors by running the Program 

1) We have 3 errors line 26 the first being a Syntax error (Indentation error) - I fixed this error by simply correcting the indentation.

    The comment error message:
        amt = float(input(“Enter the change amount: “))
    IndentationError: unexpected indent
    
    The other 2 errors on the same line 26, two errors due to mistyped apostrophes - I fixed this error by fixing the Two incorrect apostrophe character.

    The comment error message:
        amt = float(input(“Enter the change amount: “))
                          ^
    SyntaxError: invalid character '“' (U+201C)


2) Our Third error is a Syntax Error, on line 31 - I fixed this error by adding a comma in front of the first variable cost.

    The comment error message:
        print(cost "cost is {:.2f} change".format(change))
                   ^^^^^^^^^^^^^^^^^^^^^^^
    SyntaxError: invalid syntax

The logical errors in the ORIGINAL
----------------------------------

The logical errors were probably the wordings of the original program


1) A logical error I could say is was when it had
    
     dollars = int(amt)
        - this was supposed to be dollars = int(change) cause if we went with the original it would only output the amount the customer gave.
        I fixed this by changing the variables

2) Another logical error was the print statement for explaining the change
        
    print()
    print(cost "cost is {:.2f} change".format(change))
        - I would say this was wrong cause this would only print the COST and the Change instead of each of them
        I fixed this by rewriting the print statement
'''
