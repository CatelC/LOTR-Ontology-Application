from owlready2 import *


onto = get_ontology("file://lotr.owl").load()

print(list(onto.object_properties()))