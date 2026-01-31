def add(p,q):
   return p+q
def subtract(p,q):
   return p-q
def multiply(p,q):
   return p*q
def divide(p,q):
   return p/q
print("Please select the operators.")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice=input("enter your selection (a/b/c/d) ")
n1=int(input("enter first number "))
n2=int(input("enter second number "))
if choice=="a":
   print(n1,"+",n2,"=",add(n1,n2))
elif choice=="b":
   print(n1,"-",n2,"=",subtract(n1,n2))
elif choice=="c":
   print(n1,"*",n2,"=",multiply(n1,n2))
elif choice=="d":
   print(n1,"/",n2,"=",divide(n1,n2))
else:
   print("this is an ivalid input")
