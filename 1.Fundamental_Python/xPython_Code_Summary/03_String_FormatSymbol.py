salary = 5000 #integer (số nguyên)
salary_coefficient = 1.475 #float (số thực)
full_name = "Tran Ngoc Dung" #character / string

#--------------------------------- Format Symbol 1 -----------------------------------------------#

strTT1="Full name: "+full_name +"\nSalary: "+str(salary)
print(strTT1)

print("-"*50)

strTT2="Full name: %s \nSalary: %i \nSalary coefficient: %f"%(full_name,salary,salary_coefficient)
print(strTT2)

print("-"*50)

strTT3="Full name: %s \nSalary: %i \nSalary coefficient: %.2f"%(full_name,salary,salary_coefficient)
print(strTT3)


#--------------------------------- Format Symbol 2 -----------------------------------------------#

str1 = f'Full name: {full_name}\n Salary: {salary}\n Salary coefficient: {salary_coefficient}'
print(str1)

print('-'*50)

#Thêm dấu cách nghìn (dấu phẩy cho tiền lương) và làm tròn heSoLuong 2 chữ số thập phân
str2 = f'Full name: {full_name}\n Salary: {salary:,} VND\n Salary coefficient: {salary_coefficient:.2f}'
print(str2)

print('-'*50)

#Thêm dấu cách nghìn và làm tròn hai số lẻ cho tiền lương
str3 = f'Full name: {full_name}\n Salary: {salary:,.2f} VND\n Salary coefficient: {salary_coefficient}'
print(str3)
