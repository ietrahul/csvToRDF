import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's

url='https://raw.githubusercontent.com/KRontheWeb/csv2rdf-tutorial/master/example.csv'
df=pd.read_csv(url,sep=";",quotechar='"')

g = Graph()
ppl = Namespace('http://example.org/people/')
loc = Namespace('http://mylocations.org/addresses/')
schema = Namespace('http://schema.org/')

for index, row in df.iterrows():
    g.add((URIRef(ppl+row['Name']), RDF.type, FOAF.Person))
    g.add((URIRef(ppl+row['Name']), URIRef(schema+'name'), Literal(row['Name'], datatype=XSD.string) ))
    g.add((URIRef(ppl+row['Name']), FOAF.age, Literal(row['Age'], datatype=XSD.integer) ))
    g.add((URIRef(ppl+row['Name']), URIRef(schema+'address'), Literal(row['Address'], datatype=XSD.string) ))
    g.add((URIRef(loc+urllib.parse.quote(row['Address'])), URIRef(schema+'name'), Literal(row['Address'], datatype=XSD.string) ))


print(g.serialize(format='turtle'))