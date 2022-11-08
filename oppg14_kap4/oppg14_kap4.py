__author__ = 'Johannes Fjeldså'
__email__ = 'johannes.larsen.fjeldså@nmbu.no'

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-1, 1000, 10000)
y_vals = [(x + 1)**(1/4) for x in x_vals]


plt.plot(x_vals, y_vals, label=r'$y = \sqrt[4]{x+1}$')
plt.grid()
plt.legend()
plt.show()