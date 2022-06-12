"""Тестирование модуля quadratic_equation"""

import pytest

from src.exceptions import (
    ACoefficientEqualZeroError,
    DiscriminantLowerThanZeroError,
)
from src.quadratic_equation import QuadraticEquation


class TestQuadraticEquation:
    """Тестируем решение квадратного уравнения"""

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
