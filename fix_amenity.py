from pymongo import MongoClient
import re
        
def fix_amenity():
    amenity_map = {'waste_disposal':"waste_basket",
          'user_defined':"",
          'school;place_of_worship':"school",
          'preschool':"school",
          'pakring':"parking",
          'Liquor_Store':"liquor_store",
          'Green_Market':"green_market",
          'Family health clinic':"family_health_clinic",
          'Beauty':"beauty",
          'Assisted Living':"assorted_living",
          "carpark":"parking",
          'social_center':"social_centre",
          'car_parking':"parking",
          'clothing store':"clothing_store", 
          'Convenience Store':"convenience_store"}
    return amenity_map
    
def update_amenity(collection, amenity_map):
    cursor = collection.find({"amenity":{"$exists":1}})
    for doc in cursor:
        old_amenity = doc["amenity"]
        if old_amenity in amenity_map:
            new_amenity = amenity_map[old_amenity]
            if new_amenity:
                doc["amenity"] = new_amenity
            else:
                doc.pop("amenity")
        collection.save(doc)
    
def main(collection):
    dist_amenity = collection.distinct("amenity", {"amenity":{"$exists":1}})
    amenity_map = fix_amenity()
    update_amenity(collection, amenity_map)
    return dist_amenity, amenity_map

if __name__=="__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    dist_amenity, amenity_map = main(collection)
