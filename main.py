import re

# format = local_part@domain.TLD
# ^ this mean start with 
# [a-zA-Z] means all characters between a-z and A-Z
# * means atleast 0 or more times
# + means atleast 1 or more times
# {2,} means atleast 2 or more times
# $ means end with
# \. means dot character if we want to match dot character specifically otherwise 
# if . is there without \ it means any character
local_part = r'^[a-zA-Z][a-zA-Z0-9]*[\._$]*'
domain_part = r'[a-zA-Z][a-zA-Z0-9]*'
TLD_part = r'\.[a-zA-Z]{2,}$'
email_format =  local_part + '@' + domain_part + TLD_part

def isValidEmail(email):
    if re.match(email_format, email) and '..' not in email:
        return True
    return False

email = input("Enter your email: ")
if isValidEmail(email):
    print("Valid Email")
else:
    print("Invalid Email")