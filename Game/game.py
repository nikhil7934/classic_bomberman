''' This is game to run '''
import sys
import os
import time
import random
import signal
# import copy
from board import Board
# from person import Person
from bomberman import BomberMan
from enemy import Enemy
from bomb import BOMB
from getchunix import GetchUnix
from alarmexception import AlarmException

GET_CH = GetchUnix()


def alarm_handler(signum, frhame):
    ''' This is for input '''
    signum = signum
    frhame = frhame
    raise AlarmException


def input_to(timeout=1):
    ''' This is for unblocking input '''
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)
    try:
        text = GET_CH()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''


def game():
    ''' This is for game '''
    score = 0
    level = 1
    while level <= 3:
        ert = Enemy([0, 0])
        boa = Board()
        # emcells = boa.get_empty_cells()
        walls = boa.get_walls()
        enemy = []
        penemy = []
        bricks = []
        bomb1 = []
        bome = []
        bman = BomberMan()
        boa.set_bomber(bman.get_position())
        #boa.remove_empty_cells([2, 4])
        if level == 1:
            yew = 0
            while yew < 3:
                loi = random.choice(boa.get_empty_cells())
                ler1 = Enemy(loi)
                boa.remove_empty_cells(loi)
                enemy.append(ler1.get_position())
                penemy.append([(ler1.get_position())[0],
                               (ler1.get_position())[1]])
                boa.set_enemy(ler1.get_position())
                yew = yew + 1
            yew = 0
            while yew < 5:
                loi = random.choice(boa.get_empty_cells())
                boa.remove_empty_cells(loi)
                bricks.append(loi)
                boa.set_walls(loi)
                yew = yew + 1
        elif level == 2:
            yew = 0
            while yew < 4:
                loi = random.choice(boa.get_empty_cells())
                ler1 = Enemy(loi)
                boa.remove_empty_cells(loi)
                enemy.append(ler1.get_position())
                penemy.append([(ler1.get_position())[0],
                               (ler1.get_position())[1]])
                boa.set_enemy(ler1.get_position())
                yew = yew + 1
            yew = 0
            while yew < 10:
                loi = random.choice(boa.get_empty_cells())
                boa.remove_empty_cells(loi)
                bricks.append(loi)
                boa.set_walls(loi)
                yew = yew + 1
        else:
            yew = 0
            while yew < 5:
                loi = random.choice(boa.get_empty_cells())
                ler1 = Enemy(loi)
                boa.remove_empty_cells(loi)
                enemy.append(ler1.get_position())
                penemy.append([(ler1.get_position())[0], (ler1.get_position())[1]])
                boa.set_enemy(ler1.get_position())
                yew = yew + 1
            yew = 0
            while yew < 12:
                loi = random.choice(boa.get_empty_cells())
                boa.remove_empty_cells(loi)
                bricks.append(loi)
                boa.set_walls(loi)
                yew = yew + 1
        os.system('clear')
        boa.pr_board()
        print()
        print()
        print()
        print("Score: ", score)
        print("Level: ", level)
        print("Lives: ", (bman.get_position())[2])
        nextstep = time.time()
        while len(enemy):
            if (bman.get_position())[2] == 0:
                os.system('clear')
                print "#########** GAME OVER **###########"
                print "Final Score:", score
                sys.exit()
            if bome != []:
                #fox = bome.pop()
                hor = bman.get_position()
                for rur in bome:
                    if rur == [hor[0], hor[1]]:
                        hor[2] = hor[2] - 1
                        bman.update_position([2, 4, hor[2]])
                        boa.set_bomber([2, 4, hor[2]])
                        boa.make_empty(rur)
                        boa.add_empty_cells(rur)
                    elif rur in bricks:
                        bricks.remove(rur)
                        boa.add_empty_cells(rur)
                        boa.make_empty(rur)
                        score = score + 20
                    elif rur in penemy:
                        for joc in enemy:
                            if [joc[0], joc[1]] == rur:
                                joc[2] = joc[2] - 1
                            if joc[2] == 0:
                                penemy.remove(rur)
                                enemy.remove(joc)
                                score = score + 100
                                boa.make_empty(rur)
                                boa.add_empty_cells(rur)
                            else:
                                boa.set_enemy(rur)
                    elif rur in boa.get_empty_cells():
                        boa.make_empty(rur)
                        boa.add_empty_cells(rur)
                    bome.remove(rur)
                bomb1 = []
            lwe = bman.get_position()
            if bomb1 != [] and bomb1[2] == 0:
                bome = bom.set_explosion(boa)

            if bomb1 != [] and [lwe[0], lwe[1]] == [bomb1[0], bomb1[1]]:
                boa.set_bomb1(bomb1)

            elif bomb1 != [] and [lwe[0], lwe[1]] != [bomb1[0], bomb1[1]]:
                boa.set_bomb(bomb1)

            ser1 = input_to()
            if time.time() >= nextstep:
                nextstep += 1
                ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)

            if ser1 in ['a', 's', 'd', 'w', 'b', 'q']:
                if ser1 == 'q':
                    os.system('clear')
                    print "#########** QUITTED GAME **###########"
                    print("Final Score:", score)
                    sys.exit()
                if ser1 == 'b':
                    lrt = bman.get_position()
                    bom = BOMB(lrt[0], lrt[1])
                    bomb1 = bom.get_place()
                    boa.set_bomb1(bomb1)

                elif ser1 == 'a':
                    lrt = bman.get_position()

                    if [lrt[0], lrt[1] - 4] in boa.get_empty_cells():
                        boa.remove_empty_cells([lrt[0], lrt[1] - 4])
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        bman.update_position([lrt[0], lrt[1] - 4, lrt[2]])
                        boa.make_empty([lrt[0], lrt[1]])
                        boa.set_bomber([lrt[0], lrt[1] - 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                    elif [lrt[0], lrt[1] - 4] in penemy:
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        boa.remove_empty_cells([2, 4])
                        boa.make_empty([lrt[0], lrt[1]])
                        bman.update_position([2, 4, lrt[2] - 1])
                        boa.set_bomber([2, 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                elif ser1 == 's':
                    lrt = bman.get_position()
                    if [lrt[0] + 2, lrt[1]] in boa.get_empty_cells():
                        boa.remove_empty_cells([lrt[0] + 2, lrt[1]])
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        bman.update_position([lrt[0] + 2, lrt[1], lrt[2]])
                        boa.make_empty([lrt[0], lrt[1]])
                        boa.set_bomber([lrt[0] + 2, lrt[1]])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                    elif [lrt[0] + 2, lrt[1]] in penemy:
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        # Bo.removeemptycells([2,4])
                        boa.make_empty([lrt[0], lrt[1]])
                        bman.update_position([2, 4, lrt[2] - 1])
                        boa.set_bomber([2, 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                elif ser1 == 'd':
                    lrt = bman.get_position()
                    if [lrt[0], lrt[1] + 4] in boa.get_empty_cells():
                        boa.remove_empty_cells([lrt[0], lrt[1] + 4])
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        bman.update_position([lrt[0], lrt[1] + 4, lrt[2]])
                        boa.make_empty([lrt[0], lrt[1]])
                        boa.set_bomber([lrt[0], lrt[1] + 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                    elif [lrt[0], lrt[1] + 4] in penemy:
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        # Bo.removeemptycells([2,4])
                        boa.make_empty([lrt[0], lrt[1]])
                        bman.update_position([2, 4, lrt[2] - 1])
                        boa.set_bomber([2, 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                elif ser1 == 'w':
                    lrt = bman.get_position()
                    if [lrt[0] - 2, lrt[1]] in boa.get_empty_cells():
                        boa.remove_empty_cells([lrt[0] - 2, lrt[1]])
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        bman.update_position([lrt[0] - 2, lrt[1], lrt[2]])
                        boa.make_empty([lrt[0], lrt[1]])
                        boa.set_bomber([lrt[0] - 2, lrt[1]])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
                    elif [lrt[0] - 2, lrt[1]] in penemy:
                        boa.add_empty_cells([lrt[0], lrt[1]])
                        boa.make_empty([lrt[0], lrt[1]])
                        bman.update_position([2, 4, lrt[2] - 1])
                        boa.set_bomber([2, 4])
                        ert.motion_of_enemy(boa, enemy, bman, walls, bricks, penemy)
            if bomb1 != [] and bomb1[2] != 0:
                bom.set_time()
                bomb1 = bom.get_place()
            os.system('clear')
            boa.pr_board()
            print()
            print()
            print()
            print("Score: ", score)
            print("Level: ", level)
            print("Lives: ", (bman.get_position())[2])
    level += 1


game()
