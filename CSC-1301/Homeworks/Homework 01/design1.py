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

# main function
 
    # 1) Defining the main function
    # 2) Importing math, so various math functions for (pi)
    # 3) Displaying an introductory message
    # 4) Collecting the 2 input variables
    # 5) Getting the are of wafer
    # 6) Calculating the final dies that can be cut
    # 7) Printing the results from test cases above / formating the entire program
    # 8) Closin main

'''

Specifications NOTES for Implementation

    1) This program uses input; you will have to prompt the user for the inputs. The inputs can be assumed to be floats.

    2) You must use at least one function and one constant from the math library.

    3) Format the calculated wafer area to 2 places.
    
    4) You should have a main function and all code except for the import statement should be inside the main function definition.

    5) Make sure you format the lines of the output as described. The line breaks and the punctuation should be as shown. The output messages should be exactly as given.


    The equation calculates how many dies can be cut and corrects for wasted material near the edges.
    1 - Note that it should give an integer number of dies (you don't want to cut half a die).
    2 - Note that the area of the wafer is NOT an input value.
    You will have to calculate the area of the wafer given the diameter. If you need to, look up the formula for the area of a circle.


                    waferArea        兀waferDiameter
    DiesPerWafer = -----------  -   -----------------
                    dieArea          sqrt(2dieArea)


Where:
DiesPerWafer (the number of dies cut from a wafer) = the answer
waferDiameter = the diameter of the wafer (mm)
dieArea = the chip size (mm2)
waferArea = area of the wafer (mm2) (must be calculated ahead of time)

'''
