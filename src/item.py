import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name[0:10]
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return 'Ошибка! Нельзя складывать объекты, не являюшиеся экземплярами классов Phone или Item'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[0:10]

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
           Создает экземпляры класса из cvs файла
        """
        try:
            with open(file_name) as file:
                DictReader_obj = csv.DictReader(file)
                for i in DictReader_obj:
                    item = cls(i['name'], float(i['price']), int(i['quantity']))
                    cls.all.append(item)

        except FileNotFoundError:
            raise FileNotFoundError(f'FileNotFoundError: Отсутствует файл {file_name}')

        except KeyError:
            raise InstantiateCSVError(f'InstantiateCSVError: Файл {file_name} поврежден')
        except ValueError:
            raise InstantiateCSVError(f'InstantiateCSVError: Файл {file_name} поврежден')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(value):
        return int(float(value))

