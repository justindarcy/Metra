"""
realtime_trips_updates_input is the input to the file with the below
changes already made(we'll need code that can do this automatically)
** NOTE: following changes were made manually in realtime_trips_updates
	false -> False
	true -> True
	null -> null with added quotes

station_id is your station of choice
"""
realtime_trips_updates_input = [
    {
        "id": "BNSF_BN1318_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "BNSF_BN1318_V7_B",
                "route_id": "BNSF",
                "direction_id": 'null',
                "start_time": "16:20:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8581",
                "label": "1318",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 28,
                    "stop_id": "CUS",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8581",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "BNSF_BN1318_V7_B",
                        "route_id": "BNSF",
                        "direction_id": 'null',
                        "start_time": "16:20:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8581",
                        "label": "1318",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.87223815917969,
                        "longitude": -87.63816833496094,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:45:06.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.163Z"
    },
    {
        "id": "UP-W_UW512_V8_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "UP-W_UW512_V8_B",
                "route_id": "UP-W",
                "direction_id": 'null',
                "start_time": "16:25:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8527",
                "label": "512",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 28,
                    "stop_id": "OTC",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8527",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "UP-W_UW512_V8_B",
                        "route_id": "UP-W",
                        "direction_id": 'null',
                        "start_time": "16:25:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8527",
                        "label": "512",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.88888168334961,
                        "longitude": -87.66246795654297,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:39.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.163Z"
    },
    {
        "id": "UP-NW_UNW719_V8_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "UP-NW_UNW719_V8_B",
                "route_id": "UP-NW",
                "direction_id": 'null',
                "start_time": "16:30:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8456",
                "label": "719",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 22,
                    "stop_id": "FOXRG",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 23,
                    "stop_id": "CARY",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 24,
                    "stop_id": "PINGREE",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 26,
                    "stop_id": "CRYSTAL",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "WOODSTOCK",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:10:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:10:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 32,
                    "stop_id": "HARVARD",
                    "arrival": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:29:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 540,
                        "time": {
                            "low": "2017-11-20T00:29:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8456",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "UP-NW_UNW719_V8_B",
                        "route_id": "UP-NW",
                        "direction_id": 'null',
                        "start_time": "16:30:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8456",
                        "label": "719",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 42.18373489379883,
                        "longitude": -88.19210052490234,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:40.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.163Z"
    },
    {
        "id": "UP-NW_UNW722_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "UP-NW_UNW722_V7_B",
                "route_id": "UP-NW",
                "direction_id": 'null',
                "start_time": "16:35:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8526",
                "label": "722",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 15,
                    "stop_id": "ARLINGTNHT",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 16,
                    "stop_id": "MTPROSPECT",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 18,
                    "stop_id": "CUMBERLAND",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 21,
                    "stop_id": "DESPLAINES",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 22,
                    "stop_id": "DEEROAD",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 23,
                    "stop_id": "PARKRIDGE",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:06:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:06:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 24,
                    "stop_id": "EDISONPK",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:09:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:09:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 25,
                    "stop_id": "NORWOODP",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:12:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:12:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "JEFFERSONP",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 30,
                    "stop_id": "IRVINGPK",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:20:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:20:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 31,
                    "stop_id": "CLYBOURN",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:27:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:27:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 32,
                    "stop_id": "OTC",
                    "arrival": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:38:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 900,
                        "time": {
                            "low": "2017-11-20T00:38:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8526",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "UP-NW_UNW722_V7_B",
                        "route_id": "UP-NW",
                        "direction_id": 'null',
                        "start_time": "16:35:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8526",
                        "label": "722",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 42.08510971069336,
                        "longitude": -87.98573303222656,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:15.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.164Z"
    },
    {
        "id": "MD-N_MN2615_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "MD-N_MN2615_V7_B",
                "route_id": "MD-N",
                "direction_id": 'null',
                "start_time": "16:35:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8553",
                "label": "2615",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 23,
                    "stop_id": "PRAIRIEXNG",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "GRAYSLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "ROUNDLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 29,
                    "stop_id": "LONGLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 30,
                    "stop_id": "INGLESIDE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 31,
                    "stop_id": "FOXLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8553",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "MD-N_MN2615_V7_B",
                        "route_id": "MD-N",
                        "direction_id": 'null',
                        "start_time": "16:35:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8553",
                        "label": "2615",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 42.29547119140625,
                        "longitude": -87.96694946289062,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:37.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.164Z"
    },
    {
        "id": "UP-W_UW509_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "UP-W_UW509_V7_B",
                "route_id": "UP-W",
                "direction_id": 'null',
                "start_time": "16:40:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8453",
                "label": "509",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 23,
                    "stop_id": "WCHICAGO",
                    "arrival": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 25,
                    "stop_id": "GENEVA",
                    "arrival": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-19T23:55:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "LAFOX",
                    "arrival": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-20T00:04:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-20T00:04:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "ELBURN",
                    "arrival": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-20T00:24:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 480,
                        "time": {
                            "low": "2017-11-20T00:24:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8453",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "UP-W_UW509_V7_B",
                        "route_id": "UP-W",
                        "direction_id": 'null',
                        "start_time": "16:40:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8453",
                        "label": "509",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.8807373046875,
                        "longitude": -88.197998046875,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:38.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.164Z"
    },
    {
        "id": "MD-N_MN2616_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "MD-N_MN2616_V7_B",
                "route_id": "MD-N",
                "direction_id": 'null',
                "start_time": "16:45:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8537",
                "label": "2616",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 18,
                    "stop_id": "GOLF",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:46:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:46:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 19,
                    "stop_id": "MORTONGRV",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 20,
                    "stop_id": "EDGEBROOK",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 21,
                    "stop_id": "FORESTGLEN",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 24,
                    "stop_id": "MAYFAIR",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 25,
                    "stop_id": "GRAYLAND",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 26,
                    "stop_id": "HEALY",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "WESTERNAVE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 31,
                    "stop_id": "CUS",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:25:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:25:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8537",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "MD-N_MN2616_V7_B",
                        "route_id": "MD-N",
                        "direction_id": 'null',
                        "start_time": "16:45:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8537",
                        "label": "2616",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 42.05773162841797,
                        "longitude": -87.79686737060547,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:30.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.165Z"
    },
    {
        "id": "BNSF_BN1315_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "BNSF_BN1315_V7_B",
                "route_id": "BNSF",
                "direction_id": 'null',
                "start_time": "16:40:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8592",
                "label": "1315",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 25,
                    "stop_id": "NAPERVILLE",
                    "arrival": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 26,
                    "stop_id": "ROUTE59",
                    "arrival": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "AURORA",
                    "arrival": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 600,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8592",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "BNSF_BN1315_V7_B",
                        "route_id": "BNSF",
                        "direction_id": 'null',
                        "start_time": "16:40:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8592",
                        "label": "1315",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.77996826171875,
                        "longitude": -88.13945770263672,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:38.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.165Z"
    },
    {
        "id": "RI_RI322_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "RI_RI322_V7_B",
                "route_id": "RI",
                "direction_id": 'null',
                "start_time": "17:06:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8478",
                "label": "322",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 34,
                    "stop_id": "LSS",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8478",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "RI_RI322_V7_B",
                        "route_id": "RI",
                        "direction_id": 'null',
                        "start_time": "17:06:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8478",
                        "label": "322",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.874000549316406,
                        "longitude": -87.63224792480469,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:06.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.165Z"
    },
    {
        "id": "UP-N_UN822_V7_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "UP-N_UN822_V7_B",
                "route_id": "UP-N",
                "direction_id": 'null',
                "start_time": "17:10:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8420",
                "label": "822",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 23,
                    "stop_id": "EVANSTON",
                    "arrival": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:50:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:50:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 24,
                    "stop_id": "MAINST",
                    "arrival": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "RAVENSWOOD",
                    "arrival": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-19T23:59:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 29,
                    "stop_id": "OTC",
                    "arrival": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 240,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8420",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "UP-N_UN822_V7_B",
                        "route_id": "UP-N",
                        "direction_id": 'null',
                        "start_time": "17:10:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8420",
                        "label": "822",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 42.07482147216797,
                        "longitude": -87.70721435546875,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:44.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.165Z"
    },
    {
        "id": "MD-N_MN2619_V1_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "MD-N_MN2619_V1_B",
                "route_id": "MD-N",
                "direction_id": 'null',
                "start_time": "17:35:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "8519",
                "label": "2619",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 12,
                    "stop_id": "EDGEBROOK",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 13,
                    "stop_id": "MORTONGRV",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 14,
                    "stop_id": "GOLF",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 15,
                    "stop_id": "GLENVIEW",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:10:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:10:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 17,
                    "stop_id": "NBROOK",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:17:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:17:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 19,
                    "stop_id": "DEERFIELD",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:22:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:22:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 20,
                    "stop_id": "LAKEFRST",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:28:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:28:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 22,
                    "stop_id": "LIBERTYVIL",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:40:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:40:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "GRAYSLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "ROUNDLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T00:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 31,
                    "stop_id": "FOXLAKE",
                    "arrival": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T01:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 180,
                        "time": {
                            "low": "2017-11-20T01:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "8462",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "MD-N_MN2619_V1_B",
                        "route_id": "MD-N",
                        "direction_id": 'null',
                        "start_time": "17:35:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "8462",
                        "label": "2619",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.905941009521484,
                        "longitude": -87.71739196777344,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:46:35.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.166Z"
    },
    {
        "id": "ME_ME826_V6_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "ME_ME826_V6_B",
                "route_id": "ME",
                "direction_id": 'null',
                "start_time": "17:40:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "1339",
                "label": "826",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 20,
                    "stop_id": "MATTESON",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:47:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 21,
                    "stop_id": "211TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:49:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 22,
                    "stop_id": "OLYMPIA",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 23,
                    "stop_id": "FLOSSMOOR",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 24,
                    "stop_id": "HOMEWOOD",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:56:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:56:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 25,
                    "stop_id": "CALUMET",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:58:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-19T23:58:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 26,
                    "stop_id": "HAZELCREST",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 27,
                    "stop_id": "HARVEY",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 28,
                    "stop_id": "147TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:05:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 29,
                    "stop_id": "IVANHOE",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 30,
                    "stop_id": "RIVERDALE",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:09:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:09:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 33,
                    "stop_id": "KENSINGTN",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:14:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:14:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 34,
                    "stop_id": "111TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:15:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 35,
                    "stop_id": "107TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 36,
                    "stop_id": "103RD-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:17:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:17:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 37,
                    "stop_id": "95TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:19:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:19:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 38,
                    "stop_id": "91ST-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:21:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:21:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 39,
                    "stop_id": "87TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:22:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:22:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 40,
                    "stop_id": "83RD-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:23:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:23:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 41,
                    "stop_id": "79TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:24:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:24:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 42,
                    "stop_id": "75TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:26:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:26:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 44,
                    "stop_id": "63RD-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:29:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:29:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 45,
                    "stop_id": "59TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:30:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:30:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 46,
                    "stop_id": "55-56-57TH",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:32:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:32:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 47,
                    "stop_id": "51ST-53RD",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:34:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:34:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 48,
                    "stop_id": "47TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:35:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:35:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 49,
                    "stop_id": "27TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:38:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:38:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 50,
                    "stop_id": "MCCORMICK",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:39:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:39:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 51,
                    "stop_id": "18TH-UP",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:40:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:40:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 52,
                    "stop_id": "MUSEUM",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:43:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:43:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 53,
                    "stop_id": "VANBUREN",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:45:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:45:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 54,
                    "stop_id": "MILLENNIUM",
                    "arrival": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 120,
                        "time": {
                            "low": "2017-11-20T00:51:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "1339",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "ME_ME826_V6_B",
                        "route_id": "ME",
                        "direction_id": 'null',
                        "start_time": "17:40:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "1339",
                        "label": "826",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.49765396118164,
                        "longitude": -87.70280456542969,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 0,
                    "timestamp": {
                        "low": "2017-11-19T23:46:38.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.167Z"
    },
    {
        "id": "ME_ME8326_V6_B",
        "is_deleted": False,
        "trip_update": {
            "trip": {
                "trip_id": "ME_ME8326_V6_B",
                "route_id": "ME",
                "direction_id": 'null',
                "start_time": "17:39:00",
                "start_date": "20:17:11",
                "schedule_relationship": 0
            },
            "vehicle": {
                "id": "1243",
                "label": "8326",
                "license_plate": 'null'
            },
            "stop_time_update": [
                {
                    "stop_sequence": 13,
                    "stop_id": "WINDSORPK",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:48:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:48:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 14,
                    "stop_id": "SOUTHSHORE",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:50:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:50:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 15,
                    "stop_id": "BRYNMAWR",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:52:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 16,
                    "stop_id": "STONYISLND",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:54:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 44,
                    "stop_id": "63RD-UP",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:57:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 45,
                    "stop_id": "59TH-UP",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:58:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-19T23:58:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 46,
                    "stop_id": "55-56-57TH",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:00:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 47,
                    "stop_id": "51ST-53RD",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:02:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 48,
                    "stop_id": "47TH-UP",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:03:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 49,
                    "stop_id": "27TH-UP",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:06:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:06:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 50,
                    "stop_id": "MCCORMICK",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:07:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 51,
                    "stop_id": "18TH-UP",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:08:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:08:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 52,
                    "stop_id": "MUSEUM",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:11:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 53,
                    "stop_id": "VANBUREN",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:13:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:13:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                },
                {
                    "stop_sequence": 54,
                    "stop_id": "MILLENNIUM",
                    "arrival": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "departure": {
                        "delay": 0,
                        "time": {
                            "low": "2017-11-20T00:16:00.000Z",
                            "high": 0,
                            "unsigned": False
                        },
                        "uncertainty": 0
                    },
                    "schedule_relationship": 0
                }
            ],
            "timestamp": {
                "low": "2017-11-19T23:47:00.000Z",
                "high": 0,
                "unsigned": True
            },
            "delay": 'null',
            "position": {
                "id": "1243",
                "is_deleted": False,
                "trip_update": 'null',
                "vehicle": {
                    "trip": {
                        "trip_id": "ME_ME8326_V6_B",
                        "route_id": "ME",
                        "direction_id": 'null',
                        "start_time": "17:39:00",
                        "start_date": "20171119",
                        "schedule_relationship": 0
                    },
                    "vehicle": {
                        "id": "1243",
                        "label": "8326",
                        "license_plate": 'null'
                    },
                    "position": {
                        "latitude": 41.72711181640625,
                        "longitude": -87.54783630371094,
                        "bearing": 'null',
                        "odometer": 'null',
                        "speed": 'null'
                    },
                    "current_stop_sequence": 'null',
                    "stop_id": 'null',
                    "current_status": 2,
                    "timestamp": {
                        "low": "2017-11-19T23:37:50.000Z",
                        "high": 0,
                        "unsigned": True
                    },
                    "congestion_level": 'null',
                    "occupancy_status": 'null'
                },
                "alert": 'null'
            }
        },
        "vehicle": 'null',
        "alert": 'null',
        "metra-publish-tstamp": "2017-11-19T23:47:01.167Z"
    }
]
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
                print "arrival time=", v['low']
