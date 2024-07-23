name = input("Enter your username :")

if (len(name) >= 10):
  print("Username is is more then 10 characters")
else:
  print(f"Username contains {len(name)} characters")