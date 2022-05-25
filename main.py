lado = float(input( 'Usuario informe o total da area da lateral do terreno em metros: '))
frente = float(input( ' Usuario informe o total da area frente do terreno em metros:'))

print('A area lateral do terreno em metros é de: ',lado)
print('A area frontal do terreno em metros é de:',frente)

metrototal = lado * frente
print('A area total do terreno é de:' ,metrototal)

valor = float(input('Usuatio informe o valor total do metro quadrado:'))

terrenovale = metrototal * valor

print('O valor total do terreno é:' ,terrenovale)