import lagrange
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 4])
y = np.array([1, 2, 5])

input_x = np.sort(np.random.rand(100) * 6 - 1)

ans = lagrange.lagrange(x, y, input_x)

plt.scatter(x, y)
plt.plot(input_x, ans)
plt.show()
