# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

def less_than(x, y):
    return [x for x in x if x < y]

less_than([1,11,14,5,8,9], 10)


# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_Lists(list1, list2):
    final_list = list1 + list2
    final_list.sort()
    return(final_list)

merge_Lists(l_1, l_2)

