from collections import defaultdict
import re
from bs4 import BeautifulSoup
import requests
import json

# tag key count distribution
def tag_key_distrib(tag_keys, total_num):
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for e in tag_keys:
        if tag_keys[e] >= 0.01 * total_num: # 1/100
            count2 += 1
        if tag_keys[e] >= 0.001 * total_num: # 1/1000
            count3 += 1
        if tag_keys[e] >= 0.0001 * total_num: # 1/10000
            count4 += 1
        if tag_keys[e] >= 0.00001 * total_num: # 1/100,000
            count5 += 1
        if tag_keys[e] >= 0.000001 * total_num: # 1/1,000,000
            count6 += 1
    distrib = "total num of keys = {}".format(len(tag_keys)), "total_count = {}".format(total_num),\
    "num of keys count more than 0.01*total_count = {}".format(count2),\
    "num of keys count more than 0.001*total_count = {}".format(count3),\
    "num of keys count more than 0.0001*total_count = {}".format(count4),\
    "num of keys count more than 0.00001*total_count = {}".format(count5),\
    "num of keys count more than 0.000001*total_count = {}".format(count6)
    return distrib

# only will include keys count more than 0.00001*total (more than 86 times)
def tag_key_target1(tag_keys, lower_limit):
    keys_v1 = defaultdict(int)
    for e in tag_keys:
        if tag_keys[e] >= lower_limit:
            keys_v1[e] = tag_keys[e]
            key_map[e] = e
    return keys_v1

# official tag keys
def official_keys(url):
    MapFeatures = requests.get(url)
    soup = BeautifulSoup(MapFeatures.text, "lxml")
    tables = soup.find_all("table", {"class":"wikitable"})  
    key_set = set()
    for table in tables:
        trs = table.find_all("tr")
        for tr in trs:
            a = tr.find("a", {"title":re.compile("^Key:.*")})
            if a:
                key_set.add(a.text.strip())
    return key_set

# keys not in official_keys set
def problemkey(official_keySet, keys_v1):
    prob_keys = defaultdict(int)
    for e in keys_v1:
        if e not in official_keySet:
            prob_keys[e] = keys_v1[e]
    return prob_keys

# check the keys not in official_keys
def check_UserTagKey(tag_keys, key_need_check, official_keySet):
    lower = re.compile(r'^([a-z]|_)+$')
    colon = re.compile(r'^([a-z0-9]|_)+(:([a-z0-9]|_)+)+$')
    dots = re.compile(r'^([a-z]|_)+\.([a-z]|_)+$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\, \t\r\n]')

    types = {"lower":0,
            "cuser":0,
            "coff":0,
            "dot":0,
            "problem":0,
            "other":0}

    for e in types:
        types[e] = defaultdict(int)

    for e in key_need_check:
        if lower.search(e):
            types["lower"][e] = tag_keys[e]

        elif colon.search(e):
            spos = e.find(":")
            pre = e[:spos]
            if pre in official_keySet:
                types["coff"][e] = tag_keys[e]
            else:
                types["cuser"][e] = tag_keys[e]

        elif dots.search(e):
            types["dot"][e] = tag_keys[e]
        elif problemchars.search(e):
            types["problem"][e] = tag_keys[e]
        else:
            types["other"][e] = tag_keys[e]
    return types

# helper function: group by pre in cuser_dict, count occurence of each pre
def occur_count(cuser):
    pre_total = defaultdict(int)
    pre_times = defaultdict(int)

    for e in cuser:
        pre = e[:e.find(":")]
        pre_total[pre] += cuser[e]
        pre_times[pre] += 1

    pre_avg = dict([(k, pre_total[k]*1.0/pre_times[k]) for k in pre_total\
                    if pre_total[k]*1.0/pre_times[k]>863])

    return pre_avg

# fix the keys not in official key
def fix_tag_key(prob_key_types):
    saved_key = {}
    key_map = {}
    for e in prob_key_types["lower"]:
        if prob_key_types["lower"][e] >= 863:
            saved_key[e] = prob_key_types["lower"][e]
            key_map[e] = e

    large_occur = occur_count(prob_key_types["cuser"])
    for e in prob_key_types["cuser"]:
        pre = e[:e.find(":")]
        if pre in saved_key or pre in large_occur:
            saved_key[e] = prob_key_types["cuser"][e]
            key_map[e] = e

    for e in prob_key_types["coff"]:
        if e != "source:old_name:1970" and e != "old_name:1970" and e != "name:ru":
            saved_key[e] = prob_key_types["coff"][e]
            key_map[e] = e

    for e in prob_key_types["dot"]:
        saved_key[e.replace(".", ":")] = prob_key_types["dot"][e]
        key_map[e] = e.replace(".", ":")

    return saved_key,key_map
    
# after fix the keys not in official key, combine the fixed key together with keys in official key
def tag_key_target2(fixed_key, keys_v1, official_keySet, key_map):
    keys_v2 = dict([(k, v) for k, v in fixed_key.items()])
    for e in keys_v1:
        if e in official_keySet:
            keys_v2[e] = keys_v1[e]
            key_map[e] = e
    return keys_v2, key_map

# for keys in keys_v2, some keys exist in the form of both none colon and colon. for example, "building" and "building: colour"
# both exist. This brought trouble in putting them into dictionary.so, in the case of such keys, add itself as second key. for example, building now become
# building:building.
def problematic_colon_keys(keys_v2):
    problematic_main_1 = set()
    problematic_main_2 = set()
    for key in keys_v2:
        parts = key.split(":")
        if len(parts) == 2 and parts[0] in keys_v2:
            problematic_main_1.add(parts[0])
        if len(parts) == 3 and (":".join(parts[:2])) in keys_v2:
            problematic_main_2.add(":".join(parts[:2]))
    return problematic_main_1, problematic_main_2

def fix_finalkeys(key_map, keys_v2, problematic_main_1, problematic_main_2):
    final_keys = {}
    for old_key, new_key in key_map.items():
        if new_key in problematic_main_1:
            change_key = new_key + ":" + new_key
            key_map[old_key] = change_key
        elif new_key in problematic_main_2:
            change_key = new_key + ":" + new_key.split(":")[1]
            key_map[old_key] = change_key
        else:
            change_key = new_key
        final_keys[change_key] = keys_v2[new_key]
    return final_keys, key_map


# fix tag keys
def get_tagKeys(url, tag_keys, total_num):
    distrib = tag_key_distrib(tag_keys, total_num)
    keys_v1 = tag_key_target1(tag_keys, lower_limit=0.00001 * total_num)
    official_keySet = official_keys(url)
    key_need_check = problemkey(official_keySet, keys_v1)
    prob_key_types = check_UserTagKey(tag_keys, key_need_check, official_keySet)
    fixed_key, key_map = fix_tag_key(prob_key_types)
    keys_v2, key_map = tag_key_target2(fixed_key, keys_v1, official_keySet, key_map)
    problematic_main_1, problematic_main_2 = problematic_colon_keys(keys_v2)
    final_keys, key_map = fix_finalkeys(key_map, keys_v2, problematic_main_1, problematic_main_2)
    return distrib, keys_v1, official_keySet, key_need_check, prob_key_types, fixed_key, keys_v2, final_keys, key_map

# the variable "total_num" and "tagkes_stats" are from result obtained from "elem_count.py"
# after fix the tagkeys, final keys will be processed were stored in "final_keys" variable
if __name__=="__main__":
    url = "http://wiki.openstreetmap.org/wiki/Map_Features"
    total_num = 8630865
    with open("data/tagkeys_stats.txt", "r") as f:
        tagkeys_stats = json.load(f)
        
    distrib, keys_v1, official_keySet, key_need_check, prob_key_types, fixed_key, keys_v2, final_keys, key_map \
    = get_tagKeys(url, tagkeys_stats, total_num)
    
    with open("data/key_map.txt", "w") as f:
        json.dump(key_map, f)
        
