class Videojuego:
    titulo = ''
    horas_estimadas = 10
    entregado = False
    genero = ''
    compania = ''
    entregados_totales = 0

    def __init__(self,titulo,horas_estimadas,genero,compania):
        self.titulo = titulo
        self.horas_estimadas = horas_estimadas
        self.entregado
        self.genero = genero
        self.compania = compania

    # Getter de los atributos menos entregado
    def getTitulo(self):
        return self.titulo

    def getHoras_estimadas(self):
        return self.horas_estimadas

    def getGenero(self):
        return self.genero

    def getCompania(self):
        return self.compania

    def getEntregados(self):
        return self.entregados_totales

    # Setter de los atributos menos entregado
    def setTitulo(self, titulo):
        self.titulo = titulo

    def setHoras_estimaadas(self, horas):
        self.horas_estimadas = horas

    def setGenero(self, genero):
        self.genero = genero

    def setCompania(self, compania):
        self.compania = compania


    #Método toString para mostrar los datos
    def toString(self):
        print('Título: ' + self.titulo)
        print('Número de temporadas: ' + str(self.num_temporadas))
        print('Género: ' + self.genero)
        print('Entregado: ' + self.entregado)
        print('Creador: ' + self.creador)

    #Método entregar
    def entregar(self):
        if(self.entregado == False):
            self.entregado = True
            self.entregados_totales += 1
            entrega = 'Ha sido entregado el videojuego '+self.titulo
            return entrega
        else:
            yaEntregado = 'El videojuego ' +self.titulo+' ya ha sido entregado0'
            return yaEntregado
