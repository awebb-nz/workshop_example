import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

sns.set(style="white")


print('Made some changes to this! / TH')

# absolute path till parent folder
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[: len(path_array) - 1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i


# path to clean data
clean_data_path = homefolder_path + "cleaned_autos.csv"

# reading csv into raw dataframe
df = pd.read_csv(clean_data_path, encoding="latin-1")


# ## Average price of vehicle by fuel type and gearbox type


# barplot for price based on fuel type and gearbox type
fig, ax = plt.subplots(figsize=(8, 5))
colors = ["#00e600", "#ff8c1a", "#a180cc"]
sns.barplot(x="fuelType", y="price", hue="gearbox", palette="husl", data=df)
ax.set_title("Average price of vehicles by fuel type and gearbox type")
plt.show()


# saving the plot
fig.savefig((abs_path + "/vehicletype-fueltype-price.png"))


# ## Average power of a vehicle by vehicle type and gearbox type


# barplot for price based on fuel type and gearbox type
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
fig, ax = plt.subplots(figsize=(8, 5))
sns.set_palette(sns.xkcd_palette(colors))
sns.barplot(x="vehicleType", y="powerPS", hue="gearbox", data=df)
ax.set_title("Average price of vehicles by fuel type and gearbox type")
plt.show()


# saving the plot
fig.savefig((abs_path + "/vehicletype-fueltype-power.png"))
