""" 
If the string x equals "(name, date),\n", which of
the following would return a string containing "name, date"?
x.rstrip("),")
x.strip("),\n")
x.strip("\n)(,") -> right
"""
str="(name, date),\n"
print(str.strip("\n)(,"))