import pytest
from src.phone import Phone


@pytest.fixture
def phone_2():
    return Phone('mi', 150.0, 5, 1)


def test_phone_init(phone_2):
    """Создавая экземпляр класса, ожидаем получить заданные атрибуты при их запросе"""
    assert phone_2.name == 'mi'
    assert phone_2.price == 150.0
    assert phone_2.quantity == 5
    assert phone_2.number_of_sim == 1

def test_phone_number_of_sim(phone_2):
    """Проверяем возможность задать неверное количество сим-карт"""
    phone_2.number_of_sim = 2
    assert phone_2.number_of_sim == 2
    phone_2.number_of_sim = -2
    assert phone_2.number_of_sim == 2
    phone_2.number_of_sim = 0.5
    assert phone_2.number_of_sim == 2


def test_repr(phone_2):
    assert repr(phone_2) == "Phone('mi', 150.0, 5, 1)"
