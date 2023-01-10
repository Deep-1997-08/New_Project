Course="Python's course for begineers"
Course_1='Python Course for "Begineers"'
print(Course_1[5])
Paragraph='''
Hi Jay
This is to inform you that this is a course of python
Hope you understand and focus on some thing else.
thanks,
Deep Bhattacharjee'''
print(Paragraph)

# Index of the string
name='Deep Bhattacharjee'
print(name[2:-2])

first='Deep'
last='Bhattacharjee'
message=first+' ['+last+'] is a coder'
print(message)

# concatination

msg=f'{first} {last} is a coder'
print(msg)

# Length of the string

course="Python for begineers"
print(len(course))

# Converting it to upper case

print(course.upper())

# Print to lower case

print(course.lower())

# find the index of the letter

print(course.find('n' ))

# Replace words

print(course.replace('begineers', 'Absolute begineers'))
print(course.replace('P',"J"))

# validating if its in the string

print('Python' in course)