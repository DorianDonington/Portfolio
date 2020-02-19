#NIA's: 217447, 217723, 194985. Group Code: AN. Professor: Sergio Ivan Giraldo 
import logging

from .hanoi_exception import HanoiException
from .state import State
from .tower import Tower

logging.basicConfig(level = logging.INFO, format = '%(levelname)-10s  %(message)s')

class HanoiGame:
    """
    Main class for management of the data structures and moves of the game.
    """

    def __init__(self, n_discs, n_towers=3):
        """
        Initializes the game with n_discs and n_towers, which defaults to 3.
        At this step, the game can be solved and stored to consult.

        Raises a HanoiException if n_discs is negative or n_towers is less than 3.

        :param n_discs: Number of disks for this game.
        :param n_towers: Number of towers for this game. Default: 3
        """
                
        # 1.- Check the parameters
        if n_discs < 0:
            raise HanoiException ("Invalid number of disks!")
        if n_towers < 3:
            raise HanoiException ("You need at least three towers!")

        # 2.- Initialize the structure attributes (Add the code after this comment)
            
        #Una matriz dentro de la clase que contenga los diferentes estados
        self.states =  [] 

        #Discos totales
        self.n_discs = n_discs 

        #Número de torres
        self.n_towers = n_towers

        #Un booleano por si se ha resuelto recursivamente ya. False=No, True=Si 
        self.solved = False

        #Iniciamos las torres y las llenamos. Almacenamos el primer estado
        self.start_game()
        self.states.append(self.current_state)

        # 4.- Solve and store the optimal solution
        self._solve() 

    def start_game(self):
        """
        Starts the towers and fills the first one. It also creates the current state.
        
        :return: nothing
        """
        #Un array que guarde el estado actual de las torres
        self.towers = []

       #Variables de la clase torre
        for i in range(self.n_towers):
            self.towers.append(Tower())

       #Discos en la primera torre
        for i in reversed(range(self.n_discs)):
            self.towers[0].push_disc(i+1)
        
        #Inicializo el estado de la partida y lo guardo en el primer estado
        self.current_state = State (0,0,0,0,0,self.towers,self.n_discs)

    def get_state(self, step):
        """
        Returns the state at the requested step in the optimal solution.
        Raises a HanoiException if the step index is negative or bigger than the total of states in the optimal
        solution.

        :param step: The step index in the optimal solution.
        :return: The state at the requested step in the optimal solution.
        """
        if (step < 0):
            raise HanoiException ("Step must be between 0 and " + str(len(self.states))+"!")
        elif (step > (len(self.states)-1)):
            raise HanoiException ("Step must be between 0 and " + str(len(self.states)))
        else:
            return self.states[step] #Array de 0 a n. len = n+1. De ahí el -1
           
    def get_n_discs(self):
        """
        Returns the number of disks of this game.

        :return: The number of disks of this game.
        """
        return self.n_discs 

    def get_n_towers(self):
        """
        Returns the number of towers of this game.

        :return: The number of towers of this game.
        """
        return self.n_towers 

    def get_n_states(self):
        """
        Returns the number of states of the optimal solution. Ideally, it should be the size of the structure used to
        store the optimal solution states.

        :return: The number of states of the optimal solution.
        """
        return len(self.states)

    def pistas(self):
        """
        Returns the tower that should recieve a disk acordingly to the optimal solution. Returns false if the current_state does not match
        any of the steps in the optimal solution. It sums 1 for every tower stored in a specific state equal to the same tower in the current
        state, and if the n towers are equal then it returns the target for the next move

        :return: The destiny tower. False otherwise.
        """
        for i in range(len(self.states)): 
            if(sum(1 for j in range(self.get_n_towers()) if self.states[i].towers[j] == self.current_state.towers[j]) == len(self.current_state.towers)):
                return (self.states[i+1].target+1)
        return False

    def move(self, source, target, move_id=None, depth=None):
        """
        Moves a disk from source tower to target tower.
        Raises a HanoiException if source and target are the same or if the move is invalid (the disk moved is bigger
        than the last disk in the target tower, the source tower is empty...)

        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param move_id: Identifier of the movement. Useful as information for the optimal state.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        :return: The new state generated by the move.
        """

        disc = self.towers[source].pop_disc()

        try:
            self.towers[target].push_disc(disc)
        except:
            self.towers[source].push_disc(disc) #Colocamos el disco donde estaba si no puede ir en el destino
            raise HanoiException ("Ilegal move!")
        
        if self.solved == False:
            self.current_state = State(move_id,depth,disc,source,target,self.towers,self.n_discs)
        else:
            self.current_state = State(0,0,0,0,0,self.towers,self.n_discs)

        return self.current_state

    def _solve(self):
        """
        Generates and stores the optimal solution, reinitializing the towers afterwards.
        """
        self.destino = 2 #Por convención con los tests
        aux = 1 #Por convención con los tests
        sou= 0

        self._solve_rec(self.n_discs,sou,self.destino,aux)
        self.start_game()
        self.solved = True

    def _solve_rec(self, n_discs, source, target, aux, depth=0):
        """
        Recursive call to solve the hanoi game optimally.

        :param n_discs: Number of disks to be moved.
        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param aux: Tower to be used as auxiliary.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        """

        if n_discs > 0: 
            self._solve_rec(n_discs-1,source,aux,target,depth+1)
            state = self.move(source,target,move_id=len(self.states),depth = depth+1) 
            self.states.append(state)
            self._solve_rec(n_discs-1,aux,target,source,depth+1)

    def print_optimal_state(self, step):
        """
        Prints the optimal state at the selected step in the required format.

        :param step: Step index of the optimal solution.
        """

        if step > len(self.states) or step < 0:
            raise HanoiException ("Step can't be negative!")
        elif (step > (len(self.states)-1)):
            raise HanoiException ("There's only",len(self.states),"states!")
        else:
            return self.states[step] #Array de 0 a n. len = n+1. De ahí el -1

    def print_optimal_solution(self):
        """
        Prints all the states of the optimal solution in the required format.
        """
        for state in self.states:
            print(state)

    def is_finished(self):
        """
        Checks if the interactive game is finished, returns True if is finished, False otherwise.

        :return: True if the game is finished, False otherwise.
        """
        finished = False
        if len(self.current_state.towers[self.destino]) == self.n_discs: #Si la torre de destino tiene tantos discos como el total, es que hemos ganado
            finished = True
        return finished

    def get_current_state(self):
        """
        Returns the current state of the game.

        :return: The current state of the game.
        """
        return self.current_state

    def __repr__(self):
        """
        Returns a string with the internal representation of the game. This method can be used to represent the game
        information in a different format than the requested.

        :return: A string with the internal representation of the game.
        """
        return repr(self.current_state)

    def __str__(self):
        """
        Returns a string with the representation of the current state of the game in the requested format.

        :return: A string with the representation of the current state of the game in the requested format
        """
        return str(self.current_state)
