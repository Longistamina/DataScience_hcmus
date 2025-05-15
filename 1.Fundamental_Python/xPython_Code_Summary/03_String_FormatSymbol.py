tienluong=5000 #integer (số nguyên)
heSoLuong=1.475 #float (số thực)
hoten="Trần Ngọc Dung" #character / string

#--------------------------------- Format Symbol 1 -----------------------------------------------#

strTT1="Họ tên: "+hoten +"\nTiền lương: "+str(tienluong)
print(strTT1)

print("-"*50)

strTT2="Họ tên: %s \nTiền lương: %i \nHệ số lương: %f"%(hoten,tienluong,heSoLuong)
print(strTT2)

print("-"*50)

strTT3="Họ tên: %s \nTiền lương: %i \nHệ số lương: %.2f"%(hoten,tienluong,heSoLuong)
print(strTT3)


#--------------------------------- Format Symbol 2 -----------------------------------------------#

str1 = f'Họ tên: {hoten}\n Tiền lương: {tienluong}\n Hệ số  lương: {heSoLuong}'
print(str1)

print('-'*50)

#Thêm dấu cách nghìn (dấu phẩy cho tiền lương) và làm tròn heSoLuong 2 chữ số thập phân
str2 = f'Họ tên: {hoten}\n Tiền lương: {tienluong:,} VND\n Hệ số  lương: {heSoLuong:.2f}'
print(str2)

print('-'*50)

#Thêm dấu cách nghìn và làm tròn hai số lẻ cho tiền lương
str3 = f'Họ tên: {hoten}\n Tiền lương: {tienluong:,.2f} VND\n Hệ số  lương: {heSoLuong}'
print(str3)
