import pandas as pd
from ast import literal_eval

emails = pd.read_csv('email_data_dates.csv', index_col = 0)

# parse list of recipients
emails['to_parsed'] = emails['to'].apply(literal_eval)

to_list = emails['to_parsed'].tolist()
flattened_to_list = [y.strip() for x in to_list for y in x]

from_list = emails['from'].tolist()
flattened_from_list = [y.strip() for y in from_list]

from_and_to = set(flattened_from_list + flattened_to_list)

# all emails
all_emails = list(from_and_to)

# replace blanks with dummies
all_emails = ['missing' if len(x) == 0 else x for x in all_emails]

# all emails for gremlin
gremlin_emails = ["""g.addV('person').property('id', '""" + str(i) + """')""" for i in all_emails]

# zipping columns
emails['tuples'] = list(zip(emails['from'], emails['to_parsed']))

tuples = emails['tuples'].tolist()

tuples_121 = []
for tpl in tuples:
    for x in tpl[1]:
       tuples_121.append((tpl[0].strip(),x.strip()))

tuples_121_rna = [(x,'missing') if len(y) == 0 else (x,y) for x,y in tuples_121]

gremlin_tuples = ["""g.V('""" + str(x) + """').addE('emails').to(g.V('""" + str(y) + """')).property('date', '13/01/02').property('subject', 'Trump is great')""" for x,y in tuples_121_rna]
