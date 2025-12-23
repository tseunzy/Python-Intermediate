

print("==========Files (Read/Write)===========")

# Different modes for opening files
"""
Mode  Description
'r'   Read (default) - opens for reading
'w'   Write - creates new file or overwrites existing
'a'   Append - writes to end of file
'x'   Exclusive creation - fails if file exists
'b'   Binary mode - for non-text files
't'   Text mode (default)
'+'   Update mode - read and write
"""

# # Open for reading (default)
# file = open("example.txt", "r")  # Same as open("example.txt")

# # Open for writing 
# file = open("output.txt", "w")

# # Open for appending (adds to end of file)
# file = open("log.txt", "a")

# # Open for reading and writing
# file = open("data.txt", "r+")

# # Always close files
# file.close()

print("==========Using With Statement===========")

# With statement automatically closes file
with open("example76.txt", "r") as file:
    content = file.read()
    # file automatically closes when block exits
    print("file read successfully")

# No need to call file.close() - it's done automatically
print("file is close:", file.closed)  # True


print("==========Example 2===========")

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
    print("files processed")

print("==========Example 3 with exception===========")
# Handle file not found
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

print("==========Example 4===========")
with open("example76.txt", "r") as file:
    content = file.read()
    print(content)
    print(f"length: {len(content)} characters")


print("==========Reading Line by Line===========")


# Read all lines into a list readlines()
with open("example76.txt", "r") as file:
    lines = file.readlines() # this print the lines in a list
    print(f"otal lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.rstrip()}")  # rstrip removes newline characters
    print(lines[3]) # the lines are in a list, so you can use the index 

print("==========Example===========")
# readline()
with open('example76.txt', 'r') as file: 
    line = file.readline() #pass arg to it like (5)- first 5 char
    print(line)

print("==========Example===========")
# Read specific number of characters
with open("example76.txt", "r") as file:
    first_100 = file.read(100)  # Read first 100 characters
    print(f"1st 100 chars: {first_100}")
    


print("==========Example===========")
with open('example76.txt', 'r+') as file:
    print(f"starting position: {file.tell()}")

    first_five = file.read(5)
    print(f"1st 5 chars: {first_five}")
    print(f"position after reading: {file.tell()}")
    # file.seek(0, 2) # to seek at the end-- to add at the end
    # file.write(' GLORY')

    # Seek to beginning
    file.seek(0)
    print(f"position after seeking to 0: {file.tell()}")

    # Seek to specific position
    file.seek(10)  # Skip first line
    print(f"At position 10: {file.read(5)}")


     # Overwrite at specific position
    file.seek(0) # From the beginining 
    file.write("HELLO")  # Overwrites first 5 characters
    print("overwrite 1st 5 characters")





