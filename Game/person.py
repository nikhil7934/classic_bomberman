''' This is the person class cares about the all persons'''


class Person(object):
    ''' This is the person class set all postions for persons'''

    def __init__(self, xpos, ypos, life):
        self.__xpos = xpos
        self.__ypos = ypos
        self.__life = life

    def update_position(self, npos):
        '''This updates the poisition '''
        self.__life = npos[2]
        self.__xpos = npos[0]
        self.__ypos = npos[1]

    def get_position(self):
        '''This return current poisition '''
        return [self.__xpos, self.__ypos, self.__life]
