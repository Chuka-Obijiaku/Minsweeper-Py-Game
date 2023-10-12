"""
Implementation of command-line minesweeper by Chuka Obijiaku using Kylie Ying tutorial as a guide 
Kilye Ying tutorial: https://www.youtube.com/watch?v=8ext9G7xspg&t=10119s (1:27:16)

"""
import random
import re

class Board:
    #an object that stores all the data and computations needed for the game 
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        
        #make an array that makes up the board 
        self.board = self.make_board()
        
        self.dug = []
        #print(self.board) #just checking what the board looks like 
        #plant the bombs 
        #give values to spots neghboring a bomb that corresponds with the number of neighboring bombs 
     
    def make_board(self):
        #generate empty array to represent the board
        board1 = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        #plant the bombs on the board
        bombs_planted = 0 
        while bombs_planted < self.num_bombs:
            #find random x an y coordinates 
            bomb_x = random.randint(0, self.num_bombs-1)
            bomb_y = random.randint(0, self.num_bombs-1)
            if board1[bomb_y][bomb_x] == '*':
                #pass loop if location of bomb has a bomb already 
                continue
            
            board1[bomb_y][bomb_x] = '*'
            bombs_planted += 1
        #ad values to spaces the ar beside a bomb
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if board1[row][col] == '*':
                    continue
                board1[row][col] = self.check_close_bombs(row, col, board1)
            
        
        return board1
     
    def check_close_bombs(self, row, col, board):     
                
        #iterate the spaces around the tile and check if there are bombs. 
        #count the bombs
        close_bombs = 0
        for y in range((max(row-1, 0)), min(row+1, self.dim_size-1)+1):
            for x in range((max(col-1, 0)), min(col+1, self.dim_size-1)+1):
                if y == row and x == col:
                    continue
                if board[y][x] == '*':
                    close_bombs += 1
                                  
        return close_bombs 
    
    def dig(self, row, col):
        # add location to dug_square
        #return False if dig a bomb
        #return True if square is next to bomb(s)
        # if square is not touching a bomb 
        self.dug.append((row, col))
        
        if self.board[row][col] == '*':
            return False
        
        if self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1) +1):
                
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)        

        
        return True
    
    def __str__(self):
        printed_string = '      '
        visible_board = [None for _ in range(self.dim_size) for _ in range(self.dim_size)]
        #print col numbers
        for c in range(self.dim_size):
            printed_string += f'{c}   ' 
        printed_string += '\n'
        for row in range(self.dim_size):
            printed_string += f'{row}  |' # print the row numbers 
            for col in range(self.dim_size):
                
                printed_string += '| ' 
                if (row, col) in self.dug:
                    printed_string += f'{self.board[row][col]:<2}'
                else:
                    printed_string += '  '
                 
            printed_string += '\n'
            
        return printed_string 

def play():
    # make the board
    board = Board(10,10)
    safe = True
    while len(board.dug) < board.dim_size ** 2 - board.num_bombs: 
        print(board) 
        user_input = re.split(',(\\s)*', input("What space would you like to dig? input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row > board.dim_size or col < 0 or col > board.dim_size:
            print('Invalid loaction. Try again')
            continue
        safe = board.dig(row, col)
        if not safe:
            #dug a bomb
            break
    
    if safe:
        print('Congratulations!! you are the victor!')
        
        
    else:
        print('Sorry, game over')
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
        
    play_agian = input('Would you like to play again (y/n): ').lower()
    if play_agian == 'y':
        play()
    return
    
        
if __name__ == '__main__':                
    play()
      
   
        
