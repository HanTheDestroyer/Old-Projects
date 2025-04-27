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
                if self.string[self.char_counter] == '1' or '0':
                    self.start = self.end
                    self.end = self.start + self.distance
                if self.string[self.char_counter] == '[':
                    self.saved_positions.append(self.start)
                    self.saved_distances.append(self.distance)
                    self.distance = np.matmul(self.distance, self.rotation_matrix(np.radians(45)))
                    self.end = self.start
                if self.string[self.char_counter] == ']':
                    self.start = self.saved_positions.pop()
                    self.distance = self.saved_distances.pop()
                    self.distance = np.matmul(self.distance, self.rotation_matrix(np.radians(-45)))
                    self.end = self.start

    def draw(self):
        if self.string[self.char_counter] == '1' or self.string[self.char_counter] == '0':
            pg.draw.line(self.screen, pg.Color('white'), self.start, self.end, 1)

    @staticmethod
    def rotation_matrix(angle):
        rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return rot

    @staticmethod
    def iterate_string(string, iteration_count):
        for _ in range(iteration_count):
            new_string = ""
            for char in string:
                if char == '1':
                    new_string += '11'
                elif char == '0':
                    new_string += '1[0]0'
                else:
                    new_string += char
            string = new_string
        return string


if __name__ == '__main__':
    screen_size = np.array([640, 640])
    input_string = '0'
    simulation = Simulation(10, np.array([320, 600]))
    input_string = simulation.iterate_string(input_string, 6)
    input_string += " "
    print(input_string)
    simulation.add_string(input_string)
    simulation.update()
