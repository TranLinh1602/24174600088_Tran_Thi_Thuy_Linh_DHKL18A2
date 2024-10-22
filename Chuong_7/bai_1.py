#Bài1 
r = float(input("nhập bán kính hình trụ:"))
h = float(input("nhập chiều cao hình trụ:"))
pi = 3.14
if r > 0 and h > 0:
    V = pi*r*r*h
    Sxq = 2*pi*r*h
    Stp = 2*pi*r*h + 2*pi*r*r
    print(f'Thể tích hình trụ là {V:.2f}')
    print(f'Diện tích xung quanh là {Sxq:.2f}')
    print(f'Diện tích toàn phần là {Stp:.2f}')
else:
    print('Giá trị không hợp lệ')    


