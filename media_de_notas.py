arquivo = open("./lista.txt", "a")
nota1 = (float(input("digite a sua nota da atividade P1: ")))
nota2 = (float(input("digite a sua nota da Prova P1: ")))
nota3 = (float(input("digite a sua nota da atividade P2: ")))
nota4 = (float(input("digite a sua nota da Prova P2: ")))

media = (float(nota1+nota2+nota3+nota4)/4)

print("Sua média em relação a suas notas é: ",media)
if media <= 5.9:
    print("reprovado")
else:
    print("Aprovado")
arquivo.write(str(nota1)+"/n "+ str(nota2)+ "/n" + str(nota3)+ "/n"+ str(nota4)+ "/n"+ str(media)+ "/n")
arquivo.close()