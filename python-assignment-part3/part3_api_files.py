
### Task 1: File Read & Write Basics

# writing initial notes to file
# appending additional topics
# searching keyword in file

## Part A: Write 

# Writing to file
with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

# Appending to file
with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: Modules organize code into files.\n")

print("Lines appended successfully.")


##Part B: Read

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("\nReading file:\n")

# Print numbered lines
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# Count total lines
print(f"\nTotal number of lines: {len(lines)}")

# Keyword search
keyword = input("\nEnter a keyword to search: ").lower()

found = False

print("\nMatching lines:")
for line in lines:



    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")
