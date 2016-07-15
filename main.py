from code import *

raid = get_raid(1)
print raid

l1 = get_raid_location(raid)
l2 = get_city_location('Raqqa')
print get_distance(l1, l2)

print get_raid_field(raid, 'strikes')
