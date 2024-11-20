x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

n = len(x)

xp = float(input("Enter the value of x: "))

yp = 0.0

#do Lagrange interpolation
for i in range(n):
    L = 1.0  #initialize the Lagrange basis polynomial
    for j in range(n):
        if j != i:
            L *= (xp - x[j]) / (x[i] - x[j])  #compute L_i(x)
    yp += y[i] * L  #add contribution of L_i(x) to yp

print(f"For x = {xp:.1f}, the interpolated y = {yp:.1f}")