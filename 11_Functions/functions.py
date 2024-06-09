# Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14 * r * r
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) == int:
            sum += i
        else:
            return "All list items are not numbers"
    return sum
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ["September", "October", "November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Invalid month"
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**0.5) / 2*a
        x2 = (-b - delta**0.5) / 2*a
        return x1, x2
    elif delta == 0:
        x = -b / 2*a
        return x
    else:
        return "No solution"
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    return [i.capitalize() for i in lst]
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_all_numbers(n):
    return sum(range(n+1))
print(sum_all_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum([i for i in range(n+1) if i % 2 != 0])
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(n):
    return sum([i for i in range(n+1) if i % 2 == 0])
# Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    evens = len([i for i in range(n+1) if i % 2 == 0])
    odds = len([i for i in range(n+1) if i % 2 != 0])
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    return len(lst) == 0
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)
def calculate_median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2] + lst[len(lst)//2 - 1]) / 2
    else:
        return lst[len(lst)//2]
def calculate_mode(lst):
    return max(set(lst), key=lst.count)
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    mean = sum(lst) / len(lst)
    return sum([(i - mean)**2 for i in lst]) / len(lst)
def calculate_std(lst):
    return calculate_variance(lst)**0.5
# Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    return len(lst) == len(set(lst))
# Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    return len(set([type(i) for i in lst])) == 1
# Write a function which check if provided variable is a valid python variable
def is_valid_variable(var):
    return var.isidentifier()
# Go to the data folder and access the countries-data.py file.
from Data.countries_data import countries_data
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages():
    return sorted(countries_data, key=lambda x: x['languages'], reverse=True)[:10]
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries():
    return sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]