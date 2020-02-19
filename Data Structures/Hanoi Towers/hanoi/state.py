#NIA's: 217447, 217723, 194985. Group Code: AN. Professor: Sergio Ivan Giraldo 
from .hanoi_exception import HanoiException

class State:
    """
    Class for storing and managing Hanoi game states.
    """
    def __init__(self, move_id, depth, moved_disc, source, target, towers, n_discs):
        """
        Initializes a state with all the information needed to represent it in the requested format.

        :param move_id: Identifier of the move. Ideally, the step number.
        :param depth: Recursion depth at which this state is generated.
        :param moved_disc: The disc moved to reach this state. Ideally, a disk is defined just by its size.
        :param source: Tower from which the disc is moved.
        :param target: Tower to which the disc is moved.
        :param towers: Towers of the game.
        :param n_discs: Number of discs of the game.
        """

        self.move_id = move_id
        self.depth = depth
        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        self.n_discs = n_discs

        self.towers = []

        for tower in towers:
            copia = tower.as_list()
            self.towers.append(copia)
            
       # En vez de copiar las torres, copiamos los arrays de dentro
       # Eso es debido porque no es posible copiar las torres sin el import de la clase o sin usar deepcopy
       # Además, por conveniencia con los test, aunque estrictamente se pida que se devuelva una torre, en vez de eso
       # utilizaremos un array de discs. Entonces, cuando se haga referencia a self.towers dentro de esta clase o fuera, 
       # será el equivalente al atributo .discs de cuando llamamos al HanoiGame.towers. Más info en la documentación

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx. Depending on the implementation of the state, this method can be
        invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.
        :return: The tower corresponding to the idx.
        """
        if (idx < 0):
            raise HanoiException ("Index must be between 0 and ",len(self.towers)-1)
        elif (idx > len(self.towers)-1): #Array del 0 al 2. len = 3. De ahí el -1
            raise HanoiException ("There's only",len(self.towers),"towers!")
        else:
            return self.towers[idx]
        

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        repre = "Move id: %s. Rec Depth: %s. Last move: %s Disk. From: %s. To: %d. \n" % (self.move_id,self.depth,self.moved_disc,self.source+1,self.target+1)
        for i in range(len(self.towers)):
            repre += "Tower %d: %s. " % (i+1,repr(self.towers[i]))
        return repre

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        if self.move_id != 0:
            header = """\nMove id %d Rec Depth %d\nLast move: %d Disk, from %d to %d\n""" % (self.move_id,self.depth,self.moved_disc,self.source+1,self.target+1)

        else: #La cabecera no se pone en el mov_id = 0 ni en jugadas humanas
            header = "\n"  

        torres_dibujo= ""
        maxdisc = self.n_discs 
        for nivel in reversed(range(maxdisc)):
            for tower in self.towers:
                try:
                    torres_dibujo += ((maxdisc-tower[nivel])*".")+(tower[nivel]*"#")+"|"+(tower[nivel]*"#")+((maxdisc-tower[nivel])*".")+" "
                except IndexError:
                    torres_dibujo += maxdisc*"."+"|"+maxdisc*"."+" "
            
            torres_dibujo += "\n"

        torres_titulo= ""
        caracs_titulos = 7 
        caracs_base = maxdisc*2+1 #Dos bandas a cada torre mas el palo del medio
        espacios= int((caracs_base-caracs_titulos)/2)*" "
        for tower in range(len(self.towers)):
            torres_titulo += """%sTower %d%s """ % (espacios,tower+1,espacios)
        torres_titulo+="\n"

        dibujo_final= header+torres_dibujo+torres_titulo
        return str(dibujo_final)

