# 1) Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")

# 2) Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    start = 1
    end = 100
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

first_odds()
        
# 3) Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print((max(a_list)))

max_num_in_list("2,5,3,7,4")
# 4) Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type

def is_leap_year(a_year):
    if (a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 == 0):
        print(True)
    else:
        print(False)

is_leap_year(2004)  
# 5) Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type    

def is_consecutive(a_list):
    a_list = sorted(a_list)
    b_list = list(range(min(a_list), max(a_list) + 1, 1))
    if a_list == b_list:
        print(True)
    else: 
        print(False)
    
is_consecutive([2,3,4,5,6,7])



    

    

    


