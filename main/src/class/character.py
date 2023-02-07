from owlready2 import *
onto = get_ontology("file://lotr.owl").load()


with onto:

    class Personnage(Thing):
        
        
        def attack(self, weapon, enemy):
            return f"{self.name} attacks {enemy} with {weapon}, causing X damage"

        def spellcast(self, spell, enemy):
            return f"{self.name} cast {spell.name} to {enemy}"
           
        

