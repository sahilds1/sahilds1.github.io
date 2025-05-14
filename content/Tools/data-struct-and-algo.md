Title: Writing Algorithms using Python Constructs
Date: 2024-12-19
Summary: Learning Notes: [https://docs.google.com/document/d/](https://docs.google.com/document/d/1dPTWdNlQA2H2cDqxlVRRGb6ITOJRVPiCiR-kBSI5Uac/edit?usp=sharing)
Status: draft

<!-- Tocbot will turn this div into a table of contents.
<div class="toc"></div> -->

# Arithmetic Operations 

## Divide and "take the floor" with the `//` operator

"Taking the floor" of a number and truncating it are the same for positive numbers:  

```
In: 5/2
Out: 2.5

In: 5//2
Out: 2

In: math.trunc(5/2)
Out: 2

```

The floor rounds it toward negative infinity and truncating rounds toward zero.

When the numbers are negative, taking the floor and truncating aren't the same:

```
In: -5/2
Out: -2.5

In: -5//2
Out: -3

In: math.trunc(-5/2)
Out: -2

```

When you need to round toward positive infinity, you can "take the ceiling":

```
In: 5/2
Out: 2.5

In: math.ceil(5/2)
Out: 3

In: math.ceil(-5/2)
Out: -2

```

# Control Flow

## Check conditions in order and select the first true one with `if … elif … elif …`

When the conditions are mutually exclusive and exhaustive, it's easy to reason about:

```{python}
In:
output = [] 
for x in range(1, 5):
    if x % 3 == 0:
        output.append("Fizz")
    elif x % 3 != 0:
        output.append("not Fizz")

Out: ['not Fizz', 'not Fizz', 'Fizz', 'not Fizz']

```

When the conditions aren't mutually exclusive, the order of the conditions matters:

```{python}
In:
output = [] 
for x in range(12, 16):
    if x % 3 == 0:
        output.append("Fizz")
    elif x % 5 == 0:
        output.append("Buzz")
    else:
        output.append(str(x))

Out: ['Fizz', '13', '14', 'Fizz']
```


```{python}
In:
output = [] 
for x in range(12, 16):
    if x % 5 == 0:
        output.append("Buzz")
    elif x % 3 == 0:
        output.append("Fizz")
    else:
        output.append(str(x))

Out: ['Fizz', '13', '14', 'Buzz']
```

When the conditions are reordered, the output for `x=15` changes from `Fizz` to `Buzz`. 

Note the use of the `else` clause to make the `if … elif … elif …` construct exhaustive. 

To make overlapping conditions easier to reason about, we can explicitly enumerate them using logical operators:

```{python}
In:
output = [] 
for x in range(12, 16):
    if (x % 3 == 0) and (x % 5 == 0):
        output.append("FizzBuzz")
    elif (x % 3 == 0) and (x % 5 != 0):
        output.append("Fizz")
    elif (x % 5 == 0) and (x % 3 != 0):
        output.append("Buzz")
    else:
        output.append(str(x))

Out: ['Fizz', '13', '14', 'FizzBuzz']
```

If the overlapping conditions have a natural ordering, we can order them from most to least specific:

```{python}
In:
x = 10

if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10")
elif x > 0: 
    print("x is positive")
else:
    print("x is non-positive")

Out: x is positive
```

<!-- ## Iteratively execute as long as a condition is true using `while`  


```

runningsum = [nums[0]]
pointer = 1
while pointer <= len(nums)-1:
    runningsum.append(runningsum[pointer-1]+nums[pointer])

    pointer += 1

```



Iterate as long as a condition hasn't been met using a while loop 



Iteratively execute without needing to count the number of iterations using `while` 




Execute without knowing the number of iterations in advance using `while` 


Execute knowing the number of iterations in advance using  `for`


Iterate without a counter variable using a while loop

Iterate if a condition is met an unknown number of times using a while loop

A while loop is more suitable than a for loop in scenarios where you don't know in advance how many 
iterations are required and instead need to loop until a certain condition is met

In a while loop something inside the loop triggers the loop to stop 

A do while loop is executed at least one  time

The while loop condition can be a  string or list value or any sequence
The conditions used in while and if statements can contain any operators, not just comparisons.


Iterate knowing the number the number of iterations using a for loop

Iterate a known number of times  using a counter and a while loop or for loop

A while loop can be used to replace a for loop using a counter variable initialization, test and increment

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

Python’s for statement iterates over the items of any sequence (a list or a string)
Giving the user the ability to define both the iteration step and halting condition (as C), 
The counter variable  is used to  perform an operation on the sequence

Index variables for iterating through a list or two lists  can be written as an enumerate or  zip respectively 

A break statement in a for or while loop can be paired with an else clause

itertools; This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.  -->


# Data Structures

## Allocate data to dynamic arrays with `list`

The Python `list` is a dynamic array that can grow as we need it to: 

```
In:
cubes = [1, 8, 27, 65, 125]
cubes[len(cubes):] = [6 ** 3] 
cubes[len(cubes):] = [7 ** 3]

Out: [1, 8, 27, 64, 125, 216, 343]

```

Note that "indexing" and "slicing" handle out of range indices differently

The syntax for slicing is `list[start:stop:step]` where start is inclusive and stop is exclusive

If omitted, start defaults to 0 and stop defaults to to the end of the list 

```
In: cubes =  [1, 8, 27, 64, 125, 216, 343]

In: cubes[len(cubes)]
Out: IndexError: list index out of range

In: cubes[len(cubes):]
Out: []

```

Both "indexing" and "slicing" of Python lists can handle negative indices

-1 refers to the last element  and negatives indices count from the end of the list 


```
In: cubes =  [1, 8, 27, 64, 125, 216, 343]

In: cubes[-1]
Out: 343

In: cubes[-len(cubes)]
Out: 1

In: cubes[-1:-len(cubes):-1]
Out: [343, 216, 125, 65, 27, 8]

```

We can replace and remove values from a Python `list` using slicing: 

```
In: letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

In: letters[2:5] = ['C', 'D', 'E']
Out: ['a', 'b', 'C', 'D', 'E', 'f', 'g']

In: letters[2:5] = []
Out: ['a', 'b', 'f', 'g']
```

An alternative to indexing and slicing is Python list methods:

<!-- Methods that only modify mutable data structures have no return value in Python  -->

Note that list.insert(i,x) inserts x before index i

```
In: cubes = [1, 8, 27, 65, 125]

In: cubes.append(6**3)
Out: [1, 8, 27, 65, 125, 216]

In: cubes.insert(len(cubes), 7**3)
Out: [1, 8, 27, 65, 125, 216, 343]

In: cubes.insert(0,0**3)
Out: [0, 1, 8, 27, 65, 125, 216, 343]

In: cubes.pop()
Out: [0, 1, 8, 27, 65, 125, 216]

In: cubes.pop(0)
Out: [1, 8, 27, 65, 125, 216]


```

<!-- # Access data by content using hashing with `dict` and `set`

Retrieve or insert a key using square brackets

```
hash_map = {1: 2, 5: 3, 7: 2}

hash_map[5] # 3

hash_map[8] = 6

hash_map = {}

hash_map[5] # 3


```

# Get keys: use .keys(). You can iterate over this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)

.items

Delete a key using the `del`  keyword

```
del hash_map[9]

```

Update a key using square brackets

```
```



# Checking if a key exists: simply use the `in` keyword
1 in hash_map # True
9 in hash_map # False



### High level data types include the default dict which do not return an error to extract a value using a non-existent key
CPython’s dictionaries are implemented as resizable hash tables.
While looping through dict , keys and values can be retrieved same time using items


### High level data types includes collections.Count for bags or multisets in other languages
Counter objects have a dictionary interface except that they return a zero count for missing items
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.


### High level data types include the set data type can be used for membership testing and eliminating duplicate entries
. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
Python can search for items in a set or dictionary by attempting to directly accessing them without iterations, -->



<!-- 

### Implement other data structures or solve problems using the linked lists

Defining a singly linked linked list using Python classes 

Python class definition for a singly linked list *node*


# Definition for singly-linked list *node*
# class ListNode:
#     def __init__(self, val=0, next=None -> ListNode): # self.next type should be ListNode
#         self.val = val
#         self.next = next

Create linked nodes and chain them together 

# Create individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link the nodes
node1.next = node2
node2.next = node3

# node1 -> node2 -> node3

Time to execute various operations for this implementation 
Access value  at index iterate vs  array list  access in constant time 

-->


<!--

### The list can be used as a stack using the append and pop operations:

While appends and pops from the end of list are fast, doing inserts or pops from 
the beginning of a list is  slow (because all of the other elements have to be shifted by one).

-->

<!-- 

### High level data types include the str data type which are arrays of Unicode

https://docs.python.org/3/library/stdtypes.html#textseq 

-->

<!-- ### High level data type include the matrix data type provided by NumPy for multidimensional arrays
Replicating a list with * doesn’t create copies, it only creates references to the existing objects. -->

