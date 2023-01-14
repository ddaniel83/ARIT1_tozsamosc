import random

def password_generator():

    digits = "0123456789"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    pwd = ""
    min = random.randint(8,64)
    for i in range(0, min):
        pwd += random.choice(digits) + random.choice(lowercase) + random.choice(uppercase) + random.choice(special)

    print(pwd[0:min])

password_generator()
