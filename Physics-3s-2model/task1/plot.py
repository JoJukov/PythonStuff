import matplotlib.pyplot as plt
import numpy as np

import task1.F_Y_L_M


def get_plot_by_l_m_sq(l: float, m: float):
    f = task1.F_Y_L_M.y_l_m_sq(l, m)
    v = [f(i / 2) for i in range(720)]

    theta = np.arange(0., 2., 1. / 360.) * np.pi
    plt.polar(theta, v)
    plt.show()


def get_plot_by_l_m(l: float, m: float):
    f = task1.F_Y_L_M.y_l_m(l, m)
    v = [f(i / 2) for i in range(720)]

    theta = np.arange(0., 2., 1. / 360.) * np.pi
    plt.polar(theta, v)
    plt.show()
