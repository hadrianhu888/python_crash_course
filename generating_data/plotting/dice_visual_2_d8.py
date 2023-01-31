from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and a D10

die = Die(8)
die1 = Die(10)

# Make some rolls and store the results in a list

results = []
for roll_num in range(1000):
    result = die.roll() + die1.roll()
    results.append(result)

print(results)

# Analyze the results

frequencies = []
max_result = die.num_sides + die1.num_sides
for value in range(1, die.num_sides + die1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results

x_values = list(range(1, die.num_sides + die1.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
