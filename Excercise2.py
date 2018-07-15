import json
import csv

with open('example.json') as file:
	data = json.load(file)

# print(type(data))
total_capacity = 0
total_stoptime = 0

for details in data ['events_data']:

	longitude	= (details['geo_point']['longitude'])
	latitude	= (details['geo_point']['latitude'])
	stoptime 	= (details['algorithm_fields']['stop_time'])
	capacity 	= (details['algorithm_fields']['capacity'])
	
	
	#print ('Longitude :',longitude, ' ','Latitude :', latitude, ' ','StopTime : ',stoptime, ' ','Capacity :', capacity)

# 	total_capacity += capacity
# 	total_stoptime += stoptime

# print('The total capacity is:', total_capacity, 'Units', '&&', 'The total stoptime is:',stoptime/60,'Hours')


with open('emaple_csv.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter=',')
	for line in csv:
		csv_writer.writerow(line)
