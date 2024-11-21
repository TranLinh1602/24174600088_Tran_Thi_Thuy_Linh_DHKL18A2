#Hiển thị tất cả các ước của một số tự nhiên
n = int(input("Nhập số nguyên dương n: "))
if n < 0:
    print("Hãy nhập một số khác")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(f'Ước của {n} là {i}')   