import numpy as np

temperatures = np.loadtxt('CAN.csv', delimiter=',', skiprows=1)

print(temperatures)
print(temperatures.shape)

print(type(temperatures.shape))
print('Number of rows in temperatures:', temperatures.shape[0])

print('The first row', temperatures[0])
print('The first year:', temperatures[0, 0])

print('All years:', temperatures[0:, 0])
print(temperatures[0:5, 0])
print(temperatures[:5, 0])

np.max(temperatures)

max_temp = np.max(temperatures[:, 1])
min_temp = np.min(temperatures[:, 1])

print('Lowest average temperature in Canada over last 111 years was:',
        min_temp)
print('Highest average temperature in Canada over last 111 years was:',
        max_temp)

min_year = np.where(temperatures[:, 1] == min_temp)
print(min_year)

min_year_index = min_year[0]
print(min_year_index)

min_year_index = min_year_index[0]
print(min_year_index)

print('Lowest average temperature was in:', temperatures[min_year_index])

