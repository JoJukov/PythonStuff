from math import factorial, pi


def a_l_m(l: float, m: float) -> float:
    return (factorial(l - abs(m)) * (2 * l + 1) / (factorial(l + abs(m)) * (4 * pi))) ** 0.5
