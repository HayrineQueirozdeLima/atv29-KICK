import os  

nome = input("Digite seu nome: ")
#int() converte o que foi digitado em um valor inteiro
idade = int(input("Digite sua idade: "))

resp = 100 - idade;

print("--------------------------------------------------------------------")
print("Nome:",nome)
print("Idade:", idade)
print("Resposta: Faltam",resp,"anos para você chegar aos 100 anos de idade")
print("--------------------------------------------------------------------")

os.system("pause")