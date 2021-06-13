from math import sin, cos, radians


def p_l_m(l: float, m: float):
    if l == 0 and m == 0:
        return 1
    elif l == 1 and m == 0:
        return lambda x: cos(radians(x))
    elif l == 1 and m == 1:
        return lambda x: -sin(radians(x))
    elif l == 2 and m == 0:
        return lambda x: 0.5 * (3 * (cos(radians(x)))**2 - 1)
    elif l == 2 and m == 1:
        return lambda x: -3 * cos(radians(x)) * sin(radians(x))
    elif l == 2 and m == 2:
        return lambda x: 3 * (sin(radians(x)))**2
    elif l == 3 and m == 0:
        return lambda x: 0.5 * (5 * (cos(radians(x)))**3 - 3 * cos(radians(x)))
    elif l == 3 and m == 1:
        return lambda x: -1.5 * (5 * (cos(radians(x)))**2 - 1) * sin(radians(x))
    elif l == 3 and m == 2:
        return lambda x: 15 * cos(radians(x)) * sin(radians(x))**2
    elif l == 3 and m == 3:
        return lambda x: -15 * sin(radians(x))**3
    elif l == 4 and m == 0:
        return lambda x: 0.125 * (35 * cos(radians(x))**4 - 30 * cos(radians(x))**2 + 3)
    else:
        assert ValueError("BL with such input data isn't exists")
