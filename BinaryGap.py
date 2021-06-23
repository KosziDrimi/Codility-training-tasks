"""
A binary gap within a positive integer N is any maximal sequence of consecutive 
zeros that is surrounded by ones at both ends in the binary representation of N.
The function should return the length of its longest binary gap and 0 if N 
doesn't contain a binary gap.
"""


def solution(n):
    
    n = bin(n)[2:]
    n = list(n)
    
    index = []
    
    for idx, ele in enumerate(n):
        if int(ele) == 1:
            index.append(idx)
            
    mapping = {}
    
    for ind, num in enumerate(index):  
        mapping[ind] = num
        
    mapping_new = {}
    
    for ind, num in enumerate(index[:-1]):  
        mapping_new[ind] = num
                    
    gaps = [] 
    
    for key in mapping_new.keys():
        gap = mapping[key + 1] - mapping[key] - 1
        gaps.append(gap)
    
    if len(gaps) == 0:
        return 0 
    else:
        return max(gaps)


N = [1041, 9, 529, 20, 15, 32]
# out correct: 5, 2, 4, 1, 0, 0

for n in N:
    print(solution(n))
