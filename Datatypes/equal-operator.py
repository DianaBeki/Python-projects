#is vs ==
from sqlalchemy import true


print(True == 1) #true
print('' == 1) #false
print([] == 1) #false
print(10 == 10.0) #true
print([] == []) #true

# ==checks for equality
#is keyword checks if the location in memory where value stored is the same
print(True is 1) #false
print('' is 1) #false
print([] is 1) #false
print(10 is 10.0) #false
print([] is []) #false