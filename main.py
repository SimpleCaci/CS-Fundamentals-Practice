import os

base = "CS-Fundamentals-Practice"

folders = [
    "01_Python_Basics", "02_Data_Structures", "03_Strings_Files", "04_Functions_Recursion",
    "05_OOP", "06_Algorithms", "07_Intermediate_Python", "08_Leetcode_Practice",
    "09_CPP_Basics", "10_CPP_Pointers", "11_CPP_OOP", "12_CPP_STL",
    "13_CPP_Advanced", "14_CPP_FileIO", "15_Final_Project"
]

files_in_python_basics = [
    "challenge_1_intro.py",
    "challenge_2_type_conversion.py",
    "challenge_3_calc.py",
    "notes.md"
]

# Create base folder and subfolders
os.makedirs(base, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(base, folder), exist_ok=True)

# Create files inside 01_Python_Basics
for filename in files_in_python_basics:
    path = os.path.join(base, "01_Python_Basics", filename)
    open(path, "a").close()

# Create README.md at root
open(os.path.join(base, "README.md"), "a").close()

print("✅ Folder structure created successfully.")
