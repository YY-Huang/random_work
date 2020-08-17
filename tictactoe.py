


# 7 | 8 | 9
# --+---+--
# 4 | 5 | 6
# --+---+--
# 1 | 2 | 3



class Board():
    def __init__(self):
        self.state = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.num_pad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        self.number_of_moves = 0
    
    def print_avail_spots(self):
        '''
        Prints the available spots in a num pad fashion
        Unavailable spots are marked as '*'
        Available spots are marked with numbers 1-9 accordingly
        '''
        format = '\n';
        for index, row in enumerate(self.num_pad):
            if index != 0:
                format += '\n'
                format += '--+---+--'
                format += '\n'
            for index, value in enumerate(row):
                if (index != 2):
                    format += value + ' | ';
                else:
                    format += value
        return format
    
    def print(self):
        '''
        Prints the current state board of spots with players' markers if any
        '''
        format = '\n';
        for index, row in enumerate(self.state):
            if index != 0:
                format += '\n'
                format += '--+---+--'
                format += '\n'
            for index, value in enumerate(row):
                if (index != 2):
                    format += value + ' | ';
                else:
                    format += value
        return format
    
    def mark_spot(self, num_spot, marker):
        '''
        Marks a spot on the current state board.
        Takes out the available moves of a num pad state board with an '*'
        '''
        for row_index, row in enumerate(self.num_pad):
            for value_index, value in enumerate(row):

                if int(value) == num_spot:
                    self.state[row_index][value_index] = marker
                    self.num_pad[row_index][value_index] = '*'
                    return True
        return False

    def update_total_moves(self):
        '''
        Keeps track of the total moves
        Earliest winning total move is at 5
        '''
        self.number_number_of_moves += 1

    #Pseudo Code
    def suggest_spot(self, marker):
        '''
        Suggests a spot for the player to make based on the current
        reading of the available moves, and current board
        '''
        for row_index, row in enumerate(self.state):
            for value_index, value in enumerate(row):
                pass


game1 = Board();

def playGame():

    start_game = input('Do you want to play a game? Y or N \n')

    while (start_game == 'Y'):
        new_game = Board()
        print(f'Current game board is: {new_game.print()}')
        
        # Player1 picks a marker
        player1_marker = input('Pick X or O to start with \n')
        print(f'Player 1 marker is {player1_marker}')
        print(f'Current spots available: {new_game.print_avail_spots()}')

        # Player1 picks a spot
        player1_spot = int(input('Pick a spot \n'))
        player1_move = new_game.mark_spot(player1_spot, player1_marker)

        if player1_move is False:
            print('Pick new spots')
            print(f'Current spots available: {new_game.print_avail_spots()}')
        else:
            new_game.update_total_moves()
            print(f'Updated game with spot is {new_game.print()}')
            print(f'Current spots available: {new_game.print_avail_spots()}')
        break;
    
    print('Game has ended')

playGame()
