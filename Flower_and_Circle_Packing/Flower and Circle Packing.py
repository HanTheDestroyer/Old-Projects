import sys

from PIL import Image
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, flower_radius_difference):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(screen_size)
        self.screen.fill(pg.Color('black'))
        self.flowers = []
        self.img = np.array(Image.open(image_path))  # Don't worry if it shows an error on PyCharm.
        self.flower_radius_difference = flower_radius_difference
        self.flower_packing = True

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.screen.fill(pg.Color('green'))
            self.draw()
            pg.display.update()
            self.clock.tick(0)

    def draw(self):
        for flower in self.flowers:
            flower.draw(self.screen)

    def logic(self):
        if self.flower_packing:
            new_flower = Flower()
        else:
            new_flower = Circle()
        # Check if location is white. If so, try adding a flower.
        if self.img[int(new_flower.pos[1]), int(new_flower.pos[0])][0] == 255:
            # If there are no flowers in the self.flowers, add the flower.
            if not self.flowers:
                self.flowers.append(new_flower)
            # If there are flowers in the self.flowers, check if it is too close to an existing flower.
            else:
                is_a_valid_flower = True
                for flower in self.flowers:
                    distance = np.linalg.norm(flower.pos - new_flower.pos)
                    if distance < (new_flower.radius + flower.radius) * self.flower_radius_difference:
                        is_a_valid_flower = False
                if is_a_valid_flower:
                    self.flowers.append(new_flower)


class Flower:
    def __init__(self, pos=None, radius=None):
        if pos is None:
            pos_x = np.random.uniform(0, screen_size[0])
            pos_y = np.random.uniform(0, screen_size[1])
            self.pos = np.array([pos_x, pos_y])
        else:
            self.pos = pos
        self.radius = radius if radius is not None else np.random.randint(flower_min_radius, flower_max_radius)
        self.color = np.random.randint(0, 255, 3)
        self.petal_color = np.random.randint(0, 255, 3)
        self.number_of_petals = np.random.randint(4, 7)
        self.angle = np.random.uniform(0, np.pi * 2)
        self.instant_radius = 0

        self.petal_loc = []
        angle_diff = 2 * np.pi / self.number_of_petals
        petal_dist = self.radius * np.array([np.cos(self.angle), np.sin(self.angle)])
        for i in range(self.number_of_petals):
            petal_dist = np.matmul(petal_dist, self.rotation_matrix(angle_diff))
            petal_loc = petal_dist + self.pos
            self.petal_loc.append(petal_loc)

    def draw(self, screen):
        # Draw Petals
        for i in range(self.number_of_petals):
            pg.draw.circle(screen, self.petal_color, self.petal_loc[i], self.radius)
            pg.draw.circle(screen, pg.Color('black'), self.petal_loc[i], self.radius, 2)
        # Draw Center
        pg.draw.circle(screen, self.color, self.pos, self.radius)
        pg.draw.circle(screen, pg.Color('black'), self.pos, self.radius, 2)

    @staticmethod
    def rotation_matrix(angle):
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return rot


class Circle:
    def __init__(self, pos=None, radius=None):
        if pos is None:
            pos_x = np.random.uniform(0, screen_size[0])
            pos_y = np.random.uniform(0, screen_size[1])
            self.pos = np.array([pos_x, pos_y])
        else:
            self.pos = pos
        self.radius = radius if radius is not None else np.random.randint(flower_min_radius, flower_max_radius)
        self.color = np.random.randint(0, 255, 3)

    def draw(self, screen):
        if circles_are_colorful and circles_are_filled:
            pg.draw.circle(screen, self.color, self.pos, self.radius)
        if circles_are_colorful and not circles_are_filled:
            pg.draw.circle(screen, self.color, self.pos, self.radius, 2)
        if not circles_are_colorful and circles_are_filled:
            pg.draw.circle(screen, circle_color, self.pos, self.radius)
        if not circles_are_colorful and not circles_are_filled:
            pg.draw.circle(screen, circle_color, self.pos, self.radius, 2)
        if circles_are_outlined:
            pg.draw.circle(screen, pg.Color('black'), self.pos, self.radius, 2)

    @staticmethod
    def rotation_matrix(angle):
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return rot


if __name__ == '__main__':
    # Common Settings
    screen_size = np.array([960, 640])  # Set it to something smaller than your screen resolution, preferably.
    flower_max_radius = 8  # Depends on Preference. 8 is good for Flowers on a 640x640 screen. 12 for Circles.
    flower_min_radius = 2  # Set it to 2.0 for flowers and 1.0 for Circles.
    flower_packing = True  # Set it to False for Circle Packing instead of Flower Packing.
    image_path = 'img.png'
    # Circle Related Settings
    circles_are_colorful = False  # Set it to True for Colorful Circles.
    circles_are_filled = True  # Set it to True for Filled Circles.
    circle_color = np.array([255, 0, 0])  # Sets the circle color for non-colorful Circles.
    circles_are_outlined = False
    # Do not change 1.0 but 1.5 depends on preference. It tells how close flowers can be.
    if flower_packing:
        flower_radius_diff = 1.5
    else:
        flower_radius_diff = 1.0
    # Simulation Start.
    simulation = Simulation(flower_radius_diff)
    simulation.flower_packing = flower_packing
    simulation.update()
