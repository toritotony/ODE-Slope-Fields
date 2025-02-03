import matplotlib.pyplot as plt
import re
import math
import numpy as np
from sympy import symbols, sympify, parse_expr, lambdify, init_printing

init_printing(use_unicode=True)

# Get the ODE input from the user and give instructions
dydx = input("Type the ODE using x and y as ind and dep vars, + for adding, - for subtracting, / for dividing, * for multiplication, ** for exponentiation, capturing any isolated expressions within parentheses: ")

# Simplify and display to user
try:
    expressionOutput = sympify(dydx)
    print("Sympified expression:", expressionOutput)
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Define variables and evaluate the expression with these in mind
try:
    x, y = symbols('x y')
    expression = parse_expr(dydx, {"x": x, "y": y})
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Convert into callable function (emulates lambda function but converts to numpy uses math otherwise)
try:
    f = lambdify((x, y), expression, 'numpy')
except Exception as e:
    print(f"Error converting the expression to a function: {e}")
    exit()

pointSlope = []
x_range = np.arange(-10, 11)
y_range = np.arange(-10, 11)

for i in x_range:
    for j in y_range:
        try:
            slope = f(i, j)
        except Exception as e:
            print(f"Error evaluating the function at ({i}, {j}): {e}")
            continue
        pointSlope.append((i, j, slope))


plt.figure(figsize=(8, 6))
for (i, j, slope) in pointSlope:
    dx = 0.5
    dy = slope * dx
    plt.arrow(i, j, dx, dy, head_width=0.2, head_length=0.2, fc='blue', ec='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Slope Field')
plt.grid(True)
plt.legend(["Slope Field"])
plt.show()
