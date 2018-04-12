''' Extract email field
'''
import csv
import re
import pandas as pd
#from email.parser import Parser

# import data
emails = pd.read_csv('../../emails.csv')
print("finised reading")
emailf = open('email_data.csv','w')
csvwriter = csv.writer(emailf)
# Parse each field from the full enron dataset, takes too long to run from local machine
for index, email in emails.iterrows():
	content = email.message
	#print(content)	
	#fname = '../../maildir/allen-p/inbox/1.'
	#mfile = open(fname, 'r')
	#content = mfile.read()
	#print(content)
	#print(content)
	#print("content done")
	meta_find = True
	body_line = 0
	line_counter = 0
	for line in content.splitlines():
		#print(meta_find, line_counter, line)
		line_counter += 1
		if meta_find:
			#print("meta true")
			if re.search(r'^To:',line):
				to_field = re.sub(r'^To:(.*)', r'\1', line).split(',')
			if re.search(r'^Subject:', line):	
				subject_field = re.sub(r'^Subject:(.*)', r'\1', line)
				meta_find = False
			if re.search(r'^From:',line):
				from_field = re.sub(r'^From:(.*)', r'\1', line)
			if re.search(r'^Date:', line):	
				date_field = re.sub(r'^Date:(.*)', r'\1', line)
		elif len(line) == 0:
			body_line = line_counter
			break
	body_field = content.splitlines()[body_line:]
	#print("TO: ", to_field)
	#print("From: ", from_field)
	#print("date: ", date_field)
	#print("SUBJECT: ", subject_field)
	#print("Body: ", body_field)
	csvwriter.writerow([index, to_field, from_field, date_field, subject_field, body_field])
	if(index % 100) == 0:
		print(index)
emailf.close()
