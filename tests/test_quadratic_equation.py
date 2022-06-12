"""Тестирование модуля quadratic_equation"""

import pytest

from src.exceptions import (
    ACoefficientEqualZeroError,
    DiscriminantLowerThanZeroError,
)
from src.quadratic_equation import QuadraticEquation


class TestQuadraticEquation:
    """Тестируем решение квадратного уравнения ax^2 + bx + c = 0"""

    def test_quadratic_equation_has_one_roots(self) -> None:
        """Квадратное уравнение имеет один корень"""
        a = 1
        b = 2
        c = 1

        quadratic_equation = QuadraticEquation(a, b, c)
        x1, x2 = quadratic_equation.solve()

        assert x1 == x2
        assert x2 == -2

    def test_quadratic_equation_has_two_roots(self) -> None:
        """Квадратное уравнение имеет два корня"""
        a = 1
        b = 0
        c = -1

        quadratic_equation = QuadraticEquation(a, b, c)
        x1, x2 = quadratic_equation.solve()

        assert x1 == 1
        assert x2 == -1

    def test_discriminant_lower_than_zero(self) -> None:
        """Проверяем что при дискриминанте меньше нуля решений нет"""
        a = 1
        b = 0
        c = 1

        with pytest.raises(DiscriminantLowerThanZeroError) as exc_info:
            QuadraticEquation(a, b, c)

        assert exc_info.typename == "DiscriminantLowerThanZeroError"
        assert str(exc_info.value) == "Дискрименант меньше нуля"

    def test_coefficient_a_equal_zero(self) -> None:
        """Проверим, что для коэффициента a равным нулю решений нет"""
        a = 0
        b = 1
        c = 1

        with pytest.raises(ACoefficientEqualZeroError) as exc_info:
            QuadraticEquation(a, b, c)

        assert exc_info.typename == "ACoefficientEqualZeroError"
        assert str(exc_info.value) == (
            "Старший коэффициент не может быть равен нулю"
        )
