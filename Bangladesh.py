import re
def validate_mobilenumber(number):
    pattern ="^(?:\+?880|0|88)?\s?1[3456789]\d{8}$"
    result = re.search(pattern,number)
    if result is not None:
        return True
    else:
        return False
print(validate_mobilenumber('8801534567890'))
print(validate_mobilenumber('+8801589767845'))
print(validate_mobilenumber('01534567890'))
print(validate_mobilenumber('859674124'))
