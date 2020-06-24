def mass(value):
	fuel = ((value // 3) - 2)
#	print (fuel)
	global global_combined_fuel_total_for_modules
	global_combined_fuel_total_for_modules += fuel
	fuel4fuel(fuel)




# Opens the txt file that is in the same directory as the code file
with open('values.txt', "r") as f:
    # For loop to run through the txt file. It calls the massfuel function and passes the mass value across. Then the function passes the calculation value back. 
    # That value is then stored in the array
    for mass in f: