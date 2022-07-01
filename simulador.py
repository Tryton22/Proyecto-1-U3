from comunidad import Comunidad
from enfermedad import Enfermedad
import random
prob_inf = 15
prob_mor = 23
con_fis = 5
poblacion = 1000
pasos = 50

class Simulador():
    def __init__(self):
        self._comunidad = None
        self._dias = 0

    @property
    def comunidad(self):
        return self._comunidad

    @comunidad.setter
    def comunidad(self, comunidad):
        if isinstance(comunidad, Comunidad):
            self._comunidad = comunidad
        else:
            print("El tipo de dato en comunidad no corresponde")

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self,dias):
        if isinstance(dias, int):
            self._dias = dias
        else:
            print('El tipo de dato en dias no corresponde ')

    def comprobar_recuperacion_o_muerte(self, i):
        dias_enfermo = i.aumento_dias_enfermo()
        if dias_enfermo > 7:
            i.enfermo = 1
            self.comunidad._recuperados += 1
            self.comunidad._infectados -= 1
            return 0
        
        else:  
            prob_mor = self.comunidad.enfermedad.probabilidad_de_morir         
            if dias_enfermo == 1 or dias_enfermo == 7:
                probabilidad_real = prob_mor / 8   
            elif dias_enfermo == 2 or dias_enfermo == 6:
                probabilidad_real = prob_mor / 4
            elif dias_enfermo == 3 or dias_enfermo == 5:
                probabilidad_real = prob_mor / 2
            else:
                probabilidad_real = prob_mor

            probabilidad_de_morir = random.randint(0,1000)

            if probabilidad_de_morir <= probabilidad_real:
                i.enfermo = 1
                self.comunidad._recuperados += 1
                self.comunidad._infectados -= 1
                return 0
            else:
                return 1

    def contagio(self, j, factor):
        probabilidad_de_infeccion = self.comunidad.enfermedad.probabilidad_de_infectarse * factor
        probabilidad_de_infectarse = random.randint(0,100)
        
        if probabilidad_de_infectarse <= probabilidad_de_infeccion:
            j.enfermo = 0
            self.comunidad._susceptibles -= 1
            self.comunidad._infectados += 1

    def realizar_contactos(self, i):
        contactos_fisicos = random.randint(1, self.comunidad.promedio_conexion_fisica)
        while contactos_fisicos > 0:
            contacto_aleatorio = random.randint(1,len(self._comunidad._ciudadanos))
            for j in self.comunidad._ciudadanos:    
                id_contacto_aleatorio = j.id
                if id_contacto_aleatorio == contacto_aleatorio:
                    if j.enfermo == False and j.id_familia == i.id_familia:
                        self.contagio(j, 2)                                       
                    elif j.enfermo == False and j.id_familia != i.id_familia:
                        self.contagio(j, 1)
            
            contactos_fisicos -= 1

    def pandemia(self):
        dias_de_simulacion = self._dias
        while dias_de_simulacion > 0:
            for i in self._comunidad._ciudadanos:
                if i.enfermo == True and i.recuperado_getter() == False:
                    estado = self.comprobar_recuperacion_o_muerte(i)
                    if estado != 0:
                        self.realizar_contactos(i)                                                                                                                                                               
            print("INFECTADOS = ", self._comunidad._infectados, 
                  "SANOS =", self._comunidad._susceptibles, 
                  "RECUPERADOS =", self._comunidad._recuperados)                    
            dias_de_simulacion -= 1       

def main():
    covid = Enfermedad()
    covid.nombre = 'Covid-19'
    covid.probabilidad_de_infectarse = prob_inf
    covid.probabilidad_de_morir = prob_mor

    talca = Comunidad()
    talca.comunidad = 'Talca'
    talca.promedio_conexion_fisica = con_fis
    talca.num_ciudadanos = poblacion
    talca.enfermedad = covid
    talca.crear_ciudadanos()
    talca.inicio()

    simulacion = Simulador()
    simulacion.comunidad = talca
    simulacion.dias = pasos
    simulacion.pandemia()

if __name__ == "__main__":
    main()