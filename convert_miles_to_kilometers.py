def convert_distance(miles):
	km = miles * 1.6
	return km

my_trip_miles = 55
my_trip_km = 1.6*(my_trip_miles)

print("The distance in kilometers is " + str(my_trip_km))
# Should print The distance in kilometers is 88.0

print("The round-trip in kilometers is " + str(my_trip_km*2))
# Should print The round-trip in kilometers is 176.0
