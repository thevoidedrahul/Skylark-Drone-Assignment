import glob
import logging
from itertools import groupby

from PIL import Image

from util import convertToDegree, convertAltToDegrees, haversine

log = logging.getLogger(__name__)

def gpsData():
    imagesData = {}

    logging.info("loading images data from JPG files")

    for image in glob.glob('../images/*.JPG'):

        try:
            gpsInfo = Image.open(image)._getexif()[0x8825]
        except TypeError:
            log.warning("GPSInfo not found")

        gpsLatitudeRef = gpsInfo[1]
        gpsLatitude = gpsInfo[2]
        gpsLongitudeRef = gpsInfo[3]
        gpsLongitude = gpsInfo[4]
        gpsAltitudeRef = gpsInfo[5]
        gpsAltitude = gpsInfo[6]

        lat = convertToDegree(gpsLatitude)
        if gpsLatitudeRef != "N":
            lat = 0 - lat

        lon = convertToDegress(gpsLongitude)
        if gpsLongitudeRef != "E":
            lon = 0 - lon

        alt = convert_altToDegrees(gpsAltitude)
        if ord(gpsAltitudeRef) != 0:
            alt = 0 - alt

        imagesData[image[10:]] = [lon, lat, alt]

    return imagesData


def srtData():
    
    logging.info("loading coordinates from SRT file")

    with open('../videos/DJI_0301.SRT') as file:
        res = [list(g)
               for b, g in groupby(file, lambda x: bool(x.strip())) if b]

    return res
