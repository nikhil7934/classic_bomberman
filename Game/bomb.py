'''This is bomb module'''
#from board import Board
#from person import Person
#from bomberman import BomberMan
#from enemy import Enemy


class BOMB(object):
    '''This is class for BOMB'''

    def __init__(self, xpos, ypos):
        self.__xpos = xpos
        self.__ypos = ypos
        self.__time = 3

    def get_place(self):
        '''This is gives place '''
        return [self.__xpos, self.__ypos, self.__time]

    def set_time(self):
        '''Bombs explosion time '''
        self.__time -= 1

    def set_explosion(self, bop):
        ''' Set explosion time '''
        tok = self.get_place()
        tok = [tok[0], tok[1]]
        walls = bop.get_walls()
        #emtcells = bop.get_empty_cells()
        rep = [[tok[0] + 2, tok[1]], [tok[0] - 2, tok[1]],
               [tok[0], tok[1] + 4], [tok[0], tok[1] - 4]]

        for ryt in rep:
            if ryt not in walls:
                bop.set_exp(ryt)
        return rep
