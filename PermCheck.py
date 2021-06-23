"""
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
The goal is to check whether array A is a permutation.
"""


def solution(A):
    
    A.sort()
    
    if A[0] != 1:
        return 0
    
    values = []
    for item in A[:-1]:
        if item + 1 in A:
            values.append(1)
        else:
            values.append(0)
    
    if all(values):
        return 1
    else:
        return 0
        

print(solution([1, 2, 4, 5]))


# %%

    
def solution(A):
    
    from collections import Counter
    
    counter = Counter(A)
    
    if not all([True if val == 1 else False for val in counter.values()]):
        return 0    
    else:
        if sum(range(len(A) + 1)) == sum(A):
            return 1
        else:
            return 0
    
    
print(solution([5, 3, 1, 2, 4]))
   
       