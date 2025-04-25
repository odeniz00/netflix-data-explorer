import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("netflix_data.csv")

# Display basic information
print("First 5 entries:")
print(df.head())
print("\nData summary:")
print(df.describe(include="all"))

# Count shows vs movies
type_counts = df["Type"].value_counts()
print("\nType Counts:")
print(type_counts)

# Plot type counts
type_counts.plot(kind="bar", title="Content Types on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
