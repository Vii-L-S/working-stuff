import random
def rand_upp_case():
	upper_case = random.randint (65, 90)
	upper_case = chr(upper_case)
	return upper_case

def rand_low_case():
	lower_case = random.randint (97, 122)
	lower_case = chr(lower_case)
	return lower_case

def rand_digit():
	digit = random.randint (48, 57)
	digit = chr(digit)
	return digit

def symbol():
	symbol = random.randint (33, 47)
	symbol = chr(symbol)
	return symbol
	
def length_string():
	status = False
	while status == False:
		pss_len = int(input('How long do you require the password?(8-25): '))
		if (pss_len>= 8) and (pss_len <= 25):
			status = True
		return pss_len

def main():
	pass_string = ''
	pss_len = length_string()
	
	for x in range(pss_len):
		rand_selection = random.randint(1, 4)
		if (rand_selection == 1):
			pass_string = pass_string + (rand_upp_case())
		elif (rand_selection == 2):
			pass_string = pass_string + (rand_low_case())
		if (rand_selection == 3):
			pass_string = pass_string + (rand_digit())
		if (rand_selection == 4):
			pass_string = pass_string + (symbol())
			
	print(pass_string)

if __name__ == "__main__":
	main()
