import methods
from typing import Callable
from dataclasses import dataclass
from math import log, e, cos, tan


@dataclass
class ExampleTask1:
    name: str
    func: Callable[[float], float]
    a: int
    b: int
    epsilon: float = 10e-5
    max_iteration: float = 10_000
    
    def __str__(self) -> str:
        return f"Ex. '{self.name}': a = {self.a}, b = {self.b}, \
epsilon = {self.epsilon}, max iteration = {self.max_iteration}"
    

@dataclass
class ExampleTask2:
    name: str
    func: Callable[[float], float]
    a: int
    b: int
    x0: int = None
    epsilon: float = 10e-5
    max_iteration: float = 10_000
    
    def __str__(self) -> str:
        return f"Ex. '{self.name}': a = {self.a}, b = {self.b}, x0 = {self.x0}, \
epsilon = {self.epsilon}, max iteration = {self.max_iteration}"
    

test_data = [
    ExampleTask2(
        name="Билет 1", 
        func=lambda x: x + log(1 + x) - 1.5,
        a = 0,
        b = 2,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 2", 
        func=lambda x: x * 2 ** x - 1,
        a = 0,
        b = 1,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 3", 
        func=lambda x: 2**x + 5*x - 3,
        a = 0,
        b = 1,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 4", 
        func=lambda x: 5**x - 3 + e**x,
        a = 0,
        b = 1,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 5", 
        func=lambda x: x + cos(x) - 1.7,
        a = 2,
        b = 3,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 6", 
        func=lambda x: log(2 + x) + 2*x - 3,
        a = 0,
        b = 1,
        epsilon=0.0001
    ),
    ExampleTask2(
        name="Билет 17", 
        func=lambda x: tan(x)**3 - x + 1,
        a = -1,
        b = -0.5,
        epsilon=0.0001
    ),
]



for index, test in enumerate(test_data):
    result_test_newton = None
    try:
        result_test_newton = methods.method_newton(
            func=test.func,
            a=test.a,
            b=test.b,
            x0=test.x0,
            epsilon=test.epsilon,
            max_iteration=test.max_iteration
        )
    except Exception as ex:
        print(test.name, ex)
        
    print(f"""
{index+1}) {test} 
Result Method Newtons: {result_test_newton}
""")