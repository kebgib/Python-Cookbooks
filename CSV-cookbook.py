"""
Simple cookbook for CSV operations 
"""
import csv

# Opening and ingesting csv data from a directory named /CSV-Folder/
with open(f"CSV-Folder/my_csv.csv") as file:
    reader = csv.reader(file)
    data = list(reader)
    # data is a <type: list> where each index is a line from the CSV

# An easy way to observe what index numbers will be what data is with the enumerate function
# Use enumerate() on index 0 to get an easily readable index/header outline

for index, value in enumerate(data[0]):
	print(f"[{index}] -- {value}")
# Example output:
"""
[0] -- First Packet
[1] -- Last Packet
[2] -- Action
[3] -- Reason
[4] -- Initiator IP
[5] -- Initiator Country
[6] -- Initiator User
[7] -- Responder IP
[8] -- Responder Country
[9] -- Original Client IP
...
"""

# Iteration of the csv data, bypass the initial line because it will contain header information
# Isolate variables in accordance with your enumerate() output above, for example:

for line in data[1:]:		# bypassing header line contained in data[0]
	# Isolating variables for easy readability!
	initiator_ip = line[4]
	responder_ip = line[7]

"""
Write a dictionary-like object to csv
"""
# newline='' required to prevent blank row errors
with open(f'report_name.csv', mode='w', newline='') as csvfile:
	csv_headers = ['source_ip', 'destination_ip', 'source_port', 'destination_port', 'protocol']
	writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
	writer.writeheader()	  # write header values in csv_values to row 1 of the csv

	# Write to the csv using key:value pairs for ease of assignment
	writer.writerow({
		"source_ip": '10.100.0.5',
		'destination_ip': '8.8.8.8',
		'source_port': '32121',
		'destination_port': '53',
		'protocol': 'UDP'
	})