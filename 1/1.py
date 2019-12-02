# https://adventofcode.com/2019/day/1

import math

def measure_module_fuel(mass: int) -> int:
    additional_fuel_mass = math.floor(mass/3) - 2
    if additional_fuel_mass <= 0:
        return 0
    return additional_fuel_mass + measure_module_fuel(additional_fuel_mass)

def calculate_total_fuel():
    f = open("input.txt", "r")
    total_fuel = 0
    for m in f:
      total_fuel += measure_module_fuel(int(m))  
    return total_fuel

print(calculate_total_fuel())
