#Criar tabuada para somar
#Função definda com o nome de "somar", recebeu o parâmetro "somando".
#Utilizou-se o laço de repetição "for", contador "cont" e a função "range", método format também foi utilizado.

def somar(somando):
    for count in range(10):
        print("%d + %d = %d" % (somando, count+1, somando+(count+1)) )

somando = int(input("Tabuada do numero: "))
somar(somando)