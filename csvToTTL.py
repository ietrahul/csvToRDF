import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD #most common namespaces
import urllib.parse #for parsing strings to URI's

prefixConfig = "J:\GraphDB\code\prefixes.csv"
prefixDF = pd.read_csv(prefixConfig,sep=",",quotechar='"')
ttlConfig = "J:\GraphDB\code\sampleTTLConfig.csv"
ttlDF = pd.read_csv(ttlConfig,sep=",",quotechar='"')

csvSource = 'J:\GraphDB\code\sampleCSVData.csv'
df = pd.read_csv(csvSource,sep=",",quotechar='"')

g = Graph()
# demo = Namespace('http://example.com/employee/')

for index, row in prefixDF.iterrows():
    #print(row.iloc[0], row['prefix'], row['prefixURL'])
    vars()[row.iloc[0]] = Namespace(row.iloc[1])

print(demo)
# print(str('a'))

demo2 = Namespace('http://example.com/employee2/')
print('demo2--',demo2)

for index, row in df.iterrows():
      for configIndex, config in ttlDF.iterrows():
          sub = ''
          pred = ''
          obj = ''
          if config['subjectSource'] == 'column':
              sub = URIRef(config['subjectPrefix'] + ':' + str(row[config['subject']]))
          else:
              sub = config['subjectPrefix'] + ":" + str(config['subject'])
          #print('sub', sub)


          if config['predicateSource'] == 'column':
             pred = URIRef(config['predicatePrefix'] +':'+ str(row[config['predicate']]))
          else:
              if config['predicate'] == 'type':
                  pred = RDF.type
              else:
                  pred = URIRef(config['predicatePrefix'] + ':' + str(config['predicate']))
          #print('pred', pred)
          

          if config['objectSource'] == 'column':
              #obj = URIRef(config['objectPrefix'] + str(row[config['object']]))
              obj = Literal(row[config['object']], datatype=config['objectDataType'] )
          else:
              obj = URIRef(config['objectPrefix'] + ':' + str(config['object']))
        #   print('obj', obj)

          g.add((sub, pred, obj))


#     g.add((URIRef(demo+str(row['empID'])), RDF.type, URIRef(demo + 'Employee')))
#     g.add((URIRef(demo+str(row['empID'])), URIRef(demo+'Name'),  Literal(row['name'], datatype=XSD.string)))
#     g.add((URIRef(demo+str(row['empID'])), URIRef(demo+'Age'),  Literal(row['age'], datatype=XSD.string)))


print(g.serialize(format='turtle'))