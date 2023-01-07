numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Slicing using indexes
first_three_elements = numbers[0:3]  # First inclusive : second exclusive
print("First three elements: ", first_three_elements)

third_forth_elements = numbers[2:4]
print("Third & Forth element: ", third_forth_elements)

# Slicing with negative indexes

middle_elements = numbers[-4:-1]  # 0 is the first and -1 is the last for negative index
print("Middle elements using negative indexes: ", middle_elements)

# Slicing from first

three_to_last = numbers[2:]
print("From element three to last: ", three_to_last)

# Slicing from last

till_mentioned_no_of_item = numbers[:3]
print("From first till mentioned: ", till_mentioned_no_of_item)

# Slicing with step (list[start, end, step]) **default step 1

slice_with_step_two = numbers[1:6:2]
print("2 step interval sliced list(ex end 6): ", slice_with_step_two)

slice_with_step_three = numbers[1:8:3]
print("3 step sliced list(ex end 8): ", slice_with_step_three)

# Reverse a list using slicing

reversed_list = numbers[::-1]
print("Reversed list: ", reversed_list)

# Changing multiple list items

numbers[:3] = [-1, -2, -3]
print("First three elements changed: ", numbers)