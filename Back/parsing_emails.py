import pandas as pd
from email.parser import Parser

# import data
emails = pd.read_csv('emails.csv')

# parse each email and extract fields
for index, email in emails.iterrows():
    parsed = Parser().parsestr(email.message)
    emails.loc[index,'date'] = parsed['Date']
    emails.loc[index,'from'] = parsed['From']
    emails.loc[index,'to'] = parsed['To']
    emails.loc[index,'subject'] = parsed['Subject']
    emails.loc[index,'body'] = parsed.get_payload()
