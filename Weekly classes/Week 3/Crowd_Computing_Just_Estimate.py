"""
Crowd_Computing (Wisdom of Crowd)

Experiment Details (Proposed by Francis Galton in Ox Weight Judging Competition)

Estimate the number of candies in the jar
Around 75 people participates
Actual number of gems = 375
Median = 300
Average of all estimates = 351 (10% Trimmed Mean_ Remove 10%smallest and 10% largest values from the sample)

"""
# For my convenience I am taking 40 value and expecting an average 50

from statistics import mean
from scipy import stats

Estimates = [50,25,27,38,63,92,15,7,3,56,42,38,35,55,51,60,75,99,70,80,89,76,44,60,44,42,43,51,53,56,60,61,75,10,44,43,40,60,40,56]

Estimates.sort()  #Sorted in ascending order

m = stats.trim_mean(Estimates,0.1)   # Using scipy library
print(m)

"""
Or

trim_value=int(0.1*len(Estimates))
Estimates=Estimates[trim_value:]   #Trimmed the smallest 10% value
Estimates=Estimates[:len(Estimates)-trim_value]    #Trimmed the largest 10% value

print(mean(Estimates))


"""
