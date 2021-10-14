from Serie import Serie
from Videojuego import Videojuego

contador = 0

#Lista de series y videojuegos
listaSeries = [
    Serie('La que se avecina',10,'Comedia','Alberto Caballero'),
    Serie('El juego del Calamar',1,'Drama','Hwang Dong-hyuk'),
    Serie('Juego de Tronos',8,'Fantasia','George R. R: Martin'),
    Serie('The Walking Dead',11,'Drama Apocalíptico','Frank Darabont'),
    Serie('Peaky Blinders',6,'Western','Steven Knight')
]

listaVideojuego = [
    Videojuego('The Legend of Zelda: Breath of the Wild',60,'Fantasía','Nintendo'),
    Videojuego('Resident Evil : Village',8,'Terror','Capcom'),
    Videojuego('Undertale',8,'Fantasía','Tobby Fox'),
    Videojuego('Outlast',6,'Terror','Red Barrels'),
    Videojuego('Super Mario Odissey',50,'Plataformas','Nintendo')
]

#Entregamos las series y videojuegos,he agregado que no nos deje entregar un item ya entregado
print(listaSeries[0].entregar())

print(listaSeries[0].entregar())

print(listaSeries[1].entregar())
print(listaSeries[2].entregar())

print("")

print(listaVideojuego[2].entregar())
print(listaVideojuego[1].entregar())
print(listaVideojuego[4].entregar())

print("")

max = 0
aux = ''


#Bucles para hallar la serie con más temporadas y el videojuego con más horas estimadas
for i in listaSeries:
    if(max < i.getNumTemporadas()):
        max = i.getNumTemporadas()
        aux = i.getTitulo()

print('La serie con más temporadas ('+ str(max) +') es '+str(aux))

for i in listaVideojuego:
    if(max < i.getHoras_estimadas()):
        max = i.getHoras_estimadas()
        aux = i.getTitulo()

print('El videojuego con más horas estimadas ('+ str(max) +') es '+str(aux))