import re
def validate_Telephone(number):
    pattern ="(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})"
    result = re.search(pattern,number)
    if result is not None:
        return True
    else:
        return False
print(validate_Telephone('321-963-0612'))
print(validate_Telephone('321-545-0612'))
print(validate_Telephone('01534567890'))
print(validate_Telephone('859674124'))
