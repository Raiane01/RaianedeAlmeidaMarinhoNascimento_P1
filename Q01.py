from math import sqrt
def raiz (a, b, c)
	delta = b * b - 4 * a * c
	if delta < 0:
		imaginario = sqrt(-delta) / (2 * a)
		real = -b / (2 * a)
		print("Real: ",real,"Imaginario: ",imaginario)
	else: 
		resultado_1 = (-b + sqrt(delta)) / (2 * a)
		resultado_2 = (-b - sqrt(delta)) / (2 * a)
		print("Primeiro resultado: ",resultado_1,"Segundo resulado: ",resultado_2)
		return 0

