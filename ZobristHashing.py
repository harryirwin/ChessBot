import chess
import math
import random

class ZobristHashing():
    
    def __init__(self):
        # 8x8x12 array
        self.zobristTable = [[[self.rand_number() for k in range(12)] for j in range(8)] for i in range(8)]

    # random number generator for zobrist hashing
    def rand_number(self):
        min = 0
        max = pow(2, 64)
        return random.randint(min, max)
    
    # associates every piece with a number for zobrist hashing
    def indexOf(self, piece):
        if (piece=='P'):
            return 0
        elif (piece=='N'):
            return 1
        elif (piece=='B'):
            return 2
        elif (piece=='R'):
            return 3
        elif (piece=='Q'):
            return 4
        elif (piece=='K'):
            return 5
        elif (piece=='p'):
            return 6
        elif (piece=='n'):
            return 7
        elif (piece=='b'):
            return 8
        elif (piece=='r'):
            return 9
        elif (piece=='q'):
            return 10
        elif (piece=='k'):
            return 11
        else:
            return -1
    
    def getHash(self, board):
        h = 0
        map = board.piece_map()
        for i in range(0, 64):
            if i in map:
                    piece = self.indexOf(str(map[i]))
                    h ^= self.zobristTable[i % 8][i // 8][piece]
        return h

    