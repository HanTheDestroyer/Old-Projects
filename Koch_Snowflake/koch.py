import sys
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, lines):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(screen_size)
        pg.draw.circle(self.screen, pg.Color('pink'), screen_size / 2, 200)
        self.lines = lines
        self.generation_counter = -1
        self.is_increasing_generation = True

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.screen.fill(pg.Color('black'))
            self.draw()
            pg.display.flip()
            self.clock.tick(2)

    def draw(self):
        for line in self.lines:
            line.draw(self.screen, self.generation_counter)

    def logic(self):
        if self.is_increasing_generation:
            self.generation_counter += 1
            if self.generation_counter >= 6:
                self.is_increasing_generation = False

        else:
            self.generation_counter -= 1
            if self.generation_counter <= 0:
                self.is_increasing_generation = True


class Line:
    def __init__(self, start_pos, end_pos, thickness, generation=0):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.thickness = thickness
        self.color = np.array([255, 255, 255])
        self.color = np.random.randint(0, 255, 3)
        self.children = []
        self.generation = generation
        self.generate_new_pos()

    def draw(self, screen, generation):
        if self.generation >= generation:
            pg.draw.line(screen, self.color, self.start_pos, self.end_pos, self.thickness)
        else:
            for child in self.children:
                child.draw(screen, generation)

    def generate_new_pos(self):
        if self.generation <= 6:
            r = self.end_pos - self.start_pos
            p = self.start_pos + r / 3
            q = self.start_pos + 2 * r / 3

            rotation_matrix = np.array([[np.cos(np.radians(60)), -np.sin(np.radians(60))],
                                        [np.sin(np.radians(60)), np.cos(np.radians(60))]])
            pq = r / 3
            pq_rotated = np.matmul(pq, rotation_matrix)
            z = p + pq_rotated
            children = [self.start_pos, p, z, q, self.end_pos]
            for counter in range(len(children) - 1):
                self.children.append(Line(children[counter],
                                          children[counter + 1], self.thickness, generation=self.generation+1))


if __name__ == '__main__':
    screen_size = np.array([1280, 1280])

    line1 = Line(np.array([200, 640]), np.array([400, 986]), 3)
    line2 = Line(np.array([400, 986]), np.array([800, 986]), 3)
    line3 = Line(np.array([800, 986]), np.array([1000, 640]), 3)
    line4 = Line(np.array([800, 293]), np.array([1000, 640]), 3)
    line5 = Line(np.array([400, 293]), np.array([800, 293]), 3)
    line6 = Line(np.array([200, 640]), np.array([400, 293]), 3)

    simulation = Simulation([line1, line2, line3, line4, line5, line6])
    simulation.update()
