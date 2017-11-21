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
else:
    print ("\n API data access failed\n")

realtime_trips_updates_input = python_object

station_id = "RAVENSWOOD"
stop_number = 3  # stop_number is the number of stops from OTC, when OTC=1
# WHen stop number is low, train is going North, when high, train going south

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
            #print key, value
            if value <= stop_number:
                print ("Train is going North")
            elif value > stop_number:
                print ("Train is going South")
        elif key == 'arrival':
            #print key, value
            for k, v in value.iteritems():
                #print k, v
                if k == "delay":
                    print "delay=", v
                elif k == "time":
                    #print "arrival time =", v['low']
                    from_zone = tz.tzutc()
                    to_zone = tz.tzlocal()
                    # utc = datetime.utcnow()
                    utc = datetime.strptime(v['low'], '%Y-%m-%dT%H:%M:%S.000Z')
                    # Tell the datetime object that it's in UTC time zone since
                    # datetime objects are 'naive' by default
                    utc = utc.replace(tzinfo=from_zone)
                    # Convert time zone
                    central = utc.astimezone(to_zone)
                    print("arrival time =", central.strftime("%I:%M %p"))

except NameError:
    # here i want to access the static schedule and return the next
    # scheduled train and have google assistant mention that the data isn't live
    print "No live data for your scheduled stop"
