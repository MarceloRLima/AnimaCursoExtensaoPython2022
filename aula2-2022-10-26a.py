# comando imput(): Quero permitir que o usuário digite algo...
nome=input("Digite seu nome: ")

#pede a idade para o usuário "Qual sua idade?
idade=int(input("Qual a sua idade? "))

#pede o gênero para o usuário "Qual o seu gênero? (M, F ou O)"
genero=input("Qual o seu gênero? (Digite M= Masculino; F= Feminino ou O= Outros): ")

# comando de saída... exibir na tela
print(f"\nBoa noite, seu nome é {nome}")
#exiba "Sua idade é..."
print(f"Sua idade é {idade} anos")
#exiba "Você é do gênero..."
print(f"Você é do gênero {genero}")

#e se eu quisesse mostrar o DOBRO da idade informada
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostr "Você é maior de idade, ótima! Já pode beber ou dirigir!"
if idade >= 18: 
  print("\nVocê é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("\nVocê é xonfen ainda, xófen ainda...")

#E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
  
if idade >= 18 and genero == "M":
  print("\n... e você também precisa/precisou prestar o serviço militar obrigatório")
  





print("\nVai ser executada de qualquer jeito")