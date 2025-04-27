import sys
import pygame as pg
import numpy as np


class Simulation:
    def __init__(self, y_circles, x_circles):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(screen_size)
        self.y_circles = y_circles
        self.x_circles = x_circles
        self.background = pg.Surface(self.screen.get_size())
        self.background.fill(pg.Color('black'))

    def update(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.screen.fill(pg.Color('black'))
            self.screen.blit(self.background, (0, 0))
            self.draw()
            pg.display.flip()
            self.clock.tick(60)

    def draw(self):
        for circle in self.y_circles:
            circle.draw_y(self.screen)
        for circle in self.x_circles:
            circle.draw_x(self.screen)
        for x_circle in self.x_circles:
            for y_circle in self.y_circles:
                x_circle.draw_xy(y_circle, self.screen, self.background)

    def logic(self):
        for circle in self.y_circles:
            circle.rotate()
        for circle in self.x_circles:
            circle.rotate()


class RotatingCircle:
    def __init__(self, center, radius, angular_velocity, color=pg.Color('white')):
        self.center = center
        self.radius = radius
        self.color = color
        self.angular_vel = angular_velocity
        self.angle = 0
        self.dot_position = self.center + self.radius * np.array([np.cos(self.angle), np.sin(self.angle)])

    def rotate(self):
        self.angle += self.angular_vel
        self.dot_position = self.center + self.radius * np.array([np.cos(self.angle), np.sin(self.angle)])

    def draw_y(self, screen):
        pg.draw.circle(screen, self.color, self.center, self.radius, 2)
        pg.draw.circle(screen, self.color, self.dot_position, 5)
        pg.draw.line(screen, self.color, self.center, self.dot_position, 1)
        pg.draw.line(screen, self.color, self.dot_position, np.array([screen_size[0], self.dot_position[1]]), 1)

    def draw_x(self, screen):
        pg.draw.circle(screen, self.color, self.center, self.radius, 2)
        pg.draw.circle(screen, self.color, self.dot_position, 5)
        pg.draw.line(screen, self.color, self.center, self.dot_position, 1)
        pg.draw.line(screen, self.color, self.dot_position, np.array([self.dot_position[0], screen_size[1]]), 1)

    def draw_xy(self, other, screen, background):
        dot_position = np.array([self.dot_position[0], other.dot_position[1]])
        pg.draw.circle(screen, pg.Color('white'), dot_position, 5)
        pg.draw.circle(background, pg.Color('white'), dot_position, 1)


if __name__ == '__main__':
    screen_size = np.array([1160, 1120])
    y_circle1 = RotatingCircle(np.array([100, 200]), 50, 0.01, pg.Color('orange'))
    y_circle2 = RotatingCircle(np.array([100, 320]), 50, 0.02, pg.Color('cyan'))
    y_circle3 = RotatingCircle(np.array([100, 440]), 50, 0.03, pg.Color('red'))
    y_circle4 = RotatingCircle(np.array([100, 560]), 50, 0.04, pg.Color('yellow'))
    y_circle5 = RotatingCircle(np.array([100, 680]), 50, 0.05, pg.Color('green'))
    y_circle6 = RotatingCircle(np.array([100, 800]), 50, 0.06, pg.Color('purple'))
    y_circle7 = RotatingCircle(np.array([100, 920]), 50, 0.07, pg.Color('pink'))
    y_circle8 = RotatingCircle(np.array([100, 1040]), 50, 0.08, pg.Color('brown3'))



    x_circle1 = RotatingCircle(np.array([220, 80]), 50, 0.01, pg.Color('orange'))
    x_circle2 = RotatingCircle(np.array([340, 80]), 50, 0.02, pg.Color('cyan'))
    x_circle3 = RotatingCircle(np.array([460, 80]), 50, 0.03, pg.Color('red'))
    x_circle4 = RotatingCircle(np.array([580, 80]), 50, 0.04, pg.Color('yellow'))
    x_circle5 = RotatingCircle(np.array([700, 80]), 50, 0.05, pg.Color('green'))
    x_circle6 = RotatingCircle(np.array([820, 80]), 50, 0.06, pg.Color('purple'))
    x_circle7 = RotatingCircle(np.array([940, 80]), 50, 0.07, pg.Color('pink'))
    x_circle8 = RotatingCircle(np.array([1060, 80]), 50, 0.08, pg.Color('brown3'))

    simulation = Simulation([y_circle1, y_circle2, y_circle3, y_circle4, y_circle5, y_circle6, y_circle7, y_circle8],
                            [x_circle1, x_circle2, x_circle3, x_circle4, x_circle5, x_circle6, x_circle7, x_circle8])
    simulation.update()
