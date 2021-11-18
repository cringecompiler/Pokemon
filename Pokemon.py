import random
from abc import abstractmethod


class AnimeMon:
    """абстрактный класс"""
    @classmethod
    @abstractmethod
    def inc_exp(cls, value):
        pass

    @property
    @abstractmethod
    def exp(cls):
        pass

    @exp.setter
    @abstractmethod
    def exp(self, value):
        pass


def train(animemon: AnimeMon):
    """увеличение опыта на случайное число"""
    step_size, level_size = 10, 100
    sparring_qty = (level_size - animemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            animemon.inc_exp(step_size)


class BasePokemon:
    """базовый класс"""
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin():
    """миксин, заменяющий тип покемона на эмодзи"""
    emoji = {'grass': '🌿', 'fire': '🔥', 'water': '🌊', 'electric': '⚡'}

    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emoji[self.poketype])


class Pokemon(EmojiMixin, BasePokemon, AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    def inc_exp(self, value: int):
        self._exp += value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value


class Digimon(AnimeMon):
    def __init__(self, name):
        self.name = name
        self._exp = 0

    def inc_exp(self, value: int):
        self.exp += value * 8

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value


if __name__ == '__main__':
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(f'{agumon.exp = }')

    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(f'{bulbasaur.exp = }')
    print(bulbasaur)
