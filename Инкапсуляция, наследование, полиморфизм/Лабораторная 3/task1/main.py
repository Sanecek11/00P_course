class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс базовой книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("число страниц может быть только числовым значением")
        if value <= 0:
            raise ValueError("число страниц не может быть меньше нуля")
        self.pages = value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Cтраницы: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс базовой книги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("время продолжительности книги может быть только числовым значением")
        if value <= 0:
            raise ValueError("время продолжительности книги не может быть меньше нуля")
        self.duration = value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"
