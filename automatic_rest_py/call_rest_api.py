#!/usr/bin/env python3

import requests
import json
from pprint import pprint
from keys import auth_token

url = "https://api.automatic.com/"
dev = url + 'device/'
trips = url + 'trip/'
user = url + 'user/'


header_data = { 
    "Authorization": "Bearer {auth_token}".format(auth_token = auth_token),
}

r = requests.get(dev, headers = header_data)
r_content = r.content.decode()
data = json.loads(r_content)
pprint(data)

trip_options = {
        #'page': '15',
        'ended_at__lte': 1403044851.692,
        'started_at__gte':1402992299.231,
}

#trip_options = {'started_at__gte': 735362, 'ended_at__lte': 735400}

trips_r = requests.get(trips, headers = header_data, params = trip_options)
trips_content = trips_r.content.decode()
trips_data = json.loads(trips_content)


trips_meta_data = trips_data['_metadata']
trips_result = trips_data['results']
