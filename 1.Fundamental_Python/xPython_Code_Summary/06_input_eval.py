#---------------------------------------- input() --------------------------------------#
x = int(input("Input variable x: "))
y = int(input("Input variable y: "))
print("Sum x + y =", x+y)
print("Subtract x - y =", x-y)
print("Multiplication x*y = ", x*y)
print("Division x/y =", x/y)


#---------------------------------------- eval() --------------------------------------#
k1=eval('2+3+5') #---> eval considers this as a mathematic expression, hence returns 10 as the result of 2+3+5
k2=eval('25') #---> eval considers this as an integer, hence returns 25 as integer
k3=eval('1.75') #---> eval considers this as a real number, hence returns 1.75 as float
k4=eval('20,23,45') #----> eval considers this as a tuple, hence returns (20, 23, 45) as a tuple
k5=eval('[12,13,14,15]') #----> eval considers this as a list, hence returns [12, 13, 14, 15] as list
print()

k=eval('abc') #--> raise error because eval considers this abc as an undefined variable
