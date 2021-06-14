import matplotlib.pyplot as plt
import scipy.special as sp
import numpy as np

import task1.F_Y_L_M


def get_plot2_by_l_m_sq(l: float, m: float):
    f = task1.F_Y_L_M.y_l_m_sq(l, m)
    v = [f(i / 2, 0) for i in range(720)]

    theta = np.arange(0., 2., 1. / 360.) * np.pi
    plt.polar(theta, v)
    plt.show()


def get_plot2_by_l_m(l: float, m: float):
    f = task1.F_Y_L_M.y_l_m(l, m)
    v = [f(i / 2, 0) for i in range(720)]

    theta = np.arange(0., 2., 1. / 360.) * np.pi
    plt.polar(theta, v)
    plt.show()


def get_plot3_by_l_m_sq(l: float, m: float):
    theta, phi = np.meshgrid(np.linspace(0, 2 * np.pi, 90), np.linspace(0, np.pi, 90))
    xyz = np.array([np.sin(theta) * np.sin(phi),
                    np.sin(theta) * np.cos(phi),
                    np.cos(theta)])
    yy = sp.sph_harm(abs(m), l, phi, theta)
    x, y, z = np.abs(yy) * xyz
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    plot = ax.plot_surface(
        x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('gnuplot2'),
        linewidth=0, antialiased=False, alpha=0.5)

    plt.show()

