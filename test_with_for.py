import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn")

flg, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of value", fontsize=12)

ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 1000, 0, 1100000])

plt.savefig('test.png', bbox_inches='tight')

plt.show()

requested_topping = 'mushroom'

if requested_topping == 'анчоус':
    print('not unctuous')
