bill_amount = float(raw_input("What is the bill amount?> "))
tip_percentage = float(raw_input("What is the tip percentage?> "))
number_people = int(raw_input("How many people in your party?> "))

def calculate_tip(bill_amount, tip_percentage):
	tip_amount = bill_amount*(tip_percentage/100)
	return tip_amount

def total_bill(tip_amount, bill_amount):
	total_bill = tip_amount + bill_amount
	return total_bill

def split_bill(total_bill, number_people):
	price_per_person = total_bill/number_people
	return price_per_person

print calculate_tip(bill_amount, tip_percentage)
print total_bill(tip_amount, bill_amount)
print split_bill(total_bill, number_people)