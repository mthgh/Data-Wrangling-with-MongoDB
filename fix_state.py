from pymongo import MongoClient

def problematic_state(collection):
    dist_state = collection.distinct("addr.state")
    return dist_state

def fix_state(dist_state):
    state_map = {}
    s_ny = ['ON', 'BY', '10009', 'CA', 'New York']
    s_nj = ['VA', 'TX', 'New Jersey', 'NJ - New Jersey']
    for state in dist_state:
        if state in s_ny:
            state_map[state] = u'NY'
        elif state in s_nj:
            state_map[state] = u'NJ'
        else:
            state_map[state] = state.upper()

    expt = ["NJ", "NY", "CT"]
    cursor = collection.find({"addr.state":{"$exists":1}})    
    for doc in cursor:
        old_state = doc["addr"]["state"]
        if old_state not in expt:
            doc["addr"]["state"] = state_map[old_state]
            collection.save(doc)
    return state_map

def main(collection):
    dist_state = problematic_state(collection)
    state_map = fix_state(dist_state)
    return dist_state, state_map

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    
    dist_state, state_map = main(collection)

