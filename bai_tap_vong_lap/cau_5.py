#Số hoàn hảo là số mà tổng các ước(trừ nó) cộng lại bằng chính nó
n = int(input("Nhập số cần kiểm tra: "))
sobichia = n
x = 0
#tìm các ước của n
for z in range(n):
    if n % sobichia == 0 and sobichia >= 1 and sobichia != n:
        print(f"{n} chia hết cho {sobichia}")
        x+=sobichia
    sobichia = sobichia - 1

if(x == n):
    print(f"Tổng của các no là {x}, vậy {n} là số hoàn hảo.")
else:
    print(f"Tổng của các no là {x}, vậy {n} không phải số hoàn hảo.")

            
            
    
            
                    
        
    
