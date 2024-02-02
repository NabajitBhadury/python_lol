import matplotlib.pyplot as plt
import numpy as np

secion_number = 10
marks_generator = np.random.uniform(0.0, 10.0, secion_number)

plt.bar(range(1, secion_number + 1), marks_generator)
plt.show()
