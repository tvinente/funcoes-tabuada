#Tabuada do "multiplicando 9". 
#Para outros valores, basta alterar o valor do argumento.
#Alterando o parâmetro de range(1,11) para range(0, 11), a tabuada para ser exibida desde 0.

def multiplicar(multiplicando):
    for i in range(1, 11):
        print(multiplicando, 'x', i, '=', multiplicando*i)

multiplicar(9)