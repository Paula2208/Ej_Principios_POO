class Player:
    def __init__(self, id, name):
        self.__id = id  # Private attribute
        self._points = 0.0  # Protected attribute
        self.rank = "bronce"  # Public attribute
        self.name = name  # Public attribute

    def sayHi(self):
        """
        Player print his greeting
        """
        print("¡Hola! Soy el jugador " + self.name + " y soy rango " + self.rank)

    def sayPlay(self):
        """
        Player print his invitation to play
        """
        print("¡Vamos a jugar! ٩(˘◡˘)۶")

    def getId(self):
        return self.__id

    def getPoints(self):
        return self._points

    def increasePoints(self, addition):
        """
        Add points by parameters to the player's base points
        """
        self._points = self._points + addition
        self.__defineRank()

    def __defineRank(self):  # Private method
        """
        Defines rank name according to the Player's base points
        """
        if self._points <= 25:
            self.rank = "Bronce"
        elif self._points > 25 and self._points <= 50:
            self.rank = "Plata"
        elif self._points > 50 and self._points <= 75:
            self.rank = "Oro"
        elif self._points > 75 and self._points <= 100:
            self.rank = "Diamante"
        elif self._points > 100:
            self.rank = "Maestro"
