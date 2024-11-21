#Viết chương trình kiểm tra số có phải số hoàn hảo
n = int(input("Nhập n: "))
tong = 0
if n <= 1:
    print("Số này không hợp lệ")
else:
    for i in range(1,n):
        if n % i == 0:
            tong += i
    if n == tong:
        print(f'{n} la so hoan hao')    
    else:
        print(f'{n} khong la so hoan hao')        
            
                
    