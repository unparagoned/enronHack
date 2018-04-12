import pandas as pd
from email.parser import Parser
import csv
emailf = open('email_parse.csv','w')
csvwriter = csv.writer(emailf)
# import data
emails = pd.read_csv('emails.csv')
print("read files")
# Parse each field from the full enron dataset, takes too long to run from local machine

for index, email in emails.iterrows():
    emails_line = [index,email.message]
#    if pd.notnull(email['from']) == True:
#        continue
    parsed = Parser().parsestr(email.message)
    emails_line.append(parsed['Date'])
    emails_line.append(parsed['From'])
    emails_line.append(parsed['To'])
    emails_line.append(parsed['Subject'])
    emails_line.append(parsed.get_payload())
    csvwriter.writerow(emails_line)
    if (index % 100) == 0:
        print(index)
emailf.close()
