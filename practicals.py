# Add your lab practicals to this file.
#
# Each entry uses:
# practical number: {
#     "title": "Practical title",
#     "description": "Optional short description",
#     "code": "Python code here"
# }

PRACTICALS = {
    1: {
        "title": "Python Basics",
        "description": "Sample practical. Replace this with your actual lab practical.",
        "code": """# Practical 1: Python Basics

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


df = pd.read_csv(r"Enter path")


print("Original Dataset:")
print(df.head())


print("\nMissing Values Before Preprocessing:")
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


encoder = LabelEncoder()
df["Sex"] = encoder.fit_transform(df["Sex"])
df["Embarked"] = encoder.fit_transform(df["Embarked"])


scaler = StandardScaler()
df["Age"] = scaler.fit_transform(df[["Age"]])


print("\nProcessed Dataset:")
print(df.head())


print("\nMissing Values After Preprocessing:")
print(df[["Age", "Embarked"]].isnull().sum())
""",
    },
    2: {
        "title": "NumPy Operations",
        "description": "Sample practical. Replace this with your actual lab practical.",
        "code": """# Practical 2: NumPy Operations

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
""",
    },
    3: {
        "title": "Data Visualization",
        "description": "Sample practical. Replace this with your actual lab practical.",
        "code": """# Practical 3: Data Visualization

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")
plt.show()
""",
    },
}
