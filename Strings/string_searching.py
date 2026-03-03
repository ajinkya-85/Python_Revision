# find() reutrn's int
""" 
find returns
the position(index) of the first character of the first instance of substring in the string
object, or -1 if substring doesn't occur in the string
"""
str = "aaaaajinkyaaa"
print(str.find('n'))

# we can privide additional optional aurguments like range.
# first no. is start from and ignore before.
# second no. is for end and ignore after.
print(str.find("a",5,-3))
