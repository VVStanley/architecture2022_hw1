"""Решение квадратного уравнения"""
from math import sqrt

from src.exceptions import (
    ACoefficientEqualZeroError,
    DiscriminantLowerThanZeroError,
)


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

        self._d = self._calc_discriminant()
        self._check_discriminant()

    def solve(self) -> tuple:
        """Решаем квадратное уравнение"""
        x1 = self._calc_x1()
        x2 = self._calc_x2()
        return x1, x2

    def _calc_discriminant(self) -> float:
        """Высчитываем дисткриминант D = b*b - 4*a*c"""
        return self._b * self._b - 4 * self._a * self._c

    def _check_discriminant(self) -> None:
        """Дискриминант не может быть меньше нуля"""
        if self._d < 0:
            raise DiscriminantLowerThanZeroError

    def _check_coefficient_a(self, e: float) -> None:
        """Если коэффициент a равен нулю у уравнения нет решений"""
        if abs(self._a) < e:
            raise ACoefficientEqualZeroError

    def _calc_x1(self) -> float:
        """Высчитываем первый корень"""
        return - self._b + sqrt(self._d) / 2 * self._a

    def _calc_x2(self) -> float:
        """Высчитываем второй корень"""
        return - self._b - sqrt(self._d) / 2 * self._a
