#lists is an ordered sequence of objects
#l1 = [1,2,3,4,5]
# in python  lists are like arrays
#Data structure
#A way for us to organise information and data into a folder so that it can be used for different purposes.A container around your data
amazon_cart = ['notebook', 'sunglasses']
print(amazon_cart[0]) #notebook

#list slicing
'notebook'
'sunglasses'
'toys'
'grapes'
print(amazon_cart[0:2]) #notebook, sunglasses
print(amazon_cart[0::2]) #notebook,toys
#lists are mutable
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:] #used to copy the entirre list
new_cart[0] = 'gun'
print(new_cart) #gun ,sunglasses,toys
print(amazon_cart) #laptop,sunglasses,toys,grapes