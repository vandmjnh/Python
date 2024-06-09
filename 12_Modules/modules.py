### Level 1
# Writ a function which generates a six digit/character random_user_id
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_of_characters = random.randint(1, 10)
    num_of_ids = random.randint(1, 10)
    return [''.join(random.choices(string.ascii_letters + string.digits, k=num_of_characters)) for _ in range(num_of_ids)]
print(user_id_gen_by_user())
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb = [random.randint(0, 255) for _ in range(3)]
    return 'rgb(' + ','.join(map(str, rgb)) + ')'

# Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    return ['#' + ''.join(random.choices(string.hexdigits, k=6)) for _ in range(num)]

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    return [rgb_color_gen() for _ in range(random.randint(1, 10)) for _ in range(num)]
# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color, num):
    if color == 'hexa':
        return list_of_hexa_colors(num)
    elif color == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return 'Invalid color format'
print(generate_colors('hexa', 3))

### Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers
def seven_random_numbers():
    return random.sample(range(10), 7)
