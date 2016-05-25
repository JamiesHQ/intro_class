import contactlist
import twitter

contacts_list =[]

contact1 = contactlist.Contact("Julia","Schnell")
contact2 = contactlist.Contact("Jamie", "Whitacre")
contact3 = contactlist.Contact("Faith","Wei")

contacts_list.append(contact1)
contacts_list.append(contact2)
contacts_list.append(contact3)

for item_contact in contacts_list:
    print item_contact.first_name, item_contact.last_name, item_contact.mobile_phone
