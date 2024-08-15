# Quatro operações básicas 


# Limitações de 2 números 

def calculadora(): # def = função podendo ser usada novamente
    try: # vai tentar rodar o codigo

        n1 = float(input("Primeiro número: "))

        n2 = float(input("Segundo número: "))   

        print("Escolha um das 4 operações básicas a seguir: ")
        print("Digite 1 para Soma")
        print("Digite 2 para Subtração")
        print("Digite 3 para Multiplicação")
        print("Digite 4 para Divisão")

        print("                   ")

        escolha = float(input("Qual você escolhe: "))
    
        if escolha >= 1 and escolha <= 1.99:
            resultado = n1 + n2
            print(f"Seu resultado é = {resultado}")

        elif escolha >= 2 and escolha <= 2.99:
            resultado = n1 - n2
            print(f"Seu resultado é = {resultado}")

        elif escolha >= 3 and escolha <= 3.99 :
            resultado = n1 * n2
            print(f"Seu resultado é = {resultado}")

        elif escolha >= 4 and escolha <= 4.99:
            if n2 != 0:
                resultado = n1 / n2
                print(f"Seu resultado é = {resultado}")

            else:
                print("Erro: Divisão por zero")
            
        elif escolha == "":
            print("Opção inválida!Responda com o número")

        elif escolha < 1 or escolha >= 5:
            print("Por favor digite uma opção entre 1 e 4")

    except: # Se não conseguir rodar
        
        print("Coloque apenas números positivos")
        calculadora() # Caso dê erro no código, ele será chamado novamente

calculadora() # Chmando a função


    


