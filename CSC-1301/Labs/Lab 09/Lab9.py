#   CSCI 1301 – Section: 002
#   Python Lab 9

''' 
Purpose:
    Create 6 functions and test them
Pre-conditions:
    Setting user_input to a starter value
Post-conditions:
    Output from running the test conditions
'''

# Step 1 - Initialize the starting input
user_input = "FFFFFF"

# Step 2 - Create get the Red value function
def get_red(user_input):
    return int(user_input[0:2], 16)

# Step 3 - Create get the Green value function
def get_green(user_input):
    return int(user_input[2:4], 16)

# Step 4 - Create get the Blue value function
def get_blue(user_input):
    return int(user_input[4:6], 16)

# Step 5 - Function testing if Red value is less than 65
def id_protanopia(user_input):
    if get_red(user_input) < 65:
        return True
    else:
        return False

# Step 6 - Function testing if Green value is less than 65
def id_deuteranopia(user_input):
    if get_green(user_input) < 65:
        return True
    else:
        return False

# Step 7 - Function testing all the values i.e. Blue value, Red value, Green value
def id_tritanopia(user_input):
    if get_blue(user_input) > 0 and get_red(user_input) > 230 and get_green(user_input) > 230:
        return False
    else:
        return True

# Step 8 - All of the Function tests
def run_tests():
    print (get_red ('FFAAAAA')) # Red Function test

    print (get_green ('4d6285')) # Green Function test

    print (id_protanopia ('362436')) # Id Protanopia function test where Red is less than 65
    print (id_protanopia ('ABCDEF'))  # Id Protanopia function test where Red is greater than 65

    print (id_deuteranopia ('362436')) # Id Deuteranopia function test where Green is less than 65
    print (id_deuteranopia ('ABCDEF')) # Id Deuteranopia function test where Green is greater than 65

    print (id_tritanopia ('362436')) # Id Tritanopia function test where conditions are not met (aka true)
    print (id_tritanopia ('FAFB12')) # Id Tritanopia function test where conditions are met (aka false)

# Calling Test Function
run_tests()
