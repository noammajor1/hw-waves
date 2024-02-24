import math
import numpy as np
import matplotlib.pyplot as plt
vector = np.linspace(0, 1, 1000)

def exp_func(x,a):
    return np.exp(a*x)

def taylor_expansion(x, a, order):
    result = 0
    for n in range(order):
        result += (a * x)**n / np.math.factorial(n)
    return result

def create_graphs(a):
    x_values = np.linspace(-2, 2, 100)
    y_exp = exp_func(x_values,a)
    orders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_taylor_series = [taylor_expansion(x_values, a, order) for order in orders]
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_exp, label='e^x')
    for order, y_taylor in zip(orders, y_taylor_series):
        plt.plot(x_values, y_taylor, label=f'Taylor Series (Order {order})', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function e^{}x and Its Taylor Series Expansion'.format(a))
    plt.legend()
    plt.grid(True)
    plt.show()

listexp = [-2, -1, 1, 2]
for value in listexp:
    create_graphs(value)