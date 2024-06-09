# Create an empty dictionary called dog
dog = dict()
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Max'
dog['color'] = 'Black'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 5
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'male',
    'age': 25,
    'marital_status': 'single',
    'skills': ['Python', 'Java', 'C++'],
    'country': 'Nigeria',
    'city': 'Lagos',
    'address': '1, Street, Lagos, Nigeria'
}
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))
# Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
print(student['skills'])
# Get the dictionary keys as a list
keys = student.keys()
print(keys)
# Get the dictionary values as a list
values = student.values()
print(values)
# Change the dictionary to a list of tuples using items() method
items = student.items()
print(items)
# Delete one of the items in the dictionary
del student['address']
print(student)
# Delete one of the dictionaries
del student
