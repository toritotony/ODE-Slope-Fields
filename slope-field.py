import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import re

init_printing(use_latex=True)

# Get the ODE input from the user and give instructions
dydx = input("Type the ODE using x and y as independent and dependent vars, (+) for adding, (-) for subtracting, (/) for dividing, (*) for multiplication, (** or ^) for exponentiation, (e) for exponential, and any trigonometric functions as spelled, be careful with parentheses for isolating expressions: ")

# Substitute e^x with exp(x) for sympy's exp function to work with sympy's sympify function
pattern = r'\b[eE](?:\^|\*\*)(\S+)'
dydx = re.sub(pattern, r'exp(\1)', dydx)
print(f"Altered expression: {dydx}")

# Simplify and display to user
try:
    x, y = symbols('x y')
    expressionOutput = sympify(dydx, convert_xor=True)  # convert_xor converts ^ to **
    print("Sympified expression:", expressionOutput)
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Evaluate the expression given the known variables and sympy built in mathematical objects
try:
    expression = parse_expr(dydx, {"x": x, "y": y})
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Convert into callable function (emulates lambda function)
try:
    f = lambdify((x, y), expression)
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
            pointSlope.append((i, j, slope))
        except Exception as e:
            print(f"Error evaluating the function at ({i}, {j}): {e}")
            continue

# IDEA - In the future I can color arrows with a gradient based on the slope 
try: 
    plt.figure(figsize=(8, 6))
    for (i, j, slope) in pointSlope:
        dx = 0.5
        dy = slope * dx
        plt.arrow(i, j, dx, dy, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
except Exception as e:
    print(f"Error plotting slope field: {e}")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Slope Field')
plt.grid(True)
plt.legend(["Slope Field"])
plt.show()
