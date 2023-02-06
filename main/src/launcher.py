from owlready2 import *
onto = get_ontology("file://lotr.owl").load()

"""
print("Bonjour, vous pouvez maintenant utilisez l'application. Pour utiliser l'application veuillez rentrer une commande. Tapez /help pour voir la liste des commandes.")


text=input("prompt")

if (text=="/help") :
    print("Liste des commandes :")
elif (text=="/créerPerso") :
    print("")
elif (text=="/fichePerso") :
    print("")
elif (text=="/ficheEnnemie"):
    print("")
else :
    print("La commande n'est pas reconnu/ Veuillez taper ")
"""

print (list(onto.Humain.get_properties(self)))


