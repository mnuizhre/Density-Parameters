file_pth = 'save.txt'

import pandas as pd
import numpy as np
import scipy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
df = pd.read_csv(file_pth, sep='\s{1,}')
df.columns = [ 'Name of the SN', 'z_cmb', 'z_hel', 'dz', 'm', 'dm' , 'x1' , 'dx1', 'col' , 'dcol' , 'a' , 'b' , 'c', 'd', 'e', 'f','g','h' ]


df['M'] = pd.Series([-19.6 for x in range(len(df.index))]) ########Absolute magnitude of SN
df['dM'] = pd.Series([0.5 for x in range(len(df.index))]) ########Absolute magnitude ERROR of SN
df['5'] = pd.Series([5 for x in range(len(df.index))]) ########Absolute magnitude of SN
df['10'] = pd.Series([10 for x in range(len(df.index))])
M = df['M']
z_hel = df['z_hel']
m = df['m']
df['m-M'] = df['m'] - df['M']
DM = df['m-M']

df['factor'] =( DM  + df['5'] )/df['5']
g = df['factor']
dM = df['dM']
df['d_z'] = df['10'] ** g
d_z = df['d_z']

import matplotlib.pyplot as plt
plt.scatter(z_hel, d_z, label ='fn of d(z)')
  
c = 10**(df['dm'] +dM)

\begin{lstlisting}
def func_01(z, H0, Om): #Defining the function
   #Dl =  (300000/H0)*(1+z)*((1/(Om*(((1+z)**3)-1)+1)))**0.5
   #Dl =  (1/H0)*((1/(Om*(((1+z)**3)-1)+1)))**0.5
   Dl=(1/H0)*((1+z)/((Om*((1+z)**3-1))+1)**0.5)
   return Dl

a = 0 #Entering the limits of integration dl
b = 2
n = 1000000 #No. of iterations
func_02 = 0
dz = (b-a)/n 
res = np.zeros(n)
z = np.linspace(a, b , n) #Vectorisation

for i in range(n):
    func_02 = func_02 + (dz*func_01(z[i]+dz/2, 70./10**13*3.086, 0.3))
    res[i] = func_02    
    
    
plt.plot(z, res/10, label = "dispalcement")    
plt.xlabel("time")
plt.ylabel("y")
plt.legend()
plt.show()








