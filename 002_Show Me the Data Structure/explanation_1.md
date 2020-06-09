# Problem 1 : LRU Cache
To implement LRU cache problem, we can use queue data structures.
For this problem, I have used `OrderDict` because I want to use the method of 'popitem'.
By using 'popitem', we can easily remove the first element added.

# Time complexity
`get()` is `O(1)`. `set()` is `O(1)`.
Space complexity of the LRU Cache is `O(n)`.
