
# Password Generator with Custom Length and Style
import random
import string

def create_password():
    length = int(input("Enter desired password length: "))
    if length < 6:
        print("Use at least 6 characters for a strong password.")
        return

    options = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(options) for _ in range(length))
    print("Your Secure Password:", password)

create_password()
