"""Тестирование модуля quadratic_equation"""

import pytest

from src.exceptions import ACoefficientEqualZeroException
from src.quadratic_equation import QuadraticEquation


class TestQuadraticEquation:
    """Тестируем решение квадратного уравнения"""

    def test_coefficient_a_equal_zero(self) -> None:
        """Проверим, что для коэффициента a равным нулю решений нет"""
        a = 0
        b = 1
        c = 1

        with pytest.raises(ACoefficientEqualZeroException) as _:
            QuadraticEquation(a, b, c)
