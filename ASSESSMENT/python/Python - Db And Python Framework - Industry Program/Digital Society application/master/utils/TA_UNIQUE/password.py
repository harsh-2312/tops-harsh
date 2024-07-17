import string
import random

def generate_password(length=8):

    chre = string.ascii_letters + string.digits + '@_.'
    password = ''

    for i in range(length):
        password += chre[random.randrange(len(chre))]
    return password