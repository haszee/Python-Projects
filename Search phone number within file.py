import zipfile
import shutil
import os
import re
import pdb
import random

# with zipfile.ZipFile('C:\\Users\\New Owner\\Documents\\CompSciLearning\\unzip_me_for_instructions.zip', 'r') as zip_ref:
# 	zip_ref.extractall('C:\\Users\\New Owner\\Documents\\CompSciLearning')

shutil.unpack_archive('unzip_me_for_instructions.zip', 'C:\\Users\\New Owner\\Documents\\CompSciLearning')

for folder in os.listdir('C:\\Users\\New Owner\\Documents\\CompSciLearning\\extracted_content'):
	print(f'\nCurrent Folder: {folder}')
	current_folder = f'C:\\Users\\New Owner\\Documents\\CompSciLearning\\extracted_content\\{folder}'
	if folder == 'Instructions.txt':
		continue
	else:
		for text_file in os.listdir(current_folder):
			# print(f'\nCurrent file is {text_file}')
			os.chdir(current_folder)
			with open(text_file) as f:
				content = f.read()
			if re.search(r'\d{3}-\d{3}-\d{4}', content):
				phone = re.search(r'\d{3}-\d{3}-\d{4}', content)
				print('\n',phone.group())
			f.close()
		
				


