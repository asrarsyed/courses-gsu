#   CSCI 1301 – Section: 002
#   Python Lab 6
'''
  Purpose:
    To create a piece of code that analyzes the board and tells the players if anyone makes a row.

  Pre-conditions (input): 
    1) The input consists of three lines each with 3 characters.

  Post-conditions (output): 
    1) Depending on the player (X or O), print the winner and clarify what kind of row? - (Horizontal, vertical, or diagonal). 

    2) If neither player has won, you should print out “THIS IS TIE”

'''
def main():
    print("")
    print("Please Enter “X” or “O” with a space in between each in this format --> X O X - OR - O X O")


    row1_input = input("ROW0> ")
    row1_input = row1_input.split()

    row2_input = input("ROW1> ")
    row2_input = row2_input.split()

    row3_input = input("ROW2> ")
    row3_input = row3_input.split()

# 8 Ways to win for X

    # 3 ways to win horizontal
    if row1_input[0] == row1_input[1] == row1_input[2]:
        print(row1_input[0], "IS GOOD IN HORIZONTAL")

    elif row2_input[0] == row2_input[1] == row2_input[2]:
        print(row2_input[0], "IS GOOD IN HORIZONTAL")

    elif row3_input[0] == row3_input[1] == row3_input[2]:
        print(row3_input[0], "IS GOOD IN HORIZONTAL")

    # 3 ways to win vertical
    elif row1_input[0] == row2_input[0] == row3_input[0]:
        print(row1_input[0], "IS GOOD IN VERTICAL")
        
    elif row1_input[1] == row2_input[1] == row3_input[1]:
        print(row1_input[1], "IS GOOD IN VERTICAL")

    elif row1_input [2] == row2_input[2] == row3_input[2]:
        print(row1_input[2], "IS GOOD IN VERTICAL")

    # 2 ways to win diagonal
    elif row1_input[0] == row2_input[1] == row3_input[2]:
        print(row1_input[0], "IS GOOD IN DIAGONAL")



    elif row1_input[2] == row2_input[1] == row3_input[0]:
        print(row1_input[2], "IS GOOD IN DIAGONAL")
# Ways to Tie
    else:
        print("THIS IS A TIE")
    
main()
