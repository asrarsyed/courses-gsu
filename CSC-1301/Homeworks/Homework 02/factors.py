#   CSCI 1301 – Section: 002
#   Python Homework 2
'''
  Purpose:
    To find all of the factors of a integer that is taken from user.
  Pre-conditions (input): 
    The inputs could be a positive or negative integer.
  Post-conditions (output): 
    A list containing all the possible factors of the integer.
'''

# main function - Implementation
 
  # Defining the main function
def main():

  # Importing the helper module
  import helper

  # Displaying an introductory message
  print("\t*** findingFactors ***")
  print()

  # Collecting the integer input variables
  num = int(input("Please provide an integer "))

  # Defining the ‘foundFactors’ functions
  def foundfactors(x):

    if len(x) == 2:
      firstval = (f"Integer {num} is a prime number.")
      return firstval

    else:
      secondval = (f"Integer {num} is not a prime number.")
      return secondval

  # Checking if positive integer and printing the factor list
  if (num > 0):
    factor_list = helper.findingFactors(num)
    print("")
    print(f"The factors of integer {num} are:{factor_list}.")
    print("")
    print(foundfactors(factor_list))

  # Checking if positive or negative
  if (num <= 0):
    print()
    print(f"The integer {num} has no factors.")

  # Call the main function
main()

  # End of Program
