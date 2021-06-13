from cmath import exp
from task1 import F_A_L_M, F_P_L_M


def y_l_m(l: float, m: float):
    return lambda theta, alpha: F_A_L_M.a_l_m(l, m) * F_P_L_M.p_l_m(l, m)(theta) * exp((-1) ** 0.5 * m * alpha)


def y_l_m_sq(l: float, m: float):
    return lambda theta, alpha: abs(y_l_m(l, m)(theta, alpha)) * abs(y_l_m(l, m)(theta, alpha))
