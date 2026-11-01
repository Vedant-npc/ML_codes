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

print("Hello World")

a = 10
b = 20

print("Addition:", a + b)
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
