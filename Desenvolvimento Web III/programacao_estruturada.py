##
print ('Primeiro comando')
print ('Segundo comando')
print ('Terceiro comando')

##Seleção
condicao = False
if condicao:
    print ('Passou por aqui 1!')
condicao = True
if condicao:
    print ('Passou por aqui 2!')

##Iteração
lista = list(range(1,10))

for numero in lista:
    print(numero)

##Funções

def caixinha_magica(numero1,numero2):
    numero_magico = numero1+numero2
    return numero_magico

caixinha_magica(3,4)

def caixinha_magica2(numero1,numero2):
    numero_magico = numero1+numero2
    return numero_magico

print('Testes')
assert caixinha_magica(2,5) == 7
assert caixinha_magica('oi', 'mundo') == 'oimundo'

print('Primeiro experimento com TDD')
assert caixinha_magica2(10,4) == 14
assert caixinha_magica2(10,5) == 15

## Strings 
nome = 'Fatec Araras'
nome = 'Fatec Araras 2'
print (id(nome))
print (nome.upper())

##Lista

comida = []
comida.append('pão')
comida.append('queijo')
comida.append('bacon')

for compra in comida:
    print(comida)

print(compra.upper())

lista1 = []
tupla1 = ('Pão','Bacon','Leite')

#quantos elementos Bacon tem na tupla
print(tupla1.count('Bacon'))
#posição na tupla onde está o elemento
print(tupla1.index('Leite'))

#Range
r = range(1,15)
print(list(r))

r = range(1,15,2)
print(list(r))