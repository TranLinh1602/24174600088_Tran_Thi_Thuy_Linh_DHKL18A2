# Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
chuoi_nhap_vao = input("Nhap chuoi: ")
if chuoi_nhap_vao.count(".") == 1  and chuoi_nhap_vao.replace(".","").isdigit():
    print("Day la so thap phan")
else:
    print("Day khong phai so thap phan")      