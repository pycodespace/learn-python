Certainly! Here's an expanded version with examples for each data type:

# Python Data Types

Python supports several built-in data types, which can be categorized as follows:

## 1. Numeric Types

- **int**: Integer values like `1`, `100`, `-345`.
  
  ```python
  x = 10
  print(type(x))  # Output: <class 'int'>
  ```

- **float**: Floating-point values like `3.14`, `-42.0`, `1e-3`.
  
  ```python
  y = 3.14
  print(type(y))  # Output: <class 'float'>
  ```

- **complex**: Complex numbers in the form `a + bj`, where `a` and `b` are floats and `j` is the imaginary unit.
  
  ```python
  z = 2 + 3j
  print(type(z))  # Output: <class 'complex'>
  ```

## 2. Sequence Types

- **str**: String values like `'hello'`, `"world"`, `'123'`.
  
  ```python
  s = 'hello'
  print(type(s))  # Output: <class 'str'>
  ```

- **list**: Ordered collection of items of any data type, mutable.
  
  ```python
  my_list = [1, 2, 'three', 4.5]
  print(type(my_list))  # Output: <class 'list'>
  ```

- **tuple**: Ordered collection of items of any data type, immutable.
  
  ```python
  my_tuple = (1, 'two', 3.0)
  print(type(my_tuple))  # Output: <class 'tuple'>
  ```

## 3. Boolean Type

- **bool**: Represents truth values `True` and `False`.
  
  ```python
  b = True
  print(type(b))  # Output: <class 'bool'>
  ```

## 4. Set Types

- **set**: Unordered collection of unique items, mutable.
  
  ```python
  my_set = {1, 2, 3, 3, 4}
  print(type(my_set))  # Output: <class 'set'>
  ```

- **frozenset**: Immutable version of `set`.
  
  ```python
  frozen_set = frozenset({1, 2, 3})
  print(type(frozen_set))  # Output: <class 'frozenset'>
  ```

## 5. Mapping Type

- **dict**: Collection of key-value pairs, mutable.
  
  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  print(type(my_dict))  # Output: <class 'dict'>
  ```

## 6. None Type

- **NoneType**: Represents the absence of a value, similar to `null` in other languages.
  
  ```python
  none_value = None
  print(type(none_value))  # Output: <class 'NoneType'>
  ```

These data types provide the building blocks for creating complex data structures and performing various operations in Python programming.