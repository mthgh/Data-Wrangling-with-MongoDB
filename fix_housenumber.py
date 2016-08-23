from pymongo import MongoClient
import re

def check_useless_housenumber(collection):
    word_re = re.compile("[a-zA-Z]{2,}")
    useless = set()
    st = set()
    cursor = collection.find({"addr.housenumber":{"$exists":1},
                   "addr.street":{"$exists":0}})
    for doc in cursor:
        useless.add(doc["addr"]["housenumber"])
    for number in useless:
        if word_re.search(number):
            st.add(number)
    return useless, st

def fix_useless():
    housenumber_map_1 = {u'30 Vesey St':{"housenumber":"30", "street":"Vesey Street"},
                       u'359 van Brunt':{"housenumber":"359", "street":"Van Brunt Street"},
                       u'524 West 59th Street, New York, NY 10019':{"housenumber":"524", "street":"West 59th Street"},
                       u'Atlantic Ave':{"street":"Atlantic Avenue"},
                       u'48 W 37th':{"housenumber":"48", "street":"West 37Th Street"},
                       u'21-25 Robin':{"housenumber":"21-25", "street":"Robin Road"},
                       u'Route 11':{"street":"Route 11"},
                       u'Grand Street':{"street":"Grand Street"},
                       u'2734 Jerome Avenue':{"housenumber":"2734", "street":"Jerome Avenue"},
                       u'3rd Avenue':{"street":"3Rd Avenue"},
                       u'Park Street':{"street":"Park Street"},
                       u'502 9th Avenue':{"housenumber":"502", "street":"9Th Avenue"}}
    return housenumber_map_1

def check_abnormal_housenumber(dist_housenumber, useless):
    word_re = re.compile("[a-zA-Z]{2,}")
    abnormal = set()
    for number in dist_housenumber:
        if number not in useless and word_re.search(number) and number.find("REAR")==-1:
            abnormal.add(number)
    return abnormal

def fix_abnormal_housenumber():
    housenumber_map_2 = {'1-3 Washington Square North':"1-3",
                    '101 Street Avenue':"101",
                    '318 Lafayette Avenue':"318",
                    '81-40 Lefferts Blvd.':"81-40",
                    '695 Park Avenue':"695",
                    '543 9th Avenue':"543",
                    '408 West 22nd Street #2R':"408",
                    '82 nj 35 keyport, nj':"82",
                    'Gas Station':{"housename":"Gas Station"},
                    'South side of Queens Blvd at':"",}
    return housenumber_map_2

def update_housenumber_1(collection, housenumber_map_1):
    cursor = collection.find({"addr.housenumber":{"$exists":1},
                                "addr.street":{"$exists":0}})
    for doc in cursor:
        old_housenumber = doc["addr"]["housenumber"]
        doc["addr"].pop("housenumber")
        
        if old_housenumber in housenumber_map_1:
            new_housenumber = housenumber_map_1[old_housenumber]
            for key in new_housenumber:
                doc["addr"][key] = new_housenumber[key]
                
        collection.save(doc)

def update_housenumber_2(collection, housenumber_map_2):
    cursor = collection.find({"addr.housenumber":{"$exists":1}})
    
    for doc in cursor:
        old_housenumber = doc["addr"]["housenumber"]
        
        if old_housenumber in housenumber_map_2:
            new_housenumber = housenumber_map_2[old_housenumber]
            doc["addr"].pop("housenumber")           
            if type(new_housenumber) == type({}):
                for key in new_housenumber:
                    doc["addr"][key] = new_housenumber[key]
            elif new_housenumber:
                doc["addr"]["housenumber"] = new_housenumber
            collection.save(doc)

def main(collection):
    dist_housenumber = collection.distinct("addr.housenumber")
    useless, st = check_useless_housenumber(collection)
    housenumber_map_1 = fix_useless()
    abnormal = check_abnormal_housenumber(dist_housenumber, useless)
    housenumber_map_2 = fix_abnormal_housenumber()
    update_housenumber_1(collection, housenumber_map_1)
    update_housenumber_2(collection, housenumber_map_2)
    return housenumber_map_1, housenumber_map_2
    
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    housenumber_map_1, housenumber_map_2 = main(collection)
