import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import re

init_printing(use_latex=True)

# ONLY ACCEPTS AUTONOMOUS SYSTEM OF TWO ODEs
# Get the ODE input from the user and give instructions
dxdt = input("Type the ODE using t and x as independent and dependent vars, (+) for adding, (-) for subtracting, (/) for dividing, (*) for multiplication, (** or ^) for exponentiation, (e) for exponential, and any trigonometric functions as spelled, be careful with parentheses for isolating expressions: ")
dydt = input("Type the ODE using t and y as independent and dependent vars, (+) for adding, (-) for subtracting, (/) for dividing, (*) for multiplication, (** or ^) for exponentiation, (e) for exponential, and any trigonometric functions as spelled, be careful with parentheses for isolating expressions: ")

# Substitute e^x with exp(x) for sympy's exp function to work with sympy's sympify function
pattern1 = r'\b[eE](?:\^|\*\*)(\S+)'
dxdt = re.sub(pattern1, r'exp(\1)', dxdt)
dydt = re.sub(pattern1, r'exp(\1)', dydt)

# Substitute e with exp(1) for sympy's exp function to work with sympy's sympify function
pattern2 = r'\b[eE]\b(?!\^|\*\*)'
dxdt = re.sub(pattern2, r'exp(1)', dxdt)
dydt = re.sub(pattern2, r'exp(1)', dydt)
print(f"Altered system: {dxdt} and {dydt}")

# Simplify and display to user
try:
    x, y = symbols('x y')
    expressionOutputdx = sympify(dxdt, convert_xor=True)  # convert_xor converts ^ to **
    expressionOutputdy = sympify(dydt, convert_xor=True)  # convert_xor converts ^ to **

    print(f"Sympified system: {expressionOutputdx} and {expressionOutputdy}")
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Evaluate the expression given the known variables and sympy built in mathematical objects
try:
    expressiondx = parse_expr(dxdt, {"x": x, "y": y})
    expressiondy = parse_expr(dydt, {"x": x, "y": y})
except (SyntaxError, TypeError) as e:
    print(f"Invalid input: {e}")
    exit()

# Convert into callable function (emulates lambda function)
try:
    f1 = lambdify((x, y), expressiondx)
    f2 = lambdify((x, y), expressiondy)
except Exception as e:
    print(f"Error converting the expression to a function: {e}")
    exit()

pointSlope = []
x_range = np.arange(-10, 11)
y_range = np.arange(-10, 11)

for i in x_range:
    for j in y_range:
        try:
            slope1 = f1(i, j)
            slope2 = f2(i, j)
            #vector = np.sqrt(slope1**2 + slope2**2)
            pointSlope.append((i, j, slope1, slope2))
        except Exception as e:
            print(f"Error evaluating the function at ({i}, {j}): {e}")
            continue

# IDEA - In the future I can color arrows with a gradient based on the slope 
try: 
    plt.figure(figsize=(8, 6))
    dt = 0.5
    for (i, j, slope1, slope2) in pointSlope:
        dx = slope1 * dt
        dy = slope2 * dt
        plt.arrow(i, j, dx, dy, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
except Exception as e:
    print(f"Error plotting slope field: {e}")

plt.xlabel('x')
plt.ylabel('y')
plt.title('System Slope Field')
plt.grid(True)
plt.legend(["System Slope Field"])
plt.show()