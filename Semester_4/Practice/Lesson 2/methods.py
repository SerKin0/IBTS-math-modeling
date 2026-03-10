from typing import Callable
from dataclasses import dataclass


@dataclass
class Result:
    x: float
    fx: float
    count_iter: int

    def __str__(self):
        return f"x = {self.x}, f(x) = {self.fx}, iter = {self.count_iter}"


def method_dichotomy(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float = 10e-5,
    max_iteration: int = 10000,
) -> Result:
    """## Метод Дихотомии (Метод половинного деления)

    :param func: Функция f(x), непрерывная на отрезке [a,b], у которой находим пересечение с осью абцисс: f(x) = 0
    :type func: Callable[[float], float]
    :param a: Левая граница отрезка (b > a)
    :type a: float
    :param b: Правая граница отрезка (b > a)
    :type b: float
    :param epsilon: Допустимая погрешность, defaults to 10e-5
    :type epsilon: float, optional
    :param max_iteration: Максимальное количество итераций, defaults to 10000
    :type max_iteration: int, optional
    :raises RuntimeError: При превышении установленного лимита итераций
    :raises ValueError: Если значения крайних точек находятся в одной области
    :return: Единственное пересечение с осью абцисс
    :rtype: Result
    """
    # Находим значения функции в точках границ отрезка
    fa, fb = func(a), func(b)

    # Если значения крайних точек находятся в одной области, выдаем ошибку
    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")

    # Повторяем до момента переполнения установленного числа попыток
    for iter in range(max_iteration):
        # Находим середину отрезка и значение функции в ней
        c = (a + b) / 2
        fc = func(c)

        # Если знак точки a и c различен, то сдвигаем правую границу к центру,
        # иначе передвигаем левую
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

        # Если длина отрезка меньше погрешности, то возвращаем его центр
        if b - a <= epsilon:
            return Result(c, func(c), iter)

    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку
    raise RuntimeError(
        f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})"
    )


def method_chord(
    func: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float = 10e-5,
    max_iteration: int = 10000,
) -> Result:
    """## Метод Хорд

    :param func: Функция f(x), непрерывная на отрезке [a,b], у которой находим пересечение с осью абцисс: f(x) = 0
    :type func: Callable[[float], float]
    :param a: Левая граница отрезка (b > a)
    :type a: float
    :param b: Правая граница отрезка (b > a)
    :type b: float
    :param epsilon: Допустимая погрешность, defaults to 10e-5
    :type epsilon: float, optional
    :param max_iteration: Максимальное количество итераций, defaults to 10000
    :type max_iteration: int, optional
    :raises ValueError: Если значения крайних точек находятся в одной области
    :raises RuntimeError: При превышении установленного лимита итераций
    :return: Единственное пересечение с осью абцисс
    :rtype: Result
    """

    # Находим значения функции в точках границ отрезка
    fa, fb = func(a), func(b)

    # Если значения крайних точек находятся в одной области, выдаем ошибку
    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")

    # Повторяем до момента переполнения установленного числа попыток
    for iter in range(max_iteration):
        # Находим точку пересечения прямой через точки с осью абцисс
        if fb - fa == 0:
            c = (a + b) / 2
        else:
            c = a - (b - a) / (fb - fa) * fa

        # Значение функции в точке c
        fc = func(c)

        # Если расстояние от оси до точки или длина отрезка меньше допустимой погрешности
        if (abs(fc) < epsilon) or (b - a < epsilon):
            return Result(c, func(c), iter)

        # Если знак точки a и c различен, то сдвигаем правую границу к центру,
        # иначе передвигаем левую
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку
    raise RuntimeError(
        f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})"
    )


def tangent(
    func: Callable[[float], float], x0: float, epsilon: float = 10e-6
) -> tuple[float, float]:
    k = (func(x0 + epsilon) - func(x0)) / epsilon
    b = func(x0) - k * x0
    return k, b


def method_newton(
    func: Callable[[float], float],
    func_prime: Callable[[float], float],
    a: float,
    b: float,
    x0: float = None,
    epsilon: float = 10e-6,
    max_iteration: int = 10000,
) -> Result:
    # Находим значения функции в точках границ отрезка
    fa, fb = func(a), func(b)

    # Если точка не задана, то расположим ее в центре отрезка
    if x0 is None:
        x0 = (a + b) / 2

    x_cur = x0

    for iter in range(max_iteration):
        x_next = x_cur - func(x_cur) / func_prime(x_cur)

        if abs(x_next - x_cur) < epsilon or abs(func(x_next)) < epsilon:
            return Result(x_next, func(x_next), iter)

        x_cur = x_next

    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку
    raise RuntimeError(
        f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})"
    )


def method_simple_iteration(
    phi: Callable[[float], float],
    a: float,
    b: float,
    x0: float = None,
    epsilon: float = 10e-6,
    max_iteration: int = 10000,
) -> float:
    # Если точка не задана, то расположим ее в центре отрезка
    if x0 is None:
        x0 = (a + b) / 2

    x_current, x_next = x0, None

    for i in range(max_iteration):
        f_current = phi(x_current)
        x_next = f_current

        if abs(x_next - x_current) < epsilon:
            return x_next

        if not (a <= x_next <= b):
            raise ValueError("Вычисления вышли за границы отрезка")

        x_current = x_next

    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку
    raise RuntimeError(
        f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})"
    )
