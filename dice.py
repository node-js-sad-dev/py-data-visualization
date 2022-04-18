from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

results = []

for rol_num in range(1000):
    result = die_2.roll() + die_1.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title='Results of rolling 2 dies 1000 time',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
