nome_filme1,  nota_filme1, duracao_filme1 = str(input()).split("-")
y = float(nota_filme1)
nome_filme2,  nota_filme2, duracao_filme2 = input().split("-")
x = float(nota_filme2)
nome_filme3,  nota_filme3, duracao_filme3 = input().split("-")
z = float(nota_filme3)


if(float(nota_filme1) < float(4.0) and float(nota_filme2) < float(4.0) and float(nota_filme3) < float(4.0)):
    print('Nota minima nao atingida')
elif(nota_filme1 == nota_filme2 == nota_filme3):
    if(duracao_filme1 < duracao_filme2  < duracao_filme3):
        print(nome_filme1)
    elif(duracao_filme2 < duracao_filme1 < duracao_filme3):
        print(nome_filme2)
    elif (duracao_filme3 < duracao_filme1  < duracao_filme2):
        print(nome_filme3)
elif (nota_filme1 > nota_filme2 and nota_filme1 > nota_filme3):
    print(nome_filme1)
elif(nota_filme2 > nota_filme1 and nota_filme2 > nota_filme3):
    print(nome_filme2)
elif(nota_filme3 > nota_filme1 and nota_filme3 > nota_filme2):
    print(nome_filme3)
elif(nota_filme1 == nota_filme2 and duracao_filme1 < duracao_filme2):
        print(nome_filme1)
elif(nota_filme1 == nota_filme3 and duracao_filme1 < duracao_filme3):
        print(nome_filme1)
elif(nota_filme2 == nota_filme1 and duracao_filme2 < duracao_filme1):
        print(nome_filme2)
elif(nota_filme2 == nota_filme3 and duracao_filme2 < duracao_filme3):
        print(nome_filme2)
elif(nota_filme3 == nota_filme1 and duracao_filme3 < duracao_filme1):
        print(nome_filme3)
elif(nota_filme3 == nota_filme2 and duracao_filme3 < duracao_filme2):
        print(nome_filme3)
elif(nota_filme1 == nota_filme2  == nota_filme3 and duracao_filme1 < duracao_filme2  < duracao_filme3):
   print(nome_filme1)
elif (nota_filme2 == nota_filme1 == nota_filme3 and duracao_filme2 < duracao_filme3  < duracao_filme1):
    print(nome_filme2)
