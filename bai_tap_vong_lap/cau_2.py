#Tính tổng S1, S2, S3, S4
#S1 = 1+2+3+4+...+n
#tính S1= 1 + 2 + 3 + 4 + … + n
#Vì là cấp số cộng nên S1 được tính theo công thức Sn = (n*(n + 1))/2
#Tính S1
n = int(input("Nhập số n: "))
for i in range(n + 1):
    tong_S1 = (n*(n + 1))/2
    print(f'Tổng S1 là: {tong_S1}')   
    
#Tính S2    
n = int(input("Nhập n: "))
tich = 1 
for i in range(1, n):
    tich *= i
    print(f'Giá trị của S2 là: {tich}')    


