## Indexing and Slicing in Python

### Indexing
Indexing allows you to access individual elements in a sequence like a list, tuple, or string.

### Basic Indexing
- **Zero-based Indexing**: Python uses zero-based indexing, meaning the first element has an index of 0.
  ```python
  my_list = [10, 20, 30, 40, 50]
  print(my_list[0])  # Output: 10
  print(my_list[2])  # Output: 30
  ```
- **Negative Indexing**: Negative indices start from the end of the list.
  ```python
  print(my_list[-1])  # Output: 50
  print(my_list[-2])  # Output: 40
  ```

### Slicing
Slicing allows you to access a range of elements from a sequence.

### Basic Slicing
- **Syntax**: `sequence[start:stop]` where `start` is the index to begin the slice (inclusive) and `stop` is the index to end the slice (exclusive).
  ```python
  my_list = [10, 20, 30, 40, 50]
  print(my_list[1:4])  # Output: [20, 30, 40]
  ```
- **Omitting Start or Stop**: If `start` is omitted, the slice starts from the beginning. If `stop` is omitted, the slice goes to the end.
  ```python
  print(my_list[:3])  # Output: [10, 20, 30]
  print(my_list[2:])  # Output: [30, 40, 50]
  ```

### Advanced Slicing
- **Step**: `sequence[start:stop:step]` where `step` specifies the stride between elements.
  ```python
  print(my_list[0:5:2])  # Output: [10, 30, 50]
  ```
- **Negative Step**: Using a negative step reverses the order.
  ```python
  print(my_list[::-1])  # Output: [50, 40, 30, 20, 10]
  ```

### Common Slicing Patterns
- **Reversing a List**:
  ```python
  reversed_list = my_list[::-1]
  ```
- **Copying a List**:
  ```python
  copied_list = my_list[:]
  ```

### Multi-dimensional Indexing and Slicing
For multi-dimensional sequences like lists of lists, you can use multiple indices.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6
```
For slicing multi-dimensional lists:
```python
print(matrix[1:3])  # Output: [[4, 5, 6], [7, 8, 9]]
```

### Examples
1. **Accessing elements with positive and negative indices**:
   ```python
   fruits = ['apple', 'banana', 'cherry', 'date']
   print(fruits[0])    # Output: apple
   print(fruits[-1])   # Output: date
   ```

2. **Slicing with start, stop, and step**:
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   print(numbers[2:8:2])  # Output: [3, 5, 7]
   ```

3. **Reversing a string**:
   ```python
   text = "Hello, World!"
   print(text[::-1])  # Output: !dlroW ,olleH
   ```

  list[start:] means all numbers greater than start uptil the range
  list[:end] means all numbers less than end uptil the range
  list[:] means all numbers within the range


list = list(range(10)) # define a range of values 0
print(list[0:9:2])  # 0, 2, 4, 6, 8  
print(list[9:0:-2])  # 9, 7, 5, 3, 1