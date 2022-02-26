# plot a polynomial of degree 1, f(x) = 4*x-4-32 using matplotlib

import numpy as np
from matplotlib import pyplot as plt


x_lower_limit = -10
x_upper_limit = 10
x = np.linspace(x_lower_limit, x_upper_limit, num=100)

y = 4 * x + 4 - 36

y_lower_limit = -10
y_upper_limit = 10

############

fig, ax = plt.subplots()
ax.plot(x, y, )

plt.axhline(color='black')
plt.axvline(color='black')

plt.xlabel('$x$')
plt.ylabel('$y$')

ax.spines['top'].set_color('none')  #
ax.spines['bottom'].set_position('zero')

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')

ax.set_xlim([x_lower_limit, x_upper_limit])
ax.set_ylim([y_lower_limit, y_upper_limit])

ax.set_xticks(range(x_lower_limit, x_upper_limit, 1))
ax.set_yticks(range(y_lower_limit, y_upper_limit, 1))

plt.grid()
plt.show()
