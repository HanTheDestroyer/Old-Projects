import numpy as np
import pygame as pg


class Simulation:
    def __init__(self, sandpile):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([200, 200])
        self.screen.fill(pg.Color('black'))
        self.sandpile = sandpile
        self.logic()

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            self.draw()
            pg.display.flip()
            self.clock.tick(60)

    def draw(self):
        self.sandpile.draw(self.screen)

    def logic(self):
        while True:
            self.sandpile.iterate()
            row_indices, column_indices = np.where(self.sandpile.grid > 3)
            if len(row_indices) == 0:
                break


class Sandpile:
    def __init__(self):
        self.grid = np.zeros([200, 200])
        # self.fill_with_sand()
        self.grid[100][100] = 5000
        self.new_grid = np.zeros([200, 200])
        self.iteration_number = 0
        self.colors = np.array([[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]], dtype='int16')

    def fill_with_sand(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                self.grid[row][column] = np.random.randint(0, 6)

    def iterate(self):
        self.iteration_number += 1
        # Keep the cells with 1, 2 or 3 sand pieces same.
        row_indices, column_indices = np.where(self.grid < 4)
        for c in np.arange(len(row_indices)):
            self.new_grid[row_indices[c]][column_indices[c]] = self.grid[row_indices[c]][column_indices[c]]
        # If there are more than 3 sand pieces, topple.
        row_indices, column_indices = np.where(self.grid >= 4)
        for c in np.arange(len(row_indices)):
            self.topple(row_indices[c], column_indices[c])
        self.grid = self.new_grid

    def topple(self, row_index, column_index):
        max_rows = len(self.grid)
        max_columns = len(self.grid[0])
        self.new_grid[row_index][column_index] = self.grid[row_index][column_index] - 4
        if row_index < max_rows - 1:
            self.new_grid[row_index+1][column_index] += 1
        if row_index > 0:
            self.new_grid[row_index-1][column_index] += 1
        if column_index < max_columns - 1:
            self.new_grid[row_index][column_index+1] += 1
        if column_index > 0:
            self.new_grid[row_index][column_index-1] += 1

    def draw(self, screen):
        for row_i in np.arange(len(self.grid)):
            for col_i in np.arange(len(self.grid[0])):
                pg.draw.circle(screen, self.colors[self.grid[row_i][col_i].astype('int')], np.array([row_i, col_i]), 1)


if __name__ == '__main__':
    my_sandpile = Sandpile()
    simulation = Simulation(my_sandpile)
    simulation.update()

