#list methods
basket = [1,2,3,4,5]
print(len(basket))

#adding
basket.append(100)
new_list = basket
print(new_list) #1,2,3,4,5,100
print(basket) # 1,2,3,4,5,100

#insert adds a number to a specified index
basket.insert(4,100)
#extend takes iterable, loop over
basket.extend(100,101)

#removing
#pop removes an item at the end of a list
basket.pop()
basket.pop(0) #removes an item in the specified index
basket.remove(4)  #removes a specified number in a list
basket.clear() #removes everything from a list

#index value ,start, stop
basket = ['a', 'b', 'c', 'd', 'e']
basket.index('d') #3

basket.index('d', 0,4) #3

#keywords
print('d' in basket) #true
print('x' in basket) #false
#count retrurns  the number of times a value occurs in a list
print(basket.count 'd') #1

#sort modifies the list to be in order
basket.sort()
print(basket)

#sorted returns a sorted list inorder 
sorted(basket)
#copy returns a new list
basket.copy()
#reverse.reverse the basket in place
basket.reverse()