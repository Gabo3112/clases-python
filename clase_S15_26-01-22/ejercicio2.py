def posiciones(cadena ,silaba, idx):
    y=len(silaba)
    x=cadena.find(silaba)
    idx.append(x)
    nueva_cadena=cadena.replace(silaba, y*'-', 1) 
    if x == -1:
        print(idx[:1])
        return(idx[:1])
    else:
        posiciones(nueva_cadena,silaba,idx)

idx=[]
palabra=input("ingrese la frase: ")
letra=input("busque letra: ")
posiciones(palabra,letra,idx)   