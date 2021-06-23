
def solution(n):
    
    n = list(str(n))
    
    index = [idx for idx, ele in enumerate(n) if ele == '5']
   
    news = [n[:i] + n[i+1:] for i in index]
    
    nums = [int(''.join(item)) for item in news]
    
    return max(nums)
   
    

if __name__ == '__main__':
    
    numbers = [15958, -15958, -5000, 55, 505, -505]
    
    for num in numbers:
        print(solution(num))    
  