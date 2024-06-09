# Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i, end=' ')
i = 0
while i < 11:
    print(i, end=' ')
    i += 1
# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i, end=' ')
i = 10
while i > -1:
    print(i, end=' ')
    i -= 1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
    #
    ##
    ###
    ####
    #####
    ######
    #######
"""
for i  in range(7):
    print('#' * i)
# Use nested loops to create the following:
"""
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
"""
for i in range(8):
    for j in range(8):
        print('#', end=' ')
# Print the following pattern:
"""
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
"""
for i in range(11):
    print(f'{i} x {i} = {i * i}')
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i, end=' ')
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ')
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i, end=' ')
# Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is", sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is", sum_even, "And the sum of all odds is", sum_odd)
# Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from Data.countries import countries
for country in countries:
    if 'land' in country:
        print(country, end=' ')
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(len(fruits) - 1, -1, -1):
    rev.append(fruits[i])
print(rev)
# Go to the data folder and use the countries_data.py file.
from Data.countries_data import countries_data
    # What are the total number of languages in the data
languages = []
for country in countries_data:
    if country['languages'] not in languages:
        languages.append(country['languages'])
print(len(languages))
    # Find the ten most spoken languages from the data
languages_counter = {}
for country in countries_data:
    for language in country['languages']:
        if language in languages_counter:
            languages_counter[language] += 1
        else: languages_counter[language] = 1
sorted_languages = sorted(languages_counter.items(), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(sorted_languages[i][0], end=' ')
    # Find the 10 most populated countries in the world
populations = {}
for country in countries_data:
    populations[country['name']] = country['population']
sorted_populations = sorted(populations.items(), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(sorted_populations[i][0], end=' ')
