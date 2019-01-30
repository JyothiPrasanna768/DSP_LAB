import math
print("------CALCULATOR------")
def sum(a,b):
	a+=b
	return a
def sub(a,b):
	if a>b:
		a-=b
		return a
	else 
		b-=a
		return b
def mul(a,b):
	a*=b
	return a
def div(a,b):
	q=a/b
	r=a%b
	print("\n the quotient is %s"%q)
	print("\n the remainder is %s"%r)
def sqr(a):
	x=math.sqrt(a)
	return x
while(True):
	print("\n\n choose the operation you want to perform")
	print("\n\t 1.Addition") 		
	print("\n\t 2.Subtraction")
	print("\n\t 3.Multiplication")
	print("\n\t 4.Division")
	print("\n\t 5.Square root")
	print("\n\t 6.Exit")
	choice=int(input('>'))
	if choice==1:
		print("\n\n enter the two number:")
		num1=int(input('>'))
		num2=int(input('>'))
		s=sum(num1,num2)
		print("The sum is %s"%s)
	elif choice==2:
		print("\n\n enter the two number:")
		num1=int(input('>'))
		num2=int(input('>'))
		m=sub(num1,num2)
		print("The Difference is %s"%m)
	elif choice==3:
		print("\n\n enter the two number:")
		num1=int(input('>'))
		num2=int(input('>'))
		p=mul(num1,num2)
		print("The Multiplication is %s"%p)
	elif choice==4:
		print("\n\n enter the two number:")
		num1=int(input('>'))
		num2=int(input('>'))
		d=div(num1,num2)
		print("The division is %s"%d)
	elif choice==5:
		print("\n\n enter the number:")
		num1=int(input('>'))
		r=sqr(num1,num2)
		print("The square root is %s"%r)
	else:
		print("\n\n enter the two number")
		break



		
	
