"""
Convert to reverse binary

Write a program that takes in a positive integer as input
and outputs a string of 1's and 0's representing the integer in reverse binary. 
For an integer x, the algorithm is:

As long as x is greater than 0
Output x modulo 2 (remainder is either 0 or 1)
Assign x with x divided by 2

Note: The above algorithm outputs the 0's and 1's in reverse order.

Ex: If the input is: 6

the output is: 011

6 in binary is 110; the algorithm outputs the bits in reverse.

"""

def main():
    x = int(input("Give me a Positive Integer: "))
    binlist = []
    while x > 0:
        result = x % 2
        binlist.append(result)
        x = x // 2

    X = binlist.reverse()
    print(binlist)
main()