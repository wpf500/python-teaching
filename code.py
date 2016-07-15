import csv, math

city_locations = {
	'Raqqa': {'lat': 35.959411, 'lon': 38.998105},
	'Kobani': {'lat': 36.890343, 'lon': 38.350011},
	'Hasakah': {'lat': 36.511304, 'lon': 40.743107},
	'Dayr Az Zawr': {'lat': 35.329652, 'lon': 40.135034}
}

raids = list(csv.DictReader(open('data.csv')))

def get_raid(n):
	return raids[n - 1]

def get_raid_field(raid, field):
	return raid[field]

def get_raid_location(raid):
	return {'lat': raid['lat'], 'lon': raid['lon']}

def get_city_location(city):
	return city_locations[city]

def get_distance(location1, location2):
	d = 0
	R = 6371e3 # metres
	loc1_lat = math.radians(float(location1['lat']))
	loc2_lat = math.radians(float(location2['lat']))
	lat_d = math.radians(float(location2['lat'])-float(location1['lat']))
	lon_d = math.radians(float(location2['lon'])-float(location1['lon']))

	a1 = math.sin(lat_d/2) * math.sin(lat_d/2)
	a2 = math.cos(loc1_lat) * math.cos(loc2_lat) * math.sin(lon_d/2) * math.sin(lon_d/2)
	a = a1 + a2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

	d = R * c;
	return d

def get_raids():
	return raids
