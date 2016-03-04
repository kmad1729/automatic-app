from datetime import datetime, timedelta

def format_float(float_number, prec = 2):
    'format a floting point number to a given precision'
    format_string = "{{:.{precision}f}}".format(precision = prec)
    return format_string.format(float_number)

def convert_date_str_to_date_obj(date_str):
    'convert date string mm/dd/yyyy to datetime object'
    month, day, year = map(int, date_str.split('/'))
    return datetime(year = year, month = month, day = day)

def convert_date_iso_ts_to_date_obj(date_iso_timestamp):
    '''convert iso based time stamp to datetime object
    e.g 2014-06-03T15:42:52.400000Z to datetime(2014, 6, 3, 15, 42, 52, 400000)
    e.g 2014-06-03T16:01:03.100000Z to datetime(2014, 6, 3, 16, 1, 3, 100000)
    e.g 2014-06-03T05:38:07Z to datetime(2014, 6, 3, 5, 38, 7)
    '''

    if '.' in date_iso_timestamp:
        format_string = "%Y-%m-%dT%H:%M:%S.%fZ"
    else:
        format_string = "%Y-%m-%dT%H:%M:%SZ"

    return datetime.strptime(date_iso_timestamp, format_string)

def distance_metres_to_miles(dist_metres_string):
    'convert a given meters string to miles float'
    METRES_MI_CONVERSION_FACTOR = 0.000621371
    return METRES_MI_CONVERSION_FACTOR * float(dist_metres_string)

def duration_seconds_to_minutes(seconds_string):
    'convert seconds string to minutes'
    SECONDS_MIN_CONVERSION_FACTOR = 1 / 60
    return float(seconds_string) * SECONDS_MIN_CONVERSION_FACTOR

def volume_liters_to_gallons(litres_string):
    'convert liters to gallons'
    LITRE_TO_GALLON_CONVERSION_FACTOR = 0.264172
    return float(litres_string)* LITRE_TO_GALLON_CONVERSION_FACTOR
