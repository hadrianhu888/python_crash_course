import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Make a new random walk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    # Plot the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               c='red', edgecolors='none', s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    plt.savefig('rw_visual.png', bbox_inches='tight')
