def process_file_to_list():
	class_grades = open("class_grades.txt")
	#read the file into a list
	class_grades_list = class_grades.readlines()
	cleaned_scores = []
	for i in class_grades_list:
		cleaned_scores.append(i.strip())
	print cleaned_scores
	return cleaned_scores
	#return the list

def convert_score_to_letter(score):
	if i >= 90:
		print score[i] + "is A."
	else:
		print "Less than A"

	#write conditionals that convert score number to letter
	#returns a letter based on each conditional


def main():
	final_grade_list = process_file_to_list()
	convert_score_to_letter(final_grade_list)
	#call function to process file and save the list to variable
	#iterate through the list and convert the score to letter
	#print the score and the letter it converts to

if __name__ == '__main__':
	main()
