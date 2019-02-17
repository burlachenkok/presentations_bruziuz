#!/usr/bin/env python3
# elastic_net.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 10.0, 0.1)

beta = 2.0
y = (beta-1.0)*0.5*x*x + (2.0-beta)*np.abs(x)
plt.plot(x, y, 'g-', label='EN beta=' + str(beta))

beta = 1.6
y = (beta-1.0)*0.5*x*x + (2.0-beta)*np.abs(x)
plt.plot(x, y, 'r-', label='EN beta=' + str(beta))

beta = 1.1
y = (beta-1.0)*0.5*x*x + (2.0-beta)*np.abs(x)
plt.plot(x, y, 'b-', label='EN beta=' + str(beta))

beta = 1.0
y = (beta-1.0)*0.5*x*x + (2.0-beta)*np.abs(x)
plt.plot(x, y, 'c-', label='EN beta=' + str(beta))

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel('a')
plt.ylabel('$P_b(a)$')
plt.legend(loc='upper left')
plt.grid(True)
plt.title('Elastic Net')
plt.show()

