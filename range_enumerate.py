# Coding question fizz_buzz
def fizz_buzz(numbers):
    '''
    :param numbers: The list of numbers
    :type numbers: list
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''

    # Range way
    #for i in range(len(numbers)):
    #    num = numbers[i]
    #    if num % 3 == 0:
    #        numbers[i] = "fizz"
    #    if num % 5 == 0:
    #        numbers[i] = "buzz"
    #    if num % 3 == 0 and num % 5 == 0:
    #        numbers[i] = "fizzbuzz"

    # We will use the module doctest with the command `python3 -m doctest range_enumerate.py`
    # That will be looking at your doc string  took tests, and run them and compare the output

    # enumerate() is a fuction that takes in iterable and iterates through that iterable
    # and returns tuples where the first element of the tuple is the index and the second
    # element is the value.

    # [tup for tup in enumerate([1, 2, 3])] -> [(0, 1), (1, 2), (2, 3)]
    # [tup for tup in enumerate([1, 2, 3], start=10)] -> [(10, 1), (11, 2), (12, 3)]

    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"