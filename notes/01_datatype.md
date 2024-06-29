Sure! Let's add applicable operations for each data type:

# Python Data Types

Python supports several built-in data types, each with specific operations that can be performed on them:

## 1. Numeric Types

- **int**: Integer values like `1`, `100`, `-345`.
  
  ```python
  x = 10
  print(type(x))        # Output: <class 'int'>
  print(x + 5)          # Addition: 15
  print(x * 2)          # Multiplication: 20
  print(x // 3)         # Integer Division: 3
  ```

- **float**: Floating-point values like `3.14`, `-42.0`, `1e-3`.
  
  ```python
  y = 3.14
  print(type(y))        # Output: <class 'float'>
  print(y + 1.86)       # Addition: 5.0
  print(y * 2.5)        # Multiplication: 7.85
  print(y / 2)          # Division: 1.57
  ```

- **complex**: Complex numbers in the form `a + bj`, where `a` and `b` are floats and `j` is the imaginary unit.
  
  ```python
  z = 2 + 3j
  print(type(z))        # Output: <class 'complex'>
  print(z.real)         # Real part: 2.0
  print(z.imag)         # Imaginary part: 3.0
  ```

## 2. Sequence Types

- **str**: String values like `'hello'`, `"world"`, `'123'`.
  
  ```python
  s = 'hello'
  print(type(s))        # Output: <class 'str'>
  print(s.upper())      # Convert to uppercase: 'HELLO'
  print(s + ' world')   # Concatenation: 'hello world'
  print(len(s))         # Length of string: 5
  ```

- **list**: Ordered collection of items of any data type, mutable.
  
  ```python
  my_list = [1, 2, 'three', 4.5]
  print(type(my_list))  # Output: <class 'list'>
  my_list.append(6)     # Append element: [1, 2, 'three', 4.5, 6]
  print(my_list[2])     # Access element: 'three'
  print(len(my_list))   # Length of list: 5
  ```

- **tuple**: Ordered collection of items of any data type, immutable.
  
  ```python
  my_tuple = (1, 'two', 3.0)
  print(type(my_tuple)) # Output: <class 'tuple'>
  print(my_tuple[1])    # Access element: 'two'
  print(len(my_tuple))  # Length of tuple: 3
  ```

## 3. Boolean Type

- **bool**: Represents truth values `True` and `False`.
  
  ```python
  b = True
  print(type(b))        # Output: <class 'bool'>
  print(not b)          # Logical NOT: False
  print(b and False)    # Logical AND: False
  print(b or False)     # Logical OR: True
  ```

## 4. Set Types

- **set**: Unordered collection of unique items, mutable.
  
  ```python
  my_set = {1, 2, 3, 3, 4}
  print(type(my_set))   # Output: <class 'set'>
  my_set.add(5)         # Add element: {1, 2, 3, 4, 5}
  print(2 in my_set)    # Membership check: True
  print(len(my_set))    # Number of elements: 5
  ```

- **frozenset**: Immutable version of `set`.
  
  ```python
  frozen_set = frozenset({1, 2, 3})
  print(type(frozen_set)) # Output: <class 'frozenset'>
  print(2 in frozen_set)  # Membership check: True
  ```

## 5. Mapping Type

- **dict**: Collection of key-value pairs, mutable.
  
  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  print(type(my_dict))   # Output: <class 'dict'>
  print(my_dict['b'])    # Access value by key: 2
  my_dict['d'] = 4       # Add new key-value pair
  print(len(my_dict))    # Number of key-value pairs: 4
  ```

## 6. None Type

- **NoneType**: Represents the absence of a value, similar to `null` in other languages.
  
  ```python
  none_value = None
  print(type(none_value))  # Output: <class 'NoneType'>
  ```

These examples showcase typical operations and functionalities associated with each Python data type. They provide the foundation for creating complex data structures and performing various computations and manipulations in Python programming.