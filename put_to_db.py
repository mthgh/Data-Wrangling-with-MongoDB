from pymongo import MongoClient
from datetime import datetime
import lxml.etree as ET
import json

def proc(elem, key_map):
    row = {
    "id": elem.attrib["id"],
    "types": elem.tag,
    "created": {
              "version":elem.attrib["version"],
              "changeset":elem.attrib["changeset"],
              "timestamp":datetime.strptime(elem.attrib["timestamp"], "%Y-%m-%dT%H:%M:%SZ" ),
              "user":elem.attrib["user"],
              "uid":elem.attrib["uid"]
            },
    }

    if elem.tag == "node":
        row["pos"] = [float(elem.attrib["lon"]), float(elem.attrib["lat"])]
    if elem.tag == "way":
        row["nd"] = []

    for child in elem:
        if child.tag == "tag":
            tagkey = child.attrib["k"].strip()
            if tagkey in key_map:
                parts = (key_map[tagkey]).split(":")
                if len(parts) == 1:
                    row[parts[0]] = child.attrib["v"]

                if len(parts) == 2:
                    if parts[0] not in row:
                        row[parts[0]]={}
                    row[parts[0]][parts[1]] = child.attrib["v"]

                if len(parts) == 3:
                    if parts[0] not in row:
                        row[parts[0]] = {}
                    if parts[1] not in row[parts[0]]:
                        row[parts[0]][parts[1]] = {}
                    row[parts[0]][parts[1]][parts[2]] = child.attrib["v"]

        if child.tag == "nd":
            row["nd"].append(child.attrib["ref"])
    return row

def to_db(filename, key_map, collection):
    with open(filename) as f:
        context = ET.iterparse(f)
        for event, elem in context:
            if elem.tag == "node" or elem.tag=="way":
                row = proc(elem, key_map)
                collection.insert_one(row)

            if elem.tag != "tag" and elem.tag != "nd":
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    
    with open("data/key_map.txt") as f:
        key_map = json.load(f)
    to_db("data/ny.osm", key_map, collection)
