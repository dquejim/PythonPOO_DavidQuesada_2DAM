

class Electrodomestico:

    #Atributos
    PRECIO_BASE = 100
    COLOR = 'blanco'
    CONSUMO_ENERGETICO = 'F'
    PESO = 5

    # Constructor por parametros
    def __init__(self,precio_base,color,consumo_energetico,peso):
        self.PRECIO_BASE = precio_base
        self.COLOR = self.comprobarColor(color)
        self.CONSUMO_ENERGETICO = self.comprobarConsumoEnergetico(consumo_energetico)
        self.PESO = peso

    #Métodos getter de cada atributo
    def getPrecio(self):
        return self.PRECIO_BASE

    def getColor(self):
        return self.COLOR

    def getConsumo(self):
        return self.CONSUMO_ENERGETICO

    def getPeso(self):
        return self.PESO

    #Método para comprobar el consumo energetico
    def comprobarConsumoEnergetico(self,letra):
        letrasPosibles = ['A','B','C','D','E','F']

        for i in range (6) :
            if(letra.upper() == letrasPosibles[i]) :
                return letrasPosibles[i]

            else :
                return self.CONSUMO_ENERGETICO

    #Método para comprobar que el color es correcto
    def comprobarColor(self,color):
        coloresPosibles = ['blanco','negro','rojo','azul','gris']

        for i in range (5) :
            if(color.lower() == coloresPosibles[i]) :
                return coloresPosibles[i]

            else :
                return self.COLOR

    #Método para calcular el precio final del electrodomestico
    def precioFinal(self):
        precio_final = self.PRECIO_BASE

        if(self.CONSUMO_ENERGETICO == 'A'):
            precio_final = 100
        elif(self.CONSUMO_ENERGETICO == 'B') :
            precio_final = 80
        elif (self.CONSUMO_ENERGETICO == 'C'):
            precio_final = 60
        elif (self.CONSUMO_ENERGETICO == 'D'):
            precio_final = 50
        elif (self.CONSUMO_ENERGETICO == 'E'):
            precio_final = 30
        elif (self.CONSUMO_ENERGETICO == 'F'):
            precio_final = 10

        if(self.PESO > 0 and self.PESO < 19):
            precio_final += 10
        elif(self.PESO > 20 and self.PESO < 49):
            precio_final += 50
        elif (self.PESO > 50 and self.PESO < 79):
            precio_final += 80
        elif (self.PESO > 80):
            precio_final += 100

        return precio_final

    def toString(self):
        print('Precio_Base:' + str(self.PRECIO_BASE))
        print('Consumo:' + self.CONSUMO_ENERGETICO)
        print('Color:' + self.COLOR)
        print('Peso:' + str(self.PESO))

#Clase Lavadora
class Lavadora(Electrodomestico) :
    #Atributo nuevo
    CARGA = 5

    #Constructor de la clase padre + el atributo añadido
    def __init__(self,precio_base,color,consumo_energetico,peso,carga):
        Electrodomestico.__init__(self, precio_base, color, consumo_energetico, peso)
        self.CARGA = carga


    #Getter de la carga
    def getCarga(self):
        return self.CARGA

    #Nuevo método de precio final
    def precioFinal(self):
        precio_final = self.PRECIO_BASE

        if (self.CONSUMO_ENERGETICO == 'A'):
            precio_final = 100
        elif (self.CONSUMO_ENERGETICO == 'B'):
            precio_final = 80
        elif (self.CONSUMO_ENERGETICO == 'C'):
            precio_final = 60
        elif (self.CONSUMO_ENERGETICO == 'D'):
            precio_final = 50
        elif (self.CONSUMO_ENERGETICO == 'E'):
            precio_final = 30
        elif (self.CONSUMO_ENERGETICO == 'F'):
            precio_final = 10

        if (self.PESO > 0 and self.PESO < 19):
            precio_final += 10
        elif (self.PESO > 20 and self.PESO < 49):
            precio_final += 50
        elif (self.PESO > 50 and self.PESO < 79):
            precio_final += 80
        elif (self.PESO > 80):
            precio_final += 100

        if(self.CARGA > 30) :
            precio_final += 50

        return precio_final

#Clase Television
class Television(Electrodomestico) :
    #Nuevos atributos
    RESOLUCION = 40
    FOURK = False

    #Constructor con precio y peso,lo demás por defecto
    def __init__(self, precio, peso):
        self.PRECIO_BASE
        self.COLOR
        self.CONSUMO_ENERGETICO
        self.PRECIO_BASE =  precio
        self.PESO = peso
        self.RESOLUCION
        self.FOURK

    #Getter de Resolucion y FourK
    def getResolucion(self):
        return self.RESOLUCION

    def getFourK(self):
        return self.FOURK

    #Nuevo método de precio final
    def precioFinal(self):
        precio_final = self.PRECIO_BASE

        if (self.CONSUMO_ENERGETICO == 'A'):
            precio_final += 100
        elif (self.CONSUMO_ENERGETICO == 'B'):
            precio_final += 80
        elif (self.CONSUMO_ENERGETICO == 'C'):
            precio_final += 60
        elif (self.CONSUMO_ENERGETICO == 'D'):
            precio_final += 50
        elif (self.CONSUMO_ENERGETICO == 'E'):
            precio_final += 30
        elif (self.CONSUMO_ENERGETICO == 'F'):
            precio_final += 10

        if (self.PESO > 0 and self.PESO < 19):
            precio_final += 10
        elif (self.PESO > 20 and self.PESO < 49):
            precio_final += 50
        elif (self.PESO > 50 and self.PESO < 79):
            precio_final += 80
        elif (self.PESO > 80):
            precio_final += 100

        if(self.RESOLUCION > 40) :
            precio_final = precio_final * 1.3

        if(self.FOURK) :
            precio_final += 50

        return precio_final



