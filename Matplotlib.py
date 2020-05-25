import matplotlib.pyplot as plt
import numpy as np
from random import sample

x = np.linspace(0,5,11)

data = [np.random.normal(0, std, 100) for std in range(1,4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.show()