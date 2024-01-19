class Calculator:

    """Вычисляет"""

    @staticmethod
    def add(a, b):
        """ Формула площади по двум сторонам и углу между ними. """
        return a + b

    @staticmethod
    def mul(a, b):
        """ Формула площади по двум сторонам и углу между ними. """
        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
