"""
    Program: MonteCarlo.py
    Author: Aghared Alyousif
    Last date modified: 2/24/19

    Write Python program that approximates pi using the Monte Carlo method.
    Get at least the 1st 5 decimals correct i.e. 3.14159
"""

import random
import time
import math

# pi = 3.14159
# time.time() is function which gives us the time from 1970 until the time its execute
# so we can get the starting time point
start = time.time()

sumNo_of_total = 0

# number of the random points
count = 10

# loop to repeat the whole code
for j in range(count):
    No_of_pointsInsteadCircle = 0
    approx_pi = 0.0
    Total = 0

    # to find approximates pi at least the 1st 5 decimals correct 3.14159
    while abs(approx_pi - math.pi) >= 0.000002653589793:
        Total += 1
        x = random.uniform(0, 1)  # to get random number for x point
        y = random.uniform(0, 1)  # to get random number for y point
        distance = float(x**2 + y**2)**(1/2)
        #  count number of points that are inside of the circle
        if float(distance) <= 1:
            No_of_pointsInsteadCircle += 1
        #  to find approximates pi using the Monte Carlo method
        approx_pi = float(4 * No_of_pointsInsteadCircle/Total)

    print("approximates pi", j+1, " = ", approx_pi)

    print("Total iteration", j+1, "= ", Total)
    #  sum of all No_of_round
    sumNo_of_total = sumNo_of_total + Total

# calculates the average iteration count
avg_of_iteration = sumNo_of_total / count
print("The average iteration count is ", avg_of_iteration)

#  to get the time when execution done
end = time.time()

#  calculate run time
runTime = end - start

#  print the total time
print("The total time = ", runTime, "Sec")

#  to find the average time in second
print("The average time = ", runTime/count, "Sec")

#  to find the average time in minutes
minutes = runTime/60/count
print("The average time = ", minutes, "M")
