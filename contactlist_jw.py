class Contact(object):
	def __init__(self, first_name, last_name, 
				mobile_phone="", email=""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = mobile_phone
		self.email = email

	def send_email(self, message):
		print "To: %s - %s" % (self.email, message)

def save_contact(contact):
	contacts = []
	contacts.append(contact)
	return contacts

def write_to_text(contacts_list):
	for obj in contacts_list:
		print obj.__dict__
