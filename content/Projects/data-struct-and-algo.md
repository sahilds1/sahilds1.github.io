Title: Learning Notes: Data Structures and Algorithms
Date: 2024-12-19
Tags:
Slug:
Summary: Learning Notes: Data Structures and Algorithms
Status: draft

# Writing Algorithms using Python Constructs


## Control Flow

The while loop condition can be a  string or list value or any sequence
The conditions used in while and if statements can contain any operators, not just comparisons.

Giving the user the ability to define both the iteration step and halting condition (as C), 
Python’s for statement iterates over the items of any sequence (a list or a string)

Nested  if else if else statements can be written as if elif statements
For cases where you need to choose from a very large number of possibilities, 
you can create a dictionary mapping case values to functions to call. For example:

A break statement in a for or while loop can be paired with an else clause

Index variables for iterating through a list or two lists  can be written as an enumerate or  zip respectively 


## Data Structures

The variable length array high level data types  include the list which can be used as a stack or queue using append, pop and insert
CPython’s lists are really variable-length arrays, not Lisp-style linked lists. 
When items are appended or inserted, the array of references is resized.
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
While appends and pops from the end of list are fast, doing inserts or pops from 
the beginning of a list is  slow (because all of the other elements have to be shifted by one).
If we have a mutable object (list, dict, set, etc.), we can use some specific operations to mutate it and all the variables that refer to it will see the change.

High level data types include the set data type can be used for membership testing and eliminating duplicate entries
. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
Python can search for items in a set or dictionary by attempting to directly accessing them without iterations,

High level data types include the default dict which do not return an error to extract a value using a non-existent key
CPython’s dictionaries are implemented as resizable hash tables.
While looping through dict , keys and values can be retrieved same time using items


Indexing a sequence from the last index seq[len(seq)-n] can be written as  seq[-n]
S[:-1] is all of the string except for its last character, which is useful for removing the trailing newline from a string.

High level data type include the matrix data type provided by NumPy for multidimensional arrays
Replicating a list with * doesn’t create copies, it only creates references to the existing objects.

High level data types includes collections.Count for bags or multisets in other languages
Counter objects have a dictionary interface except that they return a zero count for missing items
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

