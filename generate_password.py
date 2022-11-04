import random
def generate_password(password = '', eng1 = 'abcdefghijklmnopqrstuvwxyz',eng2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',nums = ''.join([str(i) for i in range(0, 10)]),list_elem = []):
    for i in eng1:
        list_elem.append(i)
    for i in eng2:
        list_elem.append(i)
    for i in nums:
        list_elem.append(i)
    random.shuffle(list_elem)
    while len(password)<50:
        password+=list_elem[random.choice(range(0, len(list_elem)))] 
    return password
