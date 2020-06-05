import pymongo
import datatable as dt
import pandas as pd
import pprint

try:
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
except:
  print("Could not connect to Mongo")

try:
  mydb = myclient["kaggle"]
except:
  print("Could not open database kaggle")

mycollection = mydb['testje']


mf = dt.fread("movies.csv")
print(mf.head())
print(mf.shape)
print(mf.names)

nf = mf.to_numpy()
pf = mf.to_pandas()
lf = mf.to_list()

print(type(mf))
print(type(nf))
print(type(pf))

data = pf.to_dict(orient='records')
mycollection.insert_many(data)

dblist = myclient.list_database_names()
print(dblist)
collist = mydb.list_collection_names()
print(collist)

pprint.pprint(mycollection.find_one({ "Year": 2012 }))

for movie in mycollection.find({ "Year": 2000 }):
  pprint.pprint(movie)

print(mycollection.count_documents({}))
