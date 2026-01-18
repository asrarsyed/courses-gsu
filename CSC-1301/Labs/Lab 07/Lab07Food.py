#   CSCI 1301 – Section: 002
#   Python Lab 7

''' 
Purpose:
    Offer the user a choice of food items, calculate total bill

Pre-conditions:
    User enters 5 or 6 y's or n's depending on desired items (strings)

Post-conditions:
    Prompts for choices, total bill before (float) and after tip, (float) and parting message.
'''
def main():
    # name of restaurant
    print("Welcome to Dairy King")

    # give user instructions of expected inputs
    print("Please answer each question with y or n")

    # initialize total bill to zero
    total_bill = 0

    # ask first choice
    if input("Do you want a grilled cheese sandwich? ") == "y":
        total_bill += 7        #add price to total bill 
    if input("Do you want a serving of nachos? ") == "y":
        total_bill += 5 
    if input("Do you want a chicken sandwich? ") == "y":
        total_bill += 8
    while input("Do you want a Hamburger? ") == "y": # While loop to also test the input of getting cheese on burger
        total_bill += 8
        if input("Do you want cheese on that? ") == "y":
            total_bill += 2
        break
    if input("Do you want a hot dog? ") == "y":
        total_bill += 6

    # output blank line 
    print()
    # output total bill before tip 
    print(f"The total for your food is ${total_bill:.2f}")
    print(f"The total with 20% tip is ${(total_bill * .2) + total_bill:.2f}")
    print("Thank you for your business!")

main()

#! [x]