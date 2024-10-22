import math 
x = float(input('Nhập giá trị của x'))
if 0 < x < 1 and x > 1:
    F = math.log(4,x) + math.log(x, 2)
    print(f'Gia tri cua bieu thuc la: {F:.2f}')
else:
    print('Khong tinh duoc gia tri F')    