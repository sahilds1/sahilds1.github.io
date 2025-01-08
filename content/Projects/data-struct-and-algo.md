Title: Learning Notes: Data Structures and Algorithms
Date: 2024-12-19
Tags: python
Slug: data-structures-and-algorithms
Summary: Learning Notes: Data Structures and Algorithms
Status: published

# Writing Algorithms using Python Constructs

## Arithmetic Operations 

### Divide and "take the floor" in one step using the `//` operator

"Taking the floor" of a number and truncating it are the same for positive numbers 
because  the floor rounds it toward negative infinity and truncating rounds toward zero:


```
In: 5/2
Out: 2.5

In: 5//2
Out: 2

In: math.trunc(5/2)
Out: 2

```

When the numbers are negative, taking the  floor and truncating aren't the same:

```
In: -5/2
Out: -2.5

In: -5//2
Out: -3

In: math.trunc(-5/2)
Out: -2

```

When you need to round toward  positive infinity, you can "take the ceiling":

```
In: 5/2
Out: 2.5

In: math.ceil(5/2)
Out: 3

In: math.ceil(-5/2)
Out: -2

```


<!-- ## Calculate remainders using the `%` operator 

## Calculate powers using the `**` operator -->


## Control Flow

### Check conditions in order and execute the first true one using `if … elif … elif …`

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

When the conditions are reordered, the output for `x=15` changes from `Fizz` to `Buzz`. Note the use of the
`else` clause to make the `if … elif … elif …` construct exhaustive. 


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

<!--
For cases where you need to choose from a very large number of possibilities, 
you can create a dictionary mapping case values to functions to call. For example:

### The while loop condition can be a  string or list value or any sequence
The conditions used in while and if statements can contain any operators, not just comparisons.

### Python’s for statement iterates over the items of any sequence (a list or a string)
Giving the user the ability to define both the iteration step and halting condition (as C), 

### Index variables for iterating through a list or two lists  can be written as an enumerate or  zip respectively 

### A break statement in a for or while loop can be paired with an else clause

-->

## Data Structures


<!-- ### The variable length array high level data types  include the list 

which can be used as a stack or queue using append, pop and insert
CPython’s lists are really variable-length arrays, not Lisp-style linked lists. 
When items are appended or inserted, the array of references is resized.
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
While appends and pops from the end of list are fast, doing inserts or pops from 
the beginning of a list is  slow (because all of the other elements have to be shifted by one).
If we have a mutable object (list, dict, set, etc.), we can use some specific operations to mutate it and all the variables that refer to it will see the change.

### Indexing a sequence from the last index seq[len(seq)-n] can be written as  seq[-n]
S[:-1] is all of the string except for its last character, which is useful for removing the trailing newline from a string.


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
Access value  at index iterate vs  array list  access in constant time -->



<!-- ### High level data types include the set data type can be used for membership testing and eliminating duplicate entries
. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
Python can search for items in a set or dictionary by attempting to directly accessing them without iterations,

###High level data types include the default dict which do not return an error to extract a value using a non-existent key
CPython’s dictionaries are implemented as resizable hash tables.
While looping through dict , keys and values can be retrieved same time using items


### High level data type include the matrix data type provided by NumPy for multidimensional arrays
Replicating a list with * doesn’t create copies, it only creates references to the existing objects.

### High level data types includes collections.Count for bags or multisets in other languages
Counter objects have a dictionary interface except that they return a zero count for missing items
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. -->

