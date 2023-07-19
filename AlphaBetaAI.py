# Harry Irwin, CS76, October 24th 2022
# AlphaBetaAI.py implements a minimax search algorithim
# with alpha beta pruning for our chess game

import chess
import math
import random
from ZobristHashing import ZobristHashing

class AlphaBetaAI():
    def __init__(self, depth):
        self.depth = depth
        self.player = None
        self.nodes_vistited = 0
        self.zobristTable = ZobristHashing()
        self.hash = 0
        self.transposition_table = {}
        self.skip_counter = 0


    # updates the zobrist hash value based on a certain move
    def update_hash(self, move, board):
        source = move.from_square
        dest = move.to_square
        
        # if taking a piece then hash it out
        if board.piece_at(dest) != None:
            self.hash ^= self.zobristTable.zobristTable[dest % 8][dest // 8][self.zobristTable.indexOf(board.piece_type_at(dest))]
            
        # hash piece into new square
        self.hash ^= self.zobristTable.zobristTable[dest % 8][dest // 8][self.zobristTable.indexOf(board.piece_type_at(source))]
        # hash piece out of old square 
        self.hash ^= self.zobristTable.zobristTable[source % 8][source // 8][self.zobristTable.indexOf(board.piece_type_at(source))]
    
    
    def choose_move(self, board):
        #save the player for our eval function
        self.player = board.turn

        if self.hash == 0:
            self.hash = self.zobristTable.getHash(board)
        else:
            previous = board.pop()
            self.update_hash(previous, board)
            board.push(previous)
        

        self.depth += 1
        self.nodes_visited = 0
        
        
        utility, move = self.max_value(board, -math.inf, math.inf)
        self.transposition_table[self.hash] = utility, move, self.depth

        # display the number of nodes visited and the utility of our move
        print(f"nodes visited: {self.nodes_visited}")
        print(f"utility: {utility}")


        self.update_hash(move, board)
        
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
        
    # our max_value function, this time modified to prune 
    def max_value(self, board, alpha, beta):
        self.nodes_visited += 1
        self.depth -= 1

        # ensure we have not reached a terminal state
        if self.cutoff_test(board):
            return self.utility(board), None

        # otherwise loop through all the moves
        v = -math.inf
        movelist = self.shuffle_moves(board.legal_moves)
        move = movelist[0]

        for a in movelist:        
            # update the hash
            old_hash = self.hash
            #new_hash = self.update_hash(move, board)
            
            if self.hash in self.transposition_table:
                if self.transposition_table[self.hash][2] <= self.depth:
                    self.skip_counter += 1
                    v2 = self.transposition_table[self.hash][0]
                    a2 = self.transposition_table[self.hash][1]
            else:
                board.push(a)
                v2, a2 = self.min_value(board, alpha, beta)
                self.depth += 1
                board.pop()
            
            # reverse the hash
            self.hash = old_hash

            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)

            if v >= beta:
                return v, move
            
        return v, move

    # our min value function, this time modified to prune
    def min_value(self, board, alpha, beta):
        self.nodes_visited += 1
        self.depth -= 1

        # ensure we have not reached a terminal position
        if self.cutoff_test(board):
            return self.utility(board), None
        v = math.inf

        # otherwise loop through all moves
        movelist = self.shuffle_moves(board.legal_moves)
        move = movelist[0]
        for a in movelist:
            #update the hash
            
            old_hash = self.hash
            self.update_hash(move, board)

            board.push(a)
            v2, a2 = self.max_value(board, alpha, beta)
            self.depth+=1
            board.pop()

            # reverse the hash
            self.hash = old_hash

            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha: return v, move
        return v, move



    
