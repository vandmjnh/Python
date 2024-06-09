# Level 1

# Create an empty tuple
empty = tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters, brothers = ('Alice',), ('Bob',)
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
# How many siblings do you have?
siblings_count = len(siblings)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Dad', 'Mom')

# Level 2

# Unpack siblings and parents from family_members
brothers, sisters, dad, mom = family_members
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'onion')
animal_products = ('meat', 'milk', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_lt) // 2
food_stuff_tp[middle]
# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt[:3] + food_stuff_lt[-3:]
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    # Check if 'Estonia' is a nordic country
'Estonia' in nordic_countries
    # Check if 'Iceland' is a nordic country
'Iceland' in nordic_countries

