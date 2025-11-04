'''🎯 Day 4 Goal
Learn to visualize and analyze data using:
📊 Matplotlib (Intermediate)
🎨 Seaborn (Advanced styling)
📈 Real dataset insights'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Student dataset
data = {
    "Name": ["Pradip", "Sandip", "Ankit", "Amit", "Anil", "Sunil", "Ayush", "Arbind"],
    "Math": [85, 67, 56, 92, 70, 60, 88, 75],
    "Science": [90, 78, 70, 95, 82, 68, 85, 80],
    "English": [88, 72, 65, 91, 78, 69, 83, 77],
    "Gender": ["M", "M", "M", "M", "M", "M", "M", "M"],
}
df = pd.DataFrame(data)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print(df)

plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Math"], marker='o', label="Math")
plt.plot(df["Name"], df["Science"], marker='s', label="Science")
plt.plot(df["Name"], df["English"], marker='^', label="English")
plt.title("Subject-wise Marks per Student")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"], color="green")
plt.title("Average Marks per Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Subject Correlation Heatmap")
plt.show()

plt.figure(figsize=(7,4))
sns.boxplot(data=df[["Math","Science","English"]])
plt.title("Subject Marks Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df["Average"], kde=True, color="purple")
plt.title("Distribution of Average Marks")
plt.show()
