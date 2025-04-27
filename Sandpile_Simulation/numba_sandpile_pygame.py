import numpy as np
import pygame as pg
import sys


class Simulation:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([640, 640])
        self.screen.fill(pg.Color('black'))
        self.sandpile = np.loadtxt('sandpile_result.txt').astype('int')
        self.colors = np.array([[244, 164, 96], [210, 180, 140], [139, 69, 19], [101, 67, 33]], dtype='int16')

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
            self.clock.tick(60)

    def draw(self):
        for x in range(640):
            for y in range(640):
                pg.draw.circle(self.screen, self.colors[self.sandpile[x][y]], np.array([x, y]), 1)

    def logic(self):
        pass


if __name__ == '__main__':
    simulation = Simulation()
    simulation.update()
