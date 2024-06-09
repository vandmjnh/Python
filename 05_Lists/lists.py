# Level 1

# Declare an empty list
lst = list()
# Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5]
# Find the length of your list
print(len(lst))
# Get the first item, the middle item and the last item of the list
print(lst[0], lst[len(lst)//2], lst[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Minh', 19, 1.67, 'Student', 'Vietnam']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
# Print the list after modifying one of the companies
print(it_companies)
# Add an IT company to it_companies
print(it_companies.extend(['IT']))
# Insert an IT company in the middle of the companies list
print(it_companies.insert(len(it_companies)//2, 'IT'))
# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))
# Check if a certain company exists in the it_companies list.
print('Google' in it_companies)
# Sort the list using sort() method
print(it_companies.sort())
# Reverse the list in descending order using reverse() method
print(it_companies.reverse())
# Slice out the first 3 companies from the list
print(it_companies[:3])
# Slice out the last 3 companies from the list
print(it_companies[-3:])
# Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies)//2])
# Remove the first IT company from the list
print(it_companies.pop())
# Remove the middle IT company or companies from the list
print(it_companies.pop(len(it_companies)//2))
# Remove the last IT company from the list
print(it_companies.remove(it_companies[-1]))
# Remove all IT companies from the list
print(it_companies.clear())
# Destroy the IT companies list
del it_companies
# Join the following lists:
    # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    # back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = (front_end + back_end).copy()
print(full_stack.insert(full_stack.index('Redux') + 1, 'Python'))
print(full_stack.insert(full_stack.index('Redux') + 2, 'SQL'))

# Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
print(sorted(ages))
min_age = min(ages)
max_age = max(ages)
# Add the min age and the max age again to the list
ages.extend([min_age, max_age])
# Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages)//2] if len(ages) % 2 == 1 else (ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
# Find the range of the ages (max minus min)
range_age = max_age - min_age
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - average_age) == (max_age - average_age))
# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[len(countries)//2] if len(countries) % 2 == 1 else countries[len(countries)//2 - 1:len(countries)//2 + 1])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(countries[:len(countries)//2], countries[len(countries)//2:] if len(countries) % 2 == 0 else countries[:len(countries)//2 + 1], countries[len(countries)//2 + 1:])
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first, second, three, *scandic_countries = countries
print(first, second, three, scandic_countries)