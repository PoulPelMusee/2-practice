import numpy as np


well_dept = [56, 12, 66, 19, 32, 72, 27, 32]
size = len(well_dept)
well_dept = np.array(well_dept)

average = np.average(well_dept)
print(average)

t = np.power(well_dept - average, 2)
print(t)

t2 = t.sum()
print(t2)

sd_square = t2 / size
print(sd_square)

SD = np.sqrt(sd_square)
print(SD)
