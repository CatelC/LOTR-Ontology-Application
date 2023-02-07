from owlready2 import *
onto = get_ontology("file://lotr2.owl").load()


def searchInstanceOfClass(string) :
    return list(default_world.sparql("""
    PREFIX onto: <http://www.semanticweb.org/jeanb/ontologies/2023/0/untitled-ontology-5#>
SELECT ?X
WHERE {
    ?X a ?type.
    ?type rdfs:subClassOf* onto:"""+string+""" .
}
    """))


def searchIndividualMatchingProperty(objectProperty, instance): 
    return list(default_world.sparql("""
    PREFIX onto: <http://www.semanticweb.org/jeanb/ontologies/2023/0/untitled-ontology-5#>
SELECT ?p
    WHERE {
    ?p onto:"""+objectProperty+""" onto:"""+instance+""" .
}
    """))

def getPropertyOfIndividual(individual):
    return list(default_world.sparql("""
    PREFIX onto: <http://www.semanticweb.org/jeanb/ontologies/2023/0/untitled-ontology-5#>
SELECT DISTINCT ?property ?value where {
  onto:"""+individual+""" ?property ?value .
}
    """))

#print(searchInstanceOfClass("Lieu"))
#print(searchIndividualMatchingProperty("estDeRace","Istari"))
#print(searchIndividualMatchingProperty("appartientA", "Aragorn"))
#print(getPropertyOfClass("Aragorn"))


