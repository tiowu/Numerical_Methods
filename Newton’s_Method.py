import math

def f(x):
    return math.sin(x) - 0.5 * x  
    # return math.sqrt(math.cos(x)) - x  
    # return math.tan(x) - 2 * x 
    # return 5 * x**3 + 5 * x**2 + 4
    # return math.exp(x) - 5.5 * x
    # return math.exp(3 * x) + 5 * x - 2
    # return x**3 + x + 2
    # return x**2 - 7 * x + 10  

def f_prime(x):
    return math.cos(x) - 0.5  
    # return -0.5 * math.sin(x) / math.sqrt(math.cos(x)) - 1 
    # return 1 / math.cos(x)**2 - 2 
    # return 15 * x**2 + 10 * x
    # return math.exp(x) - 5.5
    # return 3 * math.exp(3 * x) + 5
    # return 3 * x**2 + 1
    # return 2 * x - 7  

x0 = 0/5

def newtons_method(x0, tolerance=1e-6, max_iterations=100):
    x_n = x0
    for n in range(max_iterations):
        f_xn = f(x_n)
        f_prime_xn = f_prime(x_n)
        
        if abs(f_prime_xn) < 1e-10:
            print("Derivative too small. Stopping iteration.")
            return None
        
        x_n1 = x_n - f_xn / f_prime_xn
        
        print(f"Iteration {n+1}: x = {x_n1:.6f}, f(x) = {f(x_n1):.6f}")
        
        # Check if the result is within the tolerance level
        if abs(x_n1 - x_n) < tolerance:
            return x_n1
        
        x_n = x_n1
    
    print("Max iterations reached without convergence.")
    return None

approximate_root = newtons_method(x0)

if approximate_root is not None:
    print(f"\nThe root is approximately x = {approximate_root:.6f}")
else:
    print("\nNewton's method did not converge.")