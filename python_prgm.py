string1 = "Hello "
name = input("Enter your Name: ")
string2 = string1 + name
print(string2)
string3 = ", welcome to Python programming"
string2 = string2 + string3
print(string2)

string = "Hello pavithra, welcome to Python programming"

# a. Print the first character
print("First character:", string[0])

# b. Print the last character
print("Last character:", string[-1])

# c. Print the first 5 characters
print("First 5 characters:", string[:5])

# d. Print the last 11 characters
print("Last 11 characters:", string[-11:])

# e. Print the string in reverse
print("Reverse string:", string[::-1])

# f. Print the word Python using slicing
print("Python:", string[22:28])

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize the sentence
print("Capitalize:", strM.capitalize())

# d. Count occurrences of character 't'
print("Count of t:", strM.count('t'))

# e. Replace Python with Machine Learning
print("Replace:", strM.replace("Python", "Machine Learning"))

# Create the first tuple
t1 = (10, 20, 30)

# Create the second tuple
t2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat the elements 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("Third element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])