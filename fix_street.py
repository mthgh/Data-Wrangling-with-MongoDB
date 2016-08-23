abbr = {"Pkwy":"Parkway", "Hwy":"Highway", "Blvd":"Boulevard", 
        "St":"Street", "Rd":"Road", "Dr":"Drive", "Ave":"Avenue", 
        "Avene":"Avenue", 'Aveneu':"Avenue", 'Ct':"Court", 
        'Cir':"Circle", 'Ctr':"Center", 'Pky':"Parkway",
        'Plz':"Plaza", 'Steet':"Street", 'Streeet':"Street", 
        'Tirnpike':"Turnpike",'Tpke':"Turnpike", 'Tunpike':"Turnpike", 
        'Tunrpike':"Turnpike", 'Turnlike':"Turnpike", "Av":"Avenue",
        "Plance":"Place", "Expy":"Expressway", "Blv":"Boulevard", "Pl":"Place","Ln":"Lane"}

expt = ["Street", "Avenue", "Boulevard", "Drive","Court", "Place", "Square", 
        "Lane", "Road", "Trail", "Parkway", "Commons", "Marketplace", "Ballfields",
        "Turnpike", "Plaza", "Terrace", 'Broadway', 'Bridge','Center','Circle', 
        'Commerce', 'Concourse', 'Course', 'Cross', 'Driveway','Expressway', 'Crescent',
        'Extension', 'Freeway', 'Garfield','Heights', 'Track', "Way", "Loop", "Walk","Cove", 
        "Highway", "Green","Gate", "Slip", "Bush", "Piers", "Camp", "Alley", "Quadrangle", 
        "Path", "Thruway", "Causeway", "Promenade", "Ridge","Esplanade"]

dirc = ["North", "West", "South", "East"]

def generate_street_map(collection):
    dist_street = collection.distinct("addr.street")
    street_map = dict([(street, street.strip().title()) for street in dist_street])
    return dist_street, street_map

def claasify_abnormal_char(street_map):
    street_char_re = re.compile("^[A-Za-z0-9]+(\s[A-Za-z0-9]+)*$")
    street_prob_char = set()

    for street in street_map.values():    
        if not street_char_re.search(street) or street.find("And ") != -1:
            street_prob_char.add(street)
    return street_prob_char

def general_street_fix(street_map, fix_method, *params):
    for old_road, road in street_map.items():
        if road:
            update, new_road = fix_method(road, *params)
            if update:
                #print [street_map[old_road]]
                street_map[old_road] = new_road
                #print [street_map[old_road]]
    return street_map

def fix_abnormal_char(road, street_prob_char):
    if road in street_prob_char:
        manual_map = {
                  "40-4 Riverwalk Place":"Riverwalk Place",
                  "Paterson - Hamburg Turnpike":"Paterson Hamburg Turnpike",
                  "150 Essex St. Ste 303":"Essex Street",
                  'Vernon Boulevard Between 33Th Road And 34Th Avenue':"Vernon Boulevard",
                  'Britton St. Bet. Olinville Ave. And Barker Ave.':"Britton Street",
                 "St. George'S Avenue":"St Georges Avenue",
                 "37Th Avenue, 14Th Street, 21St Street":"",
                 "Little Neck Bay, L.I.E., Union Tpk, Bet. Springfield Blvd, Douglaston Pkwy, Hanford St":"",
                 u'Luis Mu\xf1oz Marin Boulevard':"Luis Munoz Marin Boulevard",
                  "Nostrand Avenue;Flatbush Avenue":""}

        spe_re_1 = re.compile("[#@(;,]|\.,")
        spe_re_2 = re.compile("[.)']")

        if road in manual_map:
            new_road = manual_map[road]
        elif spe_re_1.search(road):
            g = spe_re_1.search(road).group()
            new_road = road.split(g)[0].strip().title()
        elif spe_re_2.search(road):
            g = spe_re_2.search(road).group()
            new_road = road.strip().replace(g, "").title()
        elif road.find("-") != -1:
            new_road = road.strip().replace("-", " ").title()
        else:
            new_road = ""
        return True, new_road
    return False, ""

def classify_street_types(street_map): 
    street_type_re = re.compile(r'(\s)(\S+)$', re.IGNORECASE)
    hwy_re = re.compile("(Us|Route|Rt|State|Nj|Jersey)\s")

    fix_abbr = set()
    fix_contain = set()
    fix_hwy = set()
    others = set()

    for old_road, road in street_map.items():
        m = street_type_re.search(road)
        if not m and road:
            others.add(road)
        elif m:
            g = street_type_re.search(road).group(2)
            if g in expt or (g in dirc and not hwy_re.search(road)):
                pass
            elif g in abbr:
                fix_abbr.add(road)
            elif hwy_re.search(road):
                fix_hwy.add(road)
            elif set(road.split()).intersection(abbr.keys()+expt):
                fix_contain.add(road)                            
            else:
                others.add(road)
    return fix_abbr, fix_contain, fix_hwy, others

def find_num(road_name):
    numth_re_1 = re.compile("([0-9]+)(St|Nd|Rd|Th)")
    numth_re_2 = re.compile("([0-9]+)([a-zA-Z]+)*")
    m1 = numth_re_1.search(road_name)
    m2 = numth_re_2.search(road_name)
    if m1:
        return m1.group(1)
    if m2:
        return m2.group()

def replace_abbr(road_name):
    street_type_re = re.compile(r'\b\S+$', re.IGNORECASE)
    rep = street_type_re.search(road_name).group()
    new = abbr[rep]
    return road_name.replace(rep, new)

def fix_street_types(road, fix_contain, fix_hwy, fix_abbr, others):    
    if road in fix_contain:
        street_ok_re = re.compile("^Avenue|Gibbons\sCircle|Nichol\sAvenue\sBld")
        delete = ["Washington Square Village", "H Highway 34", "Crescent Beach", "Street 1603", "Road 1", "Road 3"]
        if road in delete:
            return True, ""
        elif street_ok_re.search(road):
            return False, ""
        else:
            words = set(road.split())
            street_type_set = set(words).intersection(expt) or set(words).intersection(abbr.keys())
            street_type = street_type_set.pop()
            end_pos = road.find(street_type) + len(street_type)
            new_road = road[:end_pos]
            if abbr.get(street_type):
                new_road = new_road.replace(street_type, abbr[street_type])
            return True, new_road
    elif road in fix_hwy:
        state_re = re.compile("(State|Nj|New\sJersey|Nwe\sJersey)")
        num = find_num(road)
        if road.find("Us ") != -1:
            new_road = "Us " + num
        elif state_re.search(road):
            new_road = "State Route " + num
        elif road.find("Route") != -1 or road.find("Rt ") != -1:
            new_road = "Route " + num
        return True, new_road
    elif road in others:
        if road in ['Fordham Hill Oval', 'Park Row', 'Stuyvesant Oval', "Broadway", 'I 95']:
            return False, ""
        else:
            return True, ""
    elif road in fix_abbr:
        new_road = replace_abbr(road)
        return True, new_road
    else:
        return False, ""        

def fix_nums_1(road):
    us_re = re.compile("Us\s|Route\s|State\sRoute\s")
    numth_re = re.compile("([0-9]+)(St|Nd|Rd|Th)*")
    start_num_re = re.compile("^\d+\s")    
    words = road.split()    
    if start_num_re.search(road) and not us_re.search(road):
        if len(words) == 2:
            new_road = road.replace(words[0], words[0]+"Th")
        else:
            new_road = road[len(words[0])+1:]
        return True, new_road    
    elif len(numth_re.findall(road))>1:
        new_road = road[len(words[0])+1:]
        return True, new_road
    return False, ""

def fix_nums_2(road):
    char_num = {"First":"1St", "Second":"2Nd", "Third":"3Rd", 
                "Fourth":"4Th", "Fifth":"5Th", "Sixth":"6Th", 
                "Seventh":"7Th", "Eighth":"8Th", "Ninth":"9Th"}
    old_road = road
    for n in char_num:
        if road.find(n) != -1:
            road = road.replace(n, char_num[n])
    if old_road != road:
        return True, road
    return False, ""

def fix_direction(road):
    start_dirc = {"W":"West", "E":"East", "N":"North", "S":"South"}
    first_word = road.split()[0]
    if first_word in start_dirc:
        new_road = start_dirc[first_word] + road[len(first_word):]
        return True, new_road
    return False, ""        

def update_street(collection, street_map):
    cursor = collection.find({"addr.street":{"$exists":True}})
    for doc in cursor:
        old_street = doc["addr"]["street"]       
        if old_street not in street_map.values():
            new_street = street_map[old_street]
            if not new_street:
                doc["addr"].pop("street")
            else:
                doc["addr"]["street"] = new_street
            collection.save(doc)

def main(collection):
    dist_street, street_map = generate_street_map(collection)
    street_prob_char = claasify_abnormal_char(street_map)
    street_map = general_street_fix(street_map, fix_abnormal_char, street_prob_char)
    fix_abbr, fix_contain, fix_hwy, others = classify_street_types(street_map)
    street_map = general_street_fix(street_map, fix_street_types, fix_contain, fix_hwy, fix_abbr, others)
    street_map = general_street_fix(street_map, fix_nums_1)
    street_map = general_street_fix(street_map, fix_nums_2)
    street_map = general_street_fix(street_map, fix_direction)
    update_street(collection, street_map)
    return dist_street, street_map

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.osm
    collection = db.NY_osm
    dist_street, street_map = main(collection)

