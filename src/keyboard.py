from src.item import Item


class MixinLeng:
    Leng = 'EN'

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.Leng

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if MixinLeng.Leng == 'EN':
            self.__language = 'RU'
            MixinLeng.Leng = 'RU'
        else:
            self.__language = 'EN'
            MixinLeng.Leng = 'EN'


class Keyboard(MixinLeng, Item):
    pass
