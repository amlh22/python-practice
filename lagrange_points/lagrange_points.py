import numpy as np
import matplotlib.pyplot as plt

#Defining data variables
G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
w = 2.662e-6
E_r = 6371e3
Mn_r = 1737e3
Dist = R - Mn_r

#|——————————————————————————————————————————————————————————|#
#|                                                          |#
#|          Calculation of Lagrange Point Distance          |#
#|                                                          |#
#|——————————————————————————————————————————————————————————|#

#Setting accuracy
acc = 100

#Setting up the equation
def f(r):
    return G * M / r**2 - G * m / (R - r)**2 - w**2 * r

#Choosing initial guesses
r1 = 1e7
r2 = 2e7

guess_no = 0

while np.fabs(r2 - r1) > acc:
    if f(r2) - f(r1) == 0:
        print(r2)
    r3 = r2 - f(r2) * (r2 - r1) / (f(r2) - f(r1))
    r1 = r2
    r2 = r3
    guess_no += 1

print("The distance to Lagrange point L1 is: {:.3e}m".format(r3))
print("Number of iterations required: {}\n".format(guess_no))

#Re-defining the function to be plotted, with relevant x- and y-values
def g(r):
    return G * M / r**2 - G * m / (R - r)**2

x = np.linspace(E_r, Dist, 300)
y = g(x)

plt.plot(x, y)

plt.xlim(0, 4e8)
plt.ylim(-2, 10.5)
plt.show

plt.title('Gravitational Field Strength as a Function of Distance')
plt.xlabel('Distance [m]')
plt.ylabel('Gravitational Field Strength [ms^-2]')

print("The field strength at the surface of the Earth is: {:.3}ms^-2".format(g(E_r)))
print("The field strength at the surface of the Moon is: {:.3}ms^-2".format(abs(g(Dist))))
