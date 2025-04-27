import sys
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, flowers):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(screen_size)
        self.screen.fill(pg.Color('black'))
        self.flowers = flowers

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
            self.clock.tick(60)

    def draw(self):
        for flower in self.flowers:
            flower.draw(self.screen)

    def logic(self):
        for flower in self.flowers:
            flower.rotate()


class Flower:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        self.color = np.random.randint(0, 255, 3)
        self.petal_color = np.random.randint(0, 255, 3)
        self.number_of_petals = np.random.randint(4, 7)
        self.angle = np.random.uniform(0, np.pi * 2)
        self.instant_radius = 0

    def draw(self, screen):
        # Current Radius
        self.instant_radius += 0.25
        if self.instant_radius >= self.radius:
            self.instant_radius = self.radius

        # Draw Petals
        angle_diff = 2 * np.pi / self.number_of_petals
        petal_dist = self.instant_radius * np.array([np.cos(self.angle), np.sin(self.angle)])
        for i in range(self.number_of_petals):
            petal_dist = np.matmul(petal_dist, self.rotation_matrix(angle_diff))
            petal_loc = petal_dist + self.pos
            pg.draw.circle(screen, self.petal_color, petal_loc, self.instant_radius)
            pg.draw.circle(screen, pg.Color('black'), petal_loc, self.instant_radius, 2)

        # Draw Center
        pg.draw.circle(screen, self.color, self.pos, self.instant_radius)
        pg.draw.circle(screen, pg.Color('black'), self.pos, self.instant_radius, 2)

    def rotate(self):
        self.angle += 0.0

    @staticmethod
    def rotation_matrix(angle):
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return rot


if __name__ == '__main__':
    screen_size = np.array([640, 640])
    spacing = 40
    position = np.array([20, 20])
    my_flowers = []
    x, y = 0, 0
    while x < 16:
        while y < 16:
            my_flowers.append(Flower(position + np.array([x * spacing, y * spacing]), 8))
            print(position + np.array([x * spacing, y * spacing]))
            y += 1
        x += 1
        y = 0
    simulation = Simulation(my_flowers)
    simulation.update()
