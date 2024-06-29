example_list = [3.14159, 'apple', 23]  # Create a list of elements
empty_list = []  # Create an empty list
sequence_list = list(range(10))  # Create a list of first 10 whole numbers
print(example_list)
print(empty_list)
print(sequence_list)


#lists can hold integers, strings, characters, functions, and pretty much any other data type including other lists simultaneously

a_list = [2, 'ABC', 'A']

def foo():
    print('Hello from foo()!')

another_list = [a_list, 'Python', foo, ['yet another list']]

print(another_list[0])  # Elements of 'aList'
print(another_list[0][1])  # Second element of 'aList'
print(another_list[1])  # 'Python'
print(another_list[3])  # 'yet another list'

# You can also invoke the functions inside a list!
another_list[2]()  # 'Hello from foo()!'


### Slicing

l = list(range(10))
print(l)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(l[0:4])  # 0, 1, 2, 3

# list[start:] means all numbers greater than start uptil the range
# list[:end] means all numbers less than end uptil the range
# list[:] means all numbers within the range

# Negative Indexing
#l = list(range(10))
l = list(range(10))

print(l)
print(l[4:-1])  # 4, 5, 6, 7, 8