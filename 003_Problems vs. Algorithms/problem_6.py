def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    max = - float("inf")
    min =  float("inf")

    for it in ints:
        if it > max:
            max = it
        if it < min:
            min = it

    return (min, max)

## Example Test Case of Ten Integers
import random

print("========== Standard Case ==========")
l = [i for i in range(0, 10)]
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(-5, 12)]
random.shuffle(l)
print("Pass" if ((-5, 11) == get_min_max(l)) else "Fail")

l = [i for i in range(500, 501)]
random.shuffle(l)
print("Pass" if ((500, 500) == get_min_max(l)) else "Fail")


print("========== Edge Case ==========")
l = [i for i in range(-44, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-44, -2) == get_min_max(l)) else "Fail")

l = []
print("Pass" if (None == get_min_max(l)) else "Fail")

