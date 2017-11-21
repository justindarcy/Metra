import requests, json
from datetime import datetime
from dateutil import tz
"""
realtime_trips_updates_input is the input to the file

station_id is your station of choice
"""
# fething the data here
response = requests.get('https://gtfsapi.metrarail.com/gtfs/tripUpdates', auth=(
'f0db64a9715bf9d74470f5587b8750b2', 'd3ca32f24b4868e11c90b43fd9bb6589'))

python_object = json.loads(response.content.decode("utf-8"))

if response.status_code == 200:
	print "\nData access from Metra API successfull \n"

realtime_trips_updates_input = python_object

station_id = "RAVENSWOOD"

for x in range(0,len(realtime_trips_updates_input)):

    for key, value in realtime_trips_updates_input[x]['trip_update'].iteritems() :

        if key == 'stop_time_update':

            for v in value:  # itterating through the values list
                #print type(v)
                for key, value in v.iteritems():
                    #print key
                    if value == station_id:
                        my_station_trains = v
                        #print v  # this is for debugging purposes

try:
    for key, value in my_station_trains.iteritems():
        if key == "stop_sequence":
            print key, value
        elif key == 'arrival':
            #print key, value
            for k, v in value.iteritems():
                #print k, v
                if k == "delay":
                    print "delay=", v
                elif k == "time":
                    print "arrival time =", v['low']
                    print (tz.tzutc(v['low']))
                    # to_zone = tz.tzlocal(v['low'])
except NameError:
    # here i want to access the static schedule and return the next
    # scheduled train and have google assistant mention that the data isn't live
    print "No live data for your scheduled stop"
