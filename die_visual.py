from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = [die.roll() for el in range(1000)]

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title='Result of rolling D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
