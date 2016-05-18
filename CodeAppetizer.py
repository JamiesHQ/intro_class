food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

def convert_tuple_to_dictionary(tuple):
	dictionary = {}
	for i in range(len(food_price_tuple)):
	 	if i % 2 == 0:
	 		dictionary[food_price_tuple[i]]=food_price_tuple[i+1]
	 	# else:
	 	# 	dictionary[food_price_tuple[i]] = food_price_tuple[i]
	print food_price_tuple[i]
	return dictionary

print convert_tuple_to_dictionary(food_price_tuple)