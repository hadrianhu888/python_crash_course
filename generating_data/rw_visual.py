import os
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a new random walk
rw = RandomWalk(50)
rw.fill_walk()

# Plot the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

# Emphasize the first and last points

plt.show()
plt.savefig(os.path.join('images', 'rw_visual.png'), bbox_inches='tight')
