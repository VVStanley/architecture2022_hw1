class ACoefficientEqualZeroError(Exception):
    """Исключение возникающее если коэффициент a равен нулю"""

    def __init__(self) -> None:
        message = "Старший коэффициент не может быть равен нулю"
        super().__init__(message)


class DiscriminantLowerThanZeroError(Exception):
    """Исключение возникающее если дискрименант меньше нуля"""

    def __init__(self) -> None:
        message = "Дискрименант меньше нуля"
        super().__init__(message)


class WrongTypesArgumentsError(Exception):
    """Исключение возникающее если передали не верные типы аргументов"""

    def __init__(self) -> None:
        message = "Аргумент может быть только числом"
        super().__init__(message)
