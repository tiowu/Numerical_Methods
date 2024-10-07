import math

def g(x):
    return 2.2 * math.cos(x)

def fixed_point_method(x1, max_iterations, tolerance):
    x_n = x1
    for n in range(1, max_iterations + 1):
        x_n_plus_1 = g(x_n)
        print(f"Iteration {n}: x_{n+1} = {x_n_plus_1:.6f}")
        
        # Check for convergence
        if abs(x_n_plus_1 - x_n) < tolerance:
            print(f"Converged to {x_n_plus_1:.6f} after {n} iterations.")
            return x_n_plus_1
        x_n = x_n_plus_1
    
    print("Maximum iterations reached without convergence.")
    return x_n

x1 = 2
max_iterations = 50
tolerance = 1e-6

fixed_point_method(x1, max_iterations, tolerance)