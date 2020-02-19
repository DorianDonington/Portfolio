#NIA's: 217447, 217723, 194985. Group Code: AN. Professor: Sergio Ivan Giraldo 
from .hanoi_exception import HanoiException

class Tower:
    """
    Class for storing and managing Hanoi game towers.
    """

    def __init__(self):
        """
        Initializes the tower.
        """
        self.discs = []

    def is_empty(self):
        """
        Returns if a tower is empty or not, it is, if the tower has no discs.

        :return: True if is empty, it is, if the tower has no discs, False otherwise
        """
        if self.discs == []:
            return True
        else:
            return False

    def size(self):
        """
        Returns the size (number of discs) of the tower.

        :return: The size (number of discs) of the tower.
        """
        return len(self.discs)

    def pop_disc(self):
        """
        Removes a disc from the top of the tower and returns it.
        Raises an HanoiException if the tower is empty.

        :return: The disc removed from the top of the tower.
        """
        if not self.is_empty():
            return self.discs.pop()
        else:
            raise HanoiException ("Tower's empty!")
           
    def push_disc(self, disc):
        """
        Adds a disc to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        if self.is_empty():
            self.discs.append(disc)
        else:
            if self.discs[-1] > disc:
                self.discs.append(disc)
            else:
                raise HanoiException("Invalid move!")

    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        newlist = self.discs.copy()

        return newlist
        
    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        return str(self.discs)

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.
        Llama un str
        :return: A string with the representation of the state in the requested format
        """
        impreso = ""
        for level in reversed(range(self.size())):
            impreso+=(self.discs[0]-self.discs[level])*"."+self.discs[level]*"#"+"|"+self.discs[level]*"#"+(self.discs[0]-self.discs[level])*"."+"\n"
        return str(impreso)
