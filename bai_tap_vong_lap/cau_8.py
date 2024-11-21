# Viết chương trình nhập vào n, tìm tất cả các số hoàn hảo nhỏ hơn n
#số hoàn hảo là tổng các ước(trừ nó ra) của cộng lại bằng chính nó.

n = int(input("Nhập số cần kiểm tra: "))

#c là số chia(nhỏ hơn n)
for c in range(1, n):
    tong = 0
    #b_c là số bị chia phải nhỏ hơn số chia
    for b_c in range(1, c):
        #tìm ước
        if (c % b_c == 0):
            tong+= b_c
    if tong == c:
            print(f"{c} la so hoan hao") 
            
    

         