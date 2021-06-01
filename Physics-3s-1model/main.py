import inspect
from typing import Final
from math import pi
from inspect import getargvalues

g: Final = 9.81
Ro_water: Final = 1000
P_atm: Final = 101325
s_water: Final = 0.073


def check_if_argument_are_positive(frame):
    args: dict = getargvalues(frame)[3]
    for elem in args.items():
        if elem[1] <= 0:
            raise ValueError(f'Argument {elem[0]} should be positive')


def get_radius_from_volume(volume: float) -> float:
    check_if_argument_are_positive(inspect.currentframe())
    return (3 / 4 * volume / pi) ** (1 / 3)


def get_result(volume: float, hole_diameter: float, ro_liquid: float = Ro_water, sigma: float = s_water) -> float:
    # Проверка валидности входных данных
    check_if_argument_are_positive(inspect.currentframe())
    # Перевод мм в м
    hole_diameter /= 1000
    # Получение радиуса шара из его объема
    radius = get_radius_from_volume(volume)
    if hole_diameter >= 2 * radius:
        raise ValueError("hole diameter should be less than sphere diameter")

    f_atm = 1 / 4 * P_atm * pi * hole_diameter ** 2
    f_liquid_pressure = 1 / 2 * ro_liquid * g * radius * pi * hole_diameter ** 2
    f_tension = sigma * pi * hole_diameter
    # Происходит проверка, начнет ли жидкости вытекать
    if f_atm + f_tension >= f_liquid_pressure:
        return 0

    h_liquid = min((P_atm + 4 * sigma / hole_diameter) / (g * ro_liquid), 2 * radius)

    volume_gone = pi * radius * (2 * radius - h_liquid) ** 2 - 1 / 3 * pi * (2 * radius - h_liquid) ** 3
    return volume_gone


if __name__ == '__main__':
    print(f'answer: {get_result(1000, 3000000000, ro_liquid=13546, sigma=0.51)}')
