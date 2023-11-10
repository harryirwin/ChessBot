# MinimaxAI.py implements a minimax search algorithim
# for our chess game

import chess
import math
import random

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth
        self.player = None
        self.nodes_vistited = 0

    def choose_move(self, board):
        #save the player for our eval function
        self.player = board.turn

        self.depth += 1
        self.nodes_visited = 0

        utility, move = self.max_value(board)

        # display the number of nodes visited and the utility of our move
        print(f"nodes visited: {self.nodes_visited}")
        print(f"utility: {utility}")

        return move

    # cutoff test returns whether or not a board is in a terminal state or not
    def cutoff_test(self, board) -> bool:
        if self.depth == 0 or board.is_checkmate() or board.is_stalemate() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
            return True
        else:
            return False

    # returns the utility of a certain position from the perspective of the current player
    def utility(self, board):
        # check to see if we are at a checkmate or stalemate and handle accordingly
        if board.is_checkmate(): 
            if board.outcome().winner == self.player:
                return math.inf
            else: return -math.inf
        elif  board.is_stalemate() or board.is_seventyfive_moves() or board.is_fivefold_repetition(): return 0

        # otherwise count all pieces
        sum = 0
        mod = -1
        if self.player == chess.WHITE: 
            mod = 1

        # loop through all pieces and add to our score accordingly
        for i in range(0, 64):
            if board.piece_at(i):
                piece = board.piece_at(i).symbol()
                if piece == "P": sum += mod * 1
                elif piece == "p": sum -= mod * 1
                elif piece == "N" or piece == "B": sum += mod * 3
                elif piece == "n" or piece == "b": sum -= mod * 3
                elif piece == "R": sum += mod * 5
                elif piece == "r": sum -= mod * 5
                elif piece == "Q": sum += mod * 9
                elif piece == "q": sum -= mod * 9
        return sum

    # shuffle moves randomly shuffles the moves so that our program does not get stuck in loops
    def shuffle_moves(self, movelist):
        move_list = list()
        for a in movelist:
            move_list.append(a)

        n = len(move_list)
        for i in range(n):
            j = random.randint(0, n-1)
            element=move_list.pop(j)
            move_list.append(element)
        return move_list
        
    # first part of our minimax algorithim, returns the best move that our AI can make
    def max_value(self, board):
        self.nodes_visited += 1
        self.depth -= 1

        # ensure we have not reached the end yet
        if self.cutoff_test(board):
            return self.utility(board), None
        
        v = -math.inf

        # loop through all moves
        movelist = self.shuffle_moves(board.legal_moves)
        for a in movelist:
            board.push(a)

            # take the max of v and minvalue
            v2 = self.min_value(board)[0]
            self.depth += 1
            board.pop()
            if v2 >= v:
                v, move = v2, a
            
        return v, move

    # second part of our minimax algorithim, returns the best move that our opponent can make
    def min_value(self, board):
        self.nodes_visited += 1
        self.depth -= 1

        # ensure we are not at a terminal state
        if self.cutoff_test(board):
            return self.utility(board), None
        v = math.inf

        # shuffle the moves and then loop over them
        movelist = self.shuffle_moves(board.legal_moves)
        for a in movelist:
            board.push(a)

            # take the min of v and maxvalue
            v2 = self.max_value(board)[0]
            self.depth+=1
            board.pop()
            if v2 <= v:
                v, move = v2, a
        return v, move
