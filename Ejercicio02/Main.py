from Electrodomestico import Television
from Electrodomestico import Lavadora

#Lista de electrodomesticos
lista = [
        Television(100,50),
        Lavadora(100,'verde','F',200,31),
        Television(500,20),
        Television(50,10),
        Lavadora(400,'rojo','G',200,23),
        Lavadora(300,'azul','A',321,31),
        Television(200,10),
        Lavadora(400,'negro','F',200,22),
        Lavadora(321,'gris','B',53,17),
        Television(50,5)
]

acumuladorTelevision = 0
acumuladorLavadora = 0

#Recorremos la lista y vamos sumando los precios según el articulo
for i in lista:
    if (type(i).__name__ == 'Television') :
        acumuladorTelevision += i.precioFinal()

    if (type(i).__name__ == 'Lavadora'):
        acumuladorLavadora += i.precioFinal()

print("Precio total de las lavadoras: "+str(acumuladorLavadora)+'€')
print("Precio total de las televisiones: "+str(acumuladorTelevision)+'€')

