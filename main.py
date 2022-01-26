import pymongo
import re
myclient = pymongo.MongoClient()

mydb = myclient["Music_bot"]
mycol = mydb["songs"]
#mylist ={ "name": "مهتاب تر از باران", "address": "https://webahang.ir/single-tracks/alireza-ghorbani-mahtab-tar-az-baran/"}

#mycol.insert_one(mylist)
#regx = re.compile("^foo", re.IGNORECASE)
#mycol.find({"name":{$regx:"cdf"}})
#db.employee.find({Name: /te/}).pretty()
#mu = mycol.find({"name":{"$regex":"software","$options":"$i"}}).pretty()

def find(input):
    for x in mycol.find({"name":{"$regex":input}}):
       # if(x["name"]==input):
       print(x["name"])
       print(x["address"])

find("گنج")