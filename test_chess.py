# Harry Irwin, CS76, October 24th 2022
# test_chess.py runs various test on our algorithims


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepening import IterativeDeepening
from ZobristHashing import ZobristHashing

# # TEST 1: minimax vs minimax depth 1 (results in stalemate a lot of the time, should be pretty dumb)
# player1 = MinimaxAI(1)
# player2 = MinimaxAI(1)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())


# # TEST 2: minimax depth 1 vs minimax depth 2 (depth 2 should win)
# player1 = MinimaxAI(1)
# player2 = MinimaxAI(2)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# # Test 3: minimax depth 2 vs minimax depth 2 (could go either way)
# player1 = MinimaxAI(2)
# player2 = MinimaxAI(2)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# # Test 3: AlphaBeta depth 3 vs AlphaBeta depth 3 (should go either way)
# player1 = AlphaBetaAI(3)
# player2 = AlphaBetaAI(3)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# # Test 4: Alphabeta depth 2 vs minimax depth 2 (should go either way)
# player1 = AlphaBetaAI(2)
# player2 = MinimaxAI(2)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# # Test 5: Alphabeta depth 3 vs minimax depth 2 (alphabeta should take the win)
# player1 = AlphaBetaAI(3)
# player2 = MinimaxAI(2)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# # Test 6: Iterative deepening
# player1 = IterativeDeepening(2)
# player2 = IterativeDeepening(2)

# game = ChessGame(player1, player2)

# while not game.is_game_over():
#     print(game)
#     game.make_move()
# print(game.board)
# print(game.board.outcome())

# Test 7: scenario 1 described in ed discussion for both minimax and alphabeta
# note that the moves and utilitys should be the same for both but the alphabeta should visit less nodes
# player1 = MinimaxAI(3)
# player2 = MinimaxAI(3)

# game = ChessGame(player1, player2)

# game.board = chess.Board(fen="1k2r2r/ppp2Q2/3p3b/2nP3p/2PN4/6PB/PP3R1P/1K6 b - - 0 1")

# game.make_move()
# game.make_move()
# game.make_move()

# p1_count = 0
# p2_count = 0


# for i in range(1000):    
#     player1 = AlphaBetaAI(2)
#     player2 = AlphaBetaAI(2)

#     game = ChessGame(player1, player2)

#     while not game.is_game_over():
#         print(game)
#         game.make_move()
#     if game.board.outcome().winner:
#         p1_count += 1
#     elif not game.board.outcome().winner:
#         p2_count += 1
#     print(p1_count)
#     print(p2_count)
    #print(game.board)
    #print(game.board.outcome())
    #print(player1.skip_counter)
# game.board = chess.Board(fen="1k2r2r/ppp2Q2/3p3b/2nP3p/2PN4/6PB/PP3R1P/1K6 b - - 0 1")

p1 = 0
p2 = 0
p3 = 0
total_skips = 0
for _ in range(10):
    player1 = AlphaBetaAI(3)
    player2 = AlphaBetaAI(3)

    game = ChessGame(player1, player2)


    while not game.is_game_over():
        print(game)
        game.make_move()
    print(game.board.outcome())
    if game.board.outcome().winner:
        p1 += 1
    elif game.board.outcome().winner == None:
        p3 += 1
    else:
        p2 += 1
    print(f"Total skips for player 1: {player1.skip_counter}")
    total_skips += player1.skip_counter

print(p1)
print(p2)
print(p3)
print(total_skips)

# # Test 8: scenario 2 described in ed discussion for both minimax and alphabeta
# # note that the moves and utilitys should be the same for both but the alphabeta should visit less nodes
# player1 = MinimaxAI(3)
# player2 = MinimaxAI(3)

# game = ChessGame(player1, player2)

# game.board = chess.Board(fen="rn1r2k1/1pq2p1p/p2p1bpB/3P4/P3Q3/2PB4/5PPP/2R1R1K1 w - - 1 2")

# game.make_move()
# game.make_move()

# player1 = AlphaBetaAI(3)
# player2 = AlphaBetaAI(3)

# game = ChessGame(player1, player2)

# game.board = chess.Board(fen="rn1r2k1/1pq2p1p/p2p1bpB/3P4/P3Q3/2PB4/5PPP/2R1R1K1 w - - 1 2")

# game.make_move()
# game.make_move()

