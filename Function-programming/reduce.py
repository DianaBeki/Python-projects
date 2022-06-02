# reduce(), 
# from functools import reduce
# functools, is a tool box for tools that come with py installation
# 
from functools import reduce 
my_list = [1, 2, 3]
def multpily_by2(item):
    return item*2
# filter
def only_odd(item):
    return item % 2 != 0 # odd
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 0)) #01, 12, 33, 6
print(my_list) # [1,2,3]

my_list = [5,4,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list) # [25, 16, 9]

# list sorting

a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
# def sortList(x):
#     return x[1]

# a = [(0,2), (4,3), (9,9), (10, -1)]
# a.sort(key = sortList)
# print(a[1])