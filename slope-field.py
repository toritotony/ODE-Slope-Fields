import matplotlib
import matplotlib.pyplot as plt
import regex as re

dydx = input(prompt='please input the ODE')

dydx = str(dydx).lower().replace('t', 'x').replace('p', 'y')
