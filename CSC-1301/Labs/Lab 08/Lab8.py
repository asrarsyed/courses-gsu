#   CSCI 1301 – Section: 002
#   Python Lab 8

''' 
Purpose:
    Get these functions working properly
Pre-conditions:
    None - but we can add one if needed
Post-conditions:
    Returns should be test conditon returns - all are lists
'''


def makelist(number):
    num_list = list()  # Variable to store list

    for i in range(0, number):  # Loop to add numbers to the list
        num_list.append(i)

    return num_list  # Returns the list


print(makelist(10))  # Printing some Tests for output
print(makelist(3))
print()  # Empty line so terminal read is easier


def rocketcountdown(number):
    num_list = list()  # Variable to store list

    # Loop (in range where we start at 1 instead of 0) to insert numbers to the list
    for i in range(1, number + 1):
        # Inserts i at the index 0 (so every time it loops a new number is at 0)
        num_list.insert(0, i)
    # Appending a statement at the very end
    num_list.append('We have lift off!')

    return num_list  # Returns function


print(rocketcountdown(10))  # Printing some Tests for output
print()  # Empty line so terminal read is easier


def doubleloop(num1, num2):
    list = []  # Variable to store list
    for i in range(num1):
        for j in range(num2):
            list.append('{}:{}'.format(i, j))
    return list


print(doubleloop(2, 2))  # Printing some Tests for output
print(doubleloop(3, 4))
