# -*- coding: utf-8 -*-
import json
import os
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myenv/Lib/site-packages')))
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

wikiID = os.environ['req_query_wikiID']

#search_term = "wd:Q76"

sparql.setQuery("""SELECT ?wdLabel ?ps_Label ?wdpqLabel ?pq_Label {
  VALUES (?company) {("""
  'wd:'+wikiID+ """)}

  ?company ?p ?statement .
  ?statement ?ps ?ps_ .

  ?wd wikibase:claim ?p.
  ?wd wikibase:statementProperty ?ps.

  OPTIONAL {
  ?statement ?pq ?pq_ .
  ?wdpq wikibase:qualifier ?pq .
  }

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
} ORDER BY ?wd ?statement ?ps_
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# for result in results["results"]["bindings"]:
#     print(result)
attibutsDict = {}
for result in results["results"]["bindings"]:
    if result["wdLabel"]["value"] not in attibutsDict :
        attibutsDict[result["wdLabel"]["value"]] = result["ps_Label"]["value"]
        #print(result["wdLabel"]["value"] + " : " + result["ps_Label"]["value"])

    else :
        if type(attibutsDict[result["wdLabel"]["value"]]) is not list :
            tempList = []
            tempList.append(attibutsDict[result["wdLabel"]["value"]])
            tempList.append(result["ps_Label"]["value"])
            attibutsDict[result["wdLabel"]["value"]] = tempList

        else:
            attibutsDict[result["wdLabel"]["value"]].append(result["ps_Label"]["value"])


#remove duplication from lists
cleanDict =  {}
for key, value in attibutsDict.items() :
    if type(value) is list :
        cleanDict[key] = list(set(value))
    else :
        cleanDict[key] = value


output = open(os.environ['res'], 'w')
output.write(json.dumps(cleanDict))
#output.write(json.dumps(para))
