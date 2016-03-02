from django.shortcuts import render
from pprint import pprint

from requests.utils import quote
from datetime import datetime, timedelta
from automatic_rest_py.utils import \
    convert_date_str_to_date_obj, convert_date_iso_ts_to_date_obj, \
    distance_metres_to_miles
from automatic_rest_py.automatic_restapi_connector import get_trips_in_between
from automatic_rest_py.api_objects import Trip

import pdb

# Create your views here.

def get_next_day_resource(current_day_datetime):
    next_day = current_day_datetime + timedelta(days = 1)
    date_str = "{next_day.month}/{next_day.day}/{next_day.year}".format(
            next_day = next_day)
    return date_str

def get_prev_day_resource(current_day_datetime):
    next_day = current_day_datetime - timedelta(days = 1)
    date_str = "{next_day.month}/{next_day.day}/{next_day.year}".format(
            next_day = next_day)
    return date_str



def home(request):
    context = {}
    trip_date_str = request.GET.get('trip_date')
    #pprint(vars(request))
    if trip_date_str:
        from_date = convert_date_str_to_date_obj(trip_date_str)
        to_date = from_date + timedelta(days = 1)
        #print(from_date < to_date)
        trip_data = get_trips_in_between(from_date, to_date)
        context['trip_date'] = from_date

        context['trip_count'] =  trip_data['_metadata']['count']
        context['next_date_resource'] = get_next_day_resource(from_date)
        context['prev_date_resource'] = get_prev_day_resource(from_date)


        trip_objs = []
        for trip in trip_data['results']:
            #pdb.set_trace()
            trip_obj = Trip(**(trip))
            trip_obj.distance_mi = distance_metres_to_miles(trip_obj.distance_m, 2)
            tweet_text = "Just drove {distance_driven} miles!".format(
                    distance_driven = trip_obj.distance_mi)
            trip_obj.dist_tweet_str = \
                    '''
                    <iframe
                      src="http://platform.twitter.com/widgets/tweet_button.html?text={tweet_text}&data-url="""
                      width="140"
                      height="28"
                      title="Twitter Tweet Button"
                      style="border: 0; overflow: hidden;">
                    </iframe>
                    '''.format(tweet_text = tweet_text)
                #"https://twitter.com/intent/tweet?text={tweet_text}".format(
                        #tweet_text = tweet_text)

            
            trip_objs.append(trip_obj)

        context['trip_list'] = trip_objs


        context['trip_data'] = trip_data

    return render(request, 'scoresheet_app/home.html', context)

def last_week(request):

    from_date_str = request.GET.get('from')
    to_date_str = request.GET.get('to')

    if from_date_str and to_date_str:
        from_date = convert_date_str_to_date_obj(from_date_str)
        to_date = convert_date_str_to_date_obj(to_date_str)

        trip_data = get_trips_in_between(from_date, to_date)

        context['trip_data'] = trip_data

    return render(request, 'scoresheet_app/last_week.html', context)

