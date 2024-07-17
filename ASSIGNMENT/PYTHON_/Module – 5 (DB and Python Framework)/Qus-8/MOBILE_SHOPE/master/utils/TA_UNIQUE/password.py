import string
import random


def password_get(length=8):
    chars = string.ascii_letters + string.digits+'@_.'
    password =''
    for i in range(length):
        password += chars[random.randrange(len(chars))]
    return password
