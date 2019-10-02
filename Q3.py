def pi():
    valodePi= 1
    cont = 0
    divisor= 3
    while true:
        valor_t =0
        comparar = 1/divisor
        if cont%2==0:
            valor_t=valordePi-comparar
        else:
            valor_t=valordePi+comparar
            
        dif =4*valor_t-4*valordePi

        if dif<0:
            dif*=-1

        if dif <= (5*(10**(8))):
            break

        valordePi=valor_t
        cont+=1
        divisor+=2
        

        #print(dif)



    return 4*valordePi

print(pi)
