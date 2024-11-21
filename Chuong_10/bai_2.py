#Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
chuoi_nhap_vao = input("Nhập chuỗi: ")
ket_qua = " ".join(chuoi_nhap_vao.split())
print(f'{ket_qua}')