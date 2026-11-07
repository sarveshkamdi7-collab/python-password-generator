import string
import secrets


class PasswordError(Exception):
    '''     Raised when password length less than Minimum required or password in wrong format '''
try:
    l=int(input('Enter length of password : '))
    string_chars=string.ascii_lowercase+string.ascii_uppercase+string.digits+'!@#$%&*()_-=+'
    password=[]
    if l<16:
        raise PasswordError('Password length must be minimum 16 ')
    else:
        for i in range(len(string_chars)//2):
         password.append(secrets.choice(string_chars))

    password=''.join(password)
    print('Password is : ',password)
except PasswordError as e:
    print('Error is ',e)


        
        