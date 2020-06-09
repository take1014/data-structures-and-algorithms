# Problem 2 : File recursion
To search many folders to find the desired file, I decided to do a recursive search.
If a file with the specified extension exists in the folder, the file name is saved.
If there is another folder in the folder, the 'find_files' function is recursively called to search a deeper directory.

# Time complexity
Time complexity is `O(n)` and space complexity is `O(n)`.
