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
