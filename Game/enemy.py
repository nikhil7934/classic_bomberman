''' This module for enemy related functions '''
import random
#from board import Board
from person import Person
#from bomberman import BomberMan


class Enemy(Person):
    ''' This is module for Enemy '''

    def __init__(self, lok):
        self.rot = 0
        ert = random.choice([1, 2])
        super(Enemy, self).__init__(lok[0], lok[1], ert)

    def motion_of_enemy(self, bopp, enemy, boman, walls, bricks, penemy):
        ''' This is for motion '''
        self.rot = 1
        pock = enemy
        for pio in pock:
            roi = [[pio[0], pio[1] - 4], [pio[0], pio[1] + 4],
                   [pio[0] + 2, pio[1]], [pio[0] - 2, pio[1]]]
            while len(roi):
                k = random.choice(roi)
                if k in bopp.get_empty_cells():
                    bopp.remove_empty_cells(k)
                    bopp.add_empty_cells([pio[0], pio[1]])
                    bopp.set_enemy(k)
                    bopp.make_empty([pio[0], pio[1]])
                    enemy.remove(pio)
                    enemy.append([k[0], k[1], pio[2]])
                    penemy.append([k[0], k[1]])
                    break
                elif k == [(boman.get_position())[0], (boman.get_position())[1]]:
                    lrt = boman.get_position()
                    bopp.add_empty_cells([lrt[0], lrt[1]])
                    bopp.make_empty([lrt[0], lrt[1]])
                    boman.update_position([2, 4, lrt[2] - 1])
                    bopp.set_bomber([2, 4])
                    bopp.remove_empty_cells(k)
                    bopp.add_empty_cells([pio[0], pio[1]])
                    bopp.set_enemy(k)
                    bopp.make_empty([pio[0], pio[1]])
                    enemy.remove(pio)
                    enemy.append([k[0], k[1], pio[2]])
                    penemy.append([k[0], k[1]])
                    break
                elif k in walls + bricks:
                    roi.remove(k)
        return
