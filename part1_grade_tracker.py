###Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Loop through each student
for student in raw_students:

    #  Clean name
    clean_name = student["name"].strip().title()

    #  Convert roll to integer
    roll = int(student["roll"])

    #  Convert marks string to list of integers
    marks = [int(m) for m in student["marks_str"].split(", ")]

    #  Validate name (only alphabets)
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)

    if is_valid:
        print(f"{clean_name} → ✓ Valid name")
    else:
        print(f"{clean_name} → ✗ Invalid name")

    # Print formatted profile
    print("=" * 32)
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

    # Special condition for roll 103
    if roll == 103:
        print("\nSpecial Output:")
        print(clean_name.upper())
        print(clean_name.lower())

###Task 2 — Marks Analysis Using Loops & Conditionals
##Print Subject + Grade (using for loop)

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nGrade Report for {student_name}\n")

# Loop through subjects and marks
for i in range(len(subjects)):
    subject = subjects[i]
    score = marks[i]

    # Grade logic
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject}: {score} → {grade}")

##Calculations
# Total
total = sum(marks)

# Average
average = round(total / len(marks), 2)

# Highest
max_marks = max(marks)
max_index = marks.index(max_marks)
top_subject = subjects[max_index]

# Lowest
min_marks = min(marks)
min_index = marks.index(min_marks)
low_subject = subjects[min_index]

print("\nSummary:")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest: {top_subject} ({max_marks})")
print(f"Lowest: {low_subject} ({min_marks})")

#While Loop
new_count = 0

while True:
    subject = input("\nEnter subject name (or type 'done' to stop): ")

    if subject.lower() == "done":
        break

    marks_input = input("Enter marks (0-100): ")

    # Validate marks
    if not marks_input.isdigit():
        print("⚠ Invalid input! Please enter a number.")
        continue

    marks_value = int(marks_input)

    if marks_value < 0 or marks_value > 100:
        print("⚠ Marks should be between 0 and 100.")
        continue

    # Add valid data
    subjects.append(subject)
    marks.append(marks_value)
    new_count += 1

###Task 3 — Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nClass Performance Report")
print("-" * 40)
print(f"{'Name':<18} | {'Average':<7} | Status")
print("-" * 40)

pass_count = 0
fail_count = 0
total_avg_sum = 0

topper_name = ""
topper_avg = 0

for student in class_data:
    name = student[0]
    marks = student[1]

    avg = round(sum(marks) / len(marks), 2)
    total_avg_sum += avg

    ## Pass/Fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    ## Check topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    ## Print row
    print(f"{name:<18} | {avg:<7} | {status}")

## Class average
class_avg = round(total_avg_sum / len(class_data), 2)

print("-" * 40)
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Topper: {topper_name} ({topper_avg})")
print(f"Class Average: {class_avg}")

###Task 4 — String Manipulation Utility
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

## 1. Strip whitespace
clean_essay = essay.strip()
print("\n1. Clean Essay:")
print(clean_essay)

## 2. Convert to Title Case
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)

## 3. Count "python"
count_python = clean_essay.count("python")
print("\n3. Count of 'python':")
print(count_python)

## 4. Replace "python" with "Python 🐍"
replaced_text = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Text:")
print(replaced_text)

## 5. Split into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentences List:")
print(sentences)

## 6. Print numbered sentences
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]

    # Add period if missing
    if not sentence.endswith("."):
        sentence += "."

    print(f"{i+1}. {sentence}")



