


print('Você é cadastrado?')
print("=-=-=" * 20)

pergunta = int(input('Sim[1] ou Não[2]'))

if pergunta == 1:
    print("=-=-=" * 20)
    nome = input('Digite seu nome de usuario: ')
    senha1 = input('Digite sua senha: ')
    print("=-=-=" * 20)
    print(f'Seja bem-vindo, @{nome}')
               
        
        
        
        
        
        
elif pergunta == 2:
    print("=-=-=" * 20)
    nome = input('Crie seu nome de usuario: ')
    senha = input('Crie sua senha: ')
    print('=-=-=' * 20)
    name = input('Digite seu nome de usuario: ')
    password = input('Digite sua senha: ')
    
    if nome.lower() != name.lower() or password.lower() != senha.lower():
        print('=-=-=' * 20)
        while True:
            print('Usuario ou senha incorretos, por favor tente novamente')
            print('=-=-=' * 20)
            nametry = input('Digite seu nome de usuario: ')
            passwordtry = input('Digite sua senha: ')
            
            if nametry.lower() == nome.lower() and passwordtry.lower() == senha.lower():
                print('=-=-=' * 20)
                print(f'Seja bem-vindo, @{nome}')
                break
    else:
        print('=-=-=' * 20)
        print(f'Seja bem-vindo, @{nome}')
        
        
        
        
        
                     
                    
        

            
    
        
            

