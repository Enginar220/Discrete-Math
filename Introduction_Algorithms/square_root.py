# Write a function that takes square root of a number without using any built-in function.

def square_root(n):
    """
    Calculates the square root of a number without using built-in functions.
    
    Args:
    n (float): The number to calculate the square root of.
    
    Returns:
    float: The square root of the given number.
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    elif n == 0:
        return 0
    
    # Initial guess
    x = n / 2
    
    # Iterate until a satisfactory accuracy is achieved
    while True:
        # Calculate the next approximation using the Newton-Raphson method
        new_x = 0.5 * (x + n / x)
        # If the new approximation is close enough to the old one, return it
        if abs(x - new_x) < 1e-6:
            return new_x
        # Otherwise, use the new approximation for the next iteration
        x = new_x


print(square_root(35))