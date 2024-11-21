#Nhập vào số nguyên dương a, in ra bảng cửu chương a
a = int(input("Nhập số nguyên dương a: "))
for i in range(1, 10):
    tich = a*i
    print(f'{a} x {i} = {tich}')