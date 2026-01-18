# Course Section: CSC 2720-012

"""
Assignment: Create a secure system  to store and compare user passwords using a hash table. To achieve this, follow these requirements:
"""

from hashlib import sha256
from typing import Dict, Union


class PasswordManager:
    # Initializing a hash table (python dictionary) to store usernames and hashed passwords.
    def __init__(self) -> None:
        self.hash_table: Dict[str, str] = {}

    # Hashes a password using SHA-256.
    def hash_password(self, password: str) -> str:
        sha256_hash = sha256()
        # Convert password to bytes and hash
        sha256_hash.update(password.encode("utf-8"))
        return sha256_hash.hexdigest()

    # Save a new username and hashed password to the store.
    def save_password(self, username: str, password: str) -> str:
        if username in self.hash_table:
            return f"Error: Username '{username}' is already taken."

        hashed_password = self.hash_password(password)
        self.hash_table[username] = hashed_password
        return f"Password saved for user: {username}"

    # Compare provided password with stored password for given username.
    def compare_password(self, username: str, password: str) -> Union[bool, str]:
        if username not in self.hash_table:
            return f"Error: Username '{username}' not found."

        hashed_input_password = self.hash_password(password)
        return self.hash_table[username] == hashed_input_password

    # Change a user's password if current password is correct.
    def change_password(self, username: str, current_password: str, new_password: str) -> str:
        if username not in self.hash_table:
            return f"Error: Username '{username}' not found."

        if not self.compare_password(username, current_password):
            return "Error: Current password is incorrect."

        hashed_new_password = self.hash_password(new_password)
        self.hash_table[username] = hashed_new_password
        return "Password changed successfully."


# Test function to verify the password managers functionality.
def test_password_manager() -> None:
    manager = PasswordManager()

    # Test saving passwords
    print(manager.save_password("user1", "mypassword123"))  # Expected: Password saved for user: user1
    print(manager.save_password("user1", "newpassword456"))  # Expected: Error: Username 'user1' is already taken.
    print(manager.save_password("user2", "securepassword456"))  # Expected: Password saved for user: user2

    # Test comparing passwords
    print(manager.compare_password("user1", "mypassword123"))  # Expected: True
    print(manager.compare_password("user1", "wrongpassword"))  # Expected: False
    print(manager.compare_password("user3", "any_password"))  # Expected: Error: Username 'user3' not found.

    # Test changing password
    print(manager.change_password("user1", "mypassword123", "newpassword789"))  # Expected: Password changed successfully.
    print(manager.compare_password("user1", "newpassword789"))  # Expected: True
    print(manager.change_password("user1", "wrongpassword", "newpassword000"))  # Expected: Error: Current password is incorrect.
    print(manager.change_password("user3", "any_password", "newpassword123"))  # Expected: Error: Username 'user3' not found.


if __name__ == "__main__":
    test_password_manager()
