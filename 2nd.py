global_combined_fuel_total_for_modules = 0


def mass(value):
	fuel = ((value // 3) - 2)
#	print (fuel)
	global global_combined_fuel_total_for_modules
	global_combined_fuel_total_for_modules += fuel
	fuel4fuel(fuel)

with open('values.txt', "r") as f:
	for massvalue in f:
		mass(massvalue)
