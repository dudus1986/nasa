
# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, 
# take its mass, divide by three, round down, and subtract 2.

global_combined_fuel_total_for_modules = 0
global_extra_fuel = 0

def fuel4fuel(x):
	extrafuel = ((x // 3) - 2)
	if extrafuel >= 0:
		global global_extra_fuel
		global_extra_fuel += extrafuel
		fuel4fuel(extrafuel)
	else:
		global_extra_fuel += 0


	



def mass(value):
	fuel = ((value // 3) - 2)
#	print (fuel)
	global global_combined_fuel_total_for_modules
	global_combined_fuel_total_for_modules += fuel
	fuel4fuel(fuel)
	





# mass(12)
# mass(14)
# mass(1969)
# mass(100756)

mass(	66910	)
mass(	78957	)
mass(	58510	)
mass(	142350	)
mass(	105820	)
mass(	87317	)
mass(	100743	)
mass(	51390	)
mass(	92804	)
mass(	80752	)
mass(	70169	)
mass(	111892	)
mass(	104715	)
mass(	143166	)
mass(	126158	)
mass(	78712	)
mass(	139223	)
mass(	133863	)
mass(	85912	)
mass(	53883	)
mass(	64812	)
mass(	102254	)
mass(	52482	)
mass(	91855	)
mass(	117520	)
mass(	140253	)
mass(	76706	)
mass(	106693	)
mass(	57948	)
mass(	57578	)
mass(	115640	)
mass(	131273	)
mass(	115373	)
mass(	145219	)
mass(	100889	)
mass(	106447	)
mass(	72347	)
mass(	120250	)
mass(	56898	)
mass(	146689	)
mass(	138246	)
mass(	85068	)
mass(	55292	)
mass(	124814	)
mass(	136750	)
mass(	51820	)
mass(	70396	)
mass(	92806	)
mass(	86093	)
mass(	70467	)
mass(	122356	)
mass(	148530	)
mass(	85569	)
mass(	100492	)
mass(	87062	)
mass(	123225	)
mass(	73872	)
mass(	102104	)
mass(	91194	)
mass(	95077	)
mass(	88352	)
mass(	114906	)
mass(	141056	)
mass(	87220	)
mass(	106517	)
mass(	88867	)
mass(	95883	)
mass(	130158	)
mass(	76702	)
mass(	134241	)
mass(	50561	)
mass(	119258	)
mass(	61669	)
mass(	140396	)
mass(	145201	)
mass(	76914	)
mass(	102281	)
mass(	56618	)
mass(	145968	)
mass(	99542	)
mass(	116789	)
mass(	135633	)
mass(	114646	)
mass(	84253	)
mass(	50650	)
mass(	69127	)
mass(	95446	)
mass(	55357	)
mass(	81180	)
mass(	126940	)
mass(	133743	)
mass(	52261	)
mass(	117429	)
mass(	82291	)
mass(	110373	)
mass(	67626	)
mass(	58014	)
mass(	125342	)
mass(	129508	)
mass(	96332	)

print "Combined amount of fuel needed for the modules is shown below"
print (global_combined_fuel_total_for_modules)
print "combined amount fuel needed for the extra fuel is below"
print (global_extra_fuel)
print 'total fuel needed is'
print (global_combined_fuel_total_for_modules) + (global_extra_fuel)
print ("correct answer is 4896221")