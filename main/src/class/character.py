from equipment import Equipment
from combat import *


class Character():

    def __init__(self, level: int, classe, race, equipmentList: list[Equipment], statList, name="Radis Moisi"):
        self.name = name
        self.level = level
        self.classe = classe
        self.race = race
        self.equipmentList = equipmentList
        self.statList = statList

    def attack(self, weapon, enemy):
        return f"{self.name} attacks {enemy} with {weapon}, causing X damage"

    def spellcast(self, spell, enemy):
        return f"{self.name} cast {spell.name} to {enemy}"

