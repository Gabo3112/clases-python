lista=[]

def push(element): #push: agrear un elemento a la lista
    lista.append(element)

def pop():
    valor=lista[-1]
    del lista[-1]
    return valor

