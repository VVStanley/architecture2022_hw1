"""Решение квадратного уравнения"""


class QuadraticEquation:
    """Производим решение квадратного уравнения

    Полное квадратное уравнение имеет вид: ax^2 + bx + c = 0
    """

    def __init__(self, a: float, b: float, c: float, e: float = 1e-5):
        """Инициализация и проверка коэффициентов

        a, b, c - любые действительные числа
        :param a: Старший коэффициент
        :param b: Коэффициент при x
        :param c: Свободный член
        :param e: Погрешность для чисел с плавоющей точкой
        """
        pass