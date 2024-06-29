import array

# type: 'f' (float), initializer list: [1, 2, 3]
new_array = array.array('f', [1, 2, 3])
print(new_array[0]) 
# Array slicing #
         
initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)

print(number_array[1:5])  # 2nd to 5th
print(number_array[:-5])  # beginning to 3rd
print(number_array[5:])  # 6th to end
print(number_array[:])   # beginning to end

## Changing or adding array elements#
integers = array.array('i', [1, 2, 3, 5, 7, 10])
# changing first element
integers[0] = 0
print(integers)  # array('i', [0, 2, 3, 5, 7, 10])

## Append
numbers = array.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)  # array('i', [1, 2, 3, 4])
## Extend
# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # array('i', [1, 2, 3, 4, 5, 6, 7])

##You can concatenate two arrays using + operator
odd = array.array('i', [1, 3, 5])
even = array.array('i', [2, 4, 6])
integers = array.array('i')   # creating empty array of integer
integers = odd + even

## Delete
integer_array = array.array('i', [1, 2, 3, 3, 4])
del integer_array[2]  # removing third element
print(integer_array)  # Output: array('i', [1, 2, 3, 4])

del integer_array  # deleting entire array
#print(integer_array)  # Error: array is not defined

## Remove
integer_array = array.array('i', [10, 11, 12, 12, 13])
integer_array.remove(12)
print(integer_array)   # array('i', [10, 11, 12, 13])

## POP
print(integer_array.pop(2))   # Output: 12
print(integer_array)   # array('i', [10, 11, 13])