class Ciudadano():
    def __init__(self):
        self._comunidad = None
        self._id = None
        self._id_familia = None

        self._enfermo = False
        self._recuperado = True
        self._dias_enfermo = 0

    @property
    def comunidad(self):
        return self._comunidad

    @comunidad.setter
    def comunidad(self, comunidad):
        if isinstance(comunidad, str):
            self._comunidad = comunidad
        else:
            print("El tipo de dato en comunidad no corresponde")

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            print("El tipo de dato en id no corresponde")

    @property
    def id_familia(self):
        return self._id_familia
    @id_familia.setter
    def id_familia(self, id_familia):
        if isinstance(id_familia, int):
            self._id_familia = id_familia
        else:
            print("El tipo de dato en id_familia no corresponde")

    @property
    def enfermo(self):
        return self._enfermo

    @enfermo.setter
    def enfermo(self, enfermo):
        if isinstance(enfermo, int):
            if enfermo == 0:
                #print('El ciudadano', self.id, 'se contagio')
                self._enfermo = True
                self._recuperado = False
            if enfermo == 1:
                #print('El ciudadano', self.id, 'se recupero')
                self._recuperado = True
        else:
            print("El tipo de dato en enfermo no corresponde")

    def recuperado_getter(self):
        return self._recuperado

    def aumento_dias_enfermo(self):
        self._dias_enfermo += 1
        return self._dias_enfermo    