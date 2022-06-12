"""Решение квадратного уравнения"""

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
        self._check_discriminant(e)

    def _calc_discriminant(self) -> float:
        """Высчитываем дисткриминант D = b*b - 4*a*c"""
        return self._b * self._b - 4 * self._a * self._c

    def _check_discriminant(self, e: float) -> None:
        """Дискриминант не может быть меньше нуля"""
        if self._d < e:
            raise DiscriminantLowerThanZeroError

    def _check_coefficient_a(self, e: float) -> None:
        """Если коэффициент a равен нулю у уравнения нет решений"""
        if abs(self._a) < e:
            raise ACoefficientEqualZeroError

    def solve(self):
        """Решаем квадратное уравнение"""
        pass
