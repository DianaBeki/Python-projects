# lambda expressions, are one time anonymous functions that you dont need more that once
# 

from functools import reduce 
my_list = [1, 2, 3]
lambda param: action(param)
# filter
def only_odd(item):
    return item % 2 != 0 # odd
def accumulator(acc, item):
    return acc + item

print(list(map(lambda item: item*2, my_list))) # 2, 4, 6
print(my_list) # [1,2,3]