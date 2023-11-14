#No resultado da divisão foi utilizado  %.1f, para poder apresnetar apenas uma casa decimal.

def dividir(divisor):
    for count in range(10):
        print("%d / %d = %.1f" % (divisor, count+1, divisor / (count+1)))

divisor = int(input("Tabuada do numero: "))
dividir(divisor)