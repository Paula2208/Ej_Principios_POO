from Entities.player import Player

def absExample():
    '''
        Abstraction example execution explained 
    '''

    print('\n\r\n\r......................................../ Abstracción /........................................\n\r\n\r')

    print('''          <<< La abstracción nos permite simplificar entidades complejas representándolas \n\r( ^o^)_/      mediante atributos (cómo se "ven") y métodos (qué "hacen"). >>>\n\r''')

    print("Por ejemplo, creamos una instancia de la clase 'Player' para describir a un jugador de videojuegos.\n\r")
    
    player1 = Player(1, 'Daniela')

    print("Sus atributos son:\n\r")
    print('ID:', player1.getId())
    print('Nombre:', player1.name)
    print('Rango:', player1.rank)
    print('Puntos Totales:', player1.getPoints())

    print("\n\rSus métodos son:\n\r")
    print("* Incrementar los puntos 'increasePoints()'")
    print("    Puntos iniciales:", player1.getPoints())
    print('    Rango Inicial:', player1.rank)
    player1.increasePoints(26)
    print("    Puntos después del incremento:", player1.getPoints())
    print('    Rango después del incremento:', player1.rank)

    print("\n\r* Saludar 'sayHi()'")
    player1.sayHi()

    print("\n\r* Invitar a jugar 'sayPlay()'")
    player1.sayPlay()

    print("\n\r\n\r(っ＾▿＾)っ Aquí termina 'abstracción'.")
    print('................................................................................................\n\r\n\r')