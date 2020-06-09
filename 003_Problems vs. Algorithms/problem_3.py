def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)

def quicksort(items):
    sort_all(items, 0, len(items) - 1)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #if len(input_list) == 1:
    #    return input_list
    #if len(input_list) == 0:
    #    return 0, 0

    if len(input_list) <= 1:
        return input_list

    quicksort(input_list)

    num_max_left  = ''
    num_max_right = ''
    i = len(input_list)-1
    is_left = True

    while i >= 0:
        if is_left == True:
            num_max_left += str(input_list[i])
            is_left = False
        else:
            num_max_right += str(input_list[i])
            is_left = True
        i-=1

    return int(num_max_left), int(num_max_right)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print("========== Standard Case ==========")
test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case1)
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case2)
test_case3 = [[1, 3, 5], [53, 1]]
test_function(test_case3)

print("========== Edge Case ==========")
test_case4 = [[1, 1, 1], [11, 1]]
test_function(test_case4)
test_case5 = [[1], [1]]
test_function(test_case5)
test_case6 = [[], []]
test_function(test_case6)



