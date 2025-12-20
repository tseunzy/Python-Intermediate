
# Note When using map() and filter(), 
# you don't need to loops yourself. The funct handle the iteration internally
print("==========Map Function===========")
# map(function, iterable) - applies function to every item in iterable

# Square all numbers
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squares = map(lambda x: x**2, numbers)
print(list(squares))  

print("==========Example2===========")
# Double all numbers
def double(x):
    return x * 2

doubled = map(double, numbers)
print(list(doubled))  # [2, 4, 6, 8, 10]

print("==========Example3===========")
# Maping with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]

sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))  # [5, 7, 9]

print("==========Example4===========")
# Map stops at shortest iterable
list1 = [1, 2, 3, 4]
list2 = [5, 6]  

result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [6, 8] 

print("==========Example5===========")
# Extract specific data from list of dictionaries
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

# Get only names
def name_stud(student):
    return student['name']

names = map(name_stud, students)
print(f"Student names: {list(names)}")


print("==========Example6===========")
# Type conversion
string_numbers = ["1", "2", "3", "4", "5"]
integers = list(map(int, string_numbers))
print(f"Integers: {integers}")

print("==========Example7===========")
numbers = [1, 2, 3, 4, 5]
# Using map
squares_map = map(lambda x: x**2, numbers)

# Using list comprehension
squares_lc = [x**2 for x in numbers]

print(f"Map result: {list(squares_map)}")
print(f"List comprehension: {squares_lc}")


print("==========Filter Examples===========")

# Filter students with grade A
students = [
    {"name": "Alice", "grade": "A", "age": 20},
    {"name": "Bob", "grade": "B", "age": 21},
    {"name": "Charlie", "grade": "A", "age": 19},
    {"name": "Diana", "grade": "C", "age": 22}
]

grade_a_students = filter(lambda s: s["grade"] == "A", students)
print("students with grade A:")
for student in grade_a_students:
    print(f"  - {student['name']}")

print("==========Example2===========")
# Filter by multiple conditions
def grade_age(s):
    return s['grade'] == "A" and s['age'] < 21

young_grade_a = filter(grade_age, students)
print("\nstudents with grade A and younger:")
for student in young_grade_a:
    print(f"  - {student['name']} (age {student['age']})")

print("==========Example2===========")
# Filter strings
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
long_words = filter(lambda w: len(w) > 5, words)
print(f"\nLong words: {list(long_words)}")

print("==========Example4===========")
# Words starting with vowel
vowel_start = filter(lambda w: w[0].lower() in 'aeiou', words)
print(f"Words starting with vowel: {list(vowel_start)}")

print("==========Example5===========")
# Filter files by extension
files = ["document.pdf", "image.jpg", "data.csv", "script.py", "notes.txt"]
python_files = filter(lambda f: f.endswith('.py'), files)
print(f"Python files: {list(python_files)}")


print("==========Reduce Examples===========")

from functools import reduce

# reduce(function, iterable[, initial]) - cumulatively applies function

# sum of numbers
numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_result}")  # 15

print("==========Example2===========")
# concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(f"sentence: {sentence}")  # Hello World!

print("==========Example3===========")
# flatten nested list, 2 levels
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = reduce(lambda x, y: x + y, nested)
print(f"flatten: {flat}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("==========Example4===========")
# Calculate average with reduce
grades = [85, 92, 78, 90, 88]
average = reduce(lambda x, y: x + y, grades) / len(grades)
print(f"Average: {average:.2f}")  # 86.60

print("==========Example5===========")
# Sum with initial 10
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(f"sum with initial 10: {sum_with_initial}")  # 25



print("==========Zip Function===========")

# zip(*iterables) - it aggregates elements from each iterable

# Pair elements from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

print("==========Example2===========")
# With three lists
scores = [85, 92, 78]
result = zip(names, ages, scores)
print(list(result))  # [('Alice', 25, 85), ('Bob', 30, 92), ('Charlie', 35, 78)]

print("==========Example3===========")
# Zip stops at shortest iterable
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30]  # Shorter list

result = zip(names, ages)
print(list(result))  # [('Alice', 25), ('Bob', 30)]

print("==========Example4===========")
# Creating dictionaries from two lists
keys = ["name", "age", "city"]
values = ["alice", 25, "New York"]

person = dict(zip(keys, values))
print(f"person dictionary: {person}")
#{'name': 'Alice', 'age': 25, 'city': 'New York'}

print("==========Example5===========")
students = ["Alice", "Bob", "Charlie"]
midterm_scores = [85, 92, 78]
final_scores = [90, 88, 85]

for name, mid, final in zip(students, midterm_scores, final_scores):
    print(f"{name}: mid={mid}, final={final}")

print("==========Example6===========")
# Unzipping (inverse of zip) Use zip(*zipped) to unzip
zipped = [('a', 1), ('b', 2), ('c', 3)]
lett, numb = zip(*zipped)
print(f"\nletter: {lett}")    # ('a', 'b', 'c')
print(f"Numb: {numb}")     # (1, 2, 3)


print("==========Enumerate Function===========")

# enumerate(iterable, start=0) - adds counter to iterable

# Get index and value
fruits = ["apple", "banana", "cherry", "date"]

# without enumerate
print("without enumerate:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("==========Example 2===========")
# With enumerate
print("\nwith enumerate:")
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

print("==========Example 3===========")
# with custom start index
print("\nwith start=1:")
for i, fruit in enumerate(fruits, start=1):
    print(f"Position {i}: {fruit}")

print("==========Example 4===========")
# Convert to list
enum_list = list(enumerate(fruits))
print(f"\nas list: {enum_list}")
# [(0, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'date')]

print("==========Example 5===========")
# Enumerate characters in string
text = "Python"
for i, char in enumerate(text, start=1):
    print(f"  {i}: {char}")