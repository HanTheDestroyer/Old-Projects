import sys
import pygame as pg
import numpy as np
import colorsys


class Simulation:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.screen.fill(pg.Color('black'))
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

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
            pg.display.update()
            self.clock.tick(60)

    def logic(self):
        for tree in self.trees:
            tree.change_angle(tree.angle-angular_velocity)

    def draw(self):
        for tree in self.trees:
            tree.draw(self.screen, generations)


class Tree:
    def __init__(self, start, end, child_length, angle, hue=0.9, generation=0):
        self.start = start
        self.end = end
        self.factor = 1 / np.sqrt(2)  # In order to generate H tree, this value should be 1/sqrt(2)
        self.generation = generation
        self.child_length = child_length
        self.angle = angle
        self.hue = hue
        if self.hue <= 0:
            self.hue += 1
        elif self.hue >= 1:
            self.hue -= 1
        self.color = colorsys.hsv_to_rgb(self.hue, 1, 1)
        self.color = [int(c * 255) for c in self.color]
        self.children = []
        if self.generation < generations:
            self.populate()

    def change_angle(self, new_angle):
        """Changes the angle separating the branches"""
        self.angle = new_angle
        self.children = []
        self.populate()

    def populate(self):
        """Creates the branches"""
        direction_vec = self.end - self.start
        direction_unit_vec = direction_vec / np.linalg.norm(direction_vec)
        difference = self.child_length * direction_unit_vec
        child0_end_point = self.end + np.matmul(difference, self.rotation_matrix(self.angle))
        child1_end_point = self.end + np.matmul(difference, self.rotation_matrix(-self.angle))
        child0 = Tree(self.end, child0_end_point, self.child_length * self.factor, self.angle,
                      self.hue + 0.05, self.generation+1)
        child1 = Tree(self.end, child1_end_point, self.child_length * self.factor, self.angle,
                      self.hue + 0.05, self.generation+1)
        self.children = [child0, child1]

    def draw(self, screen, target_generation):
        """Draws the tree on the screen"""
        if self.generation <= target_generation:
            pg.draw.line(screen, self.color, self.start, self.end, 1)
            if self.children:
                for child in self.children:
                    child.draw(screen, target_generation)

    @staticmethod
    def rotation_matrix(angle):
        """Rotates a vector by given angle in radians"""
        rot = np.array([[np.cos(angle), -np.sin(angle)],
                        [np.sin(angle), np.cos(angle)]])
        return rot


if __name__ == '__main__':
    generations = 11
    simulation = Simulation()
    screen_size = np.array(simulation.screen.get_size())
    # Change in angle in which branches are separating.
    angular_velocity = np.radians(0.5)
    # Size of the trunk so that it shows up in the screen properly.
    trunk_size = screen_size[1] * 0.27777
    tree1 = Tree(np.array([screen_size[0] / 2, screen_size[1]]),
                 np.array([screen_size[0] / 2, screen_size[1] - trunk_size]), trunk_size / 2, np.radians(90))
    simulation.add_tree(tree1)
    simulation.update()
