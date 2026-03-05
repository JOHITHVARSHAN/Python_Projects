#Student Mark Analyzer (SMA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Admin\PROJECTS\AI_Projects\Python_Projects\Data\Marks.csv")
df = pd.DataFrame(data)
print(df.columns)
Avg_Marks = np.average(df["Marks"], axis=0)
print(f"Average marks is : {Avg_Marks}\n")

plt.title("Student Marks Analyzer")
plt.bar(df["Sub_Name"], df["Marks"])
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()