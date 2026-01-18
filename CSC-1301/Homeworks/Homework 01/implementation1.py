# Prolog
    # Section: 002

'''
Purpose: 
    Too calculate the wafer area & how many dies can be cut correcting for wasted material near the edges.
    (A wafer is a very thin circular slice of purified silicon that has many chips or dies.)
Pre-conditions (input):
    The diameter of the wafer in (mm) and the area of a die, the chip size in (mm^2).
Post-conditions (output):
    The area of the wafer in (mm^2) as well the the number of dies cut from a single wafer(the answer that program seeks).
'''
 
# 1) Defining the main function
def main():

    # 2) Importing math, so various math functions for (pi)
    import math
   
    # 3) Displaying an introductory message to identify the program, and a blank line
    print("Calculating the amount of dies that can be cut from a Wafer.")
    print()

    # 4) Collecting the 2 input variables
    #Given the diameter of the silicon wafer in millimeters (mm)
    waferDiameter = float(input("What is the diameter of the wafer? (mm) "))
    #Given the area of one individual chip (die) in square millimeters (mm^2)
    dieArea = float(input("What is the area of a single die? (mm^2) "))

    # 5) Getting the area of wafer
    radius = waferDiameter / 2
    waferArea = math.pi * radius ** 2

    # 6) Calculating the final dies that can be cut
    DiesPerWafer = (waferArea / dieArea) - ((math.pi * waferDiameter) / (math.sqrt(2*dieArea)))

    # 7) Printing the results from test cases above / formating the entire program
    print(f'From a wafer with area {waferArea:.2f} square millimeters you can cut {math.floor(DiesPerWafer)} dies')

# 8) Closing main
main()
