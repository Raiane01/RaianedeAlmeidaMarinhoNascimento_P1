
def nob(a,b):
    valor1=0
    valor2=0
    for i in range(len(a)):
        valor1+=int(a[i])
    for j in range(len(b)):
        valor2+=int(b[j])
    resp= valor1 + valor2
    return resp
