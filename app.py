# app.py

def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def is_positive(number):
    """Checks if a number is positive."""
    return number > 0

# Intentionally buggy function for a failing test
def multiply(a, b):
    """
    Multiplies two numbers.
    NOTE: This function is intentionally buggy for demonstration.
    It performs addition instead of multiplication.
    """
    return a + b # This is wrong, should be a * b

if __name__ == "__main__":
    print(greet("World"))
    print("Welcome to my simple application.")
    print(f"Sum of 2 and 3: {calculate_sum(2, 3)}")
    print(f"Is 5 positive? {is_positive(5)}")
    print(f"Product of 2 and 3 (buggy): {multiply(2, 3)}")






