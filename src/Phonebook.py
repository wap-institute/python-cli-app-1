import json
class Phonebook : 
    def __init__(self) : 
        newContact = {
            "name": "",
            "mobile": ""
        }
        f = open('./json/data.json')
        contacts = json.load(f)
        print("\nSaved Contacts")
        for contact in contacts : 
            print("==============")
            print(contact["name"])
            print(contact["mobile"])
        print("\nCreate contact")
        newContact['name'] = input("Enter name :- ")
        if newContact['name'] == "exit()" : quit()
        newContact['mobile'] = input("Enter number :- ")
        if newContact['mobile'] == "exit()" : quit()
        contacts.append(newContact)
        file = open("./json/data.json", "w")
        string = json.dumps(contacts)
        file.write(string)
        file.close()
        print("Contact Saved !\n")