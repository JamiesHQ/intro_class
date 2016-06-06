def calculate_tip(bill_amount, percentage):
	tip = bill_amount * percentage * .01
	return tip

def bill_splitter(bill_amount, tip_percentage, number_guests):
	tip_amount = calculate_tip(bill_amount, tip_percentage)
	bill_total = bill_amount + tip_amount
	cost_per_person = bill_total / number_guests
	return cost_per_person

cost_per_guest = bill_splitter(138.46, 18, 4)
print "Amount per person is: " + str(cost_per_guest)