import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

scatter_input_values = [2, 3, 4, 5, 6]
scatter_squares = [4 + 1, 9 + 1, 16 + 1, 25 + 1, 36 + 1]

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.scatter(2, 2, s=200)
ax.plot(input_values, squares, linewidth=10)

ax.scatter(scatter_input_values, scatter_squares, s=100)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of value", fontsize=12)

ax.tick_params(axis='both', labelsize=14)

plt.show()
