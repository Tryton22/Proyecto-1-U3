from enfermedad import Enfermedad
from ciudadano import Ciudadano
import random

class Comunidad():
    def __init__(self):
        self._comunidad = None
        self._promedio_conexion_fisica = None
        self._num_ciudadanos = None
        self._enfermedad = None

        self._susceptibles = 0
        self._infectados = 0
        self._recuperados = 0
        self._ciudadanos = []
        
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
    def promedio_conexion_fisica(self):
        return self._conexion_fisica

    @promedio_conexion_fisica.setter
    def promedio_conexion_fisica(self, conexion):
        if isinstance(conexion, int):
            self._conexion_fisica = conexion
        else:
            print("El tipo de dato en conexion fisica no corresponde")

    @property
    def num_ciudadanos(self):
        return self._num_ciudadanos

    @num_ciudadanos.setter
    def num_ciudadanos(self, num_ciudadanos):
        if isinstance(num_ciudadanos, int):
            self._num_ciudadanos = num_ciudadanos
        else:
            print("El tipo de dato en num_ciudadanos no corresponde")

    @property
    def enfermedad(self):
        return self._enfermedad
               
    @enfermedad.setter
    def enfermedad(self, enfermedad):
        if isinstance(enfermedad, Enfermedad):
            self._enfermedad = enfermedad
        else:
            print("El tipo de dato en enfermedad no corresponde")

    def crear_ciudadanos(self):
        id = 1
        id_familia = 1
        familia = 1
        cantidad_ciudadanos = self._num_ciudadanos
        
        while cantidad_ciudadanos > 0:
        
            #Se identifica si el ciudadano tendra familia o no
            posibilidad_familia = random.randint(0,10)

            if posibilidad_familia == 0 or posibilidad_familia == 1:
                familia = 1
            elif posibilidad_familia >= 2 and posibilidad_familia <= 5:
                familia = 2
            elif posibilidad_familia >= 6 and posibilidad_familia <= 8:
                familia = 3
            elif posibilidad_familia == 9 or posibilidad_familia == 10:
                familia = 4
            
            while familia > 0:
                self._ciudadano = Ciudadano()
                self._ciudadano.id = id
                self._ciudadano.id_familia = id_familia
                self._ciudadano.comunidad = self._comunidad

                self._ciudadanos.append(self._ciudadano)
                
                familia = familia - 1
                cantidad_ciudadanos = cantidad_ciudadanos - 1
                id = id + 1
                self._susceptibles += 1

                if cantidad_ciudadanos == 0:
                    familia = 0
            id_familia = id_familia + 1
                
    def inicio(self):
    
        paciente_cero = random.randint(1,len(self._ciudadanos))

        for i in self._ciudadanos:

            id_paciente_cero = i.id
            
            if id_paciente_cero == paciente_cero:
                self._susceptibles -= 1
                self._infectados += 1
                i.enfermo = 0               
        #print(self._ciudadanos)