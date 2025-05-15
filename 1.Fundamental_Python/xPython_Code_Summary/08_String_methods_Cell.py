#%%
s1 = '  it CenteR one   '
k1 = s1.capitalize() #=> '  It CenteR one   '    capitalize the first character of the string
k2 = s1.upper()      #=> '  IT CENTER ONE   '    capitalize all characters
k3 = s1.lower()      #=> '  it center one   '    decapitalize all characters
k4 = s1.title()      #=> '  It CenteR One   '    capitalize the first character of each word
k6 = s1.strip()      #=> 'it CenteR One'         remove the space character ' ' from both ends
print()

s2 = ',20 30,'
k7 = s2.strip(',') #=> '20 30' remove ',' character from both ends
#------------------------------------------------------------------------------------------------#
#%%
poem = '''
Thân em vừa trắng lại vừa tròn
Bảy nổi ba chìm với nước non
Rắn nát mặc dầu tay kẻ nặn
Mà em vẫn giữ tấm lòng son
'''
print(poem)
print(poem.count('m'))
print(poem.lower().count('m'))
#method count() distinguished uppercase from lowercase, therefor poem.count('m') and poem.lower().count('m') give different results

title = 'BÁNH TRÔI NƯỚC'
print(title.count('N',2,10)) #Count the number of character 'N' from index 2 to index 10-1 (or index 9) of the string

#---------------FIND AND REPLACE--------------#
#%%
str = 'Hoa Chanh nở giữa vườn Chanh'
strFind = 'Chanh'
strReplace = 'Cam'
strNew = str.replace(strFind, strReplace)
strNew2 = str.replace(strFind, strReplace, 1) #Replace only one time at the first matched result
print()

#------------------------------------------------#
#%%
hoten = 'Trần Thị Anh Thư'
i = hoten.find(' ') #Tìm ký tự ' ' đầu tiên từ trái qua rồi trả về index của nó
j = hoten.find(' ',i+1) #Tìm ký tự ' ' bắt đầu từ vị trí i+1 trở đi
k = hoten.rfind(' ') #Tìm ký tự ' ' theo hướng từ phải sang
print()

# %%
sdt = '0903123456'
k1 = sdt.isdigit() #=> True / Nếu có dính một ký tự alphabetic vào thì sẽ thành False
k2 = sdt.isnumeric() #=> True / Nếu có dính một ký tự alphabetic vào thì sẽ thành False

tien = '1500VND'
id = 'ASDK'
k3 = tien.isalpha() #=> F
k4 = id.isalpha() #=> T / Nếu có dính một ký tự numeric vào thì sẽ thành False
k5 = tien.isalnum() #=> F
k6 = id.isupper() #=> T
k7 = id.islower()#=> F

#%%
#------------_format()---------------#
soTien = 1200000000.453
str_tien1 = '{:,} VND'.format(soTien) # '1,200,000,000.453 VND'
str_tien2 = '{:,.2f} VND'.format(soTien) # '1,200,000,000.45 VND'
# .format() giúp chuyển dữ liệu từ số sang chuỗi 
print()

#%%
#----------------Căn lề --------------------#
strD = 'Abc'
str1 = strD.center(20)     #'        Abc         '
str2 = strD.center(20,'*') #'********Abc*********'
str3 = strD.rjust(20) #Căn lề  phải với khoảng cách 20 ký tự
str4 = strD.ljust(20) #Căn lề  trái với khoảng cách 20 ký tự
