import os
import sys
import string
import random
import requests

import api_true_random_number_gen #requires api_true_random_number_gen.py class



def rand_letter(ran_num):
		rand_name = ""
		for i in range(ran_num): #janitor note: is there a way to make this a list comprehension?
			rand_name = rand_name + random.choice(string.ascii_lowercase)
		return(rand_name)
		
		
def name_creator(x):  
	
	num_class = api_true_random_number_gen.true_random(13)

	with open('names.txt', 'w') as f:
	
		while(x > 0):
			pass_num = num_class.get_true_rand()
			f.write(rand_letter(pass_num) + "\n")
			x = x - 1
		
	f.close()
	print('...completed')
	

if __name__ == '__main__':

	#janitor note: input needs to be sanitized/re
	total_names = input('Enter number of names you would like created: ')	

	name_creator(int(total_names))