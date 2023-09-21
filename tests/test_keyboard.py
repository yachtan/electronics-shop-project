import pytest
from src.keyboard import Keyboard


@pytest.fixture
def kb_1():
    return Keyboard('kb_name', 190, 4)


def test_keyboard_init(kb_1):
    """Создавая экземпляр класса, ожидаем получить заданные атрибуты при их запросе"""
    assert kb_1.name == 'kb_name'
    assert kb_1.price == 190.0
    assert kb_1.quantity == 4
    assert kb_1.language == 'EN'

def test_keyboard_change_lang(kb_1):
    """Проверка переключения языка"""
    kb_1.change_lang()
    assert kb_1.language == 'RU'
    kb_1.change_lang()
    assert kb_1.language == 'EN'
