# Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
chuoi_nhap_vao = input("Nhập chuỗi: ")
if len(chuoi_nhap_vao) > 1 and chuoi_nhap_vao[0] == '-' and chuoi_nhap_vao[1:].isdigit():
    print("Day la so am")
else:
    print("Day khong phai so am")
        
    