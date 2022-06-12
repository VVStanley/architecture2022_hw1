"""Решение квадратного уравнения"""
from math import sqrt

from src.exceptions import (
    ACoefficientEqualZeroError,
    DiscriminantLowerThanZeroError,
    WrongTypesArgumentsError,
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
        self._c = self._check_types_argument(c)
        self._b = self._check_types_argument(b)
        self._a = self._check_types_argument(a)
        self._check_coefficient_a(e)

        self._d = self._calc_discriminant()
        self._check_discriminant(e)

    @staticmethod
    def _check_types_argument(arg: float) -> float:
        """Приводим и проверяем тип аргумента"""
        try:
            return float(arg)
        except (ValueError, TypeError):
            raise WrongTypesArgumentsError

    def solve(self) -> tuple:
        """Решаем квадратное уравнение"""
        x1 = self._calc_x1()
        x2 = self._calc_x2()
        return x1, x2

    def _calc_discriminant(self) -> float:
        """Высчитываем дисткриминант D = b*b - 4*a*c"""
        return self._b * self._b - 4 * self._a * self._c

    def _check_discriminant(self, e: float) -> None:
        """Дискриминант не может быть меньше нуля
        и если дискриминант меньше погрешности e то приравниваем его к нулю
        """
        if self._d < 0:
            raise DiscriminantLowerThanZeroError
        elif self._d != 0 and self._d < e:
            self._d = 0

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
