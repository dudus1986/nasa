import math

# Works out the fuel required for the mass passed to it
def massfuel(massentry):
    #constant divide value for 
    dividevalue = 3
    #converting the mass number from the text file into a integer
    massnumber = int(massentry)
    #Phase 1 - Divide the mass by the constant divide value off 3
    phase1 = massnumber / dividevalue
    #Phase 2 - Always round the value down
    phase2 = math.floor(phase1)
    #Phase 3 - Subtract the two
    phase3 = phase2 - 2
    #return the phase3 value to whatever function has called it
    return phase3

# Works out the fuel required for fuel needed for the initial craft mass
def fuelforfuel(fuel):
    # Creating new array to store the results in
    fuelarray2 = []
    fuelnumber = int(fuel)
    # While loop takes the fuel value passed to it and runs the loop whilst greater than 0
    while fuelnumber > 0:
        # Calls the function that carries out the calculation and takes the returned value and stores it in 'returnedvalue'
        returnedvalue = massfuel(fuelnumber)
        # If statement checks if the value returned is positive. If no then move on
        if returnedvalue > 0:
        # Adds the value to the end of the array.
            fuelarray2.append(returnedvalue)
        # uses the new value as the next input value
            fuelnumber = returnedvalue
        else:
            break
    sumoffuel = sum(fuelarray2)
    return sumoffuel

# Opens the txt file that is in the same directory as the code file
with open('values.txt', "r") as f:
    # Creating array to store the returned values in from massfuel() function
    fuelarrayformass = []
    fuelarrayforfuel = []
    # For loop to run through the txt file. It calls the massfuel function and passes the mass value across. Then the function passes the calculation value back. 
    # That value is then stored in the array
    for mass in f:
        #calls initial mass calcualtion and stores result. Not really needed, but there to just save the fuel needed for the mass
        fuelarrayformass.append(massfuel(mass))
        # Calls function that calculates the fuel needed for the mass and the fuel needed for the fuel then moves onto the next mass
        fuelarrayforfuel.append(fuelforfuel(mass))
        
# Adds up the fuel required for just the mass
fuelformass = sum(fuelarrayformass)
# Adds up the fuel required for the mass and the extra fuel
fuelforfuelfigure = sum(fuelarrayforfuel)
#The value is then printed onto the terminal
print(f'The fuel required for the mass of the craft is: {fuelformass}') 
print(f'The TOTAL required for the the craft is: {fuelforfuelfigure}')  