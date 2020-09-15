# This module stores information about a geographical
# location on Earth.

import math

RADIUS = 3958.8


class GeoLocation:

    # construct an object with a given latitude and longitude
    def __init__(self, latitude, longitude):
        try:
            self._latitude = float(latitude)
            self._longitude = float(longitude)
        except ValueError:
            print("One or more values are not compatible with 'float'")

    # return the distance in miles between two geolocations
    def distance_from(self, other):
        lat_1 = math.radians(self._latitude)
        lat_2 = math.radians(other.latitude)
        long_1 = math.radians(self._longitude)
        long_2 = math.radians(other.longitude)
        theta = math.sin(lat_1) * math.sin(lat_2) + math.cos(lat_1) * math.cos(lat_2) * math.cos(long_1 - long_2)
        central_angle = math.acos(theta)
        return RADIUS * central_angle

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    # determines if two geolocations are equal to each other
    def __eq__(self, other):
        return self._latitude == other.latitude and self._longitude == other.longitude

    # returns a string representation of the geolocation.
    def __str__(self):
        return f"({self._latitude},{self._longitude})"
