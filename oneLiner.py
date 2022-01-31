"""
Implement all functions in only one line of code!
They should contain a single return statement.
If you think of several implementations, do them all.
No need to validate user input anywhere.
"""
from imghdr import tests
import math
import re
from collections import Counter
from functools import reduce


def sum_digits(num):
    return sum([int(n) for n in list(str(num))])
    """
    Computes the sum of digits of an integer.
    """
    pass

# testing
# print(sum_digits(456))


def is_palindrome(seq):
    # solution 1
    return seq == "".join(reversed(seq))
    # solution 2
    return False if False in [True if list(str(seq))[i] == list(str(seq))[len(seq)-1-i]
                              else False for i in range(math.floor(len(seq)/2)+1)] else True
    """
    Checks whether a given sequence is a palindrome.
    (without changing the original sequence)

    Hints:
    - there are 2 easy ways:
        - one using builtin functions
        - another using a knife
    """
    pass


# tests
# print(is_palindrome("abdb"))
# print(is_palindrome("090"))


def is_gmail(string):
    return bool(re.fullmatch(re.compile(r'([a-z0-9A-Z])+@gmail.com'), string))
    """
    Checks whether a string is a Gmail email address.

    For our purposes, a valid address looks like "abcd@gmail.com".
    It must be a string of alphabetic letters (no dots) followed by '@gmail.com'.
    """
    pass

# tests
# print(is_gmail("abcd@gmail.com"))


def union(items, more_items):
    return list(set(items) | set(more_items))
    """
    Unites 2 lists/tuples into a list/tuple that contains all their elements without duplication.
    The return type must be that of the first argument `items`.
    """
    pass


# This is not a one-liner challenge, but should be 4 lines max
def distribution(items):
    myMap = {}
    for item in items:
        myMap[item] = myMap.get(item, 0) + 1
    return myMap
    """
    Finds how many times each item appears in a sequence of items.
    """
    pass

# testing
# print(distribution([1, 1, 1, 1, 3, 4, 3, 4]))


# remember us? :)
formula1Champions = [
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Alonso",
    "Alonso",
    "Räikkönen",
    "Hamilton",
    "Button",
    "Vettel",
    "Vettel",
    "Vettel",
    "Vettel",
    "Hamilton",
    "Hamilton",
    "Rosberg",
    "Hamilton",
    "Hamilton",
    "Hamilton",
    "Hamilton"
]


def all_time_champion(champions):
    myMap = distribution(champions)
    return max(myMap, key=lambda k: myMap[k])
    """
    Finds the person has the most wins.

    Hints:
    - distribution
    - max
    - lambda
    """
    pass

# tests
# print(all_time_champion(formula1Champions))


def dictify(keys, values):
    return dict(zip(keys, values))
    """
    Creates a dict mapping the given keys to the given values.
    """
    pass

# tests
# print(dictify([1, 2, 3], ["1", "2", "3"]))


def is_prime(num):
    return False if False in [False if num % n == 0 else True for n in range(2, math.floor(math.sqrt(num))+1)] else True
    """
    Checks whether a number is prime.

    Hints:
    - I can do this any day, and all day long!
    """
    pass

# tests
# print(is_prime(113))


def caesar_encrypt(plain, key):
    return "".join([chr((ord(char) + key-65) % 26 + 65) if char.isupper() else chr((ord(char) + key - 97) % 26 + 97) for char in plain])
    """
    Encrypts a string using caesar cipher, with the given key as the offset.

    Hints:
    - from string import ascii_letters
    - https://www.youtube.com/watch?v=IjcX3MVSdyA
    """
    pass

# tests
# print(caesar_encrypt("HELLO world!", 5))


def all_time_champion2(champions):
    return Counter(champions).most_common(1)[0][0]
    """
    Your previous code is cool, but now make it shorter!

    Hints:
    - from
    - collections
    - import
    - Counter
    """
    pass

# tests
# print(all_time_champion2(formula1Champions))


def factorial(num):
    return math.factorial(num)
    """
    Computes the factorial of a number (1 * 2 * 3 * ... * num).

    Hints:
    - def factorial(num):
          '''
          Computes the factorial of a number (1 * 2 * 3 * ... * num).

          Hints:
          - ...
          '''
          pass
    """
    pass

# tests
# print(factorial(5))


def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)
    """
    Composes all given functions.
    compose(f, g, h)(x) == f(g(h(x)))

    Hints:
    - from functools import reduce
    """
    pass
