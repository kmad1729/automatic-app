from datetime import datetime, timedelta

def convert_date_str_to_date_obj(date_str):
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

def distance_metres_to_miles(dist_metres, prec):
    conversion_factor = 0.000621371
    format_str = '{{:.{precision}f}}'.format(precision = prec)
    return format_str.format(conversion_factor * float(dist_metres))
