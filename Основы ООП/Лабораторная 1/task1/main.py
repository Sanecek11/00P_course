import doctest


class Keycard:
    def __init__(self, card_id: int, pin: str, owner: str):
        if not isinstance(card_id, int) or card_id <= 0:
            raise ValueError("Card ID должно быть положительным числом")
        if not isinstance(pin, str) or len(pin) != 4:
            raise ValueError("Пароль должен быть строкой из 4 символов")
        if not isinstance(owner, str) or not owner:
            raise ValueError("Имя владельца не может быть пустым")

        self.card_id = card_id
        self.pin = pin
        self.owner = owner

    def validate_pin(self, entered_pin: str) -> bool:
        """
        Проверяет введенный пароль среди имеющихся в базе.

        Args:
            entered_pin (str): Пароль введенный пользователем.

        Returns:
            bool: True если введенный пароль совпадает с базой, False если нет.
        """
        pass

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        """
        Changes the PIN if the old PIN is correct.

        Args:
            old_pin (str): Старый пароль введенный пользователем.
            new_pin (str): Новый пароль введенный пользователем.
        """
        pass

    def transfer_ownership(self, new_owner: str) -> None:
        """
        Передача ключа новому пользователю.

        Args:
            new_owner (str): Имя нового пользователя.
        """
        pass


class Headphones:
    def __init__(self, brand: str, model: str, volume: int):
        """
        Конструктор класса Headphones.

        Args:
            brand (str): Марка наушников.
            model (str): Модель наушников.
            volume (float): Громкость наушников от 0 до 100.

        Raises:
            ValueError: Если значение громкости выходит за пределы от 0 до 100.
        """
        if not 0 <= volume <= 100:
            raise ValueError("Громкость должна быть между 0 и 100")
        self.brand = brand
        self.model = model
        self.volume = volume

    def play_music(self, track: str) -> None:
        """
        Воспроизводит музыкальный трек.

        Args:
            track (str): Трек, который нужно воспроизвести.
        """
        pass

    @classmethod
    def adjust_volume(cls, level: int) -> None:
        """
        Регулирует громкость наушников.

        Args:
            level (float): Уровень громкости от 0 до 100.

        Raises:
            ValueError: Если уровень громкости выходит за пределы от 0 до 100.
        """
        if not 0 <= level <= 100:
            raise ValueError("Уровень громкости должен быть между 0 и 100")
        pass

    def change_battery(self, battery: str) -> None:
        """
        Заменяет батарею наушников.

        Args:
            battery (str): Тип батареи.
        """
        pass


class Volume:
    def __init__(self, max_volume: float, real_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param max_volume: Максимально допустимая громкость
        :param real_volume: Реальная громкость

        """

        volume = Volume(100, 0)  # инициализация экземпляра класса

        if not isinstance(max_volume, (int, float)):
            raise TypeError("Значение громкости должно быть типа int или float")
        if max_volume <= 0:
            raise ValueError("Значение громкости должно быть положительным числом")
        self.max_volume = max_volume

        if not isinstance(real_volume, (int, float)):
            raise TypeError("Значение громкости должно быть int или float")
        if real_volume < 0:
            raise ValueError("Значение громкости не может быть отрицательным числом")
        self.real_volume = real_volume

    @classmethod
    def is_volume_zero(cls) -> bool:
        """
        Функция проверяет выключен ли звук

        :return: Выключен ли звук

        """
        pass
        volume = Volume(100, 0)
        volume.is_volume_zero()

    @classmethod
    def add_volume(cls, plus_volume: float) -> None:
        """
        Увеличение громкости.
        :param plus_volume: Кол-во добавляемой громкости

        :raise ValueError: Если кол-во единиц громкости превышает допустимое, то вызываем ошибку
        """
        pass

        volume = Volume(100, 0)
        volume.add_volume(50)

        if not isinstance(plus_volume, (int, float)):
            raise TypeError("Громкость быть типа int или float")
        if plus_volume < 0:
            raise ValueError("Громкость должна положительным числом")
        if plus_volume > 100:
            raise ValueError("Громкость не может быть больше 100")

    @classmethod
    def subtract_volume(cls, minus_volume: int) -> None:
        """
        Извлечение воды из стакана.

        :param minus_volume: Кол-во ед. громкости.
        :raise ValueError: Если кол-во уменьшаемой громкости превышает имеющуюся,
        то возвращается ошибка.

        :return: Кол-во ед. уменьшенной громкости
        """
        pass

        volume = Volume(100, 0)
        volume.subtract_volume(50)


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

