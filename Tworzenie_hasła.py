import secrets
import string

max_len = 16

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = '!@#$%^&*()_+'

all_chairs = lowercase + uppercase + digits + special

pass_list = [secrets.choice(lowercase),secrets.choice(uppercase),secrets.choice(digits),secrets.choice(special)]

for i in range (max_len - 4):
    pass_list.append(secrets.choice(all_chairs))

secrets.SystemRandom().shuffle(pass_list)
password = "".join(pass_list)
print(password) 