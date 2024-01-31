import random
from game import Game, Move, Player
from copy import deepcopy

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move

class MinimaxPlayer(Player):
    def __init__(self, max_depth=3):
        super().__init__()
        # depth of minimax search
        self.max_depth = max_depth
        # id that identifies the agent's token, gets updated each move
        self.player_id = None
        # all the border positions from which is possible to extract a cube
        self.border_cubes = [(0, i) for i in range(5)] + [(4, i) for i in range(1, 5)] + [(i, 0) for i in range(5)] + [(i, 4) for i in range(1, 4)]
        # all the possible cube slides
        self.possible_slides = [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        # each player's move stores its role in the current game
        self.player_id = game.get_current_player()
        # best move tuple gets decided by a minimax policy
        _, best_move = self.minimax(game, self.max_depth, float('-inf'), float('inf'), True)
        return best_move

    def minimax(self, game: 'Game', depth, alpha, beta, maximizing_player):
        # if the recursion is at the final depth level or the current node is a final state of the game 
        if depth == 0 or game.check_winner() >= 0:
            # backpropagate the value of the state and a None-move
            return self.state_value(game.get_board()), None

        # if the current step is about maximization
        if maximizing_player:
            # reset best values
            max_eval = float('-inf')
            best_move = None
            # compute which cubes can be extracted from the board
            positions = self.get_possible_moves(game, self.player_id)

            # for each possible cube
            for from_pos in positions:
                # try each move direction
                for move in self.possible_slides:
                    # copy the current state and test if the chosen move is legal
                    new_game = deepcopy(game)
                    if new_game._Game__move(from_pos, move, self.player_id):
                        # if the move is legal proceed to the minimization step
                        eval, _ = self.minimax(new_game, depth - 1, alpha, beta, False)
                        # if the state value reached with (from_pos, move) ply is the best found yet
                        if eval > max_eval:
                            # update best values
                            max_eval = eval
                            best_move = (from_pos, move)
                        # if the max value is higher than bound beta it's not possible to find better solutions
                        if max_eval >= beta:
                            break
                        # update bound alpha
                        alpha = max(alpha, eval)

            return max_eval, best_move
            
        # if the current step is about maximization
        else:
            # reset best values
            min_eval = float('inf')
            best_move = None
            # compute which cubes can be extracted from the board
            positions = self.get_possible_moves(game, 1 - self.player_id)

            # for each possible cube
            for from_pos in positions:
                # try each move direction
                for move in self.possible_slides:
                    # copy the current state and test if the chosen move is legal
                    new_game = deepcopy(game)
                    if new_game._Game__move(from_pos, move, 1 - self.player_id):
                        # if the move is legal proceed to the maximization step
                        eval, _ = self.minimax(new_game, depth - 1, alpha, beta, True)
                        if eval < min_eval:
                            # update best values
                            min_eval = eval
                            best_move = (from_pos, move)
                        # if the min value is lower than alpha it's not possible to find better solutions
                        if min_eval <= alpha:
                            break
                        # update bound beta
                        beta = min(beta, min_eval)

            return min_eval, best_move

    def state_value(self, state):
        # evaluate current state
        test = Game()
        test._board = state
        res = test.check_winner()
        #if minimax agent won: return a positive value
        if res == self.player_id:
            return 1
        # if minimax agent lost: return a negative value
        if res == 1 - self.player_id:
            return -1
        # else return a postive value corresponding to the highest 
        # number of simbols in a single row/column/diagonal
        return self.check_board(state)
    
    def check_board(self, state):
        # evaluate how close the current state is to a winning state
        max_score = 0
        # for each row
        for x in range(state.shape[0]):
            # update the max count about how many cells the player took
            score = sum(state[x, :] == self.player_id)
            if score > max_score:
                max_score = score
        # for each column
        for y in range(state.shape[1]):
            # update the max count about how many cells the player took
            score = sum(state[:, y] == self.player_id)
            if score > max_score:
                max_score = score
        # check the diagonal
        score = sum([1 for x in range(state.shape[0]) if state[x, x] == self.player_id])
        if score > max_score:
            max_score = score
        # check the anti-diagonal
        score = sum([1 for x in range(state.shape[0]) if state[x, -(x + 1)] == self.player_id])
        if score > max_score:
            max_score = score
        return max_score / 5

    def get_possible_moves(self, game: 'Game', current_player_idx: int):
        # get all possible moves for the current player
        moves = []
        # in each border position
        for cube in self.border_cubes:
            # check if the cube is not a cube owned by the opponent
            if game.get_board()[cube[1], cube[0]] != 1 - current_player_idx:
                # if it isn't add it to the available cubes
                moves.extend([cube])
        return moves

if __name__ == '__main__':
    g = Game()
    g.print()
    player1 = MinimaxPlayer(2)
    player2 = RandomPlayer()
    winner = g.play(player1, player2)
    g.print()
    print(f"Winner: Player {winner}")

    g = Game()
    g.print()
    winner = g.play(player2, player1)
    g.print()
    print(f"Winner: Player {winner}")