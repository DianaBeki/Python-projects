# This program says hello and asks for my name

print('Hello World!')

print('What is your name?') #ask for their name
myname = input()
print('It is good to meet you,' + myname)
print('The length of your name is:')
print(len(myname))

print('what is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.' )