from funct import *
import timeit

filter_and_write_csv("household_power_consumption.txt")
print (timeit.timeit(frame, number =1))
print (timeit.timeit(array, number =1))
