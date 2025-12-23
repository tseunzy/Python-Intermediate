

print("==========List & Dictionary Comprehension===========")

# List Comprehensions [expression for item in iterable]

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"squares: {squares}")  # [1, 4, 9, 16, 25]

# Convert strings to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"uppercase: {uppercase}")  # ['HELLO', 'WORLD', 'PYTHON']

# Extract first letters
first_letters = [word[0] for word in words]
print(f"first letters: {first_letters}")  # ['h', 'w', 'p']

# Create list of lengths
lengths = [len(word) for word in words]
print(f"lengths: {lengths}")  # [5, 5, 6]


print("==========Examples===========")
# (without comprehension)
squares_w = []
for x in range(1, 6):
    squares_w.append(x**2)

# List comprehension 
squares_comp = [x**2 for x in range(1, 6)]

# Filter strings longer than 4 characters
words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = [word for word in words if len(word) > 4]
print(f"long words: {long_words}")  # ['apple', 'banana', 'elephant']


# Numbers that are even AND greater than 5
numbers = range(1, 21)
result = [n for n in numbers if n % 2 == 0 and n > 5]
print(f"Even numbers > 5: {result}")  # [6, 8, 10, 12, 14, 16, 18, 20]

print("==========Examples===========")
# Mark even/odd
numbers = [1, 2, 3, 4, 5, 6]
even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"even/odd: {even_odd}")  # ['odd', 'even', 'odd', 'even', 'odd', 'even']


# Grade classification
scores = [45, 65, 75, 85, 95, 55]
grades = ["A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F" for s in scores]
print(f"Grades: {grades}")  # ['F', 'D', 'C', 'B', 'A', 'F']



print("==========Examples===========")

# Create pairs (cartesian product)
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]

pairs = [(color, size) for color in colors for size in sizes]
print("Color-Size pairs:")
for pair in pairs:
    print(f"  {pair}")


# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table (1-5):")
for row in table:
    print(f"  {row}")

print("========== Dictionary Comprehension===========")

# Filter dictionary items
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

# Keep only even keys
even_dict = {k: v for k, v in numbers.items() if k % 2 == 0}
print(f"even dict: {even_dict}")  # {2: 'two', 4: 'four'}

# Keep items where value length > 3
long_values = {k: v for k, v in numbers.items() if len(v) > 3}
print(f"long values: {long_values}")  # {3: 'three', 5: 'five'}

# values based on condition
students = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 65}
passed = {name: "Pass" if score >= 70 else "Fail" for name, score in students.items()}
print(f"pass/Fail: {passed}")


print("========== Dictionary Comprehension===========")
# Create dict from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

person = {keys[i]: values[i] for i in range(len(keys))}
print(f"Person dict: {person}")

# using zip
person_zip = {k: v for k, v in zip(keys, values)}
print(f"Person (zip): {person_zip}")

print("========== Dictionary Comprehension===========")
# Combine multiple lists into dict of lists
students = ["Alice", "Bob"]
subjects = ["Math", "Science"]
scores = [[85, 90], [78, 92]]

student_scores = {
    student: {subject: score for subject, score in zip(subjects, student_score)}
    for student, student_score in zip(students, scores)
}
for student, grades in student_scores.items():
    print(f"  {student}: {grades}")

