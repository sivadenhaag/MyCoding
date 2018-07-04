import json

with open('example.json') as file:
	data = json.load(file)

# print(type(data))
total_capacity = 0
total_stoptime = 0

for details in data ['events_data']:

	stoptime = (details['algorithm_fields']['stop_time'])
	capacity = (details['algorithm_fields']['capacity'])
	#print ('StopTime : ',stoptime, '     ','Capacity : ', capacity)
	#To test the pull command
	#To test the pull command again

	total_capacity += capacity
	total_stoptime += stoptime

print('The total capacity is:', total_capacity, 'Units', '&&', 'The total stoptime is:',stoptime/60,'Hours')


