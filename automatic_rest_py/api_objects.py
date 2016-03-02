from .utils import convert_date_str_to_date_obj, convert_date_iso_ts_to_date_obj


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

