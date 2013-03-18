'''
Andrew Tamura
March 17, 2013

Redux Connect 4 Challenge. 

'''
from random import randint

class MoveException(Exception):
    def __init__(self, column):
        self.column = column
    def __str__(self):
        return repr('Can\'t move into this column because it\'s full')


class Connect4():
    game_board = [  [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0], ]
    
    player_turn = 0
    turn_count = 0
    
    def __init__(self):
        self.player_turn = randint(1,2)
        print 'Player %s\'s turn!' % self.player_turn
        
        
    def print_board(self):
        '''
        Prints an ASCII representation of the board
        '''
        for row_i, row in enumerate(self.game_board):
            print '\n'
            for column_i, column in enumerate(row):
                print '[%s]' % (row[column_i]),
            
        
    def reset(self):
        '''
        Puts the game_board back to initial state
        '''
        for row in self.game_board:
            for column in row:
                row[column] = 0
    
    def change_player_turn(self):
        '''
        Modify the game state after a player has moved. 
        '''
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1
    
    def find_open_spot(self, column):
        '''
        For a given column, return the location of where a piece would
        drop down to. If the column is full, throw an exception.
        '''
        for row in range(6, -1, -1):
            if self.game_board[row][column] == 0:
                return (row, column)
        raise MoveException(column)
    
    def move(self, player, column):
        '''
        Check that the the correct player is moving. If the move is invalid, 
        e.g. the column is full, throw an exception. If the move is valid,
        return the location of the piece. 
        '''
        if not player == self.player_turn:
            return False
        else:
            piece_location = self.find_open_spot(column)
            row, column = piece_location
            self.game_board[row][column] = player
            self.turn_count+1
            self.change_player_turn()
            return piece_location
    
    def check_for_winner(self):
        '''
        Loop through all locations on the board and check if there is a
        winner. Returns either 1 or 2 if there is a winner. Returns False if
        there is no winner
        
        '''
        for row_index, row in enumerate(self.game_board):
            for column_index, column in enumerate(row):
                if not row[column_index] == 0:
                    if self.check_location(row_index, column_index):
                        return row[column_index]
        return False
            
    def check_location(self, row, column):
        '''
        Returns either 1 or 2 if this location is the starting of a 
        4 in a row. Returns False if there is no winner.
        
        You can win in 8 different directions. N, S, E, W, NE, SE, SW, and NW. 
        '''
        player = self.game_board[row][column]
        if not player:
            return False
        
        if self.check_north(row, column):
            return player
        elif self.check_south(row, column):
            return player
        elif self.check_east(row, column):
            return player
        elif self.check_west(row, column):
            return player
        elif self.check_north_east(row, column):
            return player
        elif self.check_north_west(row, column):
            return player
        elif self.check_south_east(row, column):
            return player
        elif self.check_south_west(row, column):
            return player
        else:
            return false
                
                
    def check_north(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if (row-3) < 0:
            return False
        else:
            #check North
            piece_count = 0
            for row_check in range(row, row-4, -1):
                if self.game_board[row_check][column] == player:
                    piece_count += 1                    
            if piece_count == 4:
                return player
            else:
                return False
    
    def check_south(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if (row+3) > 7:
            return False
        else:
            piece_count = 0
            for row_check in range(row, row+4):
                if self.game_board[row_check][column] == player:
                    piece_count += 1

            if piece_count == 4:
                return player
            else:
                return False

                
    def check_east(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if (column+3) > 7:
            return False
        else:
            piece_count = 0
            for column_check in range(column, column+4):
                if self.game_board[row][column_check] == player:
                    piece_count += 1

            if piece_count == 4:
                return player
            else:
                return False

    def check_west(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if (column-3) < 0:
            return False
        else:
            piece_count = 0
            for column_check in range(column, column-4, -1):
                if self.game_board[row][column_check] == player:
                    piece_count += 1

            if piece_count == 4:
                return player
            else:
                return False

    def check_north_east(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if ((column+3) > 7) or ((row-3) < 0):
            return False
        else:
            piece_count = 0
            for column_check, row_check in zip(
                range(column, column+4), range(row, row-4, -1)):
                if self.game_board[row_check][column_check] == player:
                    piece_count += 1
                 
            if piece_count == 4:
                return player
            else:
                return False
   
    def check_north_west(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if ((column-3) < 0) or ((row-3) < 0):
            return False
        else:
            piece_count = 0
            for column_check, row_check in zip(
                range(column, column-4, -1), range(row, row-4, -1)):
                if self.game_board[row_check][column_check] == player:
                    piece_count += 1
            if piece_count == 4:
                return player
            else:
                return False
                 
    def check_south_east(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if ((column+3) > 7) or ((row+3) > 7):
            return False
        else:
            piece_count = 0
            for column_check, row_check in zip(
                range(column, column+4), range(row, row+4)):
                if self.game_board[row_check][column_check] == player:
                    piece_count += 1
            if piece_count == 4:
                return player
            else:
                return False

    def check_south_west(self, row, column):
        player = self.game_board[row][column]
        if not player:
            return False
        if ((column-3) < 0) or ((row+3) > 7):
            return False
        else:
            piece_count = 0
            for column_check, row_check in zip(
                range(column, column-4, -1), range(row, row+4)):
                if self.game_board[row_check][column_check] == player:
                    piece_count += 1

            if piece_count == 4:
                return player
            else:
                return False
                    