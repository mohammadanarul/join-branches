import random
import string

def unique_random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def unique_random_string_generator(size=10, number):
#     return ''.join(random.choice(number) for _ in range(size))

# print(unique_random_string_generator())