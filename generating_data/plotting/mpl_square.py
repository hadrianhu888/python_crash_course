
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Square of Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()
plt.savefig(os.path.join('images', 'mpl_square.png'), bbox_inches='tight')
