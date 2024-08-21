def even_process(n):
        ans = 0
        for i in range(1, n+1):
            ans += (i*2)**2
        return ans
    
def solution(n):
    return (1+n)**2/4 if n % 2 == 1 else even_process(int(n/2))
