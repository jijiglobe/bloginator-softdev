from pymongo import MongoClient

con = MongoClient()

db = con["testDatabase"]

myDict = { "name": "Jion",
           "donut": "glazed"
}

db.people.insert(myDict)
myDict = { "name": "Chris",
           "donut": "sprinkled"
}

db.people.insert(myDict)

people = db.people

print db.people

res = db.people.find({"name":"Jion"})
for r in res:
    print r


