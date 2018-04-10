import pandas as pd
from email.parser import Parser

# import data
emails = pd.read_csv('emails.csv')

# Parse each field from the full enron dataset, takes too long to run from local machine
for index, email in emails.iterrows():
    if pd.notnull(email['from']) == True:
        continue
    parsed = Parser().parsestr(email.message)
    emails.loc[index,'date'] = parsed['Date']
    emails.loc[index,'from'] = parsed['From']
    emails.loc[index,'to'] = parsed['To']
    emails.loc[index,'subject'] = parsed['Subject']
    emails.loc[index,'body'] = parsed.get_payload()
    if (index % 100) == 0:
        print(index)
