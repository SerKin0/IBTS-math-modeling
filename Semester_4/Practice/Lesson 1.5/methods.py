from typing import Callable


def method_dichotomy(func: Callable[[float], float], a: float, b: float, 
                     epsilon: float = 10e-5, max_iteration: int = 10000) -> float:
    """ ## Метод Дихотомии (Метод половинного деления)
    
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
    :raises InterruptedError: При превышении установленного лимита итераций
    :raises ValueError: Если значения крайних точек находятся в одной области
    :return: Единственное пересечение с осью абцисс
    :rtype: float
    """
    # Находим значения функции в точках границ отрезка
    fa, fb = func(a), func(b)
    
    # Если значения крайних точек находятся в одной области, выдаем ошибку
    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")
    
    # Повторяем до момента переполнения установленного числа попыток
    for i in range(max_iteration):
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
            return c
        
    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку 
    raise InterruptedError(f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})")


def method_chord(func: Callable[[float], float], a: float, b: float, 
                 epsilon: float = 10e-5, max_iteration: int = 10000) -> float:
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
    :raises InterruptedError: При превышении установленного лимита итераций
    :return: Единственное пересечение с осью абцисс
    :rtype: float
    """
    
    # Находим значения функции в точках границ отрезка
    fa , fb = func(a), func(b)
    
    # Если значения крайних точек находятся в одной области, выдаем ошибку
    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")
    
    # Повторяем до момента переполнения установленного числа попыток
    for i in range(max_iteration):
        # Находим точку пересечения прямой через точки с осью абцисс
        if fb - fa == 0:
            c = (a + b) / 2
        else:
            c = a - (b - a) / (fb - fa) * fa
        
        # Значение функции в точке c
        fc = func(c)

        # Если расстояние от оси до точки или длина отрезка меньше допустимой погрешности
        if (abs(fc) < epsilon) or (b - a < epsilon):
            return c
        
        # Если знак точки a и c различен, то сдвигаем правую границу к центру, 
        # иначе передвигаем левую
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        
    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку 
    raise InterruptedError(f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})")
    
    
def tangent(func: Callable[[float], float], x0: float, epsilon: float = 10e-6) -> tuple[float, float]:
    k = (func(x0 + epsilon) - func(x0)) / epsilon
    b = func(x0) - k * x0
    return k, b
    
    
def method_newton(func: Callable[[float], float], a: float, b: float, x0: float = None,
                  epsilon: float = 10e-6, max_iteration: int = 10000) -> float:
    # Находим значения функции в точках границ отрезка
    fa , fb = func(a), func(b)
    
    # Если значения крайних точек находятся в одной области, выдаем ошибку
    if fa * fb > 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")
    
    # Если точка не задана, то расположим ее в центре отрезка
    if x0 is None:
        x0 = (a + b) / 2
        
    for i in range(max_iteration):
        kl, bl = tangent(func=func, x0=x0)
        x = - bl / kl
        fx = func(x)
        
        if x < a or x > b:
            raise 
        
        if (abs(fx) < epsilon):
            return x0
        
        x0 = x
        
    # В случае, если пересечение не было найдено за отведенное количество итераций, то
    # выдаем соответствующую ошибку 
    raise InterruptedError(f"Нахождение корня превысило количество допустимых итераций ({max_iteration=})")
        
        
print(method_newton(func=lambda x: x ** 2 - 2 * x - 3, a=1, b=5))