lst = [1, 2, -5, 4]

def square(x):
    return x * x

map(square, lst)

print(list(map(square, lst)))

# Another way

result = []

for num in lst:
    result.append(square(num))

print(result)

# Both works well, let's se a 3rd way

print([square(num) for num in lst])

#The last is the more Pythonic way to do the task

# Let's see a new example
def is_odd(x):
    return x % 2 == 1

# So let's filter on our list the elements that are not odd
print(filter(is_odd, lst))

print(list(filter(is_odd, lst)))

# And using List Comprehension
print([num for num in lst if is_odd(num)])

# A more interview exercise with grids
grid  = [[0, 0, 0], [0, 0, 0]]

# Dynamically?

num_rows = 2
num_columns = 3
grid = []

# First with for loop
for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)

print(grid)

# Using List Comprehension

grid_lc = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
print(grid_lc)

# Let's now explore some functions
print(max(1, 2, 3))

# What if we want to find the number that has the max square? Well, we pass in a key param to lst.
print(max(lst, key=lambda x: x * x))

print(min(1, 2, 3))

print(min(lst, key=lambda x: x * x))

#Any function takes an iterable and returns True if any other value in the iterable are true.
print(any(lst))

print(any([True, False]))

print(any([False, False]))

# If we use any with args it will fail
# any(lst, key=lambda x: x% 2 == 1)

print([(lambda x: x % 2 == 1)(num) for num in lst])

print(any([(lambda x: x % 2 == 1)(num) for num in lst]))

print(all([(lambda x: x % 2 == 1)(num) for num in lst]))

# Above we have pretty ways to evaluate lists for a confition or attribute in common