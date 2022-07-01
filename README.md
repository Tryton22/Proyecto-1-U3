# Proyecto 1, Unidad 3, Programación Avanzada 2022
El objetivo de este proyecto era crear un simulador del comportamiento de una enfermedad 
infecciosa en un población X. Para lograrlo el profesor a cargo (Fabio Durán) 
sugirió que los distintos escenarios que se nos presentara en este simulador se 
ejecutaran a traves de pasos, que se podian pensar como dias, meses, etc, 
lo importante que se debia de ser una unidad de tiempo para ver como surgian los 
cambios en la simulacion. En este desarrollo era importante definir la aleatoridad, 
ya que tal como pasa en la realidad, una enfermedad nunca se va a comportar como se espera.

# Autores
- Claudio La Rosa
- Denise Valdés
- Matías Fonseca

# Ciudadano.py
En esta clase se definen los atributos y metodos que tendra, el objeto ciudadano dentro 
del codigo.
Los atributos definidos permiten saber el nombre de la comunidad a la que
pertenece (self._comunidad), 
otro que le da un id (self._id) y una id de su familia, si es que la tiene (self._id_familia) 
todos estos atributos estan inicializados en NONE, ya que se le agregaran valores mas adelante. 
Los demas atributos permiten saber si el ciudadano esta enfermo 
(por defecto es FALSE, ya que aun no se define ninguna infeccion), 
que en su @setter se define como un int por que toma los valores de 0 y 1 
(cualquier otro valor que se de, no hara nada) ya que, si toma el 1 se entiende que el 
ciudadano se enfermo y cambia los valores por defecto de self._enfermo y self._recuperado y 
si toma el valor 1 se entiende que el paciente enfermo se recupero (self._recuperado = True), 
si esta recuperado de la enfermedad (por defecto es TRUE, por lo mismo que dije antes) 
y cuantos dias enfermo lleva (valor por defecto = 0).

Y como metodos, aparte de los @property y @setter de los atributos, esta una funcion que 
ve que verifica si el ciudadano esta recuperado de la enfermedad o no (def recuperado_getter)
y otra que aumenta en uno el valor por defecto de los dias que el ciudadano esta enfermo 
(def aumento_dias_enfermo).

# Enfermedad.py
En esta clase se definen los atributos y metodos que tendra, el objeto enfermedad dentro
del codigo.
Los atributos de clase nos definen el nombre de la enfermedad (self._nombre), la probabilidad de
contagio que posee la enfermedad (self._probabilidad_de_infectarse) y la probabilidad que tiene 
un ciudadano contagiado de morir (self._probabilidad_de_morir). Todos estos atributos fueron
inicializados en NONE, ya que siguiendo con el codigo se les entregara un valor en concreto.

No posee ningun metodo en especial, solamente los @property y los @setter de los atributos 
explicados en el parrafo anterior.

# Comunidad.py
En esta clase se importaron Enfermedad() y Ciudadano() desde sus respectivos
archivos al igual que un random que ayuda en el tema de la aleatoridad, tambien, se
definen los atributos y metodos que tendra, el objeto comunidad dentro del codigo.
Los atributos de esta clase nos ayudan con el nombre de la comunidad (self._comunidad), 
que esta sobreescrita de la clase Ciudadano(), con el promedio de contacto fisico que tuvo
un ciudadano (self._promedio_conexion_fisica), con el numero total de ciudadanos que existen 
en la comunidad (self._num_ciudadanos), con el nombre de la enfermedad contagiosa a simular 
(self._enfermedad), que igualmente esta sobreescrita de la clase Enfermedad().
Los demas atributos nos dicen la cantidad de ciudadanos que son susceptibles a contagiarse 
(self._susceptibles), la cantidad de ciudadanos inferctados (self._infectados), la cantidad
de ciudadanos recuperados de la enfermedad (self._recuperados) y una lista que contiene 
a todos
los ciudadanos de la comunidad (self._ciudadanos).

Y como metodos, aparte de los @property y los @setter, tenemos 2 funciones, la primera se 
encarga de crear los ciudadanos de la comunidad (def crear_ciudadanos), 
definiendo los id y la familia como 1, cantidad_ciudadanos se define como su atributo 
para su actualizacion, empieza a funcionar si la cantidad de ciudadanos es mayor a 0 
y parte asignandole una familia mediante una  probabilidad del (0,10), 
manejada con la libreria random, el tamaño más grande que puede tener una familia 
son 4, si el ciudadano tiene familia, se crea el objeto Ciudadano con
sus respectivos atributos (cambiandolos por los que fueron inicializados) y aumentan los
ciudadanos capaces de infectarse y otro metodo que te asigna un paciente cero para que se
empiece a contagiar la gente y el simulador agarre ritmo (def inicio), el paciente cero es
elegido de manera random entre todos los ciudadanos creados, lo que aumenta la capacidad 
de contagiarse de los ciudadanos, el numero de infectados y pone en self._enfermo un 0, lo que
signica que un ciudadano se enfermo y no puede sanar, por ahora.

# Simulador.py
En la ultima clase del codigo se importaron Comunidad(), Enfermedad() y la libreria random, 
ademas se definen los atributos y los metodos que tendra el objeto simulacion dentro del 
codigo.
Antes de los atributos y metodos, se inicializaron distintas variables como la poblacion, la
probabilidad de morir, de infectar, contacto fisica y la cantidad de pasos (dias) de la 
simulacion, esto para que sea más facil agregarlos a los objetos creados.
Como atributos tenemos el nombre de la enfermedad, que es sobreescritura de la clase 
Comunidad()
y la cantidad de dias que van a pasar en la simulacion (self._dias)
Y, como metodos, aparte de los @property y los @setter, se tienen unas 
cuantas funciones y un main que hace
correr el programa. La primera funcion (def comprobar_recuperacion_o_muerte)
comprueba si el ciudadano infectado, efectivamente se recupera o se muere, 
mediante probabilidades usando random y cuantos dias lleva enfermo el 
ciudadano (el ciudadano no puede estar enfermo más de una semana y tiene mas posibilidades de 
morir al 4to dia). La segunda funcion (def contagio) calcula la probabilidad que tiene un 
ciudadano infectado de infectar a uno sano mediante un random del (0,100), 
si la probabilidad de infectarse es menor o igual a la de generar infeccion, 
entonces se contagia un nuevo ciudadano. La tercera funcion (def realizar_contactos)
calcula los contactos estrechos de cada uno de los ciudadanos contagiados hasta el momento. 
La cuarta funcion (def pandemia) nos muestra en pantalla el pasar de los dias definidos en
la simulacion, con el detalle de los ciudadanos infectados, sanos y recuperados.
La ultima funcion (def main), que se hizo para que el codigo no se vea tan desordenado, 
crea los objetos Enfermedad(), Comunidad() y Simulador() dandole valores a todos sus 
atributos y llamando a los metodos mas importantes de cada clase para que el codigo arranque.

Despues de estos metodos, se llama a la funcion main() para arrancar el programa y que el
codigo no se vea con tanta sobrecarga de informacion.


