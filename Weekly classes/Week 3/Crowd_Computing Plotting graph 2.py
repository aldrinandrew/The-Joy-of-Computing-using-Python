"""

"""

import matplotlib.pyplot as plt
import statistics

Estimates = [50, 25, 27, 38, 63, 92, 15, 7, 3, 56, 42, 38, 35, 55, 51, 60, 75, 99, 70, 80, 89, 76, 60, 44, 42, 43, 51,
             53, 56, 60, 61, 75, 10, 44, 43, 40, 60, 40, 56]

y = []


Estimates.sort()
trim_value = int(0.1*(len(Estimates)))
Estimates = Estimates[trim_value:]
Estimates = Estimates[:len(Estimates)-trim_value]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates, y,'r--')
plt.plot([50],[5],'g^')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.show()
