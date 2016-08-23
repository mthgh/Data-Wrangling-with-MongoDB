from pymongo import MongoClient
import re
        
def classify_postcode(dist_postcode):
    normal = []
    prob_char = []
    prob_nine = []
    others = []

    normal_zip = re.compile("^(0[6-8]|1[0-4])[0-9]{3}$")
    starts_state = re.compile("^[a-zA-Z]{2}\s(0[6-8]|1[0-4])[0-9]{3}$")
    nine_zip = re.compile("^(0[6-8]|1[0-4])[0-9]{3}-[0-9]{4}$")

    for postcode in dist_postcode:
        if normal_zip.search(postcode):
            normal.append(postcode)
        elif starts_state.search(postcode):
            prob_char.append(postcode)
        elif nine_zip.search(postcode):
            prob_nine.append(postcode)
        else:
            others.append(postcode)
    return normal, prob_char, prob_nine, others
    
def fix_postcode(normal, prob_char, prob_nine):
    need_fix = {"07052 ":"07052", '100014':"10014", 'New York, NY 10065':"10065",
               "1011":"10011", '11201;11231':"11231", '11231;11230':"11231",
               '11214;11223':"11223", "111756":"11756", '111743':"11743"}
    post_del = ['11', '2', '12', '74', '61', '56', '320', '3', 
                'NJ', '83', "19122", '22645', '90745', '40299', '97657', '29201']
    change_post = "(718) 778-0140"
    postcode_map = {}
    for postcode in normal:
        postcode_map[postcode] = postcode
    for postcode in prob_char:
        postcode_map[postcode] = postcode[3:]
    for postcode in prob_nine:
        postcode_map[postcode] = postcode[:5]
    for postcode in need_fix:
        postcode_map[postcode] = need_fix[postcode]
    for postcode in post_del:
        postcode_map[postcode] = ""
    postcode_map[change_post] = {"phone":change_post}
    return postcode_map
    
def upd_postcode(collection, postcode_map, post_del, change_post):
    cursor = collection.find({"addr.postcode":{"$exists":1}})
    for doc in cursor:
        old_postcode = doc["addr"]["postcode"]
        if old_postcode not in postcode_map.values():
            new_postcode = postcode_map[old_postcode]
            if type(new_postcode) == type({}):
                doc["addr"].pop("postcode")
                doc["phone"] = new_postcode["phone"]
            elif new_postcode:
                doc["addr"]["postcode"] = postcode_map[old_postcode]
            else:
                doc["addr"].pop("postcode")
            collection.save(doc) 

def main(collection):
    dist_postcode = collection.distinct("addr.postcode")
    normal, prob_char, prob_nine, others = classify_postcode(dist_postcode)
    postcode_map = fix_postcode(normal, prob_char, prob_nine)
    upd_postcode(collection, postcode_map, post_del, change_post)
    return postcode_map
        
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    postcode_map = main(collection)
