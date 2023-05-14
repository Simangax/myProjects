
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(1)
import stdio
import stdarray
import sys
import stddraw
import pygame
from picture import Picture
from color import Color
players = stdarray.create1D(2)
AIRPORTS = 10
INITIAL_BALANCE = 100.0
PLAYERS = 2
MAX_SUITCASE_VAL = 10
SUITCASES_PER_AIRPORT = 4
NUM_OBSTACLE_DISKS = 6
RED_DISK = 0
GREEN_DISK = 1
YELLOW_DISK = 2
CYAN_DISK = 3
BLACK_DISK = 4
MAGENTA_DISK = 5
OBSTACLE_DISK_STRINGS = ['RED', 'GREEN', 'YELLOW', 'CYAN', 'BLACK', 'MAGENTA']
WALL = '|'
CORN = '+'
LINE = '-'
ERR_TOO_FEW_ARGS = 'Too few command-line arguments were given.'
ERR_TOO_MANY_ARGS = 'Too many command-line arguments were given.'
ERR_UNIMPLEMENTED = 'This feature is not implemented for the current game mode!'
ERR_UNEXPECTED = 'Unexpected input!'
MSG_NO_NEW_GAME_TERMINATION = 'The game has ended.'
ERR_INVALID_TURN_MENU_OPTION = 'Invalid turn menu option!'
ERR_FLOAT_EXPECTED = 'A floating point number was expected!'
ERR_NOT_YES_OR_NO = 'Expected "Y" or "N" as input!'
ERR_INVALID_AIRPORT = 'Invalid airport!'
ERR_FLYING_TO_SAME_AIRPORT = 'You are already at this airport!'
ERR_FLYING_TO_OPPONENT_AIRPORT = 'You cannot fly to an airport that is occupied by your opponent!'
ERR_FLIPPING_COLLECTED_SUITCASE = 'This suitcase cannot be flipped as it has already been collected.'
ERR_FLIP_RESTRICTED = 'You are not allowed to flip this suitcase. You are trying to flip a suitcase that you have already flipped during your visit.'
ERR_INVALID_SUITCASE_POSITION = 'Invalid suitcase position!'
ERR_INVALID_SUITCASE_NUMBER = 'Invalid suitcase number! The number behind a suitcase must be a value between 1 and 10.'
ERR_BALANCE = 'Insufficient funds!'
ERR_CANT_STAY = 'You cannot stay at this airport! You cannot flip any suitcases here.'
ERR_CANT_ASK = 'You have already asked your opponent if they want to move this turn!'
ERR_EMPTY_STD_INPUT = 'Standard input is empty!'
MSG_USER_TERMINATION = 'Player terminated the game.'
ERR_NO_DISKS = 'You have no obstacle disks that may be played at the moment!'
ERR_INVALID_DISK = 'Invalid obstacle disk option given as input!'
ERR_ALREADY_PLAYED_DISK = 'You have already played this obstacle disk!'
ERR_CANT_PLAY_RED_DISK = 'You can only play the red obstacle disk directly after your opponent has refused your request for them to leave their current airport'
ERR_CANT_PLAY_CYAN_DISK = 'You cannot play the cyan disk until your opponent has moved from their first airport!'
ERR_CANT_PLAY_MAGENTA_DISK = 'You can only play the magenta disk if your opponent has collected more suitcases that you have.'
ERR_CANT_PLAY_BLACK_DISK = 'You cannot play the black disk when you are not allowed to flip any of the suitcases at your current airport!'
ERR_MUST_PLAY_HELPFUL_DISK = 'You must play a helpful disk, given your current predicament!'
MSG_INVALID_GAME_MODE = 'Invalid game mode argument. Using the default value for game_mode instead.'
MSG_INVALID_GRAPHICS_MODE = 'Invalid graphics mode indicator argument. Using the default value for graphics_mode instead.'
ASK_AIRPORT_DESTINATION = 'Player %d, please select the airport you would like to go to. (A-J)\n'
SAY_INITIAL_AIRPORT = 'Player %d has selected Airport %s as their first airport.\n\n'
SAY_FLIGHT_INFO = 'Player %d has flown from Airport %s to Airport %s at a cost of R%.2f.\n\n'
SAY_REQUEST_LEAVE = 'Player %d has asked Player %d if they would like to leave the airport.\n\n'
ASK_WANT_TO_LEAVE = 'Player %d, would you like to leave the airport? (Y/N)\n'
SAY_PLAYER_LEFT = 'Player %d has left their airport upon Player %d\'s request.\n'
SAY_REFUSED_TO_LEAVE = 'Player %d has refused Player %d\'s request to leave their airport.\n\n'
SAY_PLAY_OBSTACLE_DISK = 'Player %d has played their %s obstacle disk.\n\n'
SAY_RED_DISK = 'Player %d, you are forced to move from your current airport, but Player %d will pay for your flight.\n'
SAY_RED_DISK_DEDUCTION = 'Player %d, you have paid for Player %d\'s flight at a cost of R%.2f. Your new balance is R%.2f\n\n'
ASK_WHICH_OBSTACLE_DISK = 'Player %d, which obstacle disk would you like to use? (R/G/Y/C/B/M)\n'
SAY_GREEN_DISK = 'The positions of the four suitcases have been shuffled, at each airport.\n\n'
ASK_YELLOW_DISK_AIRPORT = 'Player %d, please select the airport whose suitcases will be swapped with the suitcases at your current airport. (A-J)\n'
SAY_YELLOW_DISK_AIRPORT = 'Player %d has swapped the suitcases of Airport %s with that of Airport %s.\n\n'
SAY_CYAN_DISK = 'Player %d is forced to pay R%.2f in taxes. Their new balance is R%.2f.\n\n'
SAY_BLACK_DISK = 'The black disk has revealed the following suitcases at Airport %s.\n\n'
SAY_MAGENTA_DISK = 'The magenta disk has added R%.2f to the balance of Player %d. Their new balance is R%.2f.\n\n'
OPT_HEADER = 'Player %d, you can do the following:\n'
OPT_ASK_OPPONENT_TO_MOVE = '\t(A)sk your opponent to leave their airport.'
OPT_STAY_AT_CURRENT_AIRPORT = '\t(S)tay at your current airport.'
OPT_FLY_TO_ANOTHER_AIRPORT = '\t(F)ly to a different airport.'
OPT_USE_OBSTACLE_DISK = '\t(U)se one of your available obstacle disks.\n'
ASK_SUITCASE_POSITION = 'Player %d, please enter the position of the suitcase you would like to flip. (1-4)\n'
SAY_SUITCASE_FLIPPED = 'Player %d has flipped the suitcase at position %d of airport %s to reveal:\n\n'
SAY_COLLECTED = 'Player %d has collected the suitcase at position %d of airport %s.\n\n'
SAY_NOT_COLLECTED = 'Player %d could not collect the suitcase at position %d of airport %s.\n\n'
LOSS_NO_MORE_MOVES = 'Player %d cannot make any more moves!\n'
LOSS_BANKRUPT = 'Player %d has been bankrupted!\n'
WIN_COLLECTED_ALL_SUITCASES = 'Player %d has collected all of their suitcases!\n'
WIN_MESSAGE = 'Player %d has won the game!\n\n'
ASK_NEW_GAME = 'Do you want to start a new game? (Y/N)'
SAY_YES_NEW_GAME = 'A new game is starting!\n'

CARD_WIDTH = 100
CARD_HEIGHT = 150
OBSTACLE_DISK_RADIUS = 30
CELL_RADIUS = 20
FONT_SIZE = 20
HEADER_HEIGHT = 40
GRID_HEIGHT = 200
SHOW_DELTA = 100
LONG_PAUSE = 1000

DEFAULT_PEN_RADIUS = 2.0
MAX_OUTPUT_LINES = 10
X_MAX = 1000 
Y_MAX = 740 
OUTPUT_AREA_HEIGHT = 500 
OUTPUT_AREA_WIDTH = 500 
GUI_OUTPUT_FONT = pygame.font.SysFont('Consolas', 15)
MAP_BACKGROUND_IMG_PATH = os.path.join("./assets_gui/", "map_background.jpg")
P1_PLANE_IMG_PATH = os.path.join("./assets_gui/", "p1.png")
P2_PLANE_IMG_PATH = os.path.join("./assets_gui/", "p2.png")
S1_SUITCASE_IMG_PATH = os.path.join("./assets_gui/", "s1.png")
S2_SUITCASE_IMG_PATH = os.path.join("./assets_gui/", "s2.png")
S3_SUITCASE_IMG_PATH = os.path.join("./assets_gui/", "s3.png")


map_image = None
p1_image = None
p2_image = None
s1_image = None
s2_image = None
s3_image = None

game_over = False

PLACE_HOLDER_BOOLEAN = False 
airport_layout = stdarray.create2D(0,0)
co_ords = stdarray.create2D(10,2)
matrix = 0
wallet = [INITIAL_BALANCE, INITIAL_BALANCE]
round_number = 1
number = 1
cost_matrix = []
curr_player = 0 
curr_player = 1
     
player_wallet = wallet[0]
player_wallet = wallet[1]





def end_game():
    global game_over
    game_over = True

def get_opponent(player):
    return 1 - player

def check_stdio_empty():
    if stdio.isEmpty():
        termination(ERR_EMPTY_STD_INPUT)

def int_to_char(index):
    return chr(index + 65)

def char_to_int(ch):
    return ord(str(ch).upper()) - 65

def read_command_line_args():

    game_mode = 0 
    graphics_mode = 0 
    if len(sys.argv) < 0:
        termination(ERR_TOO_FEW_ARGS)
    if len(sys.argv) > 3:
        termination(ERR_TOO_MANY_ARGS)
    if game_mode != 0 or game_mode != 1 or game_mode != 2:
        stdio.writeln(MSG_INVALID_GAME_MODE)
    if graphics_mode != 0 or graphics_mode != 1:
        stdio.writeln(MSG_INVALID_GRAPHICS_MODE) 
    if game_mode != 0 or graphics_mode != 0:  
        termination(ERR_UNIMPLEMENTED)
    return [game_mode, graphics_mode]

def generate_cost_matrix(airport_coordinates_matrix):
    
    max_c = float('-inf')
    min_c = float('+inf')
    new_cost_matrix = stdarray.create2D(AIRPORTS, AIRPORTS, 0.0)
    for a1 in range(AIRPORTS):
        new_cost_matrix[a1][a1] = 0.0
        for a2 in range(a1 + 1, AIRPORTS):
            new_cost_matrix[a1][a2] = (airport_coordinates_matrix[a1][0] - airport_coordinates_matrix[a2][0])**2
            new_cost_matrix[a1][a2] += (airport_coordinates_matrix[a1][1] - airport_coordinates_matrix[a2][1])**2
            new_cost_matrix[a1][a2] = new_cost_matrix[a1][a2]**0.5
            new_cost_matrix[a2][a1] = new_cost_matrix[a1][a2]
            if new_cost_matrix[a2][a1] < min_c:
                min_c = new_cost_matrix[a2][a1]
            if new_cost_matrix[a2][a1] > max_c:
                max_c = new_cost_matrix[a2][a1]
    # Scale the cost matrix values to be between 0 and upper_limit.
    upper_limit = 20.0
    for a1 in range(AIRPORTS):
        for a2 in range(a1 + 1, AIRPORTS):
            new_cost_matrix[a1][a2] = upper_limit*((new_cost_matrix[a1][a2] - min_c) / (max_c - min_c))
            new_cost_matrix[a2][a1] = new_cost_matrix[a1][a2]
    # Return the cost matrix, as calculated above.
    return new_cost_matrix

def calculate_magenta_disk_bonus(player_last_suitcase, opponent_last_suitcase):
    return (9 - player_last_suitcase) * max(0, opponent_last_suitcase - player_last_suitcase)

def show_options(player, can_ask_opponent_to_leave, can_play_obstacle, game_mode):
    if game_mode == 2:
        # Furthermore, when the game_mode variable is set to 2, indicating AI game-play, then the (AI) players cannot use obstacle disks.
        can_play_obstacle = False
        can_ask_opponent_to_leave = False
    can_fly = PLACE_HOLDER_BOOLEAN # TODO: Replace the placeholder boolean with your own code.
    can_stay = PLACE_HOLDER_BOOLEAN # TODO: Replace the placeholder boolean with your own code.
    # The four Boolean variables above indicate whether the player can do the corresponding action.
    # For example, if the player can ask the opponent to leave their airport, then the can_ask_opponent_to_leave variable will be set to True.
    #               This may be false if the player has already asked the opponent to leave their airport during this round.
    # The can_fly variable indicates whether the player can fly to another airport.
    # The can_stay variable indicates whether the player can stay at their current airport.
    # The can_play_obstacle variable indicates whether the player can play an obstacle disk.
    # NOTE: the current player can only play the red obstacle disk immediately after their opponent has refused the current player's request to fly to another airport -- assuming the current player has not yet played their red disk.
    # For the first hand-in, only the red obstacle disk is implemented. A player can only play the red obstacle disk when they have already asked the opponent to leave their airport, and the opponent has refused to leave. This implies that the red obstacle disk is only displayed sometimes!
    # When the show_options function is called after the opponent has refused to fly to a different airport, the current player will be able to select the 'U' option, but it will only display the red obstacle disk (assuming the current player has not played the red disk yet) -- no other disks should be displayed in this case!
    # If the current player has already used their red obstacle disk, the 'U' option should not be displayed after calling show_options after the opponent has refused the current player's request.
    # If the current player did not ask their opponent to leave their airport, the 'U' option should only display the other obstacle disks (depending on the non-red disks' availabilities), even if the player has not used the red disk yet.
    # Since the other disks will only be implemented for the second hand-in, only the red disk should be displayed here (noting the aforementioned rules about when the red disk can be used).

    # TODO: Replace the following placeholder code with your own code.
    # Here, you want to check if the player has lost the game because they cannot make a move that would benefit their case.
    # If the player cannot make a move that would benefit their case, they lose.
    # You may want to use a combination of the boolean variables above, as well as the helpful_disk_available() function.
    if PLACE_HOLDER_BOOLEAN:
        return

    # DO NOT MODIFY THE FOLLOWING PRINT MESSAGES. These are the options to present to the player.
    # The options are only printed if the player can make that move.
    # For example, if the player cannot fly to another airport, then the option to fly is not printed.
    # If you feel the need to change the logic of the if statements, you may do so.
    # Just be sure that the options are only printed if the player can make that move and that the options are printed in the same order as they are listed below.
    # To reiterate, you may change the logic of the if statements, but you may not change the print messages.
    stdio.writef(OPT_HEADER, player + 1)
    if can_ask_opponent_to_leave:
        stdio.writeln(OPT_ASK_OPPONENT_TO_MOVE)
    if can_stay:
        stdio.writeln(OPT_STAY_AT_CURRENT_AIRPORT)
    if can_fly:
        stdio.writeln(OPT_FLY_TO_ANOTHER_AIRPORT)
    if can_play_obstacle:
        stdio.writeln(OPT_USE_OBSTACLE_DISK)
        # TODO: Modify the following code by implementing the functionality of the red obstacle. For the first hand-in, the non-red-disk entries of the `print_obstacle_disks` array can be set to False at all times, since the other obstacle disks will only be required for the second hand-in.
        can_play_red = PLACE_HOLDER_BOOLEAN # TODO: replace the `PLACE_HOLDER_BOOLEAN` variable appropriately
        can_play_disk_array = [can_play_red, False, False, False, False, False] # TODO: You will need to add similar functionality for the other non-red disks during your implementation of the second hand-in.
        print_obstacle_disks(can_play_disk_array)
        # You will need to modify the function arguments in the previous line appropriately.
        # The majority of the `print_obstacle_disks` function is mainly applicable to the second hand-in, since the red disk is the only obstacle disk implemented for the first hand-in. Ensure that you understand when you need to display the red obstacle using `print_obstacle_disks` disk, however!
    stdio.writeln() # Make sure you do not remove this line. It is used to separate the options above from the output that follows. This is important for the marking of your program.

    # TODO: Read input from standard input, appropriately.
    # We expect the following possible inputs:
    #   - "`A`" for Ask
    #   - "`S`" for Stay
    #   - "`F`" for Fly
    #   - "`U`" for Use an obstacle disk
    # Then decide what to do next, based on the input.


 
def runner():

    game_mode, graphics_mode = read_command_line_args()
    print_command_line_args(0,0)
    global cost_matrix

    cost_matrix = stdarray.create2D(0,0,0.0)

    airport_layout = stdarray.create2D(0,0)
    co_ords = stdarray.create2D(10,2)
    for line in range(10):
        content = stdio.readLine()
        airport_layout.append(content.split(' '))
    
    for x in range(10):
        for y in range(2):
            co_ords[x][y]= float(airport_layout[x][y])
    unrevealed_suitcases = stdarray.create1D(0)

    for i in range(10):
        for j in range(2,6):
            unrevealed_suitcases.append(airport_layout[i][j])
    cost_matrix =  generate_cost_matrix(co_ords)
   
    print_cost_matrix(generate_cost_matrix(co_ords), curr_player, player_wallet, round_number)

    draw_airport_map(p1_airport_id, p2_airport_id, airport_coordinate_matrix, flight_cost_matrix, cur_player)
           

    

    game()

def game():
        players = [1, 2]
        select_airport = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        p1_airport_id = None 
        p2_airport_id = None
        p1_last_suitecase = None
        p2_last_suitecase = None
        AIRPORTS = len(select_airport)
        PLAYERS = len(players)
        suitcase_numbers_array = stdarray.create1D(10)
        allowed_to_flip_array = stdarray.create1D(4)
        collected_array = []
        curr_player = 0
        generic_grid_print(header_text, p1_position, p2_position, seperate_players, use_letters)
        

    
        available_airports = []
        number = 1
        round_number = 1
        for round_number in range(1, 11):
            curr_player = 0
            if round_number % 2 != 0:
            # Player 1's turn
                stdio.writef(ASK_AIRPORT_DESTINATION, players[0])
                select_position = stdio.readString().upper()  # convert to uppercase to avoid issues
                while select_position not in select_airport:
                # Keep asking for airport until valid one is entered
                    stdio.writef(ERR_INVALID_AIRPORT, select_position)
                    stdio.writef(ASK_AIRPORT_DESTINATION, players[0])
                    select_position = stdio.readString().upper()
            
                p1_airport_id = select_position
                stdio.writef(SAY_INITIAL_AIRPORT, players[0], p1_airport_id)
                available_airports.append(p1_airport_id)  # append selected airport to available airports
                print_airport_grid(p1_airport_id, p2_airport_id)  # print grid with selected airports

                print_airport_suitcases(suitcase_numbers_array, collected_array, allowed_to_flip_array)
                print_suitcase_grid(p1_last_suitecase, p2_last_suitecase)
                stdio.writef(ASK_SUITCASE_POSITION, players[0])
                p1_last_suitecase = stdio.readInt()  # read input as int
                stdio.writef(SAY_SUITCASE_FLIPPED, players[0], p1_last_suitecase, p1_airport_id)

                if p1_last_suitecase in allowed_to_flip_array:
                    collected_array.append(p1_last_suitecase)  # add suitcase number to collected_array
                    stdio.writef(SAY_COLLECTED, players[0], p1_last_suitecase, p1_airport_id)
                    print_suitcase_grid(p1_last_suitecase, p2_last_suitecase)
                    suitcase_numbers_array.remove(p1_last_suitecase)  # remove suitcase number from array
                    allowed_to_flip_array.remove(p1_last_suitecase)  # remove suitcase number from allowed_to_flip_array
        
        round_number = 1
        for round_number in range(1, 11,2):
              
            if round_number%2 == 0:
                curr_player = 1
            # Player 2's turn
                stdio.writef(ASK_AIRPORT_DESTINATION, players[1])
                select_position = stdio.readString().upper()
                while select_position not in select_airport:
                    stdio.writef(ERR_INVALID_AIRPORT, select_position)
                    stdio.writef(ASK_AIRPORT_DESTINATION, players[1])
                    select_position = stdio.readString().upper()
            
                p2_airport_id = select_position
                stdio.writef(SAY_INITIAL_AIRPORT, players[1], p2_airport_id)
                available_airports.append(p2_airport_id)
                print_airport_grid(p1_airport_id, p2_airport_id)

                print_airport_suitcases(suitcase_numbers_array, collected_array, allowed_to_flip_array)
                print_suitcase_grid(p1_last_suitecase, p2_last_suitecase)
                stdio.writef(ASK_SUITCASE_POSITION, players[1])
                p1_last_suitecase = stdio.readInt()  # read input as int
                stdio.writef(SAY_SUITCASE_FLIPPED, players[1], p1_last_suitecase, p1_airport_id)

                if p1_last_suitecase in allowed_to_flip_array:
                    collected_array.append(p1_last_suitecase)  # add suitcase number to collected_array
                    stdio.writef(SAY_COLLECTED, players[1], p1_last_suitecase, p1_airport_id)
                    print_suitcase_grid(p1_last_suitecase, p2_last_suitecase)
                    suitcase_numbers_array.remove(p1_last_suitecase)  # remove suitcase number from array
                    allowed_to_flip_array.remove(p1_last_suitecase)  # remove suitcase number from allowed_to_flip_array
            round_number+=1


def termination(msg):
    stdio.writef('Termination: %s', str(msg))
    sys.exit(0)

def print_obstacle_disks(can_play_disk_array):
 
    if game_over: return
    middle = ' x%11sx '
    outer1 = '     x x x     '
    outer2 = '  x         x  '
    colour_characters_array = ['R', 'G', 'Y', 'C', 'B', 'M']
    for row in range(7):
        for disk in range(len(colour_characters_array)):
            if disk == 0: stdio.write('\t')
            if not can_play_disk_array[disk]: continue
            if row == 0 or row == 6:
                stdio.write(outer1)
            elif row == 1 or row == 5:
                stdio.write(outer2)
            elif row == 2 or row == 4:
                stdio.writef(middle, ' ')
            else:
                stdio.writef(middle, colour_characters_array[disk].center(10))
        stdio.writeln()

def black_disk_print(suitcase_numbers_array, collected_array):

    if game_over: return
    space = ' '*5
    card_edge = '%5s' + CORN + LINE * 7 + CORN
    inside = space + WALL + '%-7s' + WALL
    empty = ' '*7
    uncollected = [empty, empty, ' ' * 3, empty, empty]
    taken1 = 'x     x'
    taken2 = ' x   x '
    collected = [taken1, taken2, ' ' * 3, taken2, taken1]

    for card_pos in range(SUITCASES_PER_AIRPORT):
        stdio.writef(card_edge, space)
    stdio.writeln()

    for i in range(5):
        for card_pos in range(SUITCASES_PER_AIRPORT):
            val = str(suitcase_numbers_array[card_pos]) if i == 2 else ''
            if collected_array[card_pos]:
                stdio.writef(inside, collected[i] + val)
            else:
                stdio.writef(inside, uncollected[i] + val)
        stdio.writeln()

    for card_pos in range(SUITCASES_PER_AIRPORT):
        stdio.writef(card_edge, str(card_pos+1) + '. ')
    stdio.writeln('\n')

def print_single_suitcase_number(number):
 
    if game_over: return
    card_edge = CORN + LINE * 7 + CORN
    middle = WALL + '%7s' + WALL + '\n'
    blank = ' '*7
    card_number = str(number).center(7)
    stdio.writeln(card_edge)
    for i in range(5):
        stdio.writef(middle, card_number if i == 2 else blank)
    stdio.writeln(card_edge + '\n')

def print_airport_grid(p1_airport_id, p2_airport_id):
   
    if game_over: return
    card_edge = CORN + LINE * 7 + CORN
    middle = WALL + '%7s' + WALL + '\n'
    blank = ' '*7
    card_number = str(number).center(7)
    stdio.writeln(card_edge)
    for i in range(5):
        stdio.writef(middle, card_number if i == 2 else blank)
    stdio.writeln(card_edge + '\n')

def print_airport_suitcases(suitcase_numbers_array, collected_array, allowed_to_flip_array):
 
    if game_over: return
    space = ' '*5
    card_edge = '%5s' + CORN + LINE * 7 + CORN
    inside = space + WALL + '%-7s' + WALL
    empty = ' '*7
    unflipped = ['   _   ', ' xX Xx ', ' x   x ', ' xXXXx ', empty]
    taken1 = 'x     x'
    taken2 = ' x   x '
    collected = [taken1, taken2, ' ' * 3, taken2, taken1]
    stdio.writeln('Suitcases at the current airport:')

    for card_pos in range(SUITCASES_PER_AIRPORT):
        if allowed_to_flip_array[card_pos]:
            stdio.writef(card_edge, space)
    stdio.writeln()

    for i in range(5):
        for card_pos in range(SUITCASES_PER_AIRPORT):
            if not allowed_to_flip_array[card_pos]:
                continue
            if collected_array[card_pos]:
                val = str(suitcase_numbers_array[card_pos]) if i == 2 else ''
                stdio.writef(inside, collected[i] + val)
            else:
                stdio.writef(inside, unflipped[i])
        stdio.writeln()

    for card_pos in range(SUITCASES_PER_AIRPORT):
        if allowed_to_flip_array[card_pos]:
            stdio.writef(card_edge, str(card_pos+1) + '. ')
    stdio.writeln('\n')

def write_center(text, length=5):
    stdio.writef(' %s |', text.center(length))

def print_cost_matrix(flight_cost_matrix, cur_player, cur_player_wallet, cur_round_number):

    if game_over: return
    header_line = WALL + ' %-28s%s%28s ' + WALL
    stdio.writeln(CORN + LINE * (87) + CORN)
    round_info = f'Round {cur_round_number}'
    player_info = f'Player {cur_player + 1}'.center(29)
    wallet_info = f'Balance: R{float(cur_player_wallet):.2f}'
    stdio.writef(header_line, round_info, player_info, wallet_info)
    edge = '\n' + CORN + (LINE * 7 + CORN) * 11
    stdio.writeln(edge)
    stdio.writef('%s', WALL)
    write_center(' ', length=5)
    for col in range(AIRPORTS):
        write_center(int_to_char(col))
    stdio.writeln(edge)
    for row in range(AIRPORTS):
        stdio.writef('%s', WALL)
        write_center(int_to_char(row), length=5)
        for col in range(AIRPORTS):
            write_center(f'{float(flight_cost_matrix[row][col]):.2f}')
        stdio.writeln()
    stdio.writeln(edge[1:] + '\n')

def print_suitcase_grid(p1_last_suitecase, p2_last_suitecase):
 
    header = 'Player Suitcases'
    generic_grid_print(header, p1_last_suitecase, p2_last_suitecase, True, False)

def print_airport_grid(p1_airport_id, p2_airport_id):
 
    header = 'Airplane Locations'
    generic_grid_print(header, p1_airport_id, p2_airport_id, False, True)

def generic_grid_print(header_text, p1_position, p2_position, seperate_players, use_letters):
   
    if game_over: return
    p1 = 'P1'
    p2 = 'P2'
    player_indicator = ' %2s'+ ' '*5 + '%2s ' + WALL
    centre_indicator = ' '*5 + '%-2s' + ' '*4 + WALL
    seperator = CORN + (LINE * 11 + CORN) * 5
    stdio.writeln(CORN + LINE * (12 * 5 - 1) + CORN)
    stdio.writef('%s%s%s\n', WALL, header_text.center(len(seperator) - 2), WALL)
    for row in range(2):
        stdio.writef('%s\n', seperator)
        for i in range(5):
            stdio.write(WALL)
            for col in range(5):
                cell = row * 5 + col
                if i == 2:
                    stdio.writef(centre_indicator, int_to_char(cell) if use_letters else cell + 1)
                elif seperate_players and i == 0:
                    stdio.writef(player_indicator, p1 if cell+1 == p1_position else ' ', p2 if cell+1 == p2_position else ' ')
                elif seperate_players and i == 4:
                    stdio.writef(player_indicator, p2 if cell+1 == p2_position else ' ', p1 if cell+1 == p1_position else ' ')
                elif cell == p1_position and (i == 0 or i == 4):
                    stdio.writef(player_indicator, p1, p1)
                elif cell == p2_position and (i == 0 or i == 4):
                    stdio.writef(player_indicator, p2, p2)
                else:
                    stdio.writef(centre_indicator, ' ')
            stdio.write('\n')
    stdio.writef('%s\n\n', seperator)

def print_command_line_args(game_mode_val, graphics_mode_val):
    stdio.writef('Game mode: %d\nGraphics mode: %d\n\n', game_mode_val, graphics_mode_val)

def read_images():
   
    global map_image, p1_image, p2_image, s1_image, s2_image, s3_image
    if not os.path.exists(MAP_BACKGROUND_IMG_PATH):
        raise FileNotFoundError(f'Could not find the map image at {MAP_BACKGROUND_IMG_PATH}.')
    if not os.path.exists(P1_PLANE_IMG_PATH):
        raise FileNotFoundError(f'Could not find the player 1 image at {P1_PLANE_IMG_PATH}.')
    if not os.path.exists(P2_PLANE_IMG_PATH):
        raise FileNotFoundError(f'Could not find the player 2 image at {P2_PLANE_IMG_PATH}.')
    if not os.path.exists(S1_SUITCASE_IMG_PATH):
        raise FileNotFoundError(f'Could not find the suitcase image at {S1_SUITCASE_IMG_PATH}.')
    if not os.path.exists(S2_SUITCASE_IMG_PATH):
        raise FileNotFoundError(f'Could not find the suitcase image at {S2_SUITCASE_IMG_PATH}.')
    if not os.path.exists(S3_SUITCASE_IMG_PATH):
        raise FileNotFoundError(f'Could not find the suitcase image at {S3_SUITCASE_IMG_PATH}.')
    map_image = Picture(MAP_BACKGROUND_IMG_PATH)
    p1_image = Picture(P1_PLANE_IMG_PATH)
    p2_image = Picture(P2_PLANE_IMG_PATH)
    s1_image = Picture(S1_SUITCASE_IMG_PATH)
    s2_image = Picture(S2_SUITCASE_IMG_PATH)
    s3_image = Picture(S3_SUITCASE_IMG_PATH)

def change_writing_functions_to_gui():
    stdio.writeln = gui_write
    stdio.writef = gui_writef
    stdio.write = gui_write

def gui_writef(fmt, *args):
    text = (fmt.strip()) % args
    gui_write(text)

def gui_write(text=''):
 
    global output_text_list
    text = text.replace('\n', ' ').strip()
    max_width = OUTPUT_AREA_WIDTH - 20
    max_entries = (OUTPUT_AREA_HEIGHT/2) // GUI_OUTPUT_FONT.size(' ')[1]
    words = text.split(' ')
    while len(words) > 0:
        line_words = []
        while len(words) > 0 and GUI_OUTPUT_FONT.size(' '.join(line_words + [words[0]]))[0] < max_width:
            line_words.append(words.pop(0))
        output_text_list.append((' '.join(line_words)).strip())
        while GUI_OUTPUT_FONT.size(output_text_list[-1])[0] < max_width: output_text_list[-1] += ' '
    output_text_list.append('')
    while len(output_text_list) > max_entries or (len(output_text_list) > 0 and output_text_list[0].strip() == ''):
        output_text_list.pop(0)
    draw_message_area()
    stddraw.show(SHOW_DELTA)

def rect_border(x0, y0, xl, yl):
  
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.filledRectangle(x0, y0, xl, yl)
    draw_border_lines(x0, y0, xl, yl)

def draw_border_lines(x0, y0, xl, yl):
   
    stddraw.setPenRadius(DEFAULT_PEN_RADIUS)
    stddraw.setPenColor(stddraw.DARK_GRAY)
    stddraw.line(x0, y0, x0 + xl, y0)
    stddraw.line(x0, y0, x0, y0 + yl)
    stddraw.line(x0 + xl, y0, x0 + xl, y0 + yl)
    stddraw.line(x0, y0 + yl, x0 + xl, y0 + yl)

def draw_message_area():
   
    x0 = 0
    y0 = OUTPUT_AREA_HEIGHT/2
    rect_border(x0, OUTPUT_AREA_HEIGHT/2, OUTPUT_AREA_WIDTH, OUTPUT_AREA_HEIGHT/2)
    if len(output_text_list) > 0:
        x_center = x0 + OUTPUT_AREA_WIDTH/2
        stddraw.setFontSize(15)
        stddraw.setPenColor(stddraw.BLACK)
        for i in range(len(output_text_list)):
            y_center = y0 + (i + 1) * (15)
            stddraw.text(x_center, y_center, output_text_list[len(output_text_list) -1 -i])
        stddraw.setFontSize(FONT_SIZE)

def get_flight_connection_colour(flight_cost: float):
   
    h = max(0.3, min(0.2 + (flight_cost/20.0)*0.9, 1.0))
    i = int(h * 6.0)
    f = int(255*((h * 6.0) - i))
    rgbs = [(255, f, 0), (255-f, 255, 0), (0, 255, f), (0, 255-f, 255), (f, 0, 255), (255, 0, 255-f)]
    return Color(*rgbs[i % 6])

def draw_airport_map(p1_airport_id, p2_airport_id, airport_coordinate_matrix, flight_cost_matrix, cur_player):
    
    cur_airport_id = p1_airport_id if cur_player == 0 else p2_airport_id
    map_coordinates = stdarray.create2D(AIRPORTS, 2, 0)
    padding = 0.05

    l = 500
    x0 = X_MAX - l
    y0 = 0
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')

    rect_border(x0, y0, l, l)
    stddraw.picture(map_image, x0 + l/2, y0 + l/2)
    draw_border_lines(x0, y0, l, l)

    x0 = x0 + l * padding
    y0 = y0 + l * padding
    l = l * (1 - padding*2)

    for airport in range(AIRPORTS):

        x, y = airport_coordinate_matrix[airport]
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    for airport in range(AIRPORTS):
        
        map_coordinates[airport][0] = x0 + ((airport_coordinate_matrix[airport][0] - x_min) / (x_max - x_min)) * l
        map_coordinates[airport][1] = y0 + ((airport_coordinate_matrix[airport][1] - y_min) / (y_max - y_min)) * l
  
    for airport in range(AIRPORTS):

        x1, y1 = map_coordinates[airport]
        for other_airport in range(AIRPORTS):
            if airport == other_airport:
                continue
            x2, y2 = map_coordinates[other_airport]
            f_cost = flight_cost_matrix[airport][other_airport]
            if airport == cur_airport_id:
                stddraw.setPenRadius(2.0)
            else:
                stddraw.setPenRadius(0.5)
            
            stddraw.setPenColor(get_flight_connection_colour(f_cost))
            stddraw.line(x1, y1, x2, y2)
    

    for airport in range(AIRPORTS):

        x, y = map_coordinates[airport]
        stddraw.circle(x, y, AIRPORTS)
        stddraw.text(x, y, str(airport))
    plane_image = stddraw.Image("plane.png")
    p1_x, p1_y = map_coordinates[p1_airport_id]
    p2_x, p2_y = map_coordinates[p2_airport_id]
    stddraw.picture(plane_image, p1_x, p1_y)
    stddraw.picture(plane_image, p2_x, p2_y)

    for airport in range(AIRPORTS):
        x1, y1 = map_coordinates[airport]
        for other_airport in range(AIRPORTS):
            if airport == other_airport:
                continue
            x2, y2 = map_coordinates[other_airport]
            f_cost = flight_cost_matrix[airport][other_airport]
            if airport == cur_airport_id:
                stddraw.setPenRadius(2.0)
            else:
                stddraw.setPenRadius(0.5)
            stddraw.setPenColor(get_flight_connection_colour(f_cost))
            stddraw.line(x1, y1, x2, y2)
            if airport == cur_airport_id or other_airport == cur_airport_id:
             x_mid, y_mid = ((x1 + x2)/2, (y1 + y2)/2) 

if __name__ == '__main__':
    runner()
