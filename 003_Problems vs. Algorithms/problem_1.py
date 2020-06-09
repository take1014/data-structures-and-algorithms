def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    elif (number == 0) or (number == 1):
        return number

    start = 0
    end   = number // 2

    while start <= end:
        middle = (end+start)//2
        middle_pow = middle*middle

        if middle_pow == number:
            return middle
        elif middle_pow < number:
            start = middle+1
            result = middle
        else:
            end = middle-1

    return result

print ("========== Standard Case ==========")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


print ("========== Edge Case ==========")
print("Pass" if (None == sqrt(-1)) else "Fail")
# sqrt(-1) -> None
print("Pass" if (331476 == sqrt(109876543210)) else "Fail")
# sqrt(109876543210) -> 331476
