import re

email = "daps@gmail.com"
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

if not valid:
    print("BNot a valid email")
else:
    print("Valid email")