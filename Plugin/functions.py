import random 


def randid():
    id = ''
    for i in range(10):
        id=id+random.choices('1234567890ABCDEFJHIJKLMNOPQRSTUVWXYZ')[0]
    return id
