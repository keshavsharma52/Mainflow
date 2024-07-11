import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('householdtask3.csv')
year = df['year']
income = df['income']
fig, ax = plt.subplots()
ax.bar(year, income)
ax.set_title('Bar Chart Example')
ax.set_xlabel('year')
ax.set_ylabel('income')
ax.legend([income],loc='upper left', bbox_to_anchor=(0.5,1),title='Legend')
plt.show()
