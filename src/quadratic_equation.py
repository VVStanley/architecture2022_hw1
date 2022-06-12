"""Решение квадратного уравнения"""
from src.exceptions import ACoefficientEqualZeroError


class QuadraticEquation:
    """Производим решение квадратного уравнения

    Полное квадратное уравнение имеет вид: ax^2 + bx + c = 0
    """

    def __init__(self, a: float, b: float, c: float, e: float = 1e-5) -> None:
        """Инициализация и проверка коэффициентов

        a, b, c - любые действительные числа
        :param a: Старший коэффициент
        :param b: Коэффициент при x
        :param c: Свободный член
        :param e: Погрешность для чисел с плавоющей точкой
        """
        self._c = c
        self._b = b
        self._a = a
        self._check_coefficient_a(e)

    def _check_coefficient_a(self, e: float) -> None:
        """Если коэффициент a равен нулю у уравнения нет решений"""
        if self._a < abs(e):
            raise ACoefficientEqualZeroError
