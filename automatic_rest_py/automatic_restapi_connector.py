#!/usr/bin/env python3

import json
from pprint import pprint
import requests

auth_token = '1f67dd3e61372bae1766f210758abd2a0327c683'

url = "https://api.automatic.com/"
dev = url + 'device/'
trips = url + 'trip/'
user = url + 'user/'


header_data = { 
    "Authorization": "Bearer {auth_token}".format(auth_token = auth_token),
}

def get_trips_in_between(from_date, to_date):
    'get all the trips between from_date and to_date'
    trips_url  = trips;
    trip_options = {
            'started_at__gte' : from_date.timestamp(),
            'ended_at__lte' : to_date.timestamp(),
        }
    trips_r = requests.get(trips, headers = header_data, params = trip_options)
    trips_content = trips_r.content.decode()
    trips_data = json.loads(trips_content)

    return trips_data

