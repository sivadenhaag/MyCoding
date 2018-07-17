import json
import csv

with open('example.json') as file:
	data = json.load(file)

# print(type(data))
total_capacity = 0
total_stoptime = 0

csv_data = {}
with open ("Output.csv","w") as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(['Longitude','Latitude','Stoptime','Capacity'])
	
	for details in data ['events_data']:

		longitude	= (details['geo_point']['longitude'])
		latitude	= (details['geo_point']['latitude'])
		stoptime 	= (details['algorithm_fields']['stop_time'])
		capacity 	= (details['algorithm_fields']['capacity'])
		
		#print ('Longitude :',longitude, ' ','Latitude :', latitude, ' ','StopTime : ',stoptime, ' ','Capacity :', capacity)

		csv_data['longitude'] = longitude
		csv_data['latitude'] = latitude
		csv_data['stoptime'] = stoptime
		csv_data['capacity'] = capacity

		writer.writerow(csv_data.values())

		#print(csv_data)

