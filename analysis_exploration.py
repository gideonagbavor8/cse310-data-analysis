
# import pandas as pd

# df = pd.read_csv(r"D:\CSE310\outstanding_schools_2025.csv")

# # Remove rows without a school name
# df = df.dropna(subset=["School Name"])

# print("Rows after cleaning:", len(df))
# print("\nRegions:")
# print(df["Region"].value_counts())


import pandas as pd

df = pd.read_csv(r"D:\CSE310\outstanding_schools_2025.csv")

# Remove rows without a school name
df = df.dropna(subset=["School Name"])

# Select schools in Volta Region
volta = df[df["Region"] == "Volta"]

print("Volta Region schools:", len(volta))
print("\nSchool types:")
print(volta["School Type"].value_counts())

print("\nSchool status:")
print(volta["Status"].value_counts())


basic = volta[volta["School Type"] == "basic"]

print(basic[["District", "School Name", "Status"]].to_string(index=False))