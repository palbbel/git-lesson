import random
import numpy as np
from random import *

def setup_ship(b):
    setup_4pship(b)
    x = 2
    while (x > 0):
        setup_3pship(b)
        x = x - 1
    x = 3
    while (x > 0):
        setup_2pship(b)
        x = x - 1
    x = 4
    while (x > 0):
        setup_1pship(b)
        x = x - 1


# this function checks if it's possible to setup a ship using these coordinats
def CellCheck(pol, i, j, length,
              array):  # pol-position(horizontal-1,upright-2); i,j - coordinates; lenght(of a ship); b - array[][];
    if (pol == 1):  # for horizontal position
        right = 0
        left = 0
        k = True
        endi = i + 2
        endj = j + length + 1
        for i in range(i - 1, endi):
            for j in range(j - 1, endj):
                if (i >= 0 and i <= 9 and j >= 0 and j <= 9):
                    if (b[i][j] > 0):
                        k = False
        for j in range(j, endj):
            if (j > 9):
                k = False
        if (k == True):
            right = 1

        k = True
        endj = j + 2
        for i in range(i - 1, endi):
            for j in range(j - length, endj):
                if (i >= 0 and i <= 9 and j >= 0 and j <= 9):
                    if (b[i][j] > 0):
                        k = False
        for j in range(j - 2, endj - 1):
            if (j > 9):
                k = False
        if (k == True):
            left = 1

        if (right == 0 and left == 0):
            return (0)
        if (right == 0 and left == 1):
            return (2)
        if (right == 1 and left == 0):
            return (1)
        if (right == 1 and left == 1):
            return (randint(1, 2))

    if (pol == 2):  # for upright position
        up = 0
        down = 0
        k = True
        endi = i + 2
        endj = j + 2
        for i in range(i - length, endi):
            for j in range(j - 1, endj):
                if (i >= 0 and i <= 9 and j >= 0 and j <= 9):
                    if (b[i][j] > 0):
                        k = False
        for i in range(i - length - 1, endi - 2):
            if (i > 9):
                k = False
        if (k == True):
            up = 1

        k = True
        endi = i + length + 1
        for i in range(i - 1, endi):
            for j in range(j - 1, endj):
                if (i >= 0 and i <= 9 and j >= 0 and j <= 9):
                    if (b[i][j] > 0):
                        k = False
        for i in range(i, endi):
            if (i > 9):
                k = False
        if (k == True):
            down = 1

        if (up == 0 and down == 0):
            return (0)
        if (up == 0 and down == 1):
            return (4)
        if (up == 1 and down == 0):
            return (3)
        if (up == 1 and down == 1):
            return (randint(3, 4))
            # returns:
            # 0 if ship is impossible to setup
            # possible to setup:
            # 1 right
            # 2 left
            # 3 up
            # 4 down


def setup_4pship(b):
    stand = randint(1, 2)  # 1 - horizontally; 2 - upright
    if (stand == 1):
        i = randint(0, 9)
        j = randint(0, 6)
        end = j + 3
        for j in range(j, end + 1):
            b[i][j] = 1
    else:
        i = randint(0, 6)
        j = randint(0, 9)
        end = i + 3
        for i in range(i, end + 1):
            b[i][j] = 1


def setup_3pship(b):
    check = 0;
    while (check == 0):
        stand = randint(1, 2)
        i = randint(0, 9)
        j = randint(0, 9)
        print("i=", i, "j=", j, "pol=", stand)
        check = CellCheck(stand, i, j, 3, b)
        if (check == 1):
            endj = j + 3
            print(check)
            for j in range(j, endj):
                b[i][j] = 1
        if (check == 2):
            endj = j + 1
            print(check)
            for j in range(j - 2, endj):
                b[i][j] = 1
        if (check == 3):
            endi = i + 1
            print(check)
            for i in range(i - 2, endi):
                b[i][j] = 1
        if (check == 4):
            endi = i + 3
            print(check)
            for i in range(i, endi):
                b[i][j] = 1


def setup_2pship(b):
    check = 0;
    while (check == 0):
        stand = randint(1, 2)
        i = randint(0, 9)
        j = randint(0, 9)
        check = CellCheck(stand, i, j, 2, b)
        if (check == 1):
            endj = j + 2
            for j in range(j, endj):
                b[i][j] = 1
        if (check == 2):
            endj = j + 1
            for j in range(j - 1, endj):
                b[i][j] = 1
        if (check == 3):
            endi = i + 1
            for i in range(i - 1, endi):
                b[i][j] = 1
        if (check == 4):
            endi = i + 2
            for i in range(i, endi):
                b[i][j] = 1


def setup_1pship(b):
    check = 0;
    while (check == 0):
        stand = randint(1, 2)
        i = randint(0, 9)
        j = randint(0, 9)
        check = CellCheck(stand, i, j, 1, b)
        if (check != 0):
            b[i][j] = 1


b = np.zeros((10, 10))
setup_ship(b)
for i in range(10):
    print(*[b[i, j] for j in range(10)])