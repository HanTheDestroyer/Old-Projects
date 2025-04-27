import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation


"""f(x) = 2 for 0 < x < pi, f(x) = 0 for pi < x < 2pi, f(x+2pi) = f(x)"""
# Constants
dt = 0.01
x_range = np.arange(0, 2 * np.pi, dt)
upper_fourier_element_limit = 100

# Create the real function
real_function = x_range * 0
for c, x_val in enumerate(real_function):
    if c < np.pi / dt:
        real_function[c] = 2
    else:
        real_function[c] = 0


def function_generator(a):
    """Generates parts of the Fourier Series expansion"""
    return lambda x: (1 / a) * np.sin(a * x)


def fourier(elements):
    """Generates Fourier Series expansion for n=elements"""
    functions = [function_generator(2 * i + 1) for i in np.arange(elements)]
    summation = 0
    for function in functions:
        values = function(x_range)
        summation += values
    return 1 + (4 / np.pi) * summation


fourier_for_varying_elements = []
for i in range(upper_fourier_element_limit):
    fourier_for_varying_elements.append(fourier(i))


fig = plt.figure(figsize=(9, 9), dpi=120, facecolor=[0.5, 0.5, 0.5])

ax0 = fig.add_subplot()
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim(-1, 3)
x_vs_y = ax0.plot([], [], 'r', linewidth=1, label='Fourier Series Expansion Approximation')[0]
x_vs_real_function = ax0.plot(x_range, real_function, 'k', linewidth=1, label='Real Function')[0]
ax0.set_facecolor([0.7, 0.7, 0.7])
elements_tracker_box = dict(boxstyle='circle', fc=(0.1, 0.9, 0.9), ec='g', lw=1)
elements_tracker = ax0.text(0, 0, '', color='r', size=15, bbox=elements_tracker_box)
plt.grid(c=[0.9, 0.8, 0.4])
plt.legend()


def update_plot(num):
    x_vs_y.set_data(x_range, fourier_for_varying_elements[num])
    if num+1 < 10:
        elements_tracker.set_text(f'n = 00{num+1}')
    else:
        elements_tracker.set_text(f'n = 0{num+1}')
    return x_vs_y, elements_tracker


anim = animation.FuncAnimation(fig, update_plot, frames=upper_fourier_element_limit,
                               interval=100, repeat=False, blit=True)
plt.show()
