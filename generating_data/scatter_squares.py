import matplotlib.pyplot as plt

plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title('Scatter Plot', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
plt.savefig(os.path.join('images', 'scatter_plot.png'), bbox_inches='tight')
