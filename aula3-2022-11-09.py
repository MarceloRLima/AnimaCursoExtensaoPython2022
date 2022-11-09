print("Inicio da Aula 3 (09/11/2022)\n")

contador = 1

while(contador <=10):
  print(contador)
  contador = contador + 1 #contador +=1



# Laço for (python for = for each)
fruta ="Morango"
print (fruta)

fruta1="Morango"
fruta2="Laranja"
fruta3="Pêra"

#Lista
frutas = ["Morango", "Laranja", "Pêra"]

#mostra todas
print (frutas)
#quero exibir apenas a 3a fruta (pêra)
print (frutas[2])

#Exibir quantas frutas tem na minha lista?
print(len(frutas)) # lenght = tamanho


#Quero incluir uma fruta nova
frutas.append("Manga")

print(len(frutas))
print(frutas)

print (frutas[0])
print (frutas[1])
print (frutas[2])
print (frutas[3])
#print (frutas[4])

print("Exemplo das frutas com while...")
frutas.append("Uva")

i=0 # i de index
while(i<len(frutas)):
  print(frutas[i])
  i=i+1




