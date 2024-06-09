# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print('1',[i for i in numbers if i <= 0])
# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print('2', [i for j in list_of_lists for k in j for i in k])
# Using list comprehension create the following list of tuples:
print('3', [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print('4', [[i[0].upper(), i[0][:3].upper(), i[1].upper()] for j in countries for i in j])
# Change the following list to a list of dictionaries:
print('5', [{'country': i[0], 'city': i[1]} for j in countries for i in j])
# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print('6', [' '.join(i) for j in names for i in j])
# Write a lambda function which can solve a slope or y-intercept of linear functions.
a = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
print('7', a(0, 0, 4, 16))