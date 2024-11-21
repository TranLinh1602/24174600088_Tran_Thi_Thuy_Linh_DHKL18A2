# Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi
chuoi_nhap_vao = input("Nhap chuoi: ")
ki_tu_dac_biet = 0
chu = 0 
so = 0
for i in chuoi_nhap_vao:
    if i.isalpha() == True:
        chu = chu + 1
    else:
        if i.isdigit() == True:
            so = so + 1
        else:
            ki_tu_dac_biet = ki_tu_dac_biet + 1
print(f"Chữ là: {chu}")
print(f"Số là: {so}")
print(f"Kí tự đặc biệt là: {ki_tu_dac_biet}")                   
        