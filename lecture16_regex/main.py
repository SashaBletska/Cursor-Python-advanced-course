import re

print("=======================================================")
print("1. Write a Python program which search a phone numbers.")
pattern = r'\b[\d]{3}-?[\d]{2}-?[\d]{2}\b'
text = 'Hello, my phone numbers is 125-98-70 and 8908934 and 908-98-30'
res_phone = re.findall(pattern=pattern, string=text)


def search_phone():
    if res_phone:
        str_phone = ', '.join([str(elem) for elem in res_phone])
        return f"Your phone numbers: {str_phone}"
    else:
        return "There is no phone numbers"


print(search_phone())

print("=========================================================================================================")
print("2. Write a Python program basic validation for email. Local part should be consisted of lower/upper case,\n"
      "number, underscore and dot. Domain part - the same but dot symbol could not be the first character.")
pattern = r'^[^\.][A-Za-z0-9_\.]{1,255}[^\.]@[^\.][A-Za-z0-9_\.]{1,255}\.[A-Za-z0-9_\.]{1,10}[^\.]$'
text = 'cursor.test@cursor.com.ua'
res_email = re.findall(pattern=pattern, string=text)


def email_validity():
    if res_email:
        str_email = ' '.join([str(elem) for elem in res_email])
        return f"{str_email} - valid email"
    else:
        return "Email is invalid"


print(email_validity())

print("=======================================================================")
print("3. Write a Python program to remove redundant zeros from an IP address.")
pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
text = '200.049.000.010'

res_ip_digits = re.findall(pattern=pattern, string=text)
res_to_str = '.'.join([str(elem) for elem in res_ip_digits])
del_zero = re.sub(r'\b0+(\d)', r'\1', res_to_str)

print(del_zero)

print("============================================================")
print("4. Write a Python program that check if IP address is valid.")

pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
pattern_values = r'\d{1,3}'
text = '200.049.000.010'

ip_values = re.findall(pattern=pattern_values, string=text)
res_ip_digits = re.findall(pattern=pattern, string=text)
res_to_str = '.'.join([str(elem) for elem in res_ip_digits])
del_zero = re.sub(r'\b0+(\d)', r'\1', res_to_str)


def validity():
    if len(ip_values) != 4:
        return f"{text} - invalid ip address, address must contain 4 numbers separated by point and not more than 255"
    elif del_zero:
        for m in ip_values:
            if int(m) > 255:
                return f"{text} - invalid ip address, address must contain 4 numbers separated by point " \
                       f"and not more than 255"
            elif int(ip_values[-1]) < 255:
                return f"{del_zero} - valid ip address"
            else:
                continue
    else:
        return f"{text} - invalid ip address, address must contain 4 numbers separated by point and not more than 255"


print(validity())
