import os
import pandas as pd
# import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "pandas_exercise.xlsx")

df = pd.read_excel(file_path)

# older_than_25 = df[df["age"] > 25]

# sorted_by_score = df.sort_values(by="score", ascending=False)

# multiple_sorted = df[(df["score"] > 85) & (df["age"] < 30)]

# df["full_name"] = df["first_name"] + " " + df["last_name"]

# df["passed"] = df["score"] >= 85

# df.to_excel("pandas_modified.xlsx", index=False)

# plt.figure(figsize=(8, 5))
# plt.bar(df["first_name"], df["score"], color="skyblue")
# plt.title("Score by First Name")
# plt.xlabel("First Name")
# plt.ylabel("Score")
# plt.tight_layout()
# plt.show()

# df_sorted = df.sort_values(by="age")

# plt.plot(df_sorted["age"], df_sorted["score"], marker="o")
# plt.title("Score by Age")
# plt.xlabel("Age")
# plt.ylabel("Score")
# plt.grid(True)
# plt.show()

# df["passed"] = df["score"] >= 85
# passed_counts = df["passed"].value_counts()

# plt.pie(passed_counts, labels=["Passed", "Failed"], autopct="%1.1f%%", colors=["lightgreen", "lightcoral"])
# plt.title("Pass/Fail Rate")
# plt.show()

