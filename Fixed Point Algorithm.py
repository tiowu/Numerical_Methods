import math

def g(x):
    return math.sqrt(2 + x)

def fixed_point_algorithm(x1, max_iterations):
    x_n = x1
    for n in range(1, max_iterations + 1):
        x_n_plus_1 = g(x_n)
        print(f"x_{n+1} = {x_n_plus_1:.6f}")
        x_n = x_n_plus_1

x1 = 1
max_iterations = 7

fixed_point_algorithm(x1, max_iterations)

'''
x_2 = 1.732051
x_3 = 1.931852
x_4 = 1.982890
x_5 = 1.995718
x_6 = 1.998929
x_7 = 1.999732
x_8 = 1.999933
'''