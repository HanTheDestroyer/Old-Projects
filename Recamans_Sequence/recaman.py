import sys
import pygame as pg
import numpy as np


screen_size = [960, 480]
bumper_size = 60
number_of_elements = 300


def generate_sequence(limit):
    step_size = 1
    sequence = [0]
    while step_size < limit:
        # try moving backwards
        if sequence[-1] - step_size not in sequence and sequence[-1] - step_size > 0:
            sequence.append(sequence[-1] - step_size)
        else:
            sequence.append(sequence[-1] + step_size)
        step_size += 1
    return sequence


# initialize pygame
pg.init()
screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()
screen.fill([0, 0, 0])


# calculate scale
recaman = generate_sequence(number_of_elements)
max_number = max(recaman)
length_of_line = screen_size[0] - 2 * bumper_size
scale = length_of_line / max_number

y_coord = np.ones(number_of_elements) * screen_size[1] / 2
x_coord = bumper_size + np.array(recaman) * scale

# event loop
running = True

for c in range(number_of_elements):
    pg.draw.circle(screen, [255, 255, 255], center=[x_coord[c], y_coord[c]], radius=1)

i = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

    if i > 0:
        diameter = x_coord[i] - x_coord[i - 1]
        radius = diameter / 2

        if diameter > 0:
            pg.draw.arc(screen, [255, 255, 255],
                        [x_coord[i] - diameter, y_coord[i] - radius, diameter, diameter], 0, np.pi)
        if diameter < 0:
            pg.draw.arc(screen, [255, 255, 255],
                        [x_coord[i], y_coord[i] + radius, -diameter, -diameter], np.pi, 0)

    i += 1
    if i > number_of_elements-1:
        i = 0
        screen.fill([0, 0, 0])
        pg.time.wait(4000)
    pg.display.update()
    clock.tick(30)
