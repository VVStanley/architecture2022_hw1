class ACoefficientEqualZeroException(Exception):
    """Исключение возникающее если коэффициент a равен нулю"""

    def __init__(self) -> None:
        message = "Старший коэффициент не может быть равен нулю"
        super().__init__(message)
