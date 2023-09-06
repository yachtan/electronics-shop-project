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

def test_item_calculate_total_price(phone):
    """Задавая цену и количество, ожидаем получить общую стоимость товара"""
    assert phone.calculate_total_price() == 2000.0

def test_item_apply_discount(phone):
    """Задав скидочный коэффициент 0.8 и применив метод apply_discount,
    ожидаем получить новую цену со скидкой 20%"""
    phone.pay_rate = 0.8
    phone.apply_discount()
    assert phone.price == 80.0
