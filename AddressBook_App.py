
addressBook = {'joshua': ['Chennai',123456789, 'josh@gmail.com'],
               'jeffrey': ['Bombay',123456789, 'ru@gmail.com'],
               'cathy': ['cochin',98765478, 'baby@ yahoo.com']}

'''Now we needed a while loop because if the user presses a unwanted number the code should exit'''

def get_details():
    name = input("Enter Name : ")
    city = input("Enter City : ")
    name = name.lower()
    city = city.lower()
    phone_no = int(input("Enter Mobile # : "))
    email = input("Enter mail address : ")

    return name, city, phone_no, email

while True:
    option = int(input("***  Option Menu *** \n 1.Add\n 2.Search \n 3.Update \n 4.Show All \n 5.Delete \n 6.Quit\n"))

    if option == 1:
        name,city,phone_no, email = get_details()
        if name != name:
            addressBook[name] = [city,phone_no,email]
            print("Person added succesfully ")
        else:
            print("person already exists")

    elif option == 2:

        ch = int(input(" 1 ==> Search by Name : \n 2 ==> Search by City"))
        p_found = False

        if ch == 1:
            s_name = input("Enter Name : ").lower()
            for i in addressBook.items():
                name,info = i
                if s_name == name:
                    p_found = True
                    print('{:<10}{:<10}{:<15}{:<15}'.format(name, info[0], info[1], info[2]))
            if not p_found:
                print("Person not found")
        else:
            s_city = input("Enter City : ").lower()
            for i in addressBook.items():
                name,info = i
                if s_city == info[0]:
                    p_found = True
                    print('{:<10}{:<10}{:<15}{:<15}'.format(name, info[0], info[1], info[2]))
            if not p_found:
                print("Person not found")

    elif option == 3:
        vari = True
        u_name = input("Enter Name : ").lower()
        try:
            info = addressBook[u_name]
            new_city = input("Enter the city name : ")
            new_phoneNo = int(input("Enter the new phone no : "))
            new_email = input("Enter the new email : ")
            addressBook[u_name] = [new_city,new_phoneNo,new_email]
            vari = False

        except:
            print("Person not found")

        if not vari:   # this is just an experiment as in how to break from the outer while loop if we updated and not getting the same prompt
            break




    elif option == 4:
        print('{:<10}{:<10}{:<15}{:<15}'.format("Name", "City", "Phone_No", "Email"))
        for i in addressBook.items():  # we need to add .items so that it just doesnt prints the keys but also values
            name,info = i              # in this case i will represent the key and info will be the list of values. this is the syntax
            print('{:<10}{:<10}{:<15}{:<15}'.format(name,info[0],info[1],info[2]))

    elif option == 5:
        d_name = input("Enter Name : ")
        try:
            del addressBook[d_name]
            print("Person deleted")
        except:
            print("No such person found")

    else:
        break

