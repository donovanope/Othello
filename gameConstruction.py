# Donovan Lopez. 30284497
####

PLAYER_B = 'B'
PLAYER_W = 'W'

def game_version() -> None:
    '''
        prints out which game version: FULL or SIMPLE
    '''
    print('FULL')


        
def build_board(row: int, col:int) -> list:
    '''
        builds and returns the board for the game. Dimension based on row and col
    '''
    while True:
        board = []
        
        for number in range(row):
            pieces_in_row = str(input())
            pieces_in_row = pieces_in_row.split()
            board.append(pieces_in_row)
            
        if _check_for_valid_board(board, row,col):
            return board
        else:
            print('INVALID')


def _check_for_valid_board(board: list, row: int, col: int) -> bool:
    '''
        checks if a board is the right size and
        has valid pieces ("B", "W" or "."). Returns True if
        the board is valid, returns False otherwise.
    '''
    for x in board:
        if len(x) != col:
            return False
        for y in x:
            if y != '.' and y != PLAYER_B and y != PLAYER_W:                
                return False
    return True

    
      
    


def player_goes_first(first_move: str) -> str:
    '''
        decides which piece goes first
    '''
    while True:
        if first_move == PLAYER_B or first_move == PLAYER_W:
            return True
        else:
            return False

def choose_style(style: str) -> bool:
    '''
        chooses how the winner will be decided: winner decided by
        the most or least points
    '''
    if style == '<' or style == '>':
        return True
    else:
        return False


def input_dimension(dimension: str) -> int:
    '''
        gets row or column from user. input must be an integer between 4 to 16
    '''
    while True:
        try:
            dim = int(dimension)
            if dim % 2 == 0 and dim >= 4 and dim <= 16: 
                return True
            else:
                return False
        except ValueError:
            return False

def turn_list_to_int(moves: list) -> list:
    '''
        turns the list of moves from str to int
    '''
    moves[0] = int(moves[0])
    moves[1] = int(moves[1])

    moves[0]-=1
    moves[1]-=1
    
    return moves

def first_player(player:str)-> bool:
    '''
        chooses which player goes first
        if the first player is B, then it returns True. If W, return False
    '''
    if player == PLAYER_B:
        return True
    elif player == PLAYER_W:
        return False



    



