import math 
x = float(input('Nhập giá trị của x:'))
if 0 < x < 1 or x > 1:
    F = math.log(x, 4) + math.log(2, x)
    print(f'Gia tri cua bieu thuc la: {F:.2f}')
else:
    print('Khong tinh duoc gia tri F')    