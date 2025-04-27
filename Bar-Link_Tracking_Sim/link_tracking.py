import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


class Bar:
    def __init__(self, pivot_point, radius, angular_velocity):
        self.tracking_plot = plt.subplot
        self.radius = radius
        self.ang_vel = angular_velocity
        self.pivot_point = pivot_point
        self.connected_links = []
        self.tip_position = np.zeros([2, frame_count])
        self.calculate_positions()
        self.plot = plt.subplot

    def calculate_positions(self):
        self.tip_position = self.pivot_point + self.radius * np.array([np.cos(self.ang_vel * time),
                                                                       np.sin(self.ang_vel * time)])

    def get_plot(self, ax, color, color2):
        self.plot = ax.plot([], [], color, linewidth=5)[0]
        self.tracking_plot = ax.plot([], [], color2, linewidth=1)[0]


def update_plot(t):
    # draw bars
    link1.plot.set_xdata([link1.pivot_point[0][t], link1.tip_position[0][t]])
    link1.plot.set_ydata([link1.pivot_point[1][t], link1.tip_position[1][t]])
    link2.plot.set_xdata([link2.pivot_point[0][t], link2.tip_position[0][t]])
    link2.plot.set_ydata([link2.pivot_point[1][t], link2.tip_position[1][t]])
    link3.plot.set_xdata([link3.pivot_point[0][t], link3.tip_position[0][t]])
    link3.plot.set_ydata([link3.pivot_point[1][t], link3.tip_position[1][t]])
    link4.plot.set_xdata([link4.pivot_point[0][t], link4.tip_position[0][t]])
    link4.plot.set_ydata([link4.pivot_point[1][t], link4.tip_position[1][t]])
    # draw links' past positions
    link1.tracking_plot.set_data([link1.tip_position[0][0:t], link1.tip_position[1][0:t]])
    link2.tracking_plot.set_data([link2.tip_position[0][0:t], link2.tip_position[1][0:t]])
    link3.tracking_plot.set_data([link3.tip_position[0][0:t], link3.tip_position[1][0:t]])
    link4.tracking_plot.set_data([link4.tip_position[0][0:t], link4.tip_position[1][0:t]])

    return link1.plot, link2.plot, link3.plot, link4.plot, \
           link1.tracking_plot, link2.tracking_plot, link3.tracking_plot, link4.tracking_plot


if __name__ == '__main__':
    t_0 = 0
    t_end = 45
    dt = 0.1
    time = np.arange(t_0, t_end + dt, dt)
    frame_count = len(time)

    link1 = Bar(pivot_point=np.zeros([2, frame_count]), radius=150, angular_velocity=2)
    link2 = Bar(pivot_point=link1.tip_position, radius=300, angular_velocity=4)
    link3 = Bar(pivot_point=link2.tip_position, radius=175, angular_velocity=1)
    link4 = Bar(pivot_point=link3.tip_position, radius=75, angular_velocity=10)

    fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=[0.4, 0.4, 0.4])
    gs = gridspec.GridSpec(5, 5)

    ax0 = fig.add_subplot(gs[0:5, 0:5], facecolor=[0.6, 0.6, 0.6])
    ax0.set_xlim(-1120, 1120)
    ax0.set_ylim(-630, 630)
    ax0.set_xlabel('x-position')
    ax0.set_ylabel('y-position')

    link1.get_plot(ax0, color='k', color2='k:')
    link2.get_plot(ax0, color='r', color2='r:')
    link3.get_plot(ax0, color='b', color2='b:')
    link4.get_plot(ax0, color='g', color2='g:')

    plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_count, interval=40, repeat=True, blit=True)
    plt.show()
