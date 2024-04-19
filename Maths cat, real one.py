#Yr 8 Semester 1 CAT investigation (15% of yearly mark)
#FIRST ITERATION

import random #imports the "randint" function to employ a integer randomiser function
import math #allows the"sqrt" feature to be used
import time #allows for the .sleep

print('Welcome to the pythagorean triples movement game!')
time.sleep(1)
print('Loading game...')
time.sleep(1.75)
print('Done!')


# List of Pythagorean triples stored in a dictionary
triples_dictionary = [
[3, 4, 5],
[5, 12, 13],
[8, 15, 17],
[7, 24, 25],
[20, 21, 29],
[12, 35, 37],
[9, 40, 41],
[28, 45, 53],
[11, 60, 61],
[33, 56, 65],
[16, 63, 65],
[48, 55, 73],
[13, 84, 85],
[36, 77, 85],
[39, 80, 89],
[65, 72, 97],
[20, 99, 101],
[60, 91, 109],
[15, 112, 113],
[44, 117, 125],
[88, 105, 137],
[17, 144, 145],
[24, 143, 145],
[51, 140, 149],
[85, 132, 157],
[119, 120, 169],
[52, 165, 173],
[19, 180, 181],
[57, 176, 185],
[104, 153, 185],
[95, 168, 193],
[28, 195, 197],
[133, 156, 205],
[84, 187, 205],
[21, 220, 221],
[140, 171, 221],
[60, 221, 229],
[105, 208, 233],
[120, 209, 241],
[32, 255, 257],
[23, 264, 265],
[96, 247, 265],
[69, 260, 269],
[115, 252, 277],
[160, 231, 281],
[161, 240, 289],
[68, 285, 293],
[207, 224, 305],
[136, 273, 305],
[25, 312, 313],
[75, 308, 317],
[204, 253, 325],
[36, 323, 325],
[175, 288, 337],
[180, 299, 349],
[225, 272, 353],
[27, 364, 365],
[76, 357, 365],
[252, 275, 373],
[135, 352, 377],
[152, 345, 377],
[189, 340, 389],
[228, 325, 397],
[40, 399, 401],
[120, 391, 409],
[29, 420, 421],
[87, 416, 425],
[297, 304, 425],
[145, 408, 433],
[203, 396, 445],
[84, 437, 445],
[280, 351, 449],
[168, 425, 457],
[261, 380, 461],
[31, 480, 481],
[319, 360, 481],
[93, 476, 485],
[44, 483, 485],
[155, 468, 493],
[132, 475, 493],
[217, 456, 505],
[336, 377, 505],
[220, 459, 509],
[279, 440, 521],
[308, 435, 533],
[92, 525, 533],
[341, 420, 541],
[33, 544, 545],
[184, 513, 545],
[165, 532, 557],
[396, 403, 565],
[276, 493, 565],
[231, 520, 569],
[48, 575, 577],
[368, 465, 593],
[240, 551, 601],
[35, 612, 613],
[105, 608, 617],
[336, 527, 625],
[429, 460, 629],
[100, 621, 629],
[200, 609, 641],
[315, 572, 653],
[300, 589, 661],
[385, 552, 673],
[52, 675, 677],
[37, 684, 685],
[156, 667, 685],
[111, 680, 689],
[400, 561, 689],
[185, 672, 697],
[455, 528, 697],
[260, 651, 701],
[259, 660, 709],
[333, 644, 725],
[364, 627, 725],
[108, 725, 733],
[407, 624, 745],
[216, 713, 745],
[468, 595, 757],
[39, 760, 761],
[481, 600, 769],
[195, 748, 773],
[273, 736, 785],
[56, 783, 785],
[432, 665, 793],
[168, 775, 793],
[555, 572, 797],
] #closes off the dictionary

def translate_da_player(distance, player_direction): #translation function
    
    if  player_direction < 1 or player_direction > 8: #checks to see if its a valid integer
      print('Direction must be an integer between 1 and 8. Player who didnt have that turn wins!') 
      exit()
          

    
    

    # Find the closest Pythagorean triple
    closest_pythagorean_triple = None #The code first assumes there is no nearby triple, equalling to none. The below function then finds the nearest triple
    for triple in triples_dictionary: #this line of code scans through the pythagorean triple dictionary 
        #it will stop finding a triple when the hypotenuse is greater or equal to the given distance to move
        if triple[2] >= distance:
            closest_pythagorean_triple = triple
            break #ends this section when the nearest pythagorean triple is found 

    if closest_pythagorean_triple is None : #if there is still no closest triple found
        print('No suitable triple found, the other player WINS!')
        exit()#if there is no suitible triple closeby, this value error will pop up
    # Calculate the translation based on the direction
    else :
        a, b, c = closest_pythagorean_triple #This substitutes the pythagorean triples into a, b, and c (the hypotenuse)
        player_translations_dictionary = [
            (b,a), (a,b), (-a, b), (-b, a), (-b, -a), (-a, -b), (a, -b), (b, -a)
        ] #This is a list of translations. The list of translations is based off the closest pythagorean triple
        #Translations list/dictionary contains tuples of x and y coordinates, representing 8 different methods of movement
        #EDIT: THX NEEL AND ALVIN FOR HELPING ME SOLVE THE ISSUES WITH THE TRANSLATIONS!!!
    
    if IndexError is True :
        return "Index Error"
    else :

        return player_translations_dictionary[player_direction] #returns the translation corresponding to the given direction. It is based from the translations list

def check_player_winning_condition(player, destination, imandiv_space): #code/function to check winning condition
    distance = math.sqrt((player['x'] - destination['x'])**2 + (player['y'] - destination['y'])**2) #player variables are the player's coordinate positions
    #destination variables are the destination, split into the x and y coordinates
    #bracketed equations caculate the distance between the player and the destination, conversely in x and y coordinate fashion
    #the **2 squares the coordinates, then the + symbol completes the sum of squared differences
    #math.sqrt is a function from the python math module that calculates the square root of the squared differences (aka a Euclidean distance)
    if distance <= imandiv_space:
        return True #if the distance of the player is less or equal to the buffer, 'TRUE' will be returned meaning the player reaching the destination is true
    return False #function will return a false 

def display_player_information(player, destination, distance): #player information function; allows for player position and destination to be displayed
    print(f"Player Location on the Plane: ({player['x']}, {player['y']})") #This retrieves the x and y coordinates of the player
    print(f"Destination: ({destination['x']}, {destination['y']})") #In  a similar fashion, this accesses the x and y coordinates of the desto, using a f-string to print in the format of (x,y)
    print(f"Distance from Destination: ({player['x'] - destination['x']}, {player['y'] - destination['y']})") #calculates distance from the player destination
    

def main_function() : #main function, or the main game
    
    
    player1name = input("\nEnter Player 1's name: ")
    player2name = input("Enter Player 2's name: ")
    
    
        
    

    
    
    menu = input('\nEnter 1 to start the game, and enter anything else for instructions (IMPORTANT TO READ): ') #option to see the instructions in the code
    
    
    if menu == "1" : 

    
        #starts the game if the input is 1, and takes the users to the difficulty selection
        le_player_difficulty = input('\nDifficulty selection: Easy, Medium, Hard? ')
        if le_player_difficulty == "Easy" :
            imandiv_space = 100 #imandiv space is the buffer (sry imandiv)
        elif le_player_difficulty == "Medium" :
            imandiv_space = 50
        elif le_player_difficulty == "Hard" :
            imandiv_space = 10 #THE BUFFER IS 10 ONG PLZZZZ
        else :
            print('Please select a valid option :D')
            main_function()
        #The buffer will make it easier and less time consuming for players to reach the end point. 
        #Depending on the difficulty, the size of the buffer will either be higher or lower; lower being harder
        
        #dictionaries with player information
        player1_information = {'x': random.randint(-800, 800), 
                                'y': random.randint(-800, 800),
                                'Player 1 name' :  player1name, 
                                'Personal space buffer size' : imandiv_space,
                                'Difficulty' : le_player_difficulty
        }
        #Defines the x and y coordinates, using the randint function
        #The integers in the brackets are the range of possible coordinates the players and the destination can be
        #"Random" is a function imported from pythons random list of functions
        player2_information = {'x': random.randint(-800, 800), #the format behind 'x' : (function) is so the coordinates can be called when 'x' is put into a line of code
                                'y': random.randint(-800, 800),
                                "Player 2's name" : player2name,
                                'Personal space buffer size' : imandiv_space,
                                'Difficulty' : le_player_difficulty
                                
        }                        
        #player 2 information on coordinates
        AI_coordinates = {'x' : random.randint(-800, 800), 
                        'y' : random.randint(-800, 800)
        }
        #player 3 info; yes, even the ai has info!
        destination = {'x': random.randint(-800, 800), 
                    'y': random.randint(-800, 800)
        }
        #These lines of code make 'x' equal a certain integer, same wtih the y

        
        
        
        
        
        
        print('\nLoading player summary...')
        time.sleep(1.5)
        print('\nPLAYER SUMMARY (DOUBLE CHECK EVERYTHING IS RIGHT BEFORE PLAYING!)')
        print(f"Player 1's starting coordinates: (" + str(player1_information['x']) + (' , ') + str(player1_information['y']) + ")")
        print(f"Player 2's starting coordinates: (" + str(player2_information['x']) + (' , ') + str(player2_information['y']) + ")")
        print(f"The AI's starting coordinates:(" +  str(AI_coordinates['x']) + (' , ') + str(AI_coordinates['y']) + ")")
        print(f"\nTheir goal is:(" + str(destination['x']) + (' , ') + str(AI_coordinates['y']) + ")")

        time.sleep(1.75)
    
        while True: #While true puts the game into an infinite loop
            def player_1_turn():
                print('\n' + player1_information ['Player 1 name'] + 's turn: ') #opens the player name part of the information dictionary
                #It will end when one of the players reaches the end, and the "break" function excecutes at the end of the function
                # Player 1's turn below
                distance = input("\nPlayer 1: Enter distance to move on the plane: ")
                try : #tries to convert the input into a number
                    #will only work if only a number was inputted into the input
                    distancenum = int(distance)
                except : #when it fails to convert it to a number, error message will show
                    print('Please enter a number, nothing else :)')
                    player_1_turn() #takes them back to the first question in the turn
                else :
                    
                    def contin_player_1_turn() :
                        #Asks for the distance to move, then converts it to an integer
                        #Same thing is done with the direction, the function asks for the direction to move in and converts it to an integer
                        direction = input("Player 1: Enter direction to move towards (1-8); if you enter a wrong number you'll loose your turn!: ")
                        try : #basically the same as above
                            directionnum = int(direction)
                        except : #however, when you don't input a number you will be taken to the "enter direction" question
                            print("ENTER A NUMBER PLEASE, NO LETTERS!")
                            contin_player_1_turn()
                        else :
                        
                            player_translation_on_da_plane = translate_da_player(distancenum, directionnum) #The translate function is called with paramaters in the brackets
                            #This translate function returns a tuple representing movement and change in the x and y coordinates
                            #Also determines the movement of the cartesian plane
                            player1_information['x'] += player_translation_on_da_plane[0] #The 'x' value, which was one set of coordinates updates
                            #based on the value the translation is equal to 
                            player1_information['y'] += player_translation_on_da_plane[1]
                            #Also updates the coordinates based on what was inputted above, by translation
                            #The above two lines function as the following:
                            #The x and y coordinates are updated based on the info from the translation func 
                            print('Player 1 moved.')
                            if IndexError is True : #this will accomodate the event where the inputted values are out of range
                                print('Inputted value is out of range')
                                contin_player_1_turn()
                            else :
                                display_player_information(player1_information, destination, distance)
                                print('\nProcessing code...')
                                time.sleep(1.5)
                                #displays new destination
                                if check_player_winning_condition(player1_information, destination, imandiv_space):
                                    #The check winner function, another imported function checks if all these conditions are met
                                    #This utilises the Euclidean formula for distance, most commonly used in cartesian plane codes for movement
                                    print("\nPlayer 1 wins! GGWP!")
                                    exit() #exits game
                        
                    contin_player_1_turn()         
            
            player_1_turn()
            
            
            
            
            def player_2_turn():
                print('\n' + player2_information ["Player 2's name"] + 's turn:') 
                # Player 2's turn. The code for player 2 is more or less the same as player 1, so no notes have been given for it
                distance = input("\nPlayer 2: Enter distance to move on the plane: ")
                try :
                    distancenum2 = int(distance)
                except :
                    print('please enter a number :)')
                    player_2_turn()
                else :
                    
                    
                    def contin_player_2_turn() :
                        direction = input("Player 2: Enter direction (1-8);  if you enter a wrong number you'll loose your turn: ")
                        try :
                            directionnum2 = int(direction)
                        except :
                            print('ENTER A NUMBER, WHY WOULDNT YOU!')
                            contin_player_2_turn() 
                        else :
                            translation = translate_da_player(distancenum2, directionnum2)
                            player2_information['x'] += translation[0]
                            player2_information['y'] += translation[1]
                            print("Player 2 moved.")
                            if IndexError is True :
                                print('Inputted values is out of range.')
                                contin_player_2_turn()
                            else :
                                display_player_information(player2_information, destination, distance)
                                print('\nProcessing code...')
                                time.sleep(2.5)
                                if check_player_winning_condition(player2_information, destination, imandiv_space):
                                    print("\nPlayer 2 wins! GGWP!")
                                    exit()
                    contin_player_2_turn()
                
                
            player_2_turn()



            def player_3_turn_ai() : #Player 3's turn, which is an ai
            # Player 2's turn. The code for player 2 is more or less the same as player 1, so no notes have been given for it
                print("\nAI's turn")
                distance = random.randint(1, 5) 
                direction = random.randint(1,2)
                #the ai 3rd player chooses a random distance and direction
                direction3 = direction 
                distance3 = distance 

                newplayer3dest = translate_da_player(distance3, direction3) #translates the ai's random distance and direction
                #the random distance and direction gets translated
                #this determines the ai's new position
                print('The AI is deciding where to move...')
                time.sleep(2.45) #this command from the time dictionary makes the ai take 3 seconds to decide
                #for cringe ig
                print("The AI has decided where to move!")
                print('AI location:', newplayer3dest)
                print('Destination:' + "(" + str(destination['x']) + ', ' + str(destination['y'] ) + ")") #shows the destination incase the players forgot (i guess)
                if IndexError is True : #if the ai chooses a value out of range, it will skip to player 1's turn
                    print('Index error from the ai, it has a skill issue lol')
                    player_1_turn()
                time.sleep(1.5)
    
            
            player_3_turn_ai()
        
    
    else: #displays instructions
        #NOte: \n is used in the writing to skip a line, making it clearer to read
        print('\nBASIC GAME INSTRUCTIONS')
        print('2  players will be placed randomly on an imaginary cartiesian plane. ')
        print('You will take turns moving towards your destination, by entering the amount of units and direction to move')
        print('The player that reaches the end destination first wins!')
        print('You are able to select the difficulty of the game, which changes the space buffer')
        print('The player will lose if their inputted distance are not within a nearby triple, so play it safe!')
        print('\nPERSONAL SPACE BUFFER')
        print('The space buffer is a certain radius around the destination point (in units)')
        print('It acts as a general area where the function deems the player to have reached the destination')
        print('Easy = 100 units; Medium = 50 units; Hard = 15')
        print('\nMOVING IN DIFFERENT DIRECTIONS')
        print('Direction numbers are a result of dividing a sector of a cartesian plane diagonally in two')
        print('For example, moving in direction 1 is from 0 to 45 degrees, 2 is 45 to 90 degrees, up until direction 8 from 315-360 degrees')
        print('\nERROR INPUTS')
        print("If you do not enter a whole integer in either the direction or distance to move inputs, you'll simply be asked again")
        print('When there is a case where no nearby pythagorean triple nearby, the game will end')
        print('The aim is to be as close to a pythagorean triple as possible')
        print('\nAI')
        print('The player 3 is run by an ai')
        print('It will move to random spots, choosing a random direction and distance')
        print('Imagine if the ai beats you...')
        return_menu = input('\nEnter 1 to return to the menu, and enter anything else to quit: ') #asks user to return or quit

        if return_menu == "1" :
            print('\nINTIALISING MENU...') #some text here just for fun 🥰
            time.sleep(2.5)
            main_function() #brings the user back to the game
        
        else :
            print('Bye')
            exit() #exit function
        
    

    

main_function()




