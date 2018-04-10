''' Extract email field
'''

import re
fname = '1.'
mfile = open(fname, 'r')
content = mfile.read()
#print(content)
to_field = re.sub(r'To:(.*)', '\1', content)
print(to_field)
