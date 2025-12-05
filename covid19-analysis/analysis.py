import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.plot(df['date'], df['new_cases'])
plt.title("COVID-19 New Cases")
plt.show()
