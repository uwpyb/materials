import requests
import numpy as np

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv"
print('Getting the data from:', url)
resp = requests.get(url)

print("Response from the website (200 is OK):", resp.status_code)

print("First few lines of data:")
print(resp.text[:100])

rows = resp.text.split('\n')
rows[:5]

temperatures = np.loadtxt(rows, delimiter=',', skiprows=1)
print('Number of rows in temperatures:', temperatures.shape[0])

max_temp = np.max(temperatures[:, 1])
min_temp = np.min(temperatures[:, 1])

print('Lowest yearly average temperature in Canada over the last 111 years was:', min_temp)
print('Highest yearly average temperature in Canada over the last 111 years was:', max_temp)

min_year = np.where(temperatures[:, 1] == min_temp)
max_year = np.where(temperatures[:, 1] == max_temp)

min_year_index = min_year[0]
min_year_index = min_year_index[0]
print('Lowest average temperature was in:', temperatures[min_year_index])

max_year_index = max_year[0]
max_year_index = max_year_index[0]
print('Highest average temperature was in:', temperatures[max_year_index])
