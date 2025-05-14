Title: Control Flow
Status: draft

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