Dataset: https://clarksonmsda.org/datafiles/taxi_trips/trip_data_1.csv.zip

# What are the field names?  Give descriptions for each field.
['medallion', 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']


# What datetime range does your data cover?  How many rows are there total?
Earliest datapoint: 2013-01-01 00:00:00
Latest datapoint: 2013-02-01 10:33:08
Rows: 14776615


# Give some sample data for each field.
{'medallion': '89D227B655E5C82AECF13C3F540D4CF4', 
'hack_license': 'BA96DE419E711691B9445D6A6307C170', 
'vendor_id': 'CMT', 
'rate_code': '1', 
'store_and_fwd_flag': 'N', 
'pickup_datetime': '2013-01-01 15:11:48', 
'dropoff_datetime': '2013-01-01 15:18:10', 
'passenger_count': '4', 
'trip_time_in_secs': '382', 
'trip_distance': '1.00', 
'pickup_longitude': '-73.978165', 
'pickup_latitude': '40.757977', 
'dropoff_longitude': '-73.989838', 
'dropoff_latitude': '40.751171'}


# What MySQL data types / len would you need to store each of the fields?
# int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
medallion: varchar(32)
hack_license: varchar(32)
vendor_id: varchar(3)
rate_code: int
store_and_fwd_flag: varchar(1)
pickup_datetime: datetime
dropoff_datetime: datetime
passenger_count: int 
trip_time_in_secs: int 
trip_distance: decimal(6,2) 
pickup_longitude: decimal(3,6)
pickup_latitude: decimal(3,6) 
dropoff_longitude: decimal(3,6)
dropoff_latitude: decimal(3,6)


# What is the geographic range of your data (min/max - X/Y)?
# Plot this (approximately on a map)
![map](lat_long_plot.png)
Min lat: -3547.9207
Max lat: 3477.1055
Min lon: -2771.2854
Max lon: 2228.7375


# What is the average overall computed trip distance? (You should use Haversine Distance)
# Draw a histogram of the trip distances binned anyway you see fit.
Average distance: 19.597999536473484 km

0 - 2500 km: 14747000
2500 - 5000 km: 726
5000 - 7500 km: 4193
7500 - 10000 km: 24556
10000 - 12500 km: 27
12500 - 15000 km: 18
15000 - 17500 km: 7
17500 - 20000 km: 2

Histogram in notebook cell (wonky shape)


# What are the distinct values for each field? (If applicable)
This took so long to figure out because making lists of the distinct values took so long O(n^2). Using set() instead of [] was a lot faster, it checks in 0(1)

The values are in the cell. The counts of distinct values in each field are below:

medallion has 13426 distinct values
hack_license has 32224 distinct values
vendor_id has 2 distinct values
rate_code has 14 distinct values
store_and_fwd_flag has 2 distinct values
pickup_datetime has 2303465 distinct values
dropoff_datetime has 2305816 distinct values
passenger_count has 10 distinct values
trip_time_in_secs has 6594 distinct values
trip_distance has 4368 distinct values
pickup_longitude has 40442 distinct values
pickup_latitude has 64511 distinct values
dropoff_longitude has 56249 distinct values
dropoff_latitude has 88766 distinct values


# For other numeric types besides lat and lon, what are the min and max values?
Rate code range: 0 - 210
Passenger count range: 0 - 255
Trip time range (seconds): 0 - 10800
Trip distance range (km): 0 - 100.0


# Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)
I flipped the x and y axis. Not sure what libraries I'm allowed to use for charts. I also adjusted the chart by 1.25 passengers for easier viewing.

Average number of passengers per hour:
00:00 - 1.77 avg | ***************************************************
01:00 - 1.77 avg | ***************************************************
02:00 - 1.77 avg | ****************************************************
03:00 - 1.77 avg | ****************************************************
04:00 - 1.75 avg | *************************************************
05:00 - 1.62 avg | *************************************
06:00 - 1.55 avg | ******************************
07:00 - 1.60 avg | **********************************
08:00 - 1.63 avg | *************************************
09:00 - 1.63 avg | *************************************
10:00 - 1.66 avg | ****************************************
11:00 - 1.67 avg | ******************************************
12:00 - 1.68 avg | *******************************************
13:00 - 1.69 avg | *******************************************
14:00 - 1.70 avg | ********************************************
15:00 - 1.72 avg | **********************************************
16:00 - 1.72 avg | **********************************************
17:00 - 1.70 avg | *********************************************
18:00 - 1.70 avg | *********************************************
19:00 - 1.71 avg | *********************************************
20:00 - 1.71 avg | *********************************************
21:00 - 1.72 avg | ***********************************************
22:00 - 1.74 avg | *************************************************
23:00 - 1.75 avg | **************************************************


# Create a new CSV file which has only one out of every thousand rows.
trip_data_1000.csv


# Repeat step 9 with the reduced dataset and compare the two charts.
Average number of passengers per hour:
00:00 - 1.78 avg | ****************************************************
01:00 - 1.80 avg | *******************************************************
02:00 - 1.71 avg | *********************************************
03:00 - 1.79 avg | ******************************************************
04:00 - 1.93 avg | *******************************************************************
05:00 - 1.72 avg | **********************************************
06:00 - 1.54 avg | ****************************
07:00 - 1.59 avg | **********************************
08:00 - 1.56 avg | ******************************
09:00 - 1.62 avg | *************************************
10:00 - 1.67 avg | ******************************************
11:00 - 1.58 avg | *********************************
12:00 - 1.71 avg | *********************************************
13:00 - 1.63 avg | **************************************
14:00 - 1.71 avg | *********************************************
15:00 - 1.69 avg | *******************************************
16:00 - 1.71 avg | **********************************************
17:00 - 1.72 avg | ***********************************************
18:00 - 1.65 avg | ****************************************
19:00 - 1.71 avg | **********************************************
20:00 - 1.75 avg | **************************************************
21:00 - 1.64 avg | **************************************
22:00 - 1.82 avg | ********************************************************
23:00 - 1.66 avg | *****************************************

This chart is less evenly distributed than the one generated in step 9. This is to be expected due to the Law of Large Numbers.