
p0="Make a lot of money"
p1="buy now"
p2="subscribe this"
p3="click this"

message = input("Enter your message :")
if (p0 in message or p1 in message or p2 in message or p3 in message ):
  print("This is spam !!!")

else :
  print(message)