# ODE Slope Fields Plotter

This program is responsible for taking a user input which represents the slope of function y or the ordinary differential equation that needs solving in order to provide some qualitative information using slope fields. Using sympy and matplotlib, we plot this slope field after evluating the expression and defining variables. I plan on expanding this into Euler's method to provide an alternative approach that uses numerical methods instead.

## Features
- **Simplifies Expression using Sympy**: User is prompted to input a ordinary differential equation using variables y and x, which is then simplified into a mathematical expression to be evaluated by sympy and the rest of the progam
- **Calculates Tangent Lines across X-range**: Over the grid of (-10,10) for y and x values, each possible point has their corresponding slope field line computed and saved into a list
- **Plots all Points, Lines, Directions**: For all points and lines computed for the range, plot the corresponding slope value with the given length so that afterwards you have an entire slope field for dydx which contains qualitative information about the function without numerical analysis 

## Installation

Clone the repository available here [ODE Slope Field Plotter](https://github.com/toritotony/ODE-Slope-Fields).

## Usage

1. Create a virtual environment to isolate the packages being installed in Step 2.
2. Run the command: python slope-field.py
3. Input the ordinary differential equation (dy/dx) 
4. Allow program to compute tangent line for entire grid and display plot for you to observe and potentially download

## Noteable Code Snippet

### Compute and append points and slopes to array for plotting ('slope-field.py')
```
for i in x_range:
    for j in y_range:
        try:
            slope = f(i, j)
        except Exception as e:
            print(f"Error evaluating the function at ({i}, {j}): {e}")
            continue
        pointSlope.append((i, j, slope))
```

## Dependencies

- **sympy**
- **matplotlib**
- **re**
- **numpy**

## Contributing
Contributions and feedback are welcome, especially for those looking to code up some mathematical functions for me to add onto this and expand into a general purpose tool for fellow classmates! Please open an issue to discuss your proposed changes before submitting a pull request. Ensure that all new code is properly tested and documented. 

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit)

