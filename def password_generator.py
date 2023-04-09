import random
import string
def password_generator(Len_pass = 8):#parametro escolhido len, tamanho, maioria dos sites usando 8 caracteres
    ascii_options = string.ascii_letters #criação da variável ascii
    number_options = string.digits       #criação da variável number
    punt_options = string.punctuation     #criação da variável pontuação
    options = ascii_options + number_options + punt_options #em uma única string
    
    password_user = ""
    
    for i in range(0, Len_pass):
        digit = random.choice(options)
        password_user = password_user + digit
        
    return password_user #encerrar a execução

choice_user = input("Quantos digitos tem a senha? ")

if choice_user.isdigit(): #certeza que o usuário digitou um número
    choice_user = int(choice_user) #converter para inteiro
else:
    print("Entrada inválida!")
    quit()


response = password_generator(Len_pass = choice_user) #para ser utilizada, retornar a escolha do usuário
print(f"Senha gerada:\n{response}")