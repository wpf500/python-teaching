import csv, math

city_locations = {
	'Raqqa': {'lat': 35.959411, 'lon': 38.998105},
	'Kobani': {'lat': 36.890343, 'lon': 38.350011},
	'Hasakah': {'lat': 36.511304, 'lon': 40.743107},
	'Dayr Az Zawr': {'lat': 35.329652, 'lon': 40.135034}
}

rows = list(csv.DictReader(open('data.csv')))

def get_row(n):
	return rows[n - 1]

def get_row_field(row, field):
	return row[field]

def get_row_location(row):
	return {'lat': row['lat'], 'lon': row['lon']}

def get_city_location(city):
	return city_locations[city]

def get_distance(location1, location2):
	d = 0
	R = 6371e3 # metres
	loc1_lat = math.radians(location1['lat'])
	loc2_lat = math.radians(location2['lat'])
	lat_d = math.radians(location2['lat']-location1['lat'])
	lon_d = math.radians(location2['lon']-location1['lon'])

	a1 = math.sin(lat_d/2) * math.sin(lat_d/2)
	a2 = math.cos(loc1_lat) * math.cos(loc2_lat) * math.sin(lon_d/2) * math.sin(lon_d/2)
	a = a1 + a2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

	d = R * c;
	return d

def get_rows():
	return rows