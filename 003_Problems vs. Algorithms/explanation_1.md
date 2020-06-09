## Problem 1: Finding the Square Root of an Integer
This algorithm is to search for the floored square root with binary search.
If the input number is -1, the square root cannot be calculated, so None is returned.
When the input value is 0 or 1, the square root value is the same as the input value, so the input value is returned.
The search space is divided into two parts, the mid point power is calculated, and it is checked each time whether it is larger or smaller than the specified number.

## Time and Space complexity:
Since I used binary search for the search, the time complexity is O (log (n)).
The space complexity is O (1), because it only performs array operations.

