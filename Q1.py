loop = ''
while loop != 0:
    print("\n                Fórmula equação de 2º grau")
    print("                       ax²+bx+c = 0\n")

    a = int(input("Informe o valor de A: "))
    if a == 0:  # Se a for igual a zero encerra o programa
        print("O 'A' não pode ser = 0, essa equação não pode ser resolvida.")
        loop = int(input("Digite 1 para tentar novamente e 0 para sair: "))
    elif a != 0:  # Se a for diferente de zero o programa continua
        b = int(input("informe o valor de B: "))
        c = int(input("Informe o valor de C: "))
        delta = b ** 2 - 4 * a * c  # Calculando valor de delta


        def clr():
            print('\n' * 50)


        def delta_resolucao():
            print("\nEncontrando o valor de Delta(∆):")
            print("  ∆ = b²-4*a*c")
            print("  ∆ = ({})²-4*{}*{}".format(b, a, c))
            parte1_delta = b ** 2
            parte2_delta = -4 * a * c
            if parte2_delta < 0:
                operador = ''
            else:
                operador = '+'
            print("  ∆ = {}{}{}".format(parte1_delta, operador, parte2_delta))
            print("  ∆ = {}".format(delta))


        # Equação inexistente
        if (delta < 0):  # Se delta for menor que zero, o programa é encerrado
            delta_resolucao()
            print("Delta não pode ser negativo")
            loop = int(input("Digite 1 para tentar novamente e 0 para sair: "))
            if loop == 1:
                clr()

        # Equação com uma raíz:
        elif (delta == 0):  # Se delta for igual a zero o programa continua

            # Resolvendo e mostrando resolução do Delta:
            delta_resolucao()

            # Encontrando o resultado de x e mostrando resolução:
            print("\nMostrando resulução do X:\n")
            print("x = -b ± √∆")
            print("      2*a")
            print("x = -({}) ± √{}".format(b, delta))
            print("         2*{}".format(a))
            parte1_res = -1 * b
            parte2_res = int(delta ** 0.5)
            parte3_res = 2 * a
            print("x = {} ± {}".format(parte1_res, parte2_res))
            print("      {}".format(parte3_res))

            # Valor do X:
            print("Achando o valor de X¹:")
            parte4_resx1 = parte1_res + parte2_res
            resultadox1 = parte4_resx1 / parte3_res
            print("x¹ = x² = {} + {} = {} = {}".format(parte1_res, parte2_res, parte4_resx1, resultadox1))
            print("             {}      {}".format(parte3_res, parte3_res))
			
			
			#Mostrando resumo de uma equação que possuí apenas uma raíz
            print("\nConclusões Finais:")
            print("  A equação possui apenas uma raiz.")
            print("  Delta = {}".format(delta))
            print("  x =", resultadox1)
            loop = int(input("Digite 1 para fazer outra equação e 0 para sair: "))
            if loop == 1:
                clr()
        # Equação com duas raízes:
        elif (delta > 0):  # Se delta for maior que zero o programa continua

            # Resolvendo e mostrando resulução do Delta
            delta_resolucao()

            # Encontrando o resultado de X e mostrando resolução
            print("\nEncontrando o resultado do x¹ e x²:")
            print("  x = -b ± √∆")
            print("        2*a\n")
            print("  x = -({}) ± √{}".format(b, delta))
            print("           2*{}\n".format(a))
            parte1_res = -1 * b
            parte2_res = int(delta ** 0.5)
            parte3_res = 2 * a
            print("  x = {} ± {}".format(parte1_res, parte2_res))
            print("        {}".format(parte3_res))

            # Valor de X¹
            print("\nAchando o X¹:")
            parte4_resx1 = parte1_res + parte2_res
            resultadox1 = parte4_resx1 / parte3_res
            print("  x¹ = {} + {} = {} = {}".format(parte1_res, parte2_res, parte4_resx1, resultadox1))
            print("         {}     {}".format(parte3_res, parte3_res))

            # Valor de x²
            print("\nAchando o x²:")
            parte4_resx2 = parte1_res - parte2_res
            resultadox2 = parte4_resx2 / parte3_res
            print("  x² = {} - {} = {} = {}".format(parte1_res, parte2_res, parte4_resx2, resultadox2))
            print("         {}     {}".format(parte3_res, parte3_res))

            # Mostrando resumo de uma equação que possuí duas raízes
            print("\nConclusão Final:")
            print("  ->A equação possuí duas raízes.")
            print("  ->Delta =", delta)
            print("  ->x1 =", resultadox1)
            print("  ->x2 =", resultadox2)
            loop = int(input("Digite 1 para fazer outra equação e 0 para sair: "))
            if loop == 1:
                clr()

