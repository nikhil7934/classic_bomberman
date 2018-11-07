''' This module maintains the board everytime '''


class Board(object):
    ''' This cares about the Board class '''

    def __init__(self):
        self.__rows = 42
        self.__cols = 76
        self.__board = []
        self.__emcells = []
        self.__encells = []
        self.__awalls = []
        self.__bricks = []
        self.empty_cell()
        self.walls()
        self.make_board()

    def set_bomber(self, tok):
        '''This is to set bomber'''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_green('B')

    def set_enemy(self, tok):
        ''' This is to set enemy '''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_red('E')

    def set_walls(self, tok):
        ''' This is to set walls'''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_magneta('/')

    def make_empty(self, tok):
        ''' This is to empty cell '''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_magneta(' ')

    def set_bomb1(self, tok):
        ''' this is set bomb '''
        for i in [0, 1]:
            for j in range(4):
                if i == 0:
                    self.__board[tok[0] + i][tok[1] + j] = self.pr_yellow(str(tok[2]))
                else:
                    self.__board[tok[0] + i][tok[1] + j] = self.pr_green('B')

    def set_bomb(self, tok):
        ''' This is set bomb '''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_yellow(str(tok[2]))

    def add_brick(self, tok):
        ''' This is add Bricks '''
        self.__bricks.append(tok)

    def get_bricks(self):
        ''' This is to get Bricks '''
        return self.__bricks

    def get_walls(self):
        ''' This is to get Walls '''
        return self.__awalls

    def add_enemy(self, tok):
        ''' This is to add enemy '''
        self.__encells.append(tok)

    def remove_enemy(self, tok):
        ''' This is to removes enemy'''
        self.__encells.remove(tok)

    def get_enemy(self):
        ''' This is to get Enemy '''
        return self.__encells

    def get_empty_cells(self):
        ''' This is to get empty cells'''
        if [2, 4] in self.__emcells:
            self.__emcells.remove([2, 4])
        return self.__emcells

    def add_empty_cells(self, tok):
        '''this is to get all empty cells'''
        self.__emcells.append(tok)

    def remove_empty_cells(self, tok):
        '''#this is to remove empty cells'''
        self.__emcells.remove(tok)

    def ret_game_parameters(self):
        '''#this is to parameters'''
        self.__rows = 42
        return [0, 0]

    def set_exp(self, tok):
        '''#this is to set exp'''
        for i in [tok[0], tok[0] + 1]:
            for j in range(4):
                self.__board[i][tok[1] + j] = self.pr_yellow('^')

    def make_board(self):
        '''#This is to make board'''
        rest = 0
        head1 = [(['X'] * 4) + (([' '] * 4) + (['X'] * 4)) * 9 for _ in range(24)]
        head2 = 0
        self.__board.append(['X'] * self.__cols)
        self.__board.append(['X'] * self.__cols)
        for i in range(2, self.__rows - 2):
            rest = rest + 1
            if rest == 1 or rest == 2:
                self.__board.append((['X'] * 4) + ([' '] * 68) + (['X'] * 4))
            else:
                self.__board.append(head1[head2])
                head2 = head2 + 1
                if rest == 4:
                    rest = 0
        self.__board.append(['X'] * self.__cols)
        self.__board.append(['X'] * self.__cols)

    def pr_board(self):
        '''#This is print board'''
        for row in self.__board:
            print ''.join(row)

    def pr_red(self, prt):
        '''#This is print red color'''
        self.__rows = 42
        return "\033[91m{}\033[00m" .format(prt)

    def pr_blue(self, prt):
        '''#This is to print blue color'''
        self.__rows = 42
        return '\033[34m{}\033[00m'.format(prt)

    def pr_grey(self, prt):
        '''#This is for grey color'''
        self.__rows = 42
        return "\033[97m{}\033[00m" .format(prt)

    def pr_magneta(self, prt):
        '''#This is for magneta color'''
        self.__rows = 42
        return "\033[35m{}\033[00m".format(prt)

    def pr_yellow(self, prt):
        '''#This is for yellow color'''
        self.__rows = 42
        return "\033[93m{}\033[00m" .format(prt)

    def pr_green(self, prt):
        '''#This is for green color'''
        self.__rows = 42
        return "\033[92m{}\033[00m" .format(prt)

    def empty_cell(self):
        ''''#this is for empty cells'''
        rest1 = 0
        walk = 2
        while walk < self.__rows - 2:
            rest1 = rest1 + 1
            if rest1 == 1:
                icon = 4
                while icon < 72:
                    self.__emcells.append([walk, icon])
                    icon = icon + 4
            else:
                icon = 4
                while icon < 72:
                    self.__emcells.append([walk, icon])
                    icon = icon + 8
                rest1 = 0
            walk = walk + 2

    def walls(self):
        '''#This is for walls'''
        icon = 0
        while icon < self.__rows:
            if icon in [0, self.__rows - 2]:
                jcon = 0
                while jcon < self.__cols:
                    self.__awalls.append([icon, jcon])
                    jcon = jcon + 4
            elif icon % 4 == 0:
                jcon = 0
                while jcon < self.__cols:
                    self.__awalls.append([icon, jcon])
                    jcon = jcon + 8
            else:
                self.__awalls.append([icon, 0])
                self.__awalls.append([icon, self.__cols - 5])
            icon = icon + 2
