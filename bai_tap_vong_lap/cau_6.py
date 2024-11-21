import math
n = int(input("Nhập sô nguyên dương n: "))
if n < 0:
    print("Số này không phải số chính phương")
else:
    k = math.sqrt(n)
    for i in range(n):
        if n % k == 0 and n == k**2:
            print(f'{n} là số chính phương')
            break
    else:
        print(f'{n} không phải số chính phương')
            
         
    