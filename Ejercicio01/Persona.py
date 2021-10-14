import random

#Creamos la clase persona
class Persona:

    nombre = ""
    edad = 0
    dni = ''
    sexo = "M"
    peso = 0.0
    altura = 0.0

    def __int__(self):
        self.__nombre
        self.__edad
        self.__dni
        self.__sexo
        self.__peso
        self.__altura

#Constructor por parametros
    def __init__(self,nombre,edad,dni,sexo,peso,altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


##Método que calcula el IMC
    def calcularIMC(self,peso,altura):
        try:
            imc = (peso/(altura*altura))
        except ZeroDivisionError:
            imc = 0

        if imc < 18.5 :
            return 'Está por debajo de su peso ideal'

        if imc >  25 :
            return 'Tiene sobrepeso'

        if imc > 18.5 and imc < 25 :
            return 'Está en su peso ideal'

        return imc


##Método para saber si la persona es mayor de edad
    def esMayorEdad(self):

        if self.__edad > 18:
            return 'Es mayor de edad'
        else :
            return 'Es menor de edad'


##Método para introducir el sexo de la persona,si es incorrecto,será M
    def introducirSexo(self,s):

        if s != 'M' or s != 'H':
            s = 'M'


#Método para mostrar los valores de los atributos de la clase Persona
    def toString(self):
        print('Nombre:' + self.__nombre)
        print('Edad:' + str(self.__edad))
        print('Dni:' + self.__dni)
        print('Sexo:' + self.__sexo)
        print('Peso:' + str(self.__peso))
        print('Altura:' + str(self.__altura))

#Método para generar el dni
    def generarDni(dni):

        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

        nif = random.randint(00000000,99999999)

        resto = nif % 23

        dni = repr(nif)+letras[resto]

        return dni

#Métodos getter y setter
    def setNombre(self, a):
        self.__nombre = a

    def setEdad(self, a):
        self.__edad = a

    def setSexo(self, a):
        self.__sexo = a

    def setPeso(self, a):
        self.__peso = a

    def setAltura(self, a):
        self.__altura = a

    def setDni(self, a):
        self.__dni = a

#Métodos getter de altura y peso
    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso


