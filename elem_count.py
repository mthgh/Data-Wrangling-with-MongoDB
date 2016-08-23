import lxml.etree as ET
from collections import defaultdict
import re
import json
from pprint import pprint

# iterate over the osmfile and get the respective count needed
def fast_iter(filename):
    
    elem_stats = defaultdict(int)
    attrib_stats = defaultdict(int)
    tagkey_type_stats = defaultdict(int)
    tagkeys_stats = defaultdict(int)
    
    with open(filename) as f:
        context = ET.iterparse(f)
        for event, elem in context:
            
            elem_stats = elem_count(elem, elem_stats)
            attrib_stats = attrib_count(elem, attrib_stats)
            tagkey_type_stats = tag_keyType_count(elem, tagkey_type_stats)
            tagkeys_stats = tag_key_count(elem, tagkeys_stats)
            
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context
        
    return [elem_stats, attrib_stats, tagkey_type_stats, tagkeys_stats]

# count elem
def elem_count(elem, stats_dict):
    stats_dict[elem.tag] += 1
    return stats_dict

# count every attrib of interested elem
def attrib_count(elem, stats_dict):
    if elem.tag == "node" or elem.tag=="way" or elem.tag == "tag":
        key_pre = elem.tag
        for att in elem.attrib:
            key = key_pre + "_" + att
            stats_dict[key] += 1
    return stats_dict

# check what kind of tag keys are present
def tag_keyType_count(elem, stats_dict):
    lower = re.compile(r'^([a-z]|_)+$')
    UpperNums = re.compile(r'^([a-zA-Z0-9]|_)+$')

    single_colon = re.compile(r'^([a-z]|_)+:([a-z]|_)+$')
    UpperNums_colon = re.compile(r'^([a-zA-Z0-9]|_)+(:([a-zA-Z0-9]|_)+)+$')

    dots = re.compile(r'^([a-z]|_)+\.([a-z]|_)+$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\, \t\r\n]')
    if elem.tag == "tag":
        key = elem.attrib.get("k")

        if lower.search(key):
            stats_dict["lower"] += 1
        elif UpperNums.search(key):
            stats_dict["UpperNums"] += 1

        elif single_colon.search(key):
            stats_dict["single_colon"] += 1
        elif UpperNums_colon.search(key):
            stats_dict["UpperNums_colon"] += 1

        elif dots.search(key):
            stats_dict["dots"] += 1
        elif problemchars.search(key):
            stats_dict["problemchars"] += 1

        else:
            stats_dict["others"] += 1
    return stats_dict

# count each tag key 
def tag_key_count(elem, stats_dict):
    if elem.tag == "tag":
        key = elem.attrib.get("k")
        lower_key = key.lower()
        stats_dict[lower_key] += 1
    return stats_dict

if __name__=="__main__":
    elem_stats,attrib_stats,tagkey_type_stats,tagkeys_stats = fast_iter("data/ny.osm")
    with open("data/tagkeys_stats.txt", "w") as f:
        json.dump(tagkeys_stats, f)
    print "Element Count:" 
    pprint(dict(elem_stats))
    print "\nAttrib Count:"
    pprint(dict(attrib_stats))
    print "\nTagkey Types Count:"
    pprint(dict(tagkey_type_stats))
    print "\nTotal Number of Distinct Tagkeys:", len(tagkeys_stats)
    print "\nTagkeys Count:"
    pprint(dict(tagkeys_stats))
