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
    
    

class Example:
    def __init__(self, name: str, func: Callable[[float], float], a: int, b: int, 
                 epsilon: float = 10e-5, max_iteration: float = 10000) -> None:
        
        self.name = name
        self.func = func
        
        if a > b:
            self.a, self.b = b, a
        else:
            self.a, self.b = a, b
            
        self.epsilon = epsilon
        self.max_iteration = max_iteration
    
    def __str__(self) -> str:
        return f"Ex. '{self.name}': a = {self.a}, b = {self.b}, epsilon = {self.epsilon}, max iteration = {self.max_iteration}"
    

test_data = [
    Example(
        name = "Билет 1",
        func=lambda x: 3*x**4 + 4 * x**3 - 12 * x**2 - 5,
        a = 1, b = 2,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 2",
        func=lambda x: 2*x**4 - 9 * x**3 - 60 * x**2 + 1,
        a = 0, b = 1,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 3",
        func=lambda x: 3*x**4 + 8 * x**3 + 6 * x**2 - 10,
        a = 0, b = 1,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 4",
        func=lambda x: x**5 + x**2 - 5,
        a = 1, b = 2,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 5",
        func=lambda x: 3*x**4 + 8 * x**3 + 6 * x**2 - 11,
        a = 0.5, b = 1,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 6",
        func=lambda x: x**4 - 18 * x**3 - 10,
        a = -1, b = 0,
        epsilon=0.0001
    ),
    Example(
        name = "Билет 17",
        func=lambda x: x**4 - 18 * x - 10,
        a = -1, b = 0,
        epsilon=0.0001
    ),
]

for index, test in enumerate(test_data):
    try:
        result_method_dichotomy = method_dichotomy(
            func=test.func,
            a=test.a,
            b=test.b,
            epsilon=test.epsilon,
            max_iteration=test.max_iteration
        )
    except Exception as ex:
        result_method_dichotomy = None
        print(ex)
    try:
        result_method_chord = method_chord(
            func=test.func,
            a=test.a,
            b=test.b,
            epsilon=test.epsilon,
            max_iteration=test.max_iteration
        )
    except Exception as ex:
        result_method_chord = None
        print(ex)
        
    print(f"""
{index+1}) {test} 
Result Method Dichotomy: {result_method_dichotomy}
Result Method Chord: {result_method_chord}
""")