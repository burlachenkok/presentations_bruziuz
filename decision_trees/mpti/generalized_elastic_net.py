#!/usr/bin/env python
# generalized_elastic_net.py 

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 10.0, 0.001)

beta = 0.01
y = np.log((1.0 - beta)*np.abs(x) + beta)
plt.plot(x, y, 'g-', label='generalized EN beta=' + str(beta))

beta = 0.2
y = np.log((1.0 - beta)*np.abs(x) + beta)
plt.plot(x, y, 'r-', label='generalized EN beta=' + str(beta))

beta = 0.5
y = np.log((1.0 - beta)*np.abs(x) + beta)
plt.plot(x, y, 'b-', label='generalized EN beta=' + str(beta))

beta = 0.95
y = np.log((1.0 - beta)*np.abs(x) + beta)
plt.plot(x, y, 'c-', label='generalized EN beta=' + str(beta))

plt.xlim(0, 10)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel('a')
plt.ylabel('$P_b(a)$')
plt.legend(loc='upper left')
plt.grid(True)
plt.title('Generalized Elastic Net plots')
plt.show()


