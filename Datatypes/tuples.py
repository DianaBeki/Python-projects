#Tuple are imutable lists ,cant be modified
#why tuple is important ,makes things easier when you dont want to change a list.makes code more predictable-You cant start,run reverse which makes them less flexible than lists
#They are faster than a list
#geographic location and cordinatesis a  good example of tuple

my_tuple = (1,2,3,4,5)
user = {
(1,2):[1,2,3],
'basket':[1,2,3],
'greet':'hello',
'age':20
}

print(user.items()) #returns keys and values as tuples
print(user[(1,2)]) #(1,2,3)

#Tuples 2
# Tuple has only two methods that are commonly used: count() and index()
my_tuple = (1,2,3,4,5)
print(my_tuple.count(5)) #1, gives numberof occurence of a specified number
print(my_tuple.index(5)) # 4