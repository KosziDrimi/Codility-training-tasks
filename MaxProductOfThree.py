"""
A non-empty array A consisting of N integers is given. The product of triplet 
(P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
Your goal is to find the maximal product of any triplet.
"""


def solution(A):
    
    A.sort()
    
    if A[0] < 0 and A[1] < 0 and A[-1] > 0 and A[-2] > 0 and (abs(A[0]) + abs(A[1]) > A[-1] + A[-2] or abs(A[0]) + abs(A[1]) > A[-3] + A[-2]):
        return A[0] * A[1] * A[-1]
    else:
        return A[-3] * A[-2] * A[-1]
    


if __name__ == '__main__':
    
    A = [-5, -5, 4, 5]
    B = [-5, -6, -4, -7, -10]
    C = [4, 7, 3, 2, 1, -3, -5] 
    D = [-3, 1, 2, -2, 5, 6]
  
    lists = [A, B, C, D]
    
    for lista in lists:
        print(solution(lista))  
