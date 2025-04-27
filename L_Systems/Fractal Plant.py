# https://erase.net/projects/l-systems/files/lsystems.txt
import sys
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, distance, starting_point):
        pg.init()
        self.distance = np.array([0, -distance], dtype='float')
        self.dummy_distance = np.array([0, -distance], dtype='float')
        self.start = starting_point
        self.end = self.start + self.distance
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(screen_size)
        self.screen.fill(pg.Color('black'))
        self.string = None
        self.char_counter = -1
        self.saved_positions = []
        self.saved_distances = []

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            # self.screen.fill(pg.Color('black'))
            self.draw()
            pg.display.update()
            self.clock.tick(0)

    def add_string(self, string):
        self.string = string

    def logic(self):
        if self.char_counter < len(self.string) - 1:
            self.char_counter += 1
        if self.string and self.char_counter < len(self.string) - 1:
            if self.string[self.char_counter] == 'F':
                self.start = self.end
                self.end = self.start + self.distance
            if self.string[self.char_counter] == '+':
                angle = np.radians(18) + np.random.uniform(-np.radians(18) * 0.5, np.radians(18) * 0.5)
                self.distance = np.matmul(self.distance, self.rotation_matrix(angle))
            if self.string[self.char_counter] == '-':
                angle = np.radians(18) + np.random.uniform(-np.radians(18) * 0.5, np.radians(18) * 0.5)
                self.distance = np.matmul(self.distance, self.rotation_matrix(-angle))
            if self.string[self.char_counter] == '[':
                self.saved_positions.append(self.end)
                self.saved_distances.append(self.distance)
                self.start = self.end
            if self.string[self.char_counter] == ']':
                self.end = self.saved_positions.pop()
                self.distance = self.saved_distances.pop()
                self.start = self.end

    def draw(self):
        if self.string[self.char_counter] == 'F':
            pg.draw.line(self.screen, pg.Color('green'), self.start, self.end, 1)

    @staticmethod
    def rotation_matrix(angle):
        rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return rot

    @staticmethod
    def iterate_string(string, iteration_count):
        for _ in range(iteration_count):
            new_string = ""
            for char in string:
                if char == 'F':
                    new_string += 'F[+F]F[-F]'
                else:
                    new_string += char
            string = new_string
        return string


if __name__ == '__main__':
    screen_size = np.array([640, 640])
    input_string = 'F'
    simulation = Simulation(4, np.array([320, 600]))
    input_string = simulation.iterate_string(input_string, 7)
    print(input_string)
    simulation.add_string(input_string)
    simulation.update()
