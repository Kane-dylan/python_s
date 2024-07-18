n1=int(input("enter a number :"))
n2=int(input("enter a number :"))
n3=int(input("enter a number :"))
n4=int(input("enter a number :"))

if ((n1>n2) and (n1>n3) and (n1>n4)):
  print(f"{n1} is the greatest number")
if ((n2>n1) and (n2>n3) and (n2>n4)):
  print(f"{n2} is the greatest number")
if ((n3>n2) and (n3>n1) and (n3>n4)):
  print(f"{n3} is the greatest number")
if ((n4>n2) and (n4>n3) and (n4>n1)):
  print(f"{n4} is the greatest number")