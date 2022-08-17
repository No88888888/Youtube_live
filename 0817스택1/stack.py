# stack구현

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        size[top] = item
        

top = -1
size = 10




