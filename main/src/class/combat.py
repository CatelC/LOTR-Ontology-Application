import random as rd
from launcher import *

class Spell:

    def __init__(self, name, costType, cost, damage):
        self.name=name
        self.costType=costType
        self.cost=cost
        self.damage=damage

class damage:

    def __init(self, max, min):
        self.min=min
        self.max=max
    
    def value(self):
        return rd.randint(self.min,self.max)

"""
def getDamage(attaquant,ennemie):
    
    getPropertyOfIndividual(attaquant)
    getPropertyOfIndividual(ennemie)
    return val
"""
        
