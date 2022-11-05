import json
from generate_password import generate_password 
import subprocess
subprocess.run('sudo chmod u+r user.json', shell=True)
#n = generate_password.generate_password()
def count_start():
    with open('user.json', 'r') as usp:
        dict1 = json.load(usp)
    if dict1['count']==0:
        print('Hello, you are new user) in This Mashine.')
        dict1['count']+=1
    with open('user.json', 'w') as usp:
        json.dump(dict1, usp, indent=4)
    
def creat_user():
    with open('user.json', 'r') as usp:
        dict1 = json.load(usp)
    user_name = input('Enter Your Name: ')
    password_in_system = input('Enter Your Password: ')
    if user_name in dict1.keys():
        creat_user()
    else:
        i = input(f'Your name is {user_name}, your password is {password_in_system}? n/y')
        if i == 'y':
            dict1[user_name]={user_name:{}, f'login {user_name} in sistem':None}
            dict1[user_name][f'login {user_name} in sistem']=password_in_system
            with open('user.json', 'w') as usp:
                json.dump(dict1, usp, indent=4)
            print('Allright)')
        elif i == 'n':
            creat_user()
# creat_user()
def creat_password():
    with open('user.json', 'r') as usp:
        dict1 = json.load(usp)
    user_name = input('Enter Your name in sistem: ')
    name_service = input('Enter Service')
    login_service = input('Enter Your Service login')
    password_service = generate_password()
    try:
        if name_service in dict1[user_name][user_name].keys():
            dict1[user_name][user_name][name_service][login_service]={}
            dict1[user_name][user_name][name_service][login_service]['login']=login_service
            dict1[user_name][user_name][name_service][login_service]['password']=password_service   
        else:
            dict1[user_name][user_name][name_service]={}
            dict1[user_name][user_name][name_service][login_service]={}
            dict1[user_name][user_name][name_service][login_service]['login']=login_service
            dict1[user_name][user_name][name_service][login_service]['password']=password_service
    except KeyError:
        print('Oooops reenter your information pleas')
        creat_password()    
    with open('user.json', 'w') as usp:
        json.dump(dict1, usp, indent=4)
def check_password():
    with open('user.json', 'r') as usp:
        dict1 = json.load(usp)
    user_name = input('Enter Your Name')
    service_name = input('Enter Service name')
    login_service = input('Enter Your login in service')
    try:

        return dict1[user_name][service_name]['password']
    except KeyError:
        print(f'You are entering your name as {user_name} and you are entering service name as {service_name}, it is not True Information... Reenter please)')
        check_password()            
count_start()
user_input = input('''What do you want?
1.Check your password?
2.Creat new password?
3.Creat new profile? 
Enter number: 
''')

if user_input == '1':
    check_password()
elif user_input == '2':
    creat_password()
elif user_input == '3':
    creat_user()
subprocess.run('sudo chmod u-r user.json', shell = True)



