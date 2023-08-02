from src.item import Item


class Phone(Item):
    """
    Создание экземпляра класса Phone
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        """Отображает информацию об объекте в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', " \
        f"{self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Геттер для number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """Сеттер для number_of_sim"""
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
