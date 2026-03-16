"""
Your are provided with a CSV file containing student assessment data, where each record includes scores (out of 100) for three programming subjects PF, OOP, DSA.
Considering a score 0f 40 or higher as a passing grade, you have to write a python program that load this data into suitable data structure, computes the number and percentage of students who passed and failed in each subject, and finally visualizes the pass/fail statistics using a grouped/multi bar chart for clear comparison accross all three subjects.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
data = pd.DataFrame({
    "PF":[78,35,67,23,93],
    "OOP":[16,32,78,96,66],
    "DSA":[89,14,66,16,89]
})

# Step 2: Define subjects
subjects = ["PF", "OOP", "DSA"]

pass_count = []
fail_count = []
pass_percent = []
fail_percent = []

total_students = len(data)

# Step 3: Calculate pass/fail statistics
for sub in subjects:
    passed = (data[sub] >= 40).sum()
    failed = (data[sub] < 40).sum()

    pass_count.append(passed)
    fail_count.append(failed)

    pass_percent.append((passed / total_students) * 100)
    fail_percent.append((failed / total_students) * 100)

# Print results
for i in range(len(subjects)):
    print(subjects[i])
    print("Passed:", pass_count[i], f"({pass_percent[i]:.2f}%)")
    print("Failed:", fail_count[i], f"({fail_percent[i]:.2f}%)")
    print()

# Step 4: Plot grouped bar chart
x = range(len(subjects))

plt.bar(x, pass_count, width=0.4, label="Pass")
plt.bar([i + 0.4 for i in x], fail_count, width=0.4, label="Fail")

plt.xticks([i + 0.2 for i in x], subjects)
plt.xlabel("Subjects")
plt.ylabel("Number of Students")
plt.title("Pass/Fail Statistics")
plt.legend()

plt.show()


    