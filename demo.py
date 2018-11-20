import cruveFitting
import numpy as np
import matplotlib.pyplot as plt

plt.figure()

x0 = [1, 2, 3, 4, 5]
y0 = [1, 3, 8, 18, 36]
x1 = np.arange(1, 6, 0.01)
plt.scatter(x0[:], y0[:], 25, "red")

Fitting = cruveFitting.CruveFitting(x0, y0, x1)

y_line, parameters_line = Fitting.Fitting(model="line")
y_square, parameters_square = Fitting.Fitting(model="square")
y_cube, parameters_cube = Fitting.Fitting(model="cube")
y_gauss, parameters_gauss = Fitting.Fitting(model="gauss")
y_ln, parameters_ln = Fitting.Fitting(model="ln")

plt.plot(x1, y_line, "blue")
plt.plot(x1, y_square, "yellow")
plt.plot(x1, y_cube, "green")
plt.plot(x1, y_gauss, "orange")
plt.plot(x1, y_ln, "gray")

plt.title("test")
plt.xlabel('x')
plt.ylabel('y')

plt.show()