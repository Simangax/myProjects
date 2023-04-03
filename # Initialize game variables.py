# Initialize game variables
suitcases_collected = []
wallet_balance = 100
available_disks = ['A', 'B', 'C']
available_airports = ['Airport 1', 'Airport 2', 'Airport 3']

# Player 1 selects starting airport and flips a suitcase
current_player = 1
print("Player 1's turn.")
selected_airport = input("Select a starting airport (1, 2, or 3): ")
selected_airport_name = available_airports[int(selected_airport) - 1]
print("You selected", selected_airport_name)

suitcase_number = input("Select a suitcase to flip (1-10): ")
if suitcase_number == "Q":
    print("Terminating the game. Thanks for playing!")
    quit()

if suitcase_number == str(len(suitcases_collected) + 1):
    print("You found suitcase number", suitcase_number)
    suitcases_collected.append(suitcase_number)
else:
    print("Sorry, that is not the suitcase you need.")
    
# Player 2 selects starting airport and flips a suitcase
current_player = 2
print("Player 2's turn.")
selected_airport = input("Select a starting airport (1, 2, or 3): ")
selected_airport_name = available_airports[int(selected_airport) - 1]
print("You selected", selected_airport_name)

suitcase_number = input("Select a suitcase to flip (1-10): ")
if suitcase_number == "Q":
    print("Terminating the game. Thanks for playing!")
    quit()

if suitcase_number == str(len(suitcases_collected) + 1):
    print("You found suitcase number", suitcase_number)
    suitcases_collected.append(suitcase_number)
else:
    print("Sorry, that is not the suitcase you need.")
    
# Game continues until win or lose condition is met
while True:
    # Alternate turns
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
        
    print("Player", current_player, "'s turn.")
    
    # Check for win condition
    if len(suitcases_collected) == 10:
        print("Congratulations, you have won the game!")
        break
        
    # Check for lose condition
    if wallet_balance < 0 or not available_airports or not available_disks or wallet_balance < 50:
        print("You have lost the game. Your opponent wins!")
        break
    
    # Check if player can move to a different airport
    if len(suitcases_collected) > 0:
        move_to_airport = input("Do you want to move to a different airport? (Y/N): ")
        if move_to_airport.upper() == "Y":
            print("Select an airport to move to:")
            for index, airport in enumerate(available_airports):
                print(index + 1, "-", airport)
            selected_airport = input()
            selected_airport_name = available_airports[int(selected_airport) - 1]
            print("You moved to", selected_airport_name)
            available_airports.remove(selected_airport_name)
    
    # Check if player can use an obstacle disk
    if len(available_disks) > 0:
        use_disk = input("Do you want to use an obstacle disk? (Y/N): ")
        if use_disk.upper() == "Y":
            print("Select a disk to use:")
            for index, disk in enumerate(available_disks):
                print(index + 1, "-", disk)


while True:
    play_game = input("Do you want to play a new game? (Y/N): ")
    if play_game.upper() == "Y":
        # code to start a new game goes here
        print("Starting a new game...")
    elif play_game.upper() == "N":
        print("Exiting the game. Thanks for playing!")
        break
    elif play_game.upper() == "Q":
        print("Terminating the program. Thanks for playing!")
        quit()
    else:
        print("Invalid input. Please enter Y, N or Q.")