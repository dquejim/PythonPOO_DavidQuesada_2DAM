from Persona import Persona

#Pedimos datos por teclado del primer objeto Persona
print('Introduce el nombre:')
nombre = input()

print('Introduce la edad:')
edad = int(input())

print('Introduce el sexo: (H o M)')
sexo = input()

print('Introduce el peso: (en kilos)')
peso = float(input())

print('Introduce la altura: (en metros)')
altura = float(input())

dni = ''

#Creamos la primera persona mediante los atributos pedidos por teclado y el constructor por parametros
persona1 = Persona(nombre,edad,Persona.generarDni(dni),sexo,peso,altura)
persona1.introducirSexo(sexo)

#Datos de la persona 1
print('-----Persona numero 1-----')

persona1.toString()

print(persona1.esMayorEdad())

print(persona1.calcularIMC(persona1.getPeso(),persona1.getAltura()))

#Creamos la segunda persona
persona2 = Persona(nombre,edad,Persona.generarDni(dni),Persona.sexo,Persona.peso,Persona.altura)

persona2.introducirSexo(sexo)

#Datos de la persona 2
print('-----Persona numero 2-----')

persona2.toString()

print(persona2.esMayorEdad())

print(persona2.calcularIMC(persona2.getPeso(),persona2.getAltura()))

##Creamos la tercera persona
persona3 = Persona(nombre,edad,Persona.generarDni(dni),Persona.sexo,Persona.peso,Persona.altura)

##Le modificamos los datos con los metodos setter
persona3.setNombre('Pedro')
persona3.setEdad(15)
persona3.setDni('20077578G')
persona3.setSexo('H')
persona3.setPeso(90)
persona3.setAltura(1.60)

#Datos de la persona 2
print('-----Persona numero 3-----')

persona3.toString()

print(persona3.esMayorEdad())

print(persona3.calcularIMC(persona3.getPeso(),persona3.getAltura()))
