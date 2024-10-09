import re                       #package/library regular expression
text="good day it"
if re.search("day", text):
     print("yes")
else:
     print("no")