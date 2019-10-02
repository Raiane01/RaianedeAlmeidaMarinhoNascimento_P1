r= math.sqrt(delta)
print(r)
print(' raiz 1',(-b+ r)/(2*a))
print(' raiz 2',(-b-r)/(2*a))

elif(delta<0):
    valor=1
return valor
def nob(a,b):
    valor1=0
    valor2=0
    for i in range(len(a)):
        valor1+=int(a[i])
    for j in range(len(b)):
        valor2+=int(b[j])
    resp= valor1 + valor2
    return resp

def pi():
    soma=0
    i=1
    valor=(1/i)-(i/i+2)
    while(valor>0.00000005):
        valor=(1/i)-(i/i+2)

        soma+=valor

        i+=4

        pi= 4*soma
