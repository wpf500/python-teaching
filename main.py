from code import *

# basic variables, ints, strings
n = 2
name = 'Will'

# Basic stuff: everything is case sensitive, syntax errors, etc.

print 'Hello' + name
# change name, what happens?

# talk about functions, input parameters, output (need slides here)

row2 = get_row(2)
rown = get_row(n)
# the same thing (variables instead of literals)

print get_field(row2, 'city')

row2_date = get_field(row2, 'date')
# introduce if statements, offside rule, else clauses
if row2_date == '2016-06-08':
	print 'Yes'
else:
	print 'No'

# how about multiple conditions?

raqqa_location = get_city_location('Raqqa')
row2_location = get_row_location(row2)
distance2 = get_distance(raqqa_location, row2_location)
if distance2 < 50000:
	print 'Close'
else:
	print 'Far'

row4 = get_row(4)
kobani_location = get_city_location('Kobani')
row4_location = get_row_location(row4)
distance4 = get_distance(kobani_location, row4_location)

# isn't this a lot of typing? mantra: if you're doing something repetitive
# on a computer you're doing it wrong

# how about creating a method
def is_row_near(row, city):
	location1 = get_row_location(row)
	location2 = get_city_location(city)
	distance = get_distance(location1, location2)
	# possibly introduce return distance < 50? probably not
	if distance < 50:
		return True
	else:
		return False

# possible extension: is_row_near takes distance threshold?

close2 = is_row_near(row2, 'Raqqa')
if close2:
	print 'Near Raqqa'
else:
	print 'Not near Raqqa'

close4 = is_row_near(row4, 'Kobani')
if close4:
	print 'Near Kobani'
else:
	print 'Not near Kobani'

# still typing too much. repeat mantra
# how about a method which does it all?
def print_is_row_near(row, city):
	if is_row_near(row, city):
		print 'Near ' + city
	else:
		print 'Not near ' + city

print_is_row_near(row2, 'Raqqa')
print_is_row_near(row4, 'Kobani')

# how about is row2 near Kobani?
# stress advantage of programming: variables, etc. allow you to change the outcome
# of the program with very few changes.

# introduce lists
rows = get_rows()

row2 = rows[1] # 0-based!!!
row4 = rows[3]

# that's great, but how is that any better than what we had before?
# going through all rows, introduce loops
for row in rows:
	print_is_row_near(row, 'Raqaa')
	# stuff here

# clearly doing something, but not very useful
# basic aggregation, initialise variable then add one on each occurence

# how many strikes are near Raqqa?
near_raqqa = 0
for row in rows:
	close = is_row_near(row, 'Raqqa')
	if close:
		near_raqqa = near_raqqa + 1 # near_raqqa += 1

print 'Rows near Raqqa: ' + near_raqqa

# lots of possible extras here
