print("==========RECURSION============")

"""
Recursion is a programming technique function calls itself
To solve smaller instances of the same problem
Until it reaches a BASE CASE (stopping condition)
"""

print("==========Factorial============")

# Basic recursive function for factorial
def recursive_factorial(n):
    # Base case: stopping condition
    if n <= 1:
        return 1
    
    # Recursive case: function calls itself
    return n * recursive_factorial(n - 1)

print(recursive_factorial(5))
# How this work
# if we call recursive_factorial(5)
#     recursive_factorial(5) = 5 * recursive_factorial(4) = 5 * 24 = 120
#     recursive_factorial(4) = 4 * recursive_factorial(3) = 4 * 6 = 24
#     recursive_factorial(3) = 3 * recursive_factorial(2) = 3 * 2 = 6
#     recursive_factorial(2) = 2 * recursive_factorial(1) = 2 * 1 = 2
#     recursive_factorial(1) = 1 # from the base case

# Mathematical definition:
# n! = n × (n-1)!  for n > 0
# 0! = 1


# Test factorial
print("Factorials:")
for i in range(1, 7):
    print(f"{i}! = {recursive_factorial(i)}")

# Iterative method 
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"\nRecursive 5! = {recursive_factorial(5)}")
print(f"Iterative 5! = {factorial_iterative(5)}")


print("==========FIBONANCI============")
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21
# F(n) = F(n-1) + F(n-2)
# F(0) = 0, F(1) = 1
# Addition of 1st and 2nd term will give you 3rd and so on.
def recur_fibonanci(n):
    # Base case 
    if n == 0 or n == 1:
        return n
    # Recursive
    else:
        return recur_fibonanci(n-1) + recur_fibonanci(n-2)
print(recur_fibonanci(8))


print("==========Recursion with Lists============")
# Sum of List
def sum_list(numbers):
    # empty list
    if not numbers:
        return 0
    
    # first element + sum of rest
    return numbers[0] + sum_list(numbers[1:])

print("\nSum of list:")
lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    []
]

for lst in lists:
    print(f"Sum of {lst} = {sum_list(lst)}")

print("==========Recursion with Lists============")
def find_max(numbers):
    # Base case - single element
    if len(numbers) == 1:
        return numbers[0]
    
    # Base case - empty list
    if not numbers:
        return None
    
    # Recursive case - compare first with max of rest
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest


test_list = [3, 7, 2, 9, 1]

print(f"Max in {test_list} = {find_max(test_list)}")

print("==========Palindrome ============")

#PALINDROME STRING
def palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
    
test_strings = ["racecar", "hello", "madam", "a", "level"]
for s in test_strings:
    print(f"'{s}' is palindrome: {palindrome(s)}")


print("==========Power Calculation============")

def power(base, exponent):
    # Base case - exponent is 0
    if exponent == 0:
        return 1
    
    # Recursive case
    return base * power(base, exponent - 1)

print(f"2^5 = {power(2, 5)}")      # 32
print(f"3^4 = {power(3, 4)}")      # 81
print(f"5^0 = {power(5, 0)}")      # 1


print("==========Tail Recursion============")

def factorial_tail(n, result=1):
    # Base case
    if n <= 1:
        return result
    
    # Tail recursive call, no computation after recursion
    else:
        return factorial_tail(n - 1, n * result)

print(f"5! = {factorial_tail(5)}")

print("==========Example============")
#  Check if list is sorted
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_sorted(lst[1:])
