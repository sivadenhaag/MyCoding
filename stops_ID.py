import csv
import json
import requests
from collections import Counter

#Read JSON file
#Requirement
#1. Count of records in the file, Count on a specific search
#2. Fetch a specific key and the value, based on the specific search
#3. Fetch multiple key and the value
#4. Find a key with specific conditions, like = "" | != blank | etc
#5. Update the JSON file with the changes 
#6. Write the search into an other JSON file
#7. convert a JSON file into a CSV, XML, text file and all combinations




# #csvfile = open('stops.csv', 'r')
# with open('stops.json', 'r',encoding="utf-8") as read_file:

# 	data = json.loads(read_file.read())
# 	#print(data)
# 	zone_ids = [d["zone_id"] for d in data if d["zone_id"]]
# 	print(zone_ids)


#csvfile = open('stops.csv', 'r')
# with open('stops.json', 'r',encoding="utf-8") as read_file:

# 	data = json.loads(read_file.read())
# 	#print(data)
# 	zone_ids = [d["stop_name"] for d in data if d["stop_name"]]
# 	print(zone_ids[1:100:2])

# with open('stops.json', 'r',encoding="utf-8") as read_file:

# 	data = json.loads(read_file.read())
# 	#print(data)
# 	zone_ids = [(d["stop_name"], d["zone_id"]) for d in data if d["zone_id"]]
# 	print(zone_ids[1:100:2])

### - File reads the input JSON and the results are dumped into an other JSON file
# with open('stops.json', 'r',encoding="utf-8") as read_file:

# 	data = json.loads(read_file.read())
# 	#print(data)
# 	zone_ids = [(d["stop_name"], d["zone_id"]) for d in data if d["zone_id"]]
# 	print(zone_ids[1:10])

# 	f = open('outfile.json', 'w')
# 	f.write(json.dumps(zone_ids))
# 	f.close()

with open('stops.json', 'r',encoding="utf-8") as read_file:

	data = json.loads(read_file.read())
	#print(data)
	zone_ids = [(d["parent_station"], d["wheelchair_boarding"]) for d in data if d["wheelchair_boarding"]]
	print(zone_ids[1:10])
	
	f = open('outfile.json', 'w')
	f.write(json.dumps(zone_ids))
	f.close()
