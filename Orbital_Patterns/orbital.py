import sys
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, planets=[], line_color=None, line_freq=None):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.planets = planets
        self.background = pg.Surface(self.screen.get_size())
        self.background.fill(pg.Color('black'))
        self.frame_counter = 0
        self.line_color = pg.Color('white') if line_color is None else line_color
        self.line_freq = 8 if line_freq is None else line_freq

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.screen.fill(pg.Color('black'))
            pg.draw.circle(self.background, pg.Color('yellow'), np.array(screen_size) / 2, 50)
            self.screen.blit(self.background, (0, 0))
            self.draw()
            pg.display.update()
            self.clock.tick(120)

    def logic(self):
        self.frame_counter += 1
        if self.frame_counter == self.line_freq:
            self.frame_counter = 0
        for planet in self.planets:
            planet.rotate()

    def draw(self):
        for planet in self.planets:
            planet.draw(self.screen)
        if self.frame_counter == 3:
            for i in range(len(self.planets) - 1):
                self.planets[i].draw_line(self.planets[i + 1], self.background, self.line_color)

    def add_planets(self, planets):
        self.planets.extend(planets)


class Planet:
    def __init__(self, pos=None, rotation_center=None, angle=None, angular_velocity=None, color=None):
        if pos is None:
            self.pos = np.zeros([2])
            self.pos[1] = np.random.uniform(150, min(screen_size) - 150, 1)
            self.pos[0] = np.random.uniform(max(screen_size)/2 - min(screen_size)/2 + 150,
                                            max(screen_size)/2 + min(screen_size)/2 - 150)
        else:
            self.pos = pos
        self.rotation_center = np.array(screen_size) / 2 if rotation_center is None else rotation_center
        self.angle = np.random.uniform(0, 2 * np.pi) if angle is None else angle
        self.distance = np.linalg.norm(self.pos - self.rotation_center)
        self.color = np.random.randint(0, 255, 3) if color is None else color
        if angular_velocity is None:
            self.angular_velocity = np.random.uniform(-np.radians(1), np.radians(1))
        else:
            self.angular_velocity = angular_velocity

    def rotate(self):
        self.angle += self.angular_velocity
        self.pos = self.rotation_center + self.distance * np.array([np.cos(self.angle), np.sin(self.angle)])

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, 10)

    def draw_line(self, other, surface, line_color):
        pg.draw.line(surface, line_color, self.pos, other.pos, 1)


if __name__ == '__main__':
    simulation = Simulation(line_color=pg.Color('pink'))
    screen_size = simulation.screen.get_size()
    planet1 = Planet()
    planet2 = Planet()
    planet3 = Planet()

    simulation.add_planets([planet1, planet2])
    simulation.update()
