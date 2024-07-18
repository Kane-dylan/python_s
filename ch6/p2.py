marks0 = int(input("enter your marks :"))
marks1 = int(input("enter your marks :"))
marks2 = int(input("enter your marks :"))
marks3 = int(input("enter your marks :"))
marks4 = int(input("enter your marks :"))
total_percentage = (marks0+marks1+marks2+marks3+marks4)/5

if (total_percentage>40 and marks0>=33 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
  print(f"You are passed in exam with {total_percentage}%")
else:
  print(f"You are failed in exam with {total_percentage}%")