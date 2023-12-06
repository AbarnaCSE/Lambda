import re
def validate_Password(name):
    pattern ="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    result = re.search(pattern,name)
    if result is not None:
        return True
    else:
        return False
print(validate_Password('Android11@#10'))
print(validate_Password('Iphone$45'))
print(validate_Password('Laptop#85'))
print(validate_Password('859674124'))
