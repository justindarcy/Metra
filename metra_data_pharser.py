# -*- coding: utf-8 -*-
import requests, json, calendar
from datetime import datetime
#from dateutil import tz

# ---------------------fething the data here------------------------
response = requests.get('https://gtfsapi.metrarail.com/gtfs/schedule/stop_times', auth=(
'f0db64a9715bf9d74470f5587b8750b2', 'd3ca32f24b4868e11c90b43fd9bb6589'))
static_schedule_input = json.loads(response.content.decode("utf-8"))

if response.status_code == 200:
	print ("\nData access from Metra API successfull \n")
else:
    print ("\n API data access failed\n")

response2 = requests.get('https://gtfsapi.metrarail.com/gtfs/schedule/trips', auth=('f0db64a9715bf9d74470f5587b8750b2', 'd3ca32f24b4868e11c90b43fd9bb6589'))
trips_api = json.loads(response2.content.decode("utf-8"))

response3 = requests.get('https://gtfsapi.metrarail.com/gtfs/schedule/calendar', auth=('f0db64a9715bf9d74470f5587b8750b2', 'd3ca32f24b4868e11c90b43fd9bb6589'))
calendar_api = json.loads(response3.content.decode("utf-8"))

# ---------------------fething the data here------------------------

# ----- input variables-----------
my_station_id = "RAVENSWOOD" # station you leave from
stop_number = 3  # stops away from OTC your station is
desired_direction="North"  # direction from above to below
destination = "EVANSTON" # station you go to
# ----- input variables-----------

direction='blank'
train_times=[]
future_train_times=[]
train_options_trip_id=[]
train_options_filtered=[]
next_train_id=[]

# ------calendar variables---------
day_names = list(calendar.day_name) 
today_num=(datetime.today().weekday()) #Monday is 0 and Sunday is 6
today = (day_names[today_num].lower())
service_id_list=[]
# ------calendar variables---------

def service_finder():   
    for cal in calendar_api:
        for key, value in cal.items():
    
            if key == today and value==1:
                service_id_list.append(cal['service_id'])
    return(service_id_list)


def service_id_lookup(trip_id_str):
    for trip in trips_api:
        if trip['trip_id'] == trip_id_str:
            return (trip['service_id'])


def trip_lookup(t_id):
    for t_list in static_schedule_input:
        if t_list['trip_id'] == t_id and t_list['stop_id'] == destination:

            service_id_str = service_id_lookup(t_list['trip_id'])
            service_id_list = service_finder()
            if service_id_str in service_id_list:         
                # trains stopping at ravenswood, going north, and stopping at destination for today
                train_options_trip_id.append(t_list['trip_id'])
    return train_options_trip_id


for d in static_schedule_input:
    if d['stop_id'] == my_station_id:

        if d['stop_sequence'] > stop_number:
            direction='South'
        else:
            direction='North'
            
        if direction == desired_direction:
            train_options_trip_id = trip_lookup(d['trip_id'])

            if d['arrival_time'] not in train_times and d['trip_id'] in train_options_trip_id:
                train_times.append(d['arrival_time'])
                train_options_filtered.append(d['trip_id'])
                
train_times_sort = sorted(train_times)
#print(train_times_sort, '\n')
now = datetime.now()
c=0
for t in train_times_sort:
    if t[0:2] == '24':
        t_new = datetime.strptime(t, '24:%M:%S')
        # add tomorrows year-month-day, below (+1) likely doesn't work
        t_new = t_new.replace(year=now.year, month=now.month, day=now.day+1)
        if t_new>now:
            future_train_times.append(t_new)
    else:
        t_new = datetime.strptime(t, '%H:%M:%S')
        t_new = t_new.replace(year=now.year, month=now.month, day=now.day)
        if t_new>now:
            future_train_times.append(t_new)
            next_train_id.append(train_options_filtered[c])
    c=+1


next_train = future_train_times[0]
print('next_train(scheduled)=', next_train.strftime("%I:%M %p"))
print(next_train_id[0])


# fething the live data here
response4 = requests.get('https://gtfsapi.metrarail.com/gtfs/tripUpdates', auth=(
'f0db64a9715bf9d74470f5587b8750b2', 'd3ca32f24b4868e11c90b43fd9bb6589'))
realtime_trips_updates_input = json.loads(response4.content.decode("utf-8"))

for dic in realtime_trips_updates_input:

    if dic['id'] == next_train_id[0]:
        print('live dataaaaa')
        my_delay = dic['trip_update']['stop_time_update']['arrival']['delay']
        print(my_delay)
        
my_delay_exists = 'my_delay' in locals() or 'my_delay' in globals()

if my_delay_exists:
    print('Live data exists')
    print('delay=',my_delay)
else:
    print('No live data')
