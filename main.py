# comando imput(): Quero permitir que o usuário digite algo...
nome=input("Digite seu nome: ")

#pede a idade para o usuário "Qual sua idade?
idade=int(input("Qual a sua idade? "))

# comando de saída... exibir na tela
print(f"\nBoa noite, seu nome é {nome}")
#exiba "Sua idade é..."
print(f"Sua idade é {idade} anos")

#e se eu quisesse mostrar o DOBRO da idade informada
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))
