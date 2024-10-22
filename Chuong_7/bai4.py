x = int(input("Nhập thời gian sử dụng"))
if x > 0:
    U = 220
    I = 2.7
    A = U*I*x/3600
    T = A*7000
    print(f'Số tiền phải trả là: {T}')
else:
    print('Nhập lại gia tri x')    