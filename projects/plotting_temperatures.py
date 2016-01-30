import matplotlib.pyplot as plt
import numpy as np

temperatures = np.loadtxt('CAN.csv', delimiter=',', skiprows=1)

plt.figure()
plt.plot(temperatures[:, 0], temperatures[:, 1])
plt.title('Average temperatures in Canada from 1901 to 2009')
plt.xlabel('Year')
plt.ylabel('Temperature in C')
plt.xlim([1901, 2009])

temperatures_deu = np.loadtxt('DEU.csv', delimiter=',', skiprows=1)
temperatures_hrv = np.loadtxt('HRV.csv', delimiter=',', skiprows=1)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(temperatures_hrv[:, 0], temperatures_hrv[:, 1], label='HRV', color='r',
        linewidth=2)
ax.plot(temperatures_deu[:, 0], temperatures_deu[:, 1], label='DEU', color='b',
        linewidth=2)
ax.set_title('Average temperatures from 1901 to 2009')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature in C')
ax.set_xlim([1901, 2009])

plt.legend(loc='best')
plt.grid('on')
plt.savefig('temperatures_hrv_deu.pdf')


plt.show()


