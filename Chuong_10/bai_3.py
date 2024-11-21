# Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
chuoi_nhap_vao = input("Nhập chuỗi: ")
ket_qua = chuoi_nhap_vao.split()
Ho = ket_qua[0]
Ten = ket_qua[-1]
print(f'{Ho}')
print(f'{Ten}')