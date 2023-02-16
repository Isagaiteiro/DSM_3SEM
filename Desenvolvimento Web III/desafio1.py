def caixinha_magica3(numero1,numero2):
    if numero1 > numero2:
        nummero_magico = numero1-numero2
        return nummero_magico
        
    if numero1 <= numero2:
        nummero_magico = numero1-numero2
        return 0


assert caixinha_magica3(20, 15) == 5
assert caixinha_magica3(20, 10) == 10
assert caixinha_magica3(10, 10) == 0
assert caixinha_magica3(10, 15) == 0
assert caixinha_magica3(30, 45) == 0