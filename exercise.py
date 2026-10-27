username=input("enter the user name: ")
if len(username)>12:
    print("username must be less than 12 characters")
elif username.isalpha()==False:
    print("username should only contain alphabets")
else :
    print(username)