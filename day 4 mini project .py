import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📚 Dataset
data = {
    "Name": ["Pradip","Sandip","Ankit","Amit","Anil","Sunil","Ayush","Arbind"],
    "Math": [85,67,56,92,70,60,88,75],
    "Science": [90,78,70,95,82,68,85,80],
    "English": [88,72,65,91,78,69,83,77]
}
df = pd.DataFrame(data)

df["Average"] = df[["Math","Science","English"]].mean(axis=1)

def grade(avg):
    if avg >= 85:  return "A"
    elif avg >= 70: return "B"
    elif avg >= 50: return "C"
    else:           return "Fail"

df["Grade"] = df["Average"].apply(grade)
print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"], color="skyblue", edgecolor="black")
plt.title("Average Marks per Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Math"], marker="o", label="Math")
plt.plot(df["Name"], df["Science"], marker="s", label="Science")
plt.plot(df["Name"], df["English"], marker="^", label="English")
plt.title("Subject-wise Performance")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df[["Math","Science","English"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Subject Correlation Heatmap")
plt.show()

plt.figure(figsize=(7,4))
sns.boxplot(data=df[["Math","Science","English"]])
plt.title("Marks Distribution per Subject")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df["Average"], kde=True, color="purple")
plt.title("Average Marks Distribution")
plt.show()
