from .utils import convert_date_str_to_date_obj, format_float, \
    convert_date_iso_ts_to_date_obj, duration_seconds_to_minutes, \
    distance_metres_to_miles, volume_liters_to_gallons



class Trip:
    _date_fields = [
            'started_at',
            'ended_at',
            ]

    def __init__(self, *args, **kwargs):
        for k,v in kwargs.items():
            if k in self._date_fields:
                setattr(self, k, convert_date_iso_ts_to_date_obj(v))
            else:
                setattr(self, k, v)

    @property
    def duration_min(self):
        return format_float(duration_seconds_to_minutes(self.duration_s))

    @property
    def distance_mi(self):
        return format_float(distance_metres_to_miles(self.distance_m))

    @property
    def fuel_volume_g(self):
        return format_float(volume_liters_to_gallons(self.fuel_volume_l))


