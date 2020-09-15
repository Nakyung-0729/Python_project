# display title
print("Miles Per Gallon (MPG) program")
print()

# Values
miles_driven = 150
gallons_used = 15
cost_per_gallon = 3

# calculate and round miles per gallon
miles_per_gallon = miles_driven / gallons_used
total_gas_cost = gallons_used * cost_per_gallon
cost_per_mile = cost_per_gallon / miles_per_gallon

# rounded to one decimal
total_gas_cost = round(45.0, 1)

# display the result
print()
print("Enter miles driven:        ", miles_driven)
print("Enter gallons of gas used: ", gallons_used)
print("Enter cost_per_gallon:     ", cost_per_gallon)
print('=====================')
print("Miles per gallon: ", miles_per_gallon)
print("Total gas cost:   ", total_gas_cost)
print("Cost_per_mile:    ", cost_per_mile)
print()


