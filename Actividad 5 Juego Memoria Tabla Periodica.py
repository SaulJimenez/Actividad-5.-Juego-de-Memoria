# Actividad 5 - Juego Memoria.
# Autores: Leonardo Delgado Rios-A00827915, Saul Jimenez Torres-A01283849.
# Aplicacion que desarrolla un juego de memoria. 
# Fecha de ultima modificacion: 10/30/2020.
# Se importan las librerias que se utilizaran para el correcto desarrollo de
# la aplicación.
from random import *
from turtle import *
from freegames import path

# Se definen los valores default de las variables a utilizar, en este caso la
# imagen a utilizar, el total de cuadrados que conformaran el juego de memoria
# y el estado de cada una de los cuadrados
car = path('car.gif')
#tiles = list(range(32)) * 2
listaux = ['Americio', 'Aluminio', 'Azufre', 'Bario', 'Berkelio', 'Bohrio',
             'Bromo', 'Cadmio', 'Calcio', 'Carbono', 'Cesio', 'Cromo',
             'Einstenio','Escandio', 'Europio', 'Fluor', 'Fósforo', 'Francio',
             'Germanio', 'Helio', 'Iodo', 'Iterbio', 'Manganeso', 'Mercurio',
             'Neodimio', 'Neón', 'Niquel', 'Osmio', 'Paladio', 'Plata', 'Oro',
             'Plomo']
listaux2 = ['95','13','16','56','97','107','35','48','20','6','55','24','99',
            '21','63','9','15','87','32','2','53','70','25','80','60','10',
            '28', '76', '46', '47', '79', '82' ]
tileaux = ['Am','Al','S','Ba','Bk','Bh','Br','Cd','Ca','C','Cs','Cr','Es',
            'Sc','Eu','F','P','Fr','Ge','He','I','Yb','Mn','Hg','Nd','Ne','Ni',
            'Os', 'Pd', 'Ag', 'Au', 'Pb']
tiles = tileaux * 2
state = {'mark': None}
numtaps = {'taps': 0}
hide = [True] * 64
check = [False] * 64

# Funcion square, se encarga de dibujar los segmentos de recuadros blancos con
# delineado negro.
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('white', 'gray')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Funcion index, convierte las coordenadas de x y y, en un indice para agregar
# posteriormente el número o bien el estado de cada cuadrado.
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Funcion xy, convierte el total de cuadrados en coordenadas x y y.
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Funcion tap, encargada de cambiar el estado de los cuadrados, es decir, en
# caso de que se encuentre la pareja del número seleccionado, convierte el
# valor booleano de la lista hide a false, debido a que se elimina el cuadrado
# blanco y muestra la parte de la imagen.
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    numtaps['taps'] += 1
        
# Funcion draw, encargada de dibujar los cuadros de color blanco con delineado
# negro donde se segmentan las diferentes partes del juego de memoria.
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    # Iteracion dentro la cual verifica el estado de cada uno de las tiles, en
    # caso de que el valor booleano del estado de una tile sea falso, no
    # dibujara el cuadro blanco, por lo que se mostrara parte de la imagen.
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Mientras el valor a dibujar sea diferente de null, para esta actividad
    # el valor se encuentre en un rango de 0 - 32, y que el estado del tile
    # en la lista hide sea true, dibujara el numero asignado a esa tile. Ademas
    # se mostrara el numero de taps que se han realizado al momento en la parte
    # superior derecha del cuadro blanco.
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if len(tiles[mark]) == 1:
           goto(x + 18, y + 12)
        else:
            goto(x + 5, y + 12)
        color('white')
        write(tiles[mark], font=('Arial', 16, 'normal'))
        for i in range(len(tileaux)):
            if tiles[mark] == tileaux[i]:
                goto(x + 32, y + 12)
                write(listaux2[i], font=('Arial', 7, 'normal'))
                goto(x + 3, y + 3)
                write(listaux[i], font=('Arial', 7, 'normal'))
        goto(x + 30, y + 36)
        write(numtaps['taps'])
    
    # Variable check se define con un valor default similar a hide sin embargo
    # esta con false en lugar de true, conforme se encuentren las parejas los
    # valores en hide se volveran false, por lo que si hide es igual a false
    # nos indicara que todas las parejas fueron encontradas, en cuyo caso se
    # termina la ejecucion mostrando un mensaje y el numero de taps totales.
    if hide == check:
        clear()
        up()
        color('black')
        goto(-180,0)
        write("Has ganado. Felicidades!", font=('Arial', 25, 'normal'))
        goto(-150,-30)
        write("Numero de taps: %.f" %(numtaps['taps']), font=('Arial', 25, 'normal'))
        return
        
    update()
    ontimer(draw, 100)

# Aqui se realiza la configuracion de la ventana donde se desarrollara el juego
# ademas se hace el llamado a la funcion draw para ejecutar la aplicacion.
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()