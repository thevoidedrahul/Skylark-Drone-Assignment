import csv
import logging.config

from loadData import GPSData, srt_data
from util import haversine

logging.config.fileConfig('../logging.conf')
log = logging.getLogger(__name__)


def writeFile(frameNumber, imageList):

    with open('csvoutput/videoSrtImageData.csv', 'a') as outfile:
        outfile.write(frameNumber.replace(',', '.'))
        outfile.write(',')
        outfile.write(':'.join(imageList))
        outfile.write('\n')


def getImage(imagesData, lon2, lat2, radius):
    imageList = []

    for image_name, image_data in imagesData.items():
        lon1, lat1, alt1 = map(float, image_data)

        distance = haversine(lon1, lat1, lon2, lat2)

        if distance < radius:
            imageList.append(image_name)

    return imageList


def checkFrames(frames, imagesData):
    for frame in frames:
        lon2, lat2, alt2 = frame[2].strip('\n').split(',')
        imageList = getImage(imagesData, lon2, lat2, 35)
        writeFile(frame[1].split('-->')[0], imageList)


def checkPoi(filename, imagesData):
    with open(filename, 'r') as rfile, open('csvoutput/assetPoi.csv', 'w') as wfile:

        reader = csv.DictReader(rfile)

        fieldnames = ['assetNames', 'longitude', 'latitude', 'imageNames']
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            lon2 = row['longitude']
            lat2 = row['latitude']
            imageList = getImage(imagesData, lon2, lat2, 50)

            row['imageNames'] = ':'.join(imageList)
            writer.writerow(row)


def main():
    imagesData = gpsData()
    frames = srtData()

    checkFrames(frames, imagesData)
    checkPoi('../assets.csv', imagesData)


if __name__ == '__main__':
    main()
