import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# other ways of presenting the graph with colors

# ax.scatter(x_values, y_values, c='red', s=100)
ax.scatter(x_values, y_values, c='red', s=100)
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

# Set chart title and label axes

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Square Number', fontsize=14)
ax.set_ylabel('Number', fontsize=14)

# Set size of tick labels

ax.tick_params(axis='both', which='major', labelsize=14)

# Automatically save the plot

plt.savefig('squares_plot.png', bbox_inches='tight')
