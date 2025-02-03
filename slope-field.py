import matplotlib
import matplotlib.pyplot as plt
import regex as re
import math

dydx = input(prompt='please input the ODE')

dydx = str(dydx).lower().replace('t', 'x').replace('p', 'y')

# somehow correlate string combinations using regex in order to conduct arithmetic on each point
# get every instance of the equation that isn't y or x and convert it to a math module variable (e, pi, inf, nan, etc.)
# every instance of two atrics should correlate to the power function 
# every instance of one astrics or paranthesis will indicate multiplication
# parantheses close equations so that they're done before outside 
# every instance of a slash should divide left to right or use paranthesis
# follow pemdas rule to computer correctly 

# give a zipped collection of y's and x's and dydx's, compute each value of dy/dx and save that in a new list where y, x, and dy/dx value are saved

# plot each point in the list on the same coordinate plane and output to user 
# over a range of t and as delta t is approaching 0 but not too small since lots of compute power

print("Here's your plotted slope field")