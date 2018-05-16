"""
Find the coordinates of all places called "Brussels".
Complete the code below.

- Create a class that corresponds to a Location object.
  The field names are:
           location_id, country, region, city,
           postal_code, lat, lon, metro_code, area_code

- Create one generator that opens the file and yields
  locations one at a time.
  Use CSV.reader()
  https://docs.python.org/3.6/library/csv.html#csv.reader

- Create a second function that consumes the previous
  generator (or any generator of locations), filters
  on location names and yields the matching locations.
  (This should take a city name as input.)

- Create a third function that consumes the second one,
  and prints the coordinates for the matching locations.

Also see the following article about generators:
https://cisco.jiveon.com/blogs/jonathan/2016/09/12/too-much-memory-usage-what-to-do-now
"""

import csv

class Location:
    def __init__ (self, location_id, country, region, city, postal_code, lat, lon, metro_code, area_code):
        self.location_id = location_id
        self.country = country
        self.region = region
        self.city = city
        self.postal_code = postal_code
        self.lat = lat
        self.lon = lon
        self.metro_code = metro_code
        self.area_code = area_code





def get_locations_from_file(filename: str):
    with open (filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            location_id, country, region, city, postal_code, lat, lon, metro_code, area_code = row.split(',')
            yield Location(location_id, country, region, city, postal_code, lat, lon, metro_code, area_code)

def filter_locations(locations , Cityname: str):
    for i in locations:
        if i.city == Cityname:
            yield i

def print_locations(locations):
    for i in locations:
        print('lat: ' + i.lat + ' , lon: ' + i.lon)


def main():
    locations = get_locations_from_file('locations.csv')
    filtered_locations = filter_locations(locations, 'Brussels')
    print_locations(filtered_locations)


if __name__ == '__main__':
    main()