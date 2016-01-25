import requests
import numpy as np
import matplotlib.pyplot as plt

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv"
print('Getting the data from:', url)
resp = requests.get(url)
rows = resp.text.split('\n')
temperatures = np.loadtxt(rows, delimiter=',', skiprows=1)

fig, ax = plt.subplots()
ax.plot(temperatures[:, 0], temperatures[:, 1])
ax.set_title('Average temperatures in Canada from 1901 to 2009')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature in C')
ax.set_xlim([1901, 2009])

url_hrv = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/HRV.csv"
resp_hrv = requests.get(url_hrv)
temperatures_hrv = np.loadtxt(resp_hrv.text.split('\n'), delimiter=',', skiprows=1)

url_deu = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/DEU.csv"
resp_deu = requests.get(url_deu)
temperatures_deu = np.loadtxt(resp_deu.text.split('\n'), delimiter=',', skiprows=1)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(temperatures_hrv[:, 0], temperatures_hrv[:, 1], label='HRV', color='r', linewidth=2)
ax.plot(temperatures_deu[:, 0], temperatures_deu[:, 1], label='DEU', color='b', linewidth=2)
ax.set_title('Average temperatures from 1901 to 2009')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature in C')
ax.set_xlim([1901, 2009])

plt.legend(loc='best')
plt.grid('on')

plt.savefig('temperatures_hrv_deu.pdf')
plt.show()
