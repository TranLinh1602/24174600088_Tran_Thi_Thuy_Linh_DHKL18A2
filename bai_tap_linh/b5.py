#Viết chương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó
a = int(input("Nhập số a cần kiểm tra: "))
b = int(input("Nhập số b cần kiểm tra: "))
n = 0
if a < b:
    n = b
else:
    n = a
so_bi_chia = n
for i in range(n + 1):
    if a % so_bi_chia == 0 and b % so_bi_chia == 0:
        print(f'{i}')
        break
    so_bi_chia += -1    
    
     