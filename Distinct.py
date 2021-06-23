"""
Write a function that, given an array A consisting of N integers, returns the 
number of distinct values in array A.
"""


def solution(A):
    
    from collections import Counter
    
    counter = Counter(A)
    
    return len(counter)
        

A = [2, 1, 1, 2, 3, 1, 4]

print(solution(A))
    