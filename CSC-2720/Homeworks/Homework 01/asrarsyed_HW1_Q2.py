# Course Section: CSC 2720-012

"""
Assignment: Implementing backward and forward buttons of browser using stacks.
            Create as python console application
"""


class BrowserNavigator:
    def __init__(self):
        self.currentPage = None  # current page being viewed
        self.forwardStack = []  # track forward navigation history
        self.backwardStack = []  # track backward navigation history

    def back(self):  # Handles the BACK command
        # If backward history is empty, nothing to go back to
        if not self.backwardStack:
            print("Ignored")
            return

        # Save current page to forward stack and move back to the previous page
        self.forwardStack.append(self.currentPage)
        self.currentPage = self.backwardStack.pop()  # Set the previous page as current
        print(self.currentPage)

    def forward(self):  # Handles the FORWARD command
        # If forward history is empty, nothing to move forward to
        if not self.forwardStack:
            print("Ignored")
            return

        # Save current page to backward stack and move forward to the next page
        self.backwardStack.append(self.currentPage)
        self.currentPage = self.forwardStack.pop()  # Set the next page as current
        print(self.currentPage)

    def visit(self, url):  # Handles the VISIT command
        # Validate the URL (should not be empty, too long, or contain spaces)
        if not url:
            print("Error: URL is required for VISIT command")
            return

        if len(url) > 50:  # URL must not exceed 50 characters
            print("Error: URL must not exceed 50 characters")
            return

        if " " in url:  # URL should not contain whitespace
            print("Error: URL must not contain whitespace")
            return

        # Save current page to backward stack before navigating to a new URL
        if self.currentPage:
            self.backwardStack.append(self.currentPage)

        # Set the new URL as the current page and clear the forward stack
        self.currentPage = url
        self.forwardStack.clear()  # Clear forward history since a new page was visited
        print(self.currentPage)


def main():
    # Initialize the browser navigation system
    browser = BrowserNavigator()

    while True:
        try:
            # Read the user input and split it into command and arguments
            command = input().strip().split()

            if not command:
                print("Error: Empty command")
                continue  # Skip processing if the input is empty

            # Extract the action (BACK, FORWARD, VISIT, or QUIT)
            action = command[0].upper()

            if action == "QUIT":
                break  # Exit the loop and quit the program
            elif action == "BACK":
                browser.back()  # Handle BACK command
            elif action == "FORWARD":
                browser.forward()  # Handle FORWARD command
            elif action == "VISIT":
                if len(command) < 2:  # Ensure a URL is provided for VISIT
                    print("Error: URL is required for VISIT command")
                    continue
                browser.visit(command[1])  # Pass the URL to the visit function
            else:
                print("Error: Invalid command")  # Handle unrecognized commands

        except EOFError:
            break  # End the loop if EOF is reached
        except Exception as e:
            print(f"Error: {str(e)}")  # Handle unexpected errors during execution


if __name__ == "__main__":
    main()
