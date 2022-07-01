class Enfermedad():
    def __init__(self):
        self._nombre = None
        self._probabilidad_de_infectarse= None
        self._probabilidad_de_morir = None

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print("El tipo de dato en nombre no corresponde")

    @property
    def probabilidad_de_infectarse(self):
        return self._probabilidad_de_infectarse

    @probabilidad_de_infectarse.setter
    def probabilidad_de_infectarse(self, probabilidad_de_infectarse):
        if isinstance(probabilidad_de_infectarse, int):
            self._probabilidad_de_infectarse = probabilidad_de_infectarse
        else:
            print("El tipo de dato en probabilidad_de_infectarse no corresponde")

    @property
    def probabilidad_de_morir(self):
        return self._probabilidad_de_morir

    @probabilidad_de_morir.setter
    def probabilidad_de_morir(self, probabilidad_de_morir):
        if isinstance(probabilidad_de_morir, int):
            self._probabilidad_de_morir = probabilidad_de_morir
        else:
            print("El tipo de dato en probabilidad_de_morir no corresponde")