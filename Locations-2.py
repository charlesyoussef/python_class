import csv

class Location(object):
    def __init__(self, location_id, country, region, city,
                 postal_code, lat, lon, metro_code, area_code):
        self.location_id = location_id
        self.country = country
        self.region = region
        self.city = city
        self.postal_code = postal_code
        self.lat = lat
        self.lon = lon
        self.metro_code = metro_code
        self.area_code = area_code

    def __repr__(self):
        return ('Location(location_id={!r}, region={!r}, city={!r}, '
                'postal_code={!r}, lat={!r}, lon={!r})'.format(
            self.location_id, self.region, self.city,
            self.postal_code, self.lat, self.lon))

def get_locations_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            yield Location(*row)

def filter_locations(locations, city_name):
    for loc in locations:
        if loc.city == city_name:
            yield loc

def print_locations(locations):
    for loc in locations:
        print(loc.lat, loc.lon)

def main():
    locations = get_locations_from_file('locations.csv')
    filtered_locations = filter_locations(locations, 'Brussels')
    print_locations(filtered_locations)


if __name__ == '__main__':
    main()