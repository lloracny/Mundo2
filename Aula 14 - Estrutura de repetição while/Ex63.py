#Sequência de Fibonacci v1.0

t =  int(input('Quantos termos você deseja ver? '))


cont = 0
t1 = 0
t2 = 1


while cont < t:
    print(t1, end=' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1