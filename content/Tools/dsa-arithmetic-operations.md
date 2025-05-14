Title: Arithmetic Operations
Status: draft

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