from code import *

# Was second air raid on 2016-05-04?
row2 = get_row(2)
row2_date = get_row_field(row2, 'date')
# ??? TODO

# If the second air raid was near Raqqa print 'Near Raqqa',
# otherwise print 'Not near Raqqa'
row2_location = get_row_location(row2)
raqqa_location = get_city_location('Raqqa')
distance = 0 # ??? TODO

# If the fifth strike was near Kobani print 'Near Kobani'
# otherwise print 'Not near Kobani'
row5 = get_row(5)
# ??? TODO

# Can you see repetition here?
# Remember: if you are doing somethin competitive on a computer
#           you're doing it wrong
# Can you create a function which takes a row and a city and tells
# you if its nearby?
def is_row_near(row, city):
	# ??? TODO
	return False

# Uncomment to test is_row_near
#if is_row_near(row2, 'Raqqa'):
#	print 'Near Raqqa'
#else:
#	print 'Not near Raqqa'