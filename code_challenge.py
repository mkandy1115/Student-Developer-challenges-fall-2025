# Matthew Andrus
# This is the code answer to the challenge option 2 for the student developer position.

# Option 2 (includes all 4 sections below):

"""
1: Write a function that will reverse the given input string.
For Example: function("string") -> "gnirts"
"""

def str_reverse(usrstr):
    reverse_str = usrstr[::-1] #save to reverse_str using list slicing, backward step
    return reverse_str

"""
2: Write a function that accepts three integers as input and returns as output the
largest of the three.
For Example: function(1, 3, 2) -> 3
"""

def max_of_three(num1, num2, num3):
    numlist = [num1, num2, num3] #save values to a list, since there are only three
    return max(numlist) #only returns the largest number of the list

"""
3: Write a function that calculates the factorial of an input integer using recursion.
Factorial: n! = n * (n-1) * (n-2) * ... * 1, so 3! = 3 * 2 * 1 = 6
For Example: function(3) = 6
"""

def recursive_factorial(usrnum, result = 1): #takes an  user input integer and a result(integer)
    if usrnum == 1:
        return result # Base case; returns the result if the input is 1
    else:
        result = result * usrnum # if input is not 1, times the result by the input
        return recursive_factorial(usrnum-1,result) # recursively call this fanction with an input one less than the original until it is 1.

"""
4: Write a function that calculates the Nth entry of the Fibonacci sequence (Do not
include 0 in the sequence).
Fibonacci Sequence: 1, 1, 2, 3, 5, 8, ...
The sequence is calculated by summing two numbers and adding the sum to the
sequence.
1 (the sequence starts with 1)
1 + 0 = 1 (1 was the only element, so add 0, then put the result on the end of the
sequence
1, 1
1 + 1 = 2
1, 1, 2
1 + 2 = 3
1, 1, 2, 3
2 + 3 = 5
1, 1, 2, 3, 5
etc.
So your function should behave as
function(1) -> 1
function(2) -> 1
function(3) -> 2
function(4) -> 3
function(5) -> 5
etc.
"""

def fibonacci(term_index, lst_fib = [1,1]): # takes user-input integer and a list of Fibonacci sequence, wihch is to be implemented recursively
    if term_index == 1 or term_index == 2: 
        return 1 #return 1 if input term index is 1 or 2
    elif term_index == len(lst_fib) + 1: 
        return lst_fib[term_index-2] + lst_fib[term_index-3] # Base case; returns the sum of last 2 values of the list if the index is just 1 above the length of the list
    else:
        lst_fib.append(lst_fib[len(lst_fib)-1] + lst_fib[len(lst_fib)-2]) # othewise create the list of Fibonacci sequence recursively, until the length of the list is 1 below the user-input index
        return fibonacci(term_index, lst_fib)
        

def main():
    print(str_reverse("gnik"))
    print(max_of_three(3,5,66))
    print(recursive_factorial(4))
    print(fibonacci(17))
    
if __name__ == "__main__":
    main()

