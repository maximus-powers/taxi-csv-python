# %%
# What are the fieldnames
import csv

with open('./trip_data_1.csv', 'r') as data:
    csvreader = csv.DictReader(data)

    print(csvreader.fieldnames)

# %%
# What datetime range does your data cover?  How many rows are there total?
import csv
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# init variables
earliest_pickup = None
latest_dropoff = None
counter = 0

with open('trip_data_1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        # parse the pickup and dropoff datetimes
        pickup_datetime = datetime.strptime(row['pickup_datetime'], DATE_FORMAT)
        dropoff_datetime = datetime.strptime(row['dropoff_datetime'], DATE_FORMAT)
        
        # update earliest and latest dates
        if earliest_pickup is None or pickup_datetime < earliest_pickup:
            earliest_pickup = pickup_datetime
        
        if latest_dropoff is None or dropoff_datetime > latest_dropoff:
            latest_dropoff = dropoff_datetime

        counter += 1

# now we print out the range of dates
print(f"Earliest datapoint: {earliest_pickup}")
print(f"Latest datapoint: {latest_dropoff}")
print(f"Rows: {counter}")


# %%
#  Give some sample data for each field.
import csv

with open('trip_data_1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    counter = 0
    for row in csvreader:
        counter += 1
        if counter > 3: break
        print(row)

# %%
# What is the geographic range of your data (min/max - X/Y)?
# Plot this (approximately on a map)
import csv

# had to add these, some rows had invalid data (i think)
def is_valid_latitude(lat):
    return -90 <= lat <= 90
def is_valid_longitude(lon):
    return -180 <= lon <= 180

with open('trip_data_1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    min_lat = 90.0
    min_lon = 180.0
    max_lat = -90.0
    max_lon = -180.0

    for row in csvreader:
        try:
            p_lat = float(row['pickup_latitude'])
            p_lon = float(row['pickup_longitude'])
            d_lat = float(row['dropoff_latitude'])
            d_lon = float(row['dropoff_longitude'])
        except ValueError: 
            continue

        # was getting crazy outputs, I think there's invalid data so this is a check
        if is_valid_latitude(p_lat) and is_valid_longitude(p_lon) and \
           is_valid_latitude(d_lat) and is_valid_longitude(d_lon):

            # update min and max lat
            min_lat = min(min_lat, p_lat, d_lat)
            max_lat = max(max_lat, p_lat, d_lat)

            # update min and max lon
            min_lon = min(min_lon, p_lon, d_lon)
            max_lon = max(max_lon, p_lon, d_lon)

    print(f"Min lat: {min_lat}")
    print(f"Max lat: {max_lat}")
    print(f"Min lon: {min_lon}")
    print(f"Max lon: {max_lon}")


# %%
# What is the average overall computed trip distance? (You should use Haversine Distance)
# Draw a histogram of the trip distances binned anyway you see fit.

import csv
import math
from collections import Counter

# got this func from chatgpt
def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371  # radius of earth in kilometers
    return c * r

# for crude histogram
bin_size = 2500 # km
def create_bins(distances, bin_size):
    bins = Counter((int(distance // bin_size)) for distance in distances) # counts up the number of occurances in each km range
    return bins

distances = [] # stores the distances calculated from row

with open('trip_data_1.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    row_counter = 0
    distance_total = 0.0
    for row in csvreader:
        try:
            p_lat = float(row['pickup_latitude'])
            p_lon = float(row['pickup_longitude'])
            d_lat = float(row['dropoff_latitude'])
            d_lon = float(row['dropoff_longitude'])
        except ValueError:  
            continue

        # compute distance
        distance = haversine(p_lon, p_lat, d_lon, d_lat)
        distances.append(distance)

        # add distance to running total
        distance_total += distance
        row_counter += 1

        # divide running total by number of rows
        avg_distance = distance_total / row_counter

# creates the distance counts in each bin
bins = create_bins(distances, bin_size)

# make a crazy looking histogram
for bin in sorted(bins):
    print(f'{bin * bin_size} - {(bin + 1) * bin_size} km: {bins[bin]} {"|" * int(bins[bin] / 100)}')

print(f"Average distance: {avg_distance} km")

# %%
# What are the distinct values for each field? (If applicable)

import csv

# dict for fieldnames and their distinct values
values = {}

with open('trip_data_1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # using set is much faster for checking if a value is already in the set, lists took forever
    for field in reader.fieldnames:
        values[field] = set()

    for row in reader:
        for field in reader.fieldnames:
            # skip if the row's field is none or an empty str
            if row[field] is None or row[field] == '':
                continue
            values[field].add(row[field])

# print it out
for field in reader.fieldnames:
    print(f'{field} has {len(values[field])} distinct values')
    print('\n')
    for value in values[field]:
        print(value)
    print("\n")

# %%
# For other numeric types besides lat and lon, what are the min and max values?
import csv

with open('trip_data_1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    maxs = {}
    for row in reader:
        maxs['rate_code'] = max(maxs.get('rate_code', 0), int(row['rate_code']))
        maxs['passenger_count'] = max(maxs.get('passenger_count', 0), int(row['passenger_count']))
        maxs['trip_time_in_secs'] = max(maxs.get('trip_time_in_secs', 0), int(row['trip_time_in_secs']))
        maxs['trip_distance'] = max(maxs.get('trip_distance', 0), float(row['trip_distance']))


# assuming they won't have negative vals
print(f'Rate code range: 0 - {maxs["rate_code"]}')
print(f'Passenger count range: 0 - {maxs["passenger_count"]}')
print(f'Trip time range (seconds): 0 - {maxs["trip_time_in_secs"]}')
print(f'Trip distance range (km): 0 - {maxs["trip_distance"]}')

# %%
# Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)
import csv
from datetime import datetime
from collections import defaultdict

# init a defaultdict to group passenger counts
hourly_passenger_counts = defaultdict(list)

with open('trip_data_1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # parse the pickup datetime and passenger count
            pickup_datetime = datetime.strptime(row['pickup_datetime'], '%Y-%m-%d %H:%M:%S')
            passenger_count = int(row['passenger_count'])
            hour = pickup_datetime.hour
            hourly_passenger_counts[hour].append(passenger_count)

        except ValueError as e:
            # avgs didn't look right, maybe bad data in rows dropping avg
            print(f"Error parsing row {row}: {e}")
            continue

# calc avg passengers per hour
avg_passengers = {hour: sum(counts) / len(counts) for hour, counts in hourly_passenger_counts.items() if counts}

# chart the average number of passengers
print("Average number of passengers per hour:")
for hour in range(24):
    avg = avg_passengers.get(hour, 0)
    bar = '*' * (int(avg * 100) - 125) # moved it over by 1.55 passengers
    print(f"{hour:02d}:00 - {avg:.2f} avg | {bar}")

    

# %%
# Create a new CSV file which has only one out of every thousand rows.
import csv

input_file_name = 'trip_data_1.csv'
output_file_name = 'trip_data_1000.csv'

with open(input_file_name, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # open output file, write the headers
    with open(output_file_name, 'w', newline='') as new_csvfile:
        writer = csv.DictWriter(new_csvfile, fieldnames=reader.fieldnames)
        
        # write the header to the output file
        writer.writeheader()
        
        for i, row in enumerate(reader):
            if i % 1000 == 0: # every 1000th
                writer.writerow(row)


# %%
# Repeat step 9 with the reduced dataset and compare the two charts.


import csv
from datetime import datetime
from collections import defaultdict

# init a defaultdict to group passenger counts
hourly_passenger_counts = defaultdict(list)

with open('trip_data_1000.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # parse the pickup datetime and passenger count
            pickup_datetime = datetime.strptime(row['pickup_datetime'], '%Y-%m-%d %H:%M:%S')
            passenger_count = int(row['passenger_count'])
            hour = pickup_datetime.hour
            hourly_passenger_counts[hour].append(passenger_count)

        except ValueError as e:
            # avgs didn't look right, maybe bad data in rows dropping avg
            print(f"Error parsing row {row}: {e}")
            continue

# calc avg passengers per hour
avg_passengers = {hour: sum(counts) / len(counts) for hour, counts in hourly_passenger_counts.items() if counts}

# chart the average number of passengers
print("Average number of passengers per hour:")
for hour in range(24):
    avg = avg_passengers.get(hour, 0)
    bar = '*' * (int(avg * 100) - 125) # moved it over by 1.55 passengers
    print(f"{hour:02d}:00 - {avg:.2f} avg | {bar}")


