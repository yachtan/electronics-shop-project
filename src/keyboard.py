from src.item import Item


class MixinLeng:

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):

        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'



class Keyboard(MixinLeng, Item):
    pass
