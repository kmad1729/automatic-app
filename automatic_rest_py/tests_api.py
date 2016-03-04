#!/usr/bin/env python3

import unittest
from datetime import datetime
from utils import format_float, \
        convert_date_str_to_date_obj, \
        convert_date_iso_ts_to_date_obj, \
        distance_metres_to_miles, \
        duration_seconds_to_minutes, \
        volume_liters_to_gallons

class UtilsTests(unittest.TestCase):
    def test_format_float(self):
        self.assertEqual("3.14", format_float(3.1415926))
        self.assertEqual("3.142", format_float(3.1415926, 3))
        self.assertEqual("3.1416", format_float(3.1415926, 4))
        self.assertEqual("3", format_float(3.1415926, 0))

    def test_convert_date_iso_ts_to_date_obj(self):
        date_str1 = "2014-06-03T15:42:52.400000Z"
        date_str2 = "2014-06-03T15:42:52Z"
        exp_date_obj1 = datetime(2014, 6, 3, 15, 42, 52, 400000)
        exp_date_obj2 = datetime(2014, 6, 3, 15, 42, 52)
        self.assertIsInstance(convert_date_iso_ts_to_date_obj(date_str1), 
                datetime)
        self.assertEqual(convert_date_iso_ts_to_date_obj(date_str1), 
                exp_date_obj1)
        self.assertEqual(convert_date_iso_ts_to_date_obj(date_str2), 
                exp_date_obj2)

    def test_convert_date_str_to_date_obj(self):
        date_str1= "3/2/2014"
        date_str2 = "3/2/14"
        date_str3 = "03/02/2014"
        exp_obj = datetime(2014, month = 3, day = 2)
        self.assertIsInstance(convert_date_str_to_date_obj(date_str1), datetime)
        self.assertEqual(convert_date_str_to_date_obj(date_str1), exp_obj)
        self.assertEqual(convert_date_str_to_date_obj(date_str2), 
                datetime(14, month = 3, day = 2))
        self.assertEqual(convert_date_str_to_date_obj(date_str3), exp_obj)
        with self.assertRaises(ValueError):
            convert_date_str_to_date_obj('1/8')
            convert_date_str_to_date_obj('December/23/2014')

    def test_distance_metres_to_miles(self):
        self.assertEqual(distance_metres_to_miles('100.12'), 0.06221166452)
        self.assertEqual(distance_metres_to_miles('1'), 0.000621371)
        self.assertEqual(distance_metres_to_miles('0'), 0.0)
        with self.assertRaises(ValueError):
            m = distance_metres_to_miles('foo')

    def test_duration_seconds_to_minutes(self):
        self.assertEqual(duration_seconds_to_minutes('60'), 1.0)
        self.assertNotEqual(duration_seconds_to_minutes('60'), 1.1)
        self.assertEqual(duration_seconds_to_minutes('360'), 6.0)
        self.assertEqual(duration_seconds_to_minutes('73.3'), 1.2216666666666667)

    def test_volume_liters_to_gallons(self):
        self.assertEqual(volume_liters_to_gallons('30'), 7.925160000000001)
        self.assertEqual(volume_liters_to_gallons('1'), 0.264172)


if __name__ == "__main__":
    unittest.main()
