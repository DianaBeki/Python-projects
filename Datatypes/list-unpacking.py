# list unpacking
#breakdown
a,b,c = [1, 2, 3]
a,b,c = [1,2,3,4,5,6,7,8,9]
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# summary
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)  #1
print(b) #2
print(c) #3
print(other) #4,5,6,7,8
print(d) #9