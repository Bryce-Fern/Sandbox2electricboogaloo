Enter_password = input("Enter your password: ")
while Enter_password != "":
    for i in range(Enter_password):
        print('*', end=' ')
    print()
else:
    print("Invalid Password")
