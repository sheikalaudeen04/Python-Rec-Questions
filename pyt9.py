import random
def gen_pass(l,uc,di,sym):
    char = 'abcdefghijklmnopqrstuvwxyz'
    if uc:
        char += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if di:
        char += '0123456789'
    if sym:
        char += r'!@#$%^&*()_+-={}[]\|;:~`<,>.?/' 

    password = ''.join(random.choice(char) for i in range(l))
    return password

def criteria():
    l= int(input("Enter the length of the password: "))
    uc= input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    di= input("Include digits? (yes/no): ").lower() == 'yes'
    sym= input("Include symbols? (yes/no): ").lower() == 'yes'

    return l,uc,di,sym

l,uc,di,sym = criteria()
password = gen_pass(l,uc,di,sym)
print("Generated password: ",password)
