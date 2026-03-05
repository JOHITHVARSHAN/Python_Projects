#Weather data plotter (WDP)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Df = pd.DataFrame(pd.read_csv(r"Data\weather_data.csv"))
print(Df.columns)
df = Df.head(20)

plt.title("1. Temperature V/S Precipitation")
plt.scatter(df["Temperature_C"], df["Precipitation_mm"])
plt.xlabel("Temperature")
plt.ylabel("Precipitation")
plt.show()

plt.title("2.Temperature V/S Humidity")
plt.scatter(df["Temperature_C"], df["Humidity_pct"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.show()

plt.title("3. Temperature V/S Wind Speed")
plt.scatter(df["Temperature_C"], df["Wind_Speed_kmh"])
plt.xlabel("Temperature")
plt.ylabel("Wind Speed")
plt.show()

plt.title("4. Temperature V/S Humidity")
plt.scatter(df["Temperature_C"], df["Humidity_pct"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.show()

plt.title("4. Percipitation V/S Wind Speed")
plt.scatter(df["Precipitation_mm"], df["Wind_Speed_kmh"])
plt.xlabel("Temperature")
plt.ylabel("Wind Speed")
plt.show()

plt.title("5. Humidity V/S Wind Speed")
plt.scatter(df["Humidity_pct"], df["Wind_Speed_kmh"])
plt.xlabel("Humidity")
plt.ylabel("Wind Speed")
plt.show()