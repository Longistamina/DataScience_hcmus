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
full_name = 'Trần Thị Anh Thư'
i = full_name.find(' ') #Find the first ' ' character from left to right, and return its index
j = full_name.find(' ', i+1) #Find ' ' character from index i to end
k = full_name.rfind(' ') #Find the first ' ' character from RIGHT to left, and return its index
print()

# %%
phone = '0903123456'
k1 = phone.isdigit() #=> True if all characters are DIGITS. Else if there is at least one alphabetic character, return False
k2 = phone.isnumeric() #=> True if all characters are NUMERIC. Else if there is at least one alphabetic character, return False

money = '1500VND'
id = 'ASDK'
k3 = money.isalpha() #=> True if all characters are ALPHABETIC. Else if there is at least one numeric or digit character, return False
k4 = id.isalpha() #=> True if all the characters are alphanumeric (like "Company123", "4student5")
k5 = money.isalnum() #=> F
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
