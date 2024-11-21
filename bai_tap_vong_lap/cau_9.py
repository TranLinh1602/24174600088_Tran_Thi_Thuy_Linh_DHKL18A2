n = int(input("Nhập số cần kiểm tra: "))
for i in range(1, n + 1 ):
    for k in range(1, int(n**0.5) + 1):
        if k * k == i:
            print(f'{i}')
            break
        