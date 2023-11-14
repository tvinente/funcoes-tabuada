#Criar tabuada
#Função definda com o nome de "multiplicar", recebeu o parâmetro "multiplicando", representando o número que será multiplicado na tabuada.
#Utilizou-se o laço de repetição "for", contador "cont" e a função "range", método format também foi utilizado (sem format o resultado seria "9 1 9")

def multiplicar(multiplicando):
    for count in range(10):
        print("%d x %d = %d" % (multiplicando, count+1, multiplicando*(count+1)) )

multiplicando = int(input("Tabuada do numero: "))
multiplicar(multiplicando)