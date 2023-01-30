import matplotlib.pyplot as plt
import os
import numpy as np


plt.style.use('seaborn-darkgrid')
x_axis = range(1, 5000)
y_axis = [x**3 for x in x_axis]
fig, ax = plt.subplots()
fig = plt.scatter(x_axis, y_axis, c=y_axis, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title('Scatter Plot', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

plt.savefig(os.path.join('images', 'scatter_plot.png'), bbox_inches='tight')
