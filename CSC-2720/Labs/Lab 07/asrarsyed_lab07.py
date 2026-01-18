# Course Section: CSC 2720-012

'''
Assignment: Implement three methods in Python that handle hashing and compression for different types of keys

hash(key):
    This function generates a unique number (called a hash) based on the type of the key.
    
    If the key is:
        An integer: return the number itself.
        A float: return the whole number part of the float.
        A string: calculate a special number using a polynomial hash (this is just a formula to convert a string into a number).
        A custom object: calculate a polynomial hash using the memory address of the object (which you can get with id() in Python).
        Any other type: print an error saying "The provided key is not hashable!".

compress_division(hash_code, N):
    This function takes a hash code and compresses it into a smaller number (an index) by dividing the hash by N.
    It then returns the remainder and is called the "division method."

compress_MAD(hash_code, a, b, p, N):
    This function also compresses the hash code but uses the MAD (Multiply-Add-And-Divide) method.
    It multiplies the hash code by a, adds b, divides by p, and then takes the remainder when divided by N.

Limitations: Do not use the built-in ‘hash()’ method in any of your functions.
'''

# A dictionary that maps the types to inline functions (lambdas) that handle hashing
hash_functions = {
    int: lambda typeKey: typeKey,  # If the key is an integer, return it directly
    float: lambda typeKey: int(typeKey),  # If the key is a float, return the integer part
    str: lambda typeKey: sum(ord(char) * (31 ** i) for i, char in enumerate(typeKey)),  # Polynomial hash for strings
    object: lambda typeKey: sum(ord(char) * (31 ** i) for i, char in enumerate(str(id(typeKey)))),  # Polynomial hash for object's memory address (converted to a string)
}

# Uses the dictionary to find the appropriate hash logic
def hash_key(key):
    key_type = type(key)
    if key_type in hash_functions:
        return hash_functions[key_type](key)
    elif hasattr(key, '__dict__'):  # For custom objects, hashing based on the object’s ID
        return sum(ord(char) * (31 ** i) for i, char in enumerate(str(id(key))))
    else:
        print("The provided key is not hashable!")
        return None

def compress_division(hash_code, N):
    return hash_code % N


def compress_MAD(hash_code, a, b, p, N):
    return ((hash_code * a + b) // p) % N

key1 = 123
key2 = 45.67
key3 = "example"

class A:
    def __init__(self, id):
        self.id = id

key4 = A(1)  # an object of a custom type

# Hash values
print('Hash codes: ')
print(hash_key(key1))  # 123
print(hash_key(key2))  # 45.0
print(hash_key(key3))  # Polynomial hash for the string "example"
print(hash_key(key4))  # Polynomial hash for the memory address of the object

# Compression examples
hash_code = 12345
print('Hash table index: ',compress_division(hash_code, 100))  # Division method
print('Hash table index: ',compress_MAD(hash_code, 2, 3, 10007, 100))  # MAD method