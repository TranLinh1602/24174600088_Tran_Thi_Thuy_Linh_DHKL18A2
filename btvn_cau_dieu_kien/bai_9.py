# Tính cước tacxi: 
print("1. Xe 4 chỗ\n2. Xe 7 chỗ")
loaixe = float(input("Nhập loại xe bạn muốn đi:"))
if loaixe != 1 and loaixe != 2:
    print("Bạn chỉ được chọn 1 trong 2 xe")
# -	Loại xe 4 chỗ
elif loaixe == 1:
    print("Bạn đã chọn loại xe 4 chỗ.")
    km = float(input("Nhập số km bạn muốn di chuyển:"))
    if km < 0:
        print("Số km không được nhỏ hơn 0.")
    elif km <= 20:
        #đi dưới 20km thì trừ đi 0.8km giá mở cửa
        gia_mua_cua = 11000
        km_dichuyen = ((km - 0.8)) * 12100
        print(f"Số tiền phải trả là {float(gia_mua_cua + km_dichuyen)}vnđ")

    elif km > 20:
        #đi hơn 20km thì trừ đi 0.8 với 20km đầu.
        gia_mua_cua = 11000
        km_20 = 20 * 12100
        km_dichuyen = (km - 0.8 - 20) * 10000
        print(f"Số tiền phải trả là {float(gia_mua_cua + km_dichuyen)}vnđ")



# -	Loại  xe 7 chỗ
elif loaixe == 2:
    print("Bạn đã chọn loại xe 7 chỗ.")
    km = float(input("Nhập số km bạn muốn di chuyển:"))
    if km < 0:
        print("Số km không được nhỏ hơn 0.")
    elif km <= 30:
        #đi dưới 30km thì trừ đi 0.8km giá mở cửa
        gia_mua_cua = 13000
        km_dichuyen = ((km - 0.8)) * 14100
        print(f"Số tiền phải trả là {float(gia_mua_cua + km_dichuyen)}vnđ")

    elif km > 30:
        #đi hơn 30km thì trừ đi 0.8 với 30km đầu.
        gia_mua_cua = 13000
        km_20 = 20 * 12100
        km_dichuyen = (km - 0.8 - 20) * 12000
        print(f"Số tiền phải trả là {float(gia_mua_cua + km_dichuyen)}vnđ")