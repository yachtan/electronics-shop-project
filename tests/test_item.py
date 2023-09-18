"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def phone():
    return Item('samsung', 100.0, 20)


def test_item_init(phone):
    """Создавая экземпляр класса, ожидаем получить заданные атрибуты при их запросе"""
    assert phone.name == 'samsung'
    assert phone.price == 100.0
    assert phone.quantity == 20


@pytest.fixture
def phone_1():
    return Item('samsung_0000', 100.0, 2)


def test_item_init(phone_1):
    """Проверяем создание класса с длинным именем"""
    assert phone_1.name == 'samsung_00'

def test_repr(phone):
    assert repr(phone) == "Item('samsung', 100.0, 20)"


def test_str(phone):
    assert str(phone) == 'samsung'


def test_item_calculate_total_price(phone):
    """Задавая цену и количество, ожидаем получить общую стоимость товара"""
    assert phone.calculate_total_price() == 2000.0


def test_item_apply_discount(phone):
    """Задав скидочный коэффициент 0.8 и применив метод apply_discount,
    ожидаем получить новую цену со скидкой 20%"""
    phone.pay_rate = 0.8
    phone.apply_discount()
    assert phone.price == 80.0


def test_name(phone):
    """Проверяем возможность изменения наименования товара.
    При слишком длинном имени остается первые 10 символов"""
    phone.name = 'Nokia 3310'
    assert phone.name == 'Nokia 3310'
    phone.name = 'Nokia 2210123'
    assert phone.name == 'Nokia 2210'


def test_string_to_number(phone):
    """Проверяем работу статического метода"""
    assert phone.string_to_number('5') == 5
    assert phone.string_to_number('6.7') == 6
    assert phone.string_to_number('8.0') == 8


@pytest.fixture
def items_from_csv():
    test_file_name = '../tests/for_testing.csv'
    Item.instantiate_from_csv(test_file_name)
    return Item.all


def test_instantiate_from_csv(items_from_csv):
    """Проверяем метод создания экземпляров из файла. Для тестирования создан файл:"""
    # test_file_name = 'tests/for_testing.csv'
    # Item.instantiate_from_csv(test_file_name)
    assert len(items_from_csv) == 4
    assert items_from_csv[0].name == 'Name_1'
    assert items_from_csv[1].price == 1000
    assert items_from_csv[2].quantity == 7
    assert items_from_csv[3].calculate_total_price() == 2500

def test_add(phone, phone_1):
    assert phone + phone_1 == 22
    assert phone + 3 == 'Ошибка! Нельзя складывать объекты, не являюшиеся экземплярами классов Phone или Item'

