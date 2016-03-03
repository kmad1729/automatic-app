from django.shortcuts import render
from django.http import Http404
from pprint import pprint

from requests.utils import quote
from datetime import datetime, timedelta
from automatic_rest_py.utils import \
    convert_date_str_to_date_obj, convert_date_iso_ts_to_date_obj, \
    distance_metres_to_miles, format_float, duration_seconds_to_minutes, \
    volume_liters_to_gallons
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
        try:
            from_date = convert_date_str_to_date_obj(trip_date_str)
        except ValueError:
            raise Http404("invalid date format {}".format(trip_date_str))
            
        to_date = from_date + timedelta(days = 1)
        #print(from_date < to_date)
        trip_data = get_trips_in_between(from_date, to_date)
        context['trip_date'] = from_date

        trip_count = int(trip_data['_metadata']['count'])
        context['next_date_resource'] = get_next_day_resource(from_date)
        context['prev_date_resource'] = get_prev_day_resource(from_date)
        if trip_count  > 0:
            context['trip_count'] =  trip_data['_metadata']['count']

            total_dist_m = 0
            total_duration_s = 0
            total_fuel_consumed_l = 0
            total_fuel_cost_usd = 0

            trip_objs = []
            for ind, trip in enumerate(trip_data['results'], 1):
                #pdb.set_trace()
                trip_obj = Trip(**(trip))
                trip_obj.trip_index = ind

                total_dist_m += float(trip_obj.distance_m)
                total_duration_s += float(trip_obj.duration_s)
                total_fuel_consumed_l += float(trip_obj.fuel_volume_l)
                total_fuel_cost_usd += float(trip_obj.fuel_cost_usd)
                
                trip_objs.append(trip_obj)

            context['trip_list'] = trip_objs
            context['trip_data'] = trip_data


            context['total_dist_mi'] = format_float(
                    distance_metres_to_miles(total_dist_m))

            context['total_duration_min'] = format_float(
                    duration_seconds_to_minutes(total_duration_s))

            context['total_fuel_consumed_g'] = format_float(
                    volume_liters_to_gallons(total_fuel_consumed_l))

            context['total_fuel_cost_usd'] = format_float(total_fuel_cost_usd)

            tweet_text = "I drove {total_dist_mi} miles on {date_driven:%A, %b-%d-%Y}!".format(
                    total_dist_mi = context['total_dist_mi'], 
                    date_driven = trip_obj.started_at )
            context["day_summary_tweet"] = \
                    '''
                    <iframe
                      src="https://platform.twitter.com/widgets/tweet_button.html?text={tweet_text}"
                      width="200"
                      height="30"
                      title="Twitter Tweet Button"
                      style="border: 0; overflow: hidden;">
                    </iframe>
                    '''.format(tweet_text = tweet_text)

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

