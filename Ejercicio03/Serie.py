class Serie:
    titulo =  ''
    num_temporadas = 3
    entregado = False
    genero = ''
    creador = ''

    entregados_totales = 0

    #Constructor con todos los atributos menos entregado
    def __init__(self,titulo,num_temporadas,genero,creador):
        self.titulo = titulo
        self.num_temporadas = num_temporadas
        self.entregado
        self.genero = genero
        self.creador = creador
        self.entregados_totales

    #Getter de los atributos menos entregado
    def getTitulo(self):
        return self.titulo

    def getNumTemporadas(self):
        return self.num_temporadas

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador

    def getEntregados(self):
        return self.entregados_totales

    #Setter de los atributos menos entregado
    def setTitulo(self,titulo):
        self.titulo = titulo

    def setNumTemporadas(self, num):
        self.num_temporadas = num

    def setGenero(self, genero):
        self.genero = genero

    def setCreador(self, creador):
        self.creador = creador

    #Métodos para mostrar los datos
    def toString(self):
        print('Título: '+self.titulo)
        print('Número de temporadas: ' + str(self.num_temporadas))
        print('Género: ' + self.genero)
        print('Entregado: ' + self.entregado)
        print('Creador: ' + self.creador)

    #Método entregar
    def entregar(self):
        if (self.entregado == False):
            self.entregado = True
            self.entregados_totales += 1
            entrega = 'Ha sido entregado el videojuego ' + self.titulo
            return entrega
        else:
            yaEntregado = 'La serie '+self.titulo+' ya ha sido entregada'
            return yaEntregado