Title: Learning Notes: Pointer Dynamics
Date: 2025-06-05
Status: published

<!-- Pointers at two different positions, we can compare the elements and make decisions based on comparisons
Comparing every two elements doesn't take advantage of predictable dynamics exist within data structure  -->

<!-- Two Pointers -->

Sorted array: When we move a pointer we can predict whether the value being moved to is greater or smaller

```
#167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) -1

        while i < j:

            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i]+numbers[j] < target:
                i = i+1
            elif numbers[i]+numbers[j] > target:
                j = j-1
```

Symmetrical pattern allows us to move two pointers toward the center


```

#125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        l = [c for c in s if ((c in string.ascii_lowercase) or (c in string.digits))]
        s = "".join(l)

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right -1

        return True


```

Fast and Slow Pointers: Relative position of two pointers gathers information about the data structure rather than indexing

```
#876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        while (fast.next is not None) and (fast is not None):

            fast = fast.next.next
            slow = slow.next

        return slow

"""
