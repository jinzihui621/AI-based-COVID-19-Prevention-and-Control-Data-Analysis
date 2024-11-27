import pandas as pd
import matplotlib.pyplot as plt

# Load the result1.csv file
result1_df = pd.read_csv("result2.csv")
# Location Analysis: Frequency of close contacts at different locations
location_analysis = result1_df['次密接场所ID'].value_counts().head(10)  # Top 10 locations
# Plotting the top 10 locations with most close contacts
plt.figure(figsize=(12, 6))
location_analysis.plot(kind='bar')
plt.title('Top 10 Locations with Secondary Contact')
plt.xlabel('Location ID')
plt.ylabel('Number of Close Contacts')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()