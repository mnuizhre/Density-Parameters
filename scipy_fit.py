import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from numpy import genfromtxt

pth = 'made.csv'


mn= genfromtxt(pth, delimiter=',')
print(np.shape(mn))
x = mn[1:,2]
y = mn[1:,24]

#plt.scatter(x, y)
m = (mn[1:,5])*(mn[1:,24])

plt.errorbar(x,y, yerr=m, fmt="o", label = "Original Observation data")


def SQfunction(x,a,b):
      return a*x**2+b*x
constants = cf(SQfunction,x,y)
a_fit = constants[0][0]                 
b_fit = constants[0][1]

fit = []
for i in x:
  fit.append(SQfunction(i,a_fit,b_fit))



plt.plot(x,fit,c='k',label="Fit")
plt.legend()
plt.xlabel("z")
plt.ylabel("$d_L$")
plt.title("Fitting the data using SciPy for $ax^2 + b$")
plt.show()
print(constants)
constants = op, cov
