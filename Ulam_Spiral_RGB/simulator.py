import pygame as pg
import numpy as np
import sys
import settings as st
import eratosthenes
import colorsys


class Simulator:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(np.array(st.screen_size, dtype='int16'))
        self.screen.fill(pg.Color('black'))
        self.primes = eratosthenes.sieve_of_eratosthenes(100000)

        self.center = np.array([st.screen_size[0] / 2, st.screen_size[1] / 2])

        self.step_size = 5  # how many pixels to move at once.
        self.step = np.array([self.step_size, 0])  # start by moving right.
        # step type changes with rotations. Step to right, to up, to left, to down and to right again.
        self.step_type = 0
        self.when_to_rotate = 1  # how many times should simulation go in one direction.
        self.number_of_rotations = 0  # every two rotations, system should update its direction[step type].
        self.loop_counter = 1  # Generic counter

        self.hue = 0  # start hue counter with zero
        self.hue_step = 0.0001

    # Pygame Basics
    def update(self):
        self.screen.fill(pg.Color('black'))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.draw()
            pg.display.update()
            self.clock.tick()

    def draw(self):
        if self.loop_counter in self.primes:
            self.hue += self.hue_step
            if self.hue > 1:
                self.hue -= 1
            rgb = colorsys.hsv_to_rgb(self.hue, 1, 1)
            rgb = [int(c * 255) for c in rgb]
            pg.draw.circle(self.screen, color=rgb, center=self.center, radius=2)

        elif self.loop_counter not in self.primes:
            pg.draw.circle(self.screen, color=[120, 120, 120], center=self.center, radius=0)
            pass

    def logic(self):
        if self.number_of_rotations == 2:
            self.when_to_rotate += 1
            self.number_of_rotations = 0

        self.center += self.step
        self.step_type += 1
        self.loop_counter += 1
        
        # changing directions.
        if self.step_type == self.when_to_rotate:
            self.step_type = 0
            self.number_of_rotations += 1
            if self.step[0] == self.step_size and self.step[1] == 0:
                self.step[0] = 0
                self.step[1] = -self.step_size
            elif self.step[0] == 0 and self.step[1] == -self.step_size:
                self.step[0] = -self.step_size
                self.step[1] = -0
            elif self.step[0] == -self.step_size and self.step[1] == 0:
                self.step[0] = 0
                self.step[1] = self.step_size
            elif self.step[0] == 0 and self.step[1] == self.step_size:
                self.step[0] = self.step_size
                self.step[1] = 0


if __name__ == '__main__':
    simulator = Simulator()
    simulator.update()
