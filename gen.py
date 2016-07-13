import math, random, csv
from datetime import timedelta, datetime

locations = [
	{'name': 'Kobani', 'location': [36.890343, 38.350011]},
	{'name': 'Hasakah', 'location': [36.511304, 40.743107]},
	{'name': 'Raqqa', 'location': [35.959411, 38.998105]},
	{'name': 'Deir', 'location': [35.329652, 40.135034]}
]

lat_step = 0.00338396
lon_step = 0.00338396

print lat_step, lon_step

start = datetime(2016, 1, 1)
end = datetime(2016, 7, 1)

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def get_distance(lat1, lon1, lat2, lon2):
	d = 0
	R = 6371e3 # metres
	loc1_lat = math.radians(lat1)
	loc2_lat = math.radians(lat2)
	lat_d = math.radians(lat2-lat1)
	lon_d = math.radians(lon2-lon1)

	a1 = math.sin(lat_d/2) * math.sin(lat_d/2)
	a2 = math.cos(loc1_lat) * math.cos(loc2_lat) * math.sin(lon_d/2) * math.sin(lon_d/2)
	a = a1 + a2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

	d = R * c;
	return d

w = csv.writer(open('data.csv', 'w'))
w.writerow(['date','strikes','lat','lon'])

for i in xrange(5000):
	loc = random.choice(locations)
	lat_n = random.random() * 400 - 200
	lon_n = random.random() * 400 - 200
	lat = loc['location'][0] + lat_step * lat_n
	lon = loc['location'][1] + lon_step * lon_n
	date = random_date(start, end).strftime('%Y-%m-%d')
	strikes = random.randint(1, 8)
	w.writerow([date, strikes, lat, lon])