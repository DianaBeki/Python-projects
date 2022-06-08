#create a function that receives a list and a function
#The function passed will return True or Faslse if a list
#value is odd
#The surrounding function will return a list of odd numbers

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
         
def change_list(list,func):
    oddlist = []
    for i in list:

        if func(i):
            oddlist.append(i)
        return oddlist
        print(change_list(aList, is_it_odd))