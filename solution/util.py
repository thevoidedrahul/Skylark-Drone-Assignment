import logging
from math import asin, cos, radians, sin, sqrt

log = logging.getLogger(__name__)

def haversine(lon1, lat1, lon2, lat2, alt1=0, alt2=0):

    earth_radius = 6371
    lon1, lat1, lon2, lat2 = map(radians, list(
        map(float, [lon1, lat1, lon2, lat2])))

    difflon = lon2 - lon1
    difflat = lat2 - lat1
    diffalt = alt2 - alt1
    a = sin(difflat / 2)**2 + cos(lat1) * cos(lat2) * sin(difflon / 2)**2
    c = 2 * asin(sqrt(a))
    distance = earth_radius * c * 1000

    distance = distance ** 2 + diffalt ** 2

    return sqrt(distance)


def convertToDegree(value):

    degrees = float(value[0][0]) / float(value[0][1])

    minutes = float(value[1][0]) / float(value[1][1])

    seconds = float(value[2][0]) / float(value[2][1])

    return degrees + (minutes / 60.0) + (seconds / 3600.0)


def convertAltToDegree(value):

    return float(value[0]) / float(value[1])
