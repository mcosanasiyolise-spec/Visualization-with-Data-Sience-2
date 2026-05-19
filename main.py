import matplotlib.pyplot as plt

Year = [1920,1930,1940,1950,1960,1970,1980,1990.20000,2010]
Unemployment_Rate =[9.8,12,8,7,6.9,7,6.5,6.2,5.5,6.3]

plt.plot(Year, Unemployment_Rate, color='red', marker='o')
plt.titel('Unployment Rate Vs Year', fontsize=14)
plt.xlable('Year', fontsize=14)
plt.ylable('Unploymen Rate', fontsize=14)
plt.grid(True)
plt.show