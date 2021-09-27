def outer(login):
    def wrapper_login():
        iwjwlewkkkkkkkkkrlrlrjw
        return login
    
def auth(name,password):
    if name=='abcd' and password=='1234':
        print('authenticated')
        return True
    else:
        return False

def login(name,password):
    if auth(name,password):
        print('Logged in')
    else:
        print('Wrong')

name,password=input('Enter name : '),input('Enter password : ')
login(name,password)