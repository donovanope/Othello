import tkinter
import point
import spots_model
import OthelloGame

class SpotsApplication:
    def __init__(self):
        
        self._state = spots_model.SpotsState()
        self.board = []
        self._root_window = tkinter.Tk()


        self.row_size = 4
        self.col_size = 6
        self.box_size = 0

        if self.row_size > self.col_size:
            self.box_size = (16/self.row_size)*40
        else:
            self.box_size = (16/self.col_size)*40        


        self.current_move = []
        self.piece_list = []


        self.B_score = 0
        self.W_score = 0

        self.B_points = tkinter.StringVar()
        self.W_points = tkinter.StringVar()
        self.turn_and_winner_var = tkinter.StringVar()
        


        self.B_points.set('')
        self.W_points.set('')
        self.turn_and_winner_var.set("")

  
        self.canvas = tkinter.Canvas(
            master = self._root_window, width = 640, \
            height = 640,
            background = '#006000')

        
        self.canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.canvas.bind('<Button-1>', self._on_canvas_clicked)
        
        self.canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self.winner_and_turn = tkinter.Label(
            master = self._root_window, textvariable = self.turn_and_winner_var)
        
        self.winner_and_turn.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            )


        self.padding = tkinter.Label(
            master = self._root_window)
        
        self.padding.grid(
            row = 2 , column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self.B_score = tkinter.Label(
            master = self._root_window, textvariable = self.B_points)
        
        self.B_score.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        
        self.W_score = tkinter.Label(
            master = self._root_window, textvariable = self.W_points)
        
        self.W_score.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E)

        self.whose_turn = False
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self.make_board()
        
 

        self._bob = tkinter.Button(master = self._root_window, text = 'X',\
                width = 20, height = 10, command = self.make_square)
        
        self._bob.grid(row = 0, column = 1, padx = 2, pady = 2,\
              sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        
    def make_board(self):
        '''
            makes the board for behind the scenes
        '''
        for x in range(self.row_size):
            self.board.append([])

            for y in range(self.col_size):
     
                self.board[x].append('.')

        
    def run(self):
        self._root_window.mainloop()
        
    def make_square(self):
        '''
            makes the board lines
        '''
        for x in range(self.row_size):
            for y in range(self.col_size):
                self.canvas.create_rectangle(y*self.box_size ,x*self.box_size,\
                                             (y+1)*self.box_size,(x+1)*self.box_size, outline="black")
        self.make_invisible_pieces()
        self._bob.destroy()

        
        self._start_game = tkinter.Button(master = self._root_window, text = 'Start',\
                width = 3, height = 1, command = self.start)
        
        self._start_game.grid(row = 1, column = 0, \
              sticky = tkinter.E + tkinter.S + tkinter.S )
        
        self.turn_and_winner_var.set('Instructions: Click in a square to place a tile. The first click places a\
 Black tile, \nsecond click places a white tile and the third tile clears the space')

    def start(self):
        '''
            after setup, starts the game
        '''
        self.canvas.bind('<Button-1>', self._make_move)

        self._start_game.destroy()
        self.game = OthelloGame.OthelloGame(self.board, '>')

        point_list = self.game.check_points()
        self.B_score = point_list[0]
        self.W_score = point_list[1]
        self.B_points.set('Black: {}'.format(self.B_score))
        self.W_points.set('White: {}'.format(self.W_score))

        self.play_game()

        
    def make_invisible_pieces(self):
        '''
            puts "invisible" pieces in the rectangles
        '''
        for x in range(self.row_size):
            self.piece_list.append([])

            for y in range(self.col_size):
     
                self.piece_list[x].append(
                self.canvas.create_oval(y*self.box_size+6,x*self.box_size+6,\
                    (y+1)*self.box_size-6,(x+1)*self.box_size-6,outline = '#006000', fill="#006000")
                )
            
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''
            when the board click, it takes in the coordinates
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        click_point = point.from_pixel(
            event.x, event.y, width, height)
        self.board_setup(event)

    def board_setup(self, event: tkinter.Event):
        '''
            depending where the user clicks, a piece will appear. This is for setting up the board
        '''
        for x in range(self.row_size):
            self.piece_list.append([])

            for y in range(self.col_size):
                if event.x > y*self.box_size and event.x < (y+1)*self.box_size\
                   and event.y > x*self.box_size and event.y < (x+1)*self.box_size:
                    if self.board[x][y] == '.':
                        self.canvas.itemconfig(self.piece_list[x][y], fill = 'black', outline = 'black')
                        self.board[x][y] = 'B'

                    elif self.board[x][y] == 'B':
                        self.canvas.itemconfig(self.piece_list[x][y], fill = 'white', outline = 'white')
                        self.board[x][y] = 'W'
                        
                    elif self.board[x][y] == 'W':
                        self.canvas.itemconfig(self.piece_list[x][y], fill = '#006000', outline = '#006000')
                        self.board[x][y] = '.'


    def _make_move(self, event):
        '''
            when player clicks a square, it will make a move
        '''
        for x in range(self.row_size):
            self.piece_list.append([])
            for y in range(self.col_size):
                if event.x > y*self.box_size and event.x < (y+1)*self.box_size\
                   and event.y > x*self.box_size and event.y < (x+1)*self.box_size:
                    if self.board[x][y] == '.':

                        self.current_move = [x,y]
                        self.play_game()
                        


    def putting_pieces_on_the_board(self):
        ''' 
            creates a board according to  self.board
        ''' 
        for x in range(self.row_size):
            for y in range(self.col_size):

                if self.board[x][y] == '.':
                    self.canvas.itemconfig(self.piece_list[x][y], fill = '#006000', outline = '#006000')

                elif self.board[x][y] == 'B':
                    self.canvas.itemconfig(self.piece_list[x][y], fill = 'black', outline = 'black')
                    
                elif self.board[x][y] == 'W':
                    self.canvas.itemconfig(self.piece_list[x][y], fill = 'white', outline = 'white')


                        
    def play_game(self):
        '''
            plays the game
        '''
        try:
            self.game.check_if_gameover()

            
            if self.whose_turn:
                self.game.player = 'B'
                self.game.check_for_moves()

                if self.game.check_valid_moves():
                    
                    self.whose_turn = False
                    
                else:
                    if self.game.make_the_move(self.current_move):
                        
                        self.game._valid_moves_list_turns_to_zero()

                        self.whose_turn = False
                
    
                        
            else:
                self.game.player = 'W'
                self.game.check_for_moves()

                if self.game.check_valid_moves():
                    self.whose_turn = True
                    
                else:
                    
                    if self.game.make_the_move(self.current_move):
                        self.game._valid_moves_list_turns_to_zero()

                        self.whose_turn = True
                        
            self.putting_pieces_on_the_board()

            point_list = self.game.check_points()
            self.B_score = point_list[0]
            self.W_score = point_list[1]
            self.B_points.set('Black: {}'.format(self.B_score))
            self.W_points.set('White: {}'.format(self.W_score))
            self.game.check_if_gameover()
            
            if len(self.game.B_moves_list) == 0:
                self.whose_turn = False

            elif len(self.game.W_moves_list) == 0:
                self.whose_turn = True

            self.check_whose_turn()

        except OthelloGame.GameOverError:
            
            self.get_winner()
      
    def check_whose_turn(self):
        '''
            checks whose turn it is
        '''
        if self.whose_turn:
            self.turn_and_winner_var.set("Black's Turn")
        else:
            self.turn_and_winner_var.set("White's Turn")
    def get_winner(self):
        '''
            checks for winner and puts it in the label
        '''
        self.game.check_winner()
        if self.game.winner == 'NONE':
            self.turn_and_winner_var.set("Tie")
        elif self.game.winner == 'W':
            self.turn_and_winner_var.set("White wins")
        elif self.game.winner == 'B':
            self.turn_and_winner_var.set("Black wins")


      
    def recreate_pieces(self, canvas_size):
        '''
            puts "invisible" pieces in the rectangles
        '''
        self.piece_list = []
        for x in range(self.row_size):
            self.piece_list.append([])

            for y in range(self.col_size):
                
                if self.board[x][y] == '.':
                    self.piece_list[x].append(
                        self.canvas.create_oval(y*canvas_size+6,x*canvas_size+6,\
                        (y+1)*canvas_size-6,(x+1)*canvas_size-6, fill = '#006000', outline = '#006000')
                        )
                    
                elif self.board[x][y] == 'B':
                    self.piece_list[x].append(
                        self.canvas.create_oval(y*canvas_size+6,x*canvas_size+6,\
                       (y+1)*self.box_size-6,(x+1)*self.box_size-6, fill = 'black', outline = 'black')
                    )
                    
                elif self.board[x][y] == 'W':
                    self.piece_list[x].append(
                        self.canvas.create_oval(y*canvas_size+6,x*canvas_size+6,\
                        (y+1)*canvas_size-6,(x+1)*canvas_size-6,outline = 'white', fill="white")
                )


    def recreate_square(self, canvas_size):
        '''
            makes the board lines
        '''
        for x in range(self.row_size):
            for y in range(self.col_size):
                self.canvas.create_rectangle(y*canvas_size ,x*canvas_size,\
                                             (y+1)*canvas_size,(x+1)*canvas_size, outline="black")

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._redraw_all()       


    def _redraw_all(self) -> None:
        pass





