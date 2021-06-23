"""
An array A consisting of N different integers is given. The array contains integers
in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
"""


def solution(A):
    
    A.sort()
    
    if len(A) == 0 or A[0] != 1:
        return 1
    for item in A:
        if item + 1 in A:
            continue
        else: 
            return item + 1


print(solution([1, 2, 4]))



# %%

def solution(A):
    
    if len(A) == 0:
        return 1
    elif sum(range(max(A) + 1)) - sum(A) == 0: 
        return max(A) + 1
    else:
        return sum(range(max(A) + 1)) - sum(A)


print(solution([1, 2, 4]))
