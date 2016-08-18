# Fianl Project for Data Wrangling with MongoDB
## Contents
1. [Project Summary] (#summary)
2. [Problems Encountered In the Map] (#problems)
    1. [overview of the dataset] (#count)
    2. hello  
3. [Data Overview] (#overview)
4. [Additional Ideas] (#addtional)

## <a name="summary"></a>1. Project Summary
This is the final project from udacity's online course "Data Wrangling with MongoDB". The task is to choose any area of the world from https://www.openstreetmap.org and use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data.
  
**_Map Area : Great New York City Area_**  
**_Open Street Map URL_**: https://www.openstreetmap.org/export#map=10/40.7202/-73.8638   
**_Data Source (OSM XML)_**: https://mapzen.com/data/metro-extracts/metro/new-york_new-york/  

## <a name="problems"></a>2. Problems Encountered In the Map  
### <a name="count">i. overview of the dataset
To get an idea of the size of the dataset, ```elem_count.py``` was used to count the element, attribute and tagkeys present in this dataset. With the result showing below. (Only node, way and the corresponding subelements will be processed)

<pre>
 Element Count:          Attrib Count:                          Total Number of Distinct Tagkeys: 1469
 {'bounds': 1,           {'node_changeset': 9125861,            
 'member': 98515,         'node_id': 9125861,                   Tagkey Types Count:
 'nd': 11821306,          'node_lat': 9125861,                  {'UpperNums_colon': 70370,
 'node': 9125861,         'node_lon': 9125861,                   'dots': 24991,
 'osm': 1,                'node_timestamp': 9125861,             'lower': 3392866,
 'relation': 8081,        'node_uid': 9125861,                   'others': 27,
 'tag': 8630865,          'node_user': 9125861,                  'problemchars': 7,
 'way': 1503605}          'node_version': 9125861,               'single_colon': 5109466,
                          'tag_k': 8630865,                      'UpperNums': 33138,}
                          'tag_v': 8630865,                    
                          'way_changeset': 1503605,            Tagkeys Count(stored in data/tagkeys_stats.txt):
                          'way_id': 1503605,                   {'building': 1197472,
                          'way_timestamp': 1503605,             'height': 1102643,
                          'way_uid': 1503605,                   'nycdoitt:bin': 1079114,
                          'way_user': 1503605,                  'addr:street': 927273,
                          'way_version': 1503605}               ......}
</pre>
### <a name="fix_tagkey">ii. problematic tag keys
From the result above in point i, every tag key was counted. It was found that many of tag keys appear only once. In order to pick up resonable tag keys for processing, functions in ```fix_tagkeys.py``` were used to fix tagkeys.  

First, a distribition of the count of the tag keys were calculated (stored in "distrib" variable)  
```
'total num of distinct keys = 1469',  
'total num of keys = 8630865',  
'num of keys count more than 86308 times (0.01*total_count) = 16',  
'num of keys count more than 8630 times (0.001*total_count) = 51',  
'num of keys count more than 863 times (0.0001*total_count) = 148',  
'num of keys count more than 86 times (0.00001*total_count) = 322',  
'num of keys count more than 8 times (0.000001*total_count) = 593'  
```
Based on the result, only keys appear more than 0.00001*total_count times (86 times) will be processed. The other keys are so rare, or they might have the meaning with one of the keys appear more often. For example, "alt_name_1" which appear 4 times most likely to have the same meaning as "alt_name" (appear 1442 times). Also, something like "to" (appear 57 times) is ambiguous and something like "name:wa" (appear 1 time) is so rare.

 
 
 
 
 



