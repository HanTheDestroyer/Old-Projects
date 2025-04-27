import sys

import numpy as np
import matplotlib.pyplot as plt
import pygame as pg

number_of_iterations = 100000
mode = 'pygame'
# mode = 'matplotlib'


def function_1(a, b):
    transformation = np.array([[0, 0],
                               [0, 0.16]])
    inputs = np.array([[a], [b]])
    resultant = np.dot(transformation, inputs)
    return resultant[0], resultant[1]


def function_2(a, b):
    transformation = np.array([[0.85, 0.04],
                               [-0.04, 0.85]])
    inputs = np.array([[a], [b]])
    resultant = np.dot(transformation, inputs) + np.array([[0], [1.6]])
    return resultant[0], resultant[1]


def function_3(a, b):
    transformation = np.array([[0.20, -0.26],
                               [0.23, 0.22]])
    inputs = np.array([[a], [b]])
    resultant = np.dot(transformation, inputs) + np.array([[0], [1.6]])
    return resultant[0], resultant[1]


def function_4(a, b):
    transformation = np.array([[-0.15, 0.28],
                               [0.26, 0.24]])
    inputs = np.array([[a], [b]])
    resultant = np.dot(transformation, inputs) + np.array([[0], [0.44]])
    return resultant[0], resultant[1]


functions = [function_1, function_2, function_3, function_4]
x = np.zeros([number_of_iterations], dtype=float)
y = np.zeros([number_of_iterations], dtype=float)

for i in np.arange(1, number_of_iterations):
    function = np.random.choice(functions, p=np.array([0.01, 0.85, 0.07, 0.07]))
    x[i], y[i] = function(x[i-1], y[i-1])

if mode == 'matplotlib':
    fig = plt.figure(dpi=120, facecolor=[0.4, 0.4, 0.4])
    ax0 = fig.add_subplot()
    ax0.scatter(x, y, s=1, label=f'{number_of_iterations} data points', c='Green')
    plt.legend()
    plt.show()


if mode == 'pygame':
    pg.init()
    screen = pg.display.set_mode([1200, 1200])
    clock = pg.time.Clock()
    scale = 120
    running = 1
    while running:
        if running > number_of_iterations-1:
            running = 1
            screen.fill([0, 0, 0])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
        pg.draw.circle(screen, color=[0, 255 - y[running] * 20, 0],
                       center=[x[running] * scale + 600, 1200 - y[running] * scale], radius=1)
        pg.display.update()
        clock.tick()
        running += 1

    pg.quit()
