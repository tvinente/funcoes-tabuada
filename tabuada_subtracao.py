#O print("%d - %d = %d" % (sub, count+1, sub-(count+1))), também pode ser trabalhado na seguinte forma: print("%d - %d = %d" % (count+1, sub, (count+1) - sub))

def subtrair(sub):
    for count in range(10):
        print("%d - %d = %d" % (sub, count+1, sub-(count+1)))
        
sub = int(input("Tabuada do numero: "))
subtrair(sub)

