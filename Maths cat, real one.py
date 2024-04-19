import random #imports the "randint" function to employ a integer randomiser function
import math #allows the"sqrt" feature to be used


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
      print('Direction must be an integer between 1 and 8. ') 
      exit()
          

    
    

    # Find the closest Pythagorean triple
    closest_pythagorean_triple = None #The code first assumes there is no nearby triple, equalling to none. The below function then finds the nearest triple
    for triple in triples_dictionary: #this line of code scans through the pythagorean triple dictionary 
        #it will stop finding a triple when the hypotenuse is greater or equal to the given distance to move
        if triple[2] >= distance:
            closest_pythagorean_triple = triple
            break #ends this section when the nearest pythagorean triple is found 
    
    if closest_pythagorean_triple is None : #if there is still no closest triple found
        print('No suitable triple found (placeholder probs)')
        exit()#if there is no suitible triple closeby, this value error will pop up
    # Calculate the translation based on the direction
    else :
        a, b, c = closest_pythagorean_triple #This substitutes the pythagorean triples into a, b, and c (the hypotenuse)
        player_translations_dictionary = [
            (b,a), (a,b), (-a, b), (-b, a), (-b, -a), (-a, -b), (a, -b), (b, -a)
        ] #
def main_func(): 

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
        #player 3 info; yes, even the ai has info!
        destination = {'x': random.randint(-800, 800), 
                    'y': random.randint(-800, 800)
        }

       def player_1_turn():
                print('\n' + player1_information ['Player 1 name'] + 's turn: ') #opens the player name part of the information dictionary
                #It will end when one of the players reaches the end, and the "break" function excecutes at the end of the function
                # Player 1's turn below
                distance = input("\nPlayer 1: Enter distance to move on the plane: ")
                distance = input('Enter distance to move on the plane: ')
                direction = input("Player 1: Enter direction to move towards (1-8); if you enter a wrong number you'll loose your turn!: ")
                player1_information['x'] += player_translation_on_da_plane[0] #The 'x' value, which was one set of coordinates updates
                #based on the value the translation is equal to 
                player1_information['y'] += player_translation_on_da_plane[1]
                print('Player turn test done')
                          
                            
                                
                           
            
    player_1_turn()
