
def registration_form():
    print("Registration Form")
    print()

    #get input from user
    first_name = input("Enter First Name:\t")
    last_name = input("Enter Last Name:\t")
    birth_year = input("Enter Birth year\t")
    print()

    #create strings
    name = first_name + ' ' + last_name
    temp_password = first_name + '*' + birth_year

    #display the results
    print("Welcome", name, "!")
    print("Your registration is complete!")
    print("Your temporary password is: ", temp_password)

registration_form()
