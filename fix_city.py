from pymongo import MongoClient
import re
import pandas as pd

def check_city(dist_city):
    end_with_state_re = re.compile(",|\s(ny|ct|nj)$", re.IGNORECASE)
    city = set()
    city_state = set()
    
    for c in dist_city:
        if not end_with_state_re.search(c):
            city.add(c)
        else:
            city_state.add(c)
    return city, city_state

def fix_city_with_state(city, city_state):
    city_map = {}

    for c in city:
        city_map[c] = c.strip().title()
    for c in city_state:
        if c.find(",")==-1:
            new_city = c[:-3]
            state = c[-2:]
            postcode = ""
        else:
            new_city, state = c.split(",")
            postcode = ""
            if state == " New York":
                state = "NY"
            if re.search("\d", state):
                state, postcode = state.strip().split(" ")
        if not state:
            city_map[c] = new_city.title()
        elif not postcode:
            city_map[c] = [new_city.title(), state.strip().upper()]
        else:
            city_map[c] = [new_city.title(), state.upper(), postcode]
    return city_map

def stnd_town(filename):
    with open(filename) as f:
        town = pd.read_csv(f, sep='\t',names=range(19), dtype=str)
    ny_town = town[((town[10]=="NY")|(town[10]=="NJ")|(town[10]=="CT"))& (town[6]=="P")][1].unique()
    return ny_town

def problematic_city(city_map, ny_town):
    prob_city_name = set()
    for name in city_map.values():
        if type(name) == type([]):
            name = name[0]
        if str(name) not in ny_town:
            prob_city_name.add(name)
    return prob_city_name

def classify_city(prob_city_name):
    city_del = ["2", "Town", "M", "Carson", "Turnpike"]
    city_upd = {"Manhattan Nyc":"Manhattan",
               "Hastings On Hudson": "Hastings-on-Hudson",
               'Hastings-On-Hudson':"Hastings-on-Hudson",
               "S Plainfield":"South Plainfield",
               "Bethpate":"Bethpage",
               "Brookklyn":"Brooklyn",
               "West Harrison":"Harrison",
               "White Plaine":"White Plain",
               "Woodside":"Queens",
               "Woodside (Queens)":"Queens",
               'Woodhaven':"Queens",
               "Hisckville":"Hicksville",
               "Hasbrouck Hts":"Hasbrouck Heights",
               "New York":"New York City",
               "Ny":"New York City",
               'Bowery Bay':"Bowery"}
    for name in prob_city_name:
        if name.endswith("Township"):
            city_upd[name] = name[:-8].strip()
    return city_del, city_upd

def fix_problematic_city(city_del, city_upd, city_map):
    for old_name,new_name in city_map.items():        
        if type(new_name) == type([]):
            if new_name[0] in city_del:
                new_name[0] = ""
            elif new_name[0] in city_upd:
                new_name[0] = city_upd[new_name[0]]
        else:
            if new_name in city_del:
                city_map[old_name] = ""
            elif new_name in city_upd:
                city_map[old_name] = city_upd[new_name]
    return city_map

def update_city(collection, city_map):
    cursor = collection.find({"addr.city":{"$exists":1}})
    for doc in cursor:
        old_name = doc["addr"]["city"]
        new_name = city_map[old_name]
        if old_name != new_name:
            if type(new_name) == type([]):
                if not doc["addr"].get("state"):
                    state = new_name[1]
                    doc["addr"]["state"] = state
                if not doc["addr"].get("postcode") and len(new_name) == 3:
                    zipcode = new_name[2]
                    doc["addr"]["postcode"] = zipcode
                new_name = new_name[0]
            if new_name:
                doc["addr"]["city"] = new_name
            else:
                doc["addr"].pop("city")
            collection.save(doc)

def main(filename, collection):
    dist_city = collection.distinct("addr.city")
    city, city_state = check_city(dist_city)
    city_map = fix_city_with_state(city, city_state)
    ny_town = stnd_town(filename)
    prob_city_name = problematic_city(city_map, ny_town)
    city_del, city_upd = classify_city(prob_city_name)
    city_map = fix_problematic_city(city_del, city_upd, city_map)
    update_city(collection, city_map)
    return dist_city, ny_town, city_map

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    
    dist_city, ny_town, city_map = main("data/US_town.txt", collection)
  
