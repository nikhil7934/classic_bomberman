''' This module for Bomberman which inherites from Person Class '''
#from board import Board
from person import Person


class BomberMan(Person):
    '''This is a class for Bomberman cares for position of bomberman everytime '''

    def __init__(self):
        super(BomberMan, self).__init__(2, 4, 3)
