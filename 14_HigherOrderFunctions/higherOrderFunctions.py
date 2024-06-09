countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Level 1
# Explain the difference between map, filter, and reduce.
# Explain the difference between higher order function, closure and decorator
# Define a call function before map, filter or reduce, see examples.
def square(x):
    return x**2
print(list(map(square, numbers)))
def isEven(x):
    return x % 2 == 0
print(list(filter(isEven, numbers)))
def add(x, y):
    return x + y
from functools import reduce
print(reduce(add, numbers))
# Use for loop to print each country in the countries list.
for country in countries:
    print(country, end=' ')
# Use for to print each name in the names list.
for name in names:
    print(name, end=' ')
# Use for to print each number in the numbers list.
for number in numbers:
    print(number, end=' ')
print('\n')
## Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
countriesLst = list(map(lambda uppercase: uppercase.upper(), countries))
print(countriesLst)
# Use map to create a new list by changing each number to its square in the numbers list
numbersLst = list(map(square, numbers))
# Use map to change each name to uppercase in the names list
namesLst = list(map(lambda letter: letter.upper(), names))
# Use filter to filter out countries containing 'land'.
countriesLand = list(filter(lambda country: 'land' in country, countries))
print(countriesLand)
# Use filter to filter out countries having exactly six characters.
countriesSix = list(filter(lambda country: len(country) == 6, countries))
print(countriesSix)
# Use filter to filter out countries containing six letters and more in the country list.
countriesSixMore = list(filter(lambda country: len(country) >= 6, countries))
print(countriesSixMore)
# Use filter to filter out countries starting with an 'E'
countriesE = list(filter(lambda country: country.startswith('E'), countries))
print(countriesE)
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result = reduce(add, list(filter(isEven, list(map(square, numbers)))))
print(result)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def getStringLists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_list = getStringLists(mixed_list)
print(string_list)
# Use reduce to sum all the numbers in the numbers list.
sumAll = reduce(add, numbers)
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concatenate = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ' and ' + countries[-1] + ' are north European countries'
print(concatenate)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorizeCountries(pattern):
    return list(filter(lambda country: pattern in country.lower(), countries))
print(categorizeCountries('es'))
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def dictionary(countries):
    from collections import defaultdict
    dct = defaultdict(int)
    for country in countries:
        dct[country[0]] += 1
    return dict(dct)
print(dictionary(countries))
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
import json
with open('D:/WorkSpace/Github/Python/14_HigherOrderFunctions/countries_data.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)
def get_first_ten_contries(countries):
    return list(map(lambda x: x["name"], countries))[:10]
print(get_first_ten_contries(countries))
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_contries(countries):
    return list(map(lambda x: x["name"], countries))[-10:]
print(get_last_ten_contries(countries))
## Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
from countries_data import countries_data
# Sort countries by name, by capital, by population
countries_data.sort(key=lambda x: x["name"])
countries_data.sort(key=lambda x: x["capital"])
countries_data.sort(key=lambda x: x["population"])
# Sort out the ten most spoken languages by location.
languages = []
for country in countries_data:
    languages.extend(country["languages"])
from collections import Counter
languages = Counter(languages)
print(languages.most_common(10))
# Sort out the ten most populated countries.
countries_data.sort(key=lambda x: x["population"], reverse=True)
