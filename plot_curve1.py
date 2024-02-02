import matplotlib.pyplot as plt
import numpy as np

plot_values = np.arange(1, 100)

O_n_plots = plot_values
O_n_square_plot = plot_values ** 2

plt.plot(plot_values, O_n_plots, label='O(n)')
plt.plot(plot_values, O_n_square_plot, label='O(n^2)')
plt.xlabel("n")
plt.ylabel("Operations")
plt.title('Function plotting')

plt.legend()
plt.show()
