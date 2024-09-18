import numpy as np

def newtons_method(f, f_prime, x0, tol=1e-7, max_iter=1000):
    """
    Performs Newton's Method to find the root of a function.
    
    Parameters:
    f (function): The function whose root we want to find.
    f_prime (function): The derivative of the function.
    x0 (float): The initial guess for the root.
    tol (float): The tolerance for convergence (default 1e-7).
    max_iter (int): The maximum number of iterations (default 1000).
    
    Returns:
    float: The approximate root.
    int: The number of iterations performed.
    """
    
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            print("Derivative is zero. No solution found.")
            return None, i
        
        # Update using Newton's method formula
        x_new = x - fx / fpx
        
        # Check if the update is within tolerance
        if abs(x_new - x) < tol:
            return x_new, i + 1
        
        x = x_new
    
    print("Maximum number of iterations reached. Solution may not have converged.")
    return x, max_iter

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x

x0 = 1.0

root, iterations = newtons_method(f, f_prime, x0)

if root is not None:
    print(f"Root found: {root} in {iterations} iterations.")