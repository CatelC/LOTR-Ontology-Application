from owlready2 import *
onto = get_ontology("file://lotr2.owl").load()

with onto:
    class Lieu(Thing):
        python_name="lieu"