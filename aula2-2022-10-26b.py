#Pede o nome do aluno e sua nota (o a 10) e, se ele tirou nota 10, mostra "{nome}, você é bichão, mesmo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, você é o bichão, mesmo...")
#Uso da função elif

elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho!")
elif (nota > 10 or nota <0):
  print(f"Desculpe, mas essa nota é inválida!")
else: # é sempre, automaticamente, o que as duas condições não trataram
  print("Burro, não tirou dez...")


