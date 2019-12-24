# Donovan Lopez. 30284497
####


PLAYER_B = 'B'
PLAYER_W = 'W'




class GameOverError(Exception):
    '''
    if raised, the game is over. The game ends if there are no more
    possible moves or if all the spaces are filled.
    
    '''
    pass

class OthelloGame:
    def __init__(self, board: list, game_mode: str):
        '''
            initializes the components for a game of Othello
        '''
        self.gamemode = game_mode
        
        self.valid_moves_list = []
        self.board = board
        self.player = ''
        self.W_points = 0
        self.B_points = 0

        self.gameover_check = False

        self.B_moves_list = [1]
        self.W_moves_list = [2]

        self.tiles_flipped = []
        
        self.winner = ''
        
    def _check_index(self, row: int, col: int)-> bool:
        '''
            checks if index for 2d list is valid (not negative or over
            the dimensions
        '''
        if row < 0 or row >= len(self.board):
            return True
        
        if col < 0 or col >= len(self.board[0]):
            return True
        
        return False

    def _valid_moves_list_turns_to_zero(self)-> None:
        '''
            turns the list of valid points to an empty list
        '''
        self.valid_moves_list = []
        self.tiles_flipped = []
        
    def print_board(self) -> None:
        '''
            prints the board with the points for each player and
            whose turn it is
        '''

        self.check_points()
        print('B: {}  W: {}'.format(self.B_points, self.W_points))
       
        
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                print(self.board[x][y], end =' ')
            print()
        if self.gameover_check:
            self.check_winner()
            print('WINNER: {}'.format(self.winner))

        else:
            print('TURN: {}'.format(self.player))


    def check_valid_moves(self) -> bool:
        '''
        if there are no valid moves for a player, it returns True.
        if there are valid moves, returns False
        '''
        if len(self.valid_moves_list) == 0:
            return True
        else:
            return False

            
    def check_for_moves(self) -> None:
        '''
            checks for valid moves for every possible space and,
            if the space/move is valid, it is stored in valid_moves_list
        '''
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):

                if self.board[row][col] == '.':

                    if self._check_upper_right(row, col):
                        self.valid_moves_list.append([row,col])
                        
                    if self._check_right(row, col):
                        self.valid_moves_list.append([row,col])
                       
                    if self._check_lower_right(row, col):
                        self.valid_moves_list.append([row,col])


                    if self.check_lower(row, col):
                        self.valid_moves_list.append([row,col])
                        
                    if self._check_upper(row, col):
                        self.valid_moves_list.append([row,col])


                    if self._check_upper_left(row, col):
                        self.valid_moves_list.append([row,col])
                        
                    if self._check_left(row, col):
                        self.valid_moves_list.append([row,col])
                        
                    if self._check_lower_left(row, col):
                        self.valid_moves_list.append([row,col])
                        
        if self.player == PLAYER_B:
            self.B_moves_list = self.valid_moves_list
        elif self.player == PLAYER_W: 
            self.W_moves_list = self.valid_moves_list
            

            
    def check_points(self) -> list:
        '''
            counts up all the points for each player
        '''
        self.W_points = 0
        self.B_points = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == PLAYER_B:
                    self.B_points +=1
                elif self.board[row][col] == PLAYER_W:
                    self.W_points +=1
        return [self.B_points, self.W_points]

    def check_winner(self)-> None:
        '''
            checks to see if there is winner, depending on the game mode
        '''
        if self.W_points == self.B_points:
            self.winner = 'NONE'
            
        # more wins
        if self.gamemode == '>':
        
            if self.W_points > self.B_points:
                self.winner = PLAYER_W
                
            elif self.W_points < self.B_points:
                self.winner = PLAYER_B
        # fewest wins
        if self.gamemode == '<':
        
            if self.W_points < self.B_points:
                self.winner = PLAYER_W
                
            elif self.W_points > self.B_points:
                self.winner = PLAYER_B




    
    def check_if_gameover(self)-> None:
        '''
            checks if the game is over by checking if there are no possible
            moves left for both players or if all the spaces are down
        '''
        temp_player = self.player
        self.player = PLAYER_B
        self.valid_moves_list = []
        self.check_for_moves()
        self.valid_moves_list = []

        self.player = PLAYER_W
        self.check_for_moves()
        self.valid_moves_list = []

        self.player = temp_player
        
        if len(self.B_moves_list) == 0 and len(self.W_moves_list) == 0:
            self.gameover_check = True
            raise GameOverError()

        



#
#check spaces/flips functions
#


#right

    def _check_upper_right(self, row: int, col: int) -> bool:
        '''
            checks the upper left of a chosen space
        '''
        if self._check_index( row - 1, col + 1):
            return False
        
        if self.board[row-1][col+1] == '.':
            return False

        if self.board[row-1][col+1] == self.player:
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:

                return False
            else:
                return True
            
        elif self.board[row-1][col+1] != self.player:
            if self._check_upper_right(row-1, col+1):
    
                return True


    def _check_right(self, row: int, col: int) -> bool:
        '''
           checks the right of a chosen space
        '''
        if self._check_index(row,col+1):
            return False

        if self.board[row][col+1] == '.':
            return False
                        
            
        if self.board[row][col+1] == self.player:
            
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
   
                return False
            else:
                return True
            
        elif self.board[row][col+1] != self.player:
            
            
            if self._check_right(row, col+1):

                return True

            
    def _check_lower_right(self, row: int, col: int) -> bool:
        '''
            checks the lower right of a chosen space
        '''
        if self._check_index(row + 1,col +1):
            return False
        
        if self.board[row+1][col+1] == '.':
            return False
        
        if self.board[row+1][col+1] == self.player:
            
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
  
                return False
            else:
                return True
            
        elif self.board[row+1][col+1] != self.player:
            
            
            if self._check_lower_right(row+1, col+1):
               
                return True

#center
            
    def _check_upper(self, row: int, col: int) -> bool:
        '''
            checks above a chosen space
        '''
    
        if self._check_index(row - 1, col):

            return False
        
        if self.board[row-1][col] == '.':
            return False
        
        if self.board[row-1][col] == self.player:
                
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
               
                return False
            else:
               
                return True
                
        elif self.board[row-1][col] != self.player:


            if self._check_upper(row-1, col):
                
                return True   


    def check_lower(self, row: int, col: int) -> bool:
        '''
            checks below a chosen space
        '''
        if self._check_index(row+1 ,col):
            return False
        
        if self.board[row+1][col] == '.':
            return False

        if self.board[row+1][col] == self.player:
                
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
 
                return False
            else:
     
                return True
                
        elif self.board[row+1][col] != self.player:


            if self.check_lower(row+1, col):
                
                return True   

# left

    def _check_upper_left(self, row: int, col: int) -> bool:
        '''
           checks the upper left of a chosen space
        '''
        if self._check_index(row - 1,col - 1):
            return False
        
        if self.board[row-1][col-1] == '.':
            return False

        if self.board[row-1][col-1] == self.player:
                
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
                
                return False
            else:
                
                return True
                
        elif self.board[row-1][col-1] != self.player:


            if self._check_upper_left(row-1, col-1):
        
                return True

            

    def _check_left(self, row: int, col: int) -> bool:
        '''
            checks the left of a chosen space
        '''
        if self._check_index(row,col - 1):
            return False
        
        if self.board[row][col-1] == '.':
            return False

        if self.board[row][col-1] == self.player:
                
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
                
                return False
            else:
                
                return True
                
        elif self.board[row][col-1] != self.player:

            if self._check_left(row, col-1):
              
                return True


    def _check_lower_left(self, row: int, col: int) -> bool:
        '''
        checks the lower left of a chosen space
        '''
        if self._check_index(row+1 ,col - 1):
            return False
        
        if self.board[row+1][col-1] == '.':
            return False

        if self.board[row+1][col-1] == self.player:
                
            if self.board[row][col] == '.' or\
               self.board[row][col] == self.player:
               
                return False
            else:
                
                return True
                
        elif self.board[row+1][col-1] != self.player:


            if self._check_lower_left(row+1, col-1):
                
                return True
            


#
#move/flip spaces functions
#





#
#left column
#
    def _move_upper_left(self, row: int, col:int) -> list:
        '''
            checks and makes the move for the spaces to the upper left
            of the space (row and col)
        '''
        if self._check_index(row - 1,col - 1):
            return self.board
        
        if self.board[row-1][col-1] == '.':
            return self.board
        

        if self.board[row-1][col-1] != self.player:
            self._move_upper_left(row-1, col-1)
            
            if self.board[row-1][col-1] == self.player:
                self.board[row][col] = self.player
                self.tiles_flipped.append([row, col])

            
        elif self.board[row-1][col-1] == self.player:

            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board


    def _move_left(self, row:int, col:int) ->list:
        '''
            checks and makes the move for the spaces to the left
            of the space (row and col)
        '''
        if self._check_index(row,col - 1):
            return self.board
        
        if self.board[row][col-1] == '.':
            return self.board
        
        if self.board[row][col-1] != self.player:
            self._move_left(row, col-1)
            
            if self.board[row][col-1] == self.player:
                self.board[row][col] = self.player
                self.tiles_flipped.append([row, col])

        elif self.board[row][col-1] == self.player:
            
            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])
            

        return self.board

    def _move_lower_left(self, row:int, col:int) -> list:
        '''
            checks and makes the move for the spaces to the lower left
            of the space (row and col)
        '''
        if self._check_index(row+1 ,col - 1):
            return self.board
        
        if self.board[row+1][col-1] == '.':
            return self.board
        
        if self.board[row+1][col-1] != self.player:
            self._move_lower_left(row+1, col-1)
            
            if self.board[row+1][col-1] == self.player:
                self.board[row][col] = self.player
                self.tiles_flipped.append([row, col])
            
        elif self.board[row+1][col-1] == self.player:
            
            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])
            

        return self.board


#
#center
#
    def _move_upper(self, row: int, col:int) -> list:
        '''
            checks and makes the move for the spaces below space (row and col)
        '''
        if self._check_index(row - 1, col):
            return self.board
        
        if self.board[row-1][col] == '.':
            return self.board
        
        if self.board[row-1][col] != self.player:
            self._move_upper( row-1, col)
            self.tiles_flipped.append([row, col])
            
            if self.board[row-1][col] == self.player:
                self.board[row][col] = self.player
            
        elif self.board[row-1][col] == self.player:

            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board


    def _move_lower(self, row:int, col:int) ->list:
        '''
            checks and makes the move for the spaces below the space (row and col)
        '''
        
        if self._check_index(row+1 ,col):
            return self.board
        
        if self.board[row+1][col] == '.':
            return self.board
        
        if self.board[row+1][col] != self.player:
            self._move_lower(row+1, col)
            self.tiles_flipped.append([row, col])
            
            if self.board[row+1][col] == self.player:
                self.board[row][col] = self.player
            
        elif self.board[row+1][col] == self.player:
            
            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board



#
#right column
#
    def _move_upper_right(self, row:int, col:int)-> list:
        '''
            checks and makes the move for the spaces to the upper right
            of the space (row and col)
        '''
        if self._check_index(row - 1, col + 1):
            return self.board
        
        if self.board[row-1][col+1] == '.':
            return self.board
        
        if self.board[row-1][col+1] != self.player:
            self._move_upper_right( row-1, col+1)
            
            if self.board[row-1][col+1] == self.player:
                self.board[row][col] = self.player
                self.tiles_flipped.append([row, col])
            
        elif self.board[row-1][col+1] == self.player:

            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board

    def _move_right(self, row: int, col:int) -> list:
        '''
            checks and makes the move for the spaces to the right
            of the space (row and col)
        '''
        if self._check_index( row,col+1):
            return self.board

        if self.board[row][col+1] == '.':
            return self.board
        
        if self.board[row][col+1] != self.player:
            self._move_right(row, col+1)
            
            if self.board[row][col+1] == self.player:
                self.board[row][col] = self.player
                self.tiles_flipped.append([row, col])

        elif self.board[row][col+1] == self.player:

            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board

    def _move_lower_right(self, row: int, col: int)-> list:
        '''
            checks and makes the move for the spaces to the lower right
            of the space (row and col)
        '''
        
        if self._check_index(row + 1,col +1):
            return self.board
        
        if self.board[row+1][col+1] == '.':
            return self.board
        
        if self.board[row+1][col+1] != self.player:
            self._move_lower_right(row+1, col+1)
            self.tiles_flipped.append([row, col])
            
            if self.board[row+1][col+1] == self.player:
                self.board[row][col] = self.player
            
        elif self.board[row+1][col+1] == self.player:

            if self.board[row][col] == '.':
                return self.board
            
            self.board[row][col] = self.player
            self.tiles_flipped.append([row, col])

        return self.board


    def _turn_made(self, turn:list)-> bool:
        '''
            makes the move on the space and turns over the pieces
        '''
        
        if self.board[turn[0]][turn[1]] == '.':
            
            
            self.board = self._move_upper_left( turn[0], turn[1])

            self.board = self._move_left(turn[0], turn[1])

            self.board = self._move_lower_left(turn[0], turn[1])



            self.board = self._move_lower( turn[0], turn[1])


            self.board = self._move_upper(turn[0], turn[1])


            self.board = self._move_upper_right(turn[0],turn[1])
            
            self.board = self._move_right( turn[0],turn[1])
            
            self.board = self._move_lower_right( turn[0], turn[1])

            return True

        else:
            
            return False


    def make_the_move(self, turn) -> bool:
        '''
            gets move from user until the move is valid
        '''
        if turn in self.valid_moves_list:
            
            if self._turn_made(turn):
                return True
                
            
        else:
            
            return False
        
        










        







