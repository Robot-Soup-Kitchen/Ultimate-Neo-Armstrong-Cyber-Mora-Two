import random
import math

def main():
    print("Hey, welcome to neo mora\n1 - PVE (1 player)\n2 - PVP (2 players)")
    choice = input("which mode do you want to play? \n")
    if choice == '1':
        game = PVEGame()
        try: 
            game.play()
        except:
            print("Yo, stop cheating!")
    elif choice == '2':
        game = PVPgame()
        game.PVPplay()
    else:
        print("WTF dude, you dumb?")
    
    print()
    print("ye!!!! thanks for playing!")
        


class PVEGame():

    def play(self):

        print("You are playing Ultimate Neo Armstrong Cyber Mora 2: Training Mode")
        print()
        pnumber = self.getPlayerNumber()
        print("Your Opponent played a number")
        cnumber = self.CPUNumber()
    
        pguess = self.getPlayerGuess()
        print("Your Oppenent has guessed")
        cguess = self.CPUGuess(cnumber)

        total = pnumber + cnumber
        print()
        fingerprint(pnumber, cnumber)
        print("Your Opponent played: %d" % cnumber)
        print("You guessed: %d" % pguess)
        print("Your Opponent guessed: %d" % cguess)
        print("The total was: %d + %d = %d" % (pnumber, cnumber, total))
        if ((pguess == total) and(cguess == total)):
            print("DRAW")
        elif pguess == total:
            print("WIN")
        elif cguess == total:
            print("LOSE")
        else:
            print("YOU BOTH LOSE")
        print()



    def getPlayerNumber(self):
        num  = input("Play a number: ")
        if not num.isnumeric():
            raise Exception
        elif ((int(num) < 0) or (int(num) > 5)):
            raise Exception
        else:
            return int(num)
    
    def getPlayerGuess(self):
        num  = input("Make your guess: ")
        if not num.isnumeric():
            raise Exception
        elif ((int(num) < 0) or (int(num) > 10)):
            raise Exception
        else:
            return int(num)

    def CPUNumber(self):
        return random.randint(0, 5)

    def CPUGuess(self, guess):
        return random.randint(guess, guess + 5)

class PVPgame():

    def PVPplay(self):
        print("Ultimate Neo Armstrong Cyber Mora 2: Duel Mode")
        
        print("Select a number of fingers between 0 and 5. Choose wisely. The goal is to guess the sum of both members' fingers.")
        
        selectScreen = 1
        while selectScreen == 1:
            InputP1 = int(input("Contestant 1, choose your fingers!!! Fingers: "))
            if InputP1 < 0 or InputP1 > 5:
                print("Wrong! The number must be between 0 and 5!!")
            else:
                selectScreen = 0
                
        selectScreen = 1
        print("\n")
        while selectScreen == 1:
            InputP2 = int(input("Contestant 2, choose your fingers!!! Fingers: "))
            if InputP2 < 0 or InputP2 > 5:
                print("Wrong! The number must be between 0 and 5!!")
            else:
                selectScreen = 0            
        
        actualSum = InputP1 + InputP2
        
        print("Contestants have given their fingers.")
        GuessP1 = input("Contestant 1, do not hesitate, and make your guess! Guessed sum: ")
        print("\n")
        GuessP2 = input("Contestant 2, make your guess, and make your peace! Guessed sum: ")
        
        #Check which player was closer
        CheckP1 = abs(int(actualSum) - int(GuessP1))
        CheckP2 = abs(int(actualSum) - int(GuessP2))
        
        if CheckP1 < CheckP2:
            win = "Looks like contestant 1 came out victorious!\nThe new champion of Ultimate Neo Armstrong Cyber Mora 2 is crowned!"
        elif CheckP1 > CheckP2:
            win = "Contestant 2 is the winner!\nThe new champion of Ultimate Neo Armstrong Cyber Mora 2 is crowned!"
        else:
            win = "It's a tie! Both contestants fought valiantly!"
            
        print(win)
    
        
def fingerprint(player1, player2):
    p1one = ['         /"\                  |',
"        |\./|                 |",
"        |   |                 |",
"        |   |                 |",
"        |>*<|                 |",
"        |   |                 |",
"     /'\|   |/'\              |",
" /'\|   |   |   |             |",
"|   |   |   |   |\            |",
"|   |   |   |   |  \          |",
"| *   *   *   * |>  >         |",
"|                  /          |",
" |               /            |",
"  |            /              |",
"   \          |               |",
"    | PLAYER1 |               |"]
    
    p1two =[ "                                    |",
"                                    |",
"                                    |",
'/"\                                 |',
"\\./\                                |",
" \   \        /'\          _        |",
"  \>*<\   /'\|   |/'\    // \       |",
"   \   \ |   |   |   |  / \ /       |",
"    \   \|   |   |   | / >*/        |",
"     |   |   |   |   |/   /         |",
"     | *   *   *   * |>  >          |",
"     |                  /           |",
"      |               /             |",
"       |            /               |",
"        \          |                |",
"         | PLAYER1 |                |"]
    
    p1three = ['         /"\                  |',
'     /"\|\./|/"\              |',
"    |\./|   |\./|             |",
"    |   |   |   |             |",
"    |   |>*<|>*<|             |",
"    |   |   |   |             |",
"    |   |   |   |             |",
" /'\|   |   |   |             |",
"|   |   |   |   |\            |",
"|   |   |   |   |  \          |",
"| *   *   *   * |>  >         |",
"|                  /          |",
" |               /            |",
"  |            /              |",
"   \          |               |",
"    | PLAYER1 |               |"]
    
    p1four = ['         /"\                  |',
'     /"\|\./|/"\              |',
"    |\./|   |\./|             |",
' /"\|   |   |   |             |',
"|\./|   |>*<|   |             |",
"|   |>*<|   |>*<|             |",
"|>*<|   |   |   |             |",
"|   |   |   |   |             |",
"|   |   |   |   |\            |",
"|   |   |   |   |  \          |",
"| *   *   *   * |>  >         |",
"|                  /          |",
" |               /            |",
"  |            /              |",
"   \          |               |",
"    | PLAYER1 |               |"]
    
    p1five =['         /"\                  |',
'     /"\|\./|/"\              |',
"    |\./|   |\./|             |",
' /"\|   |   |   |             |',
"|\./|   |>*<|   |             |",
"|   |>*<|   |>*<|    _        |",
"|>*<|   |   |   |   // \      |",
"|   |   |   |   |  / \ /      |",
"|   |   |   |   | / >*/       |",
"|   |   |   |   |/   /        |",
"| *   *   *   * |>  >         |",
"|                  /          |",
" |                /           |",
"  |             /             |",
"   \           |              |",
"    | PLAYER1  |              |"]
    
    p2one = ['                  /"\ ',
"                 |\./|",
"                 |   |",
"                 |   |",
"                 |>*<|",
"                 |   |",
"              /'\|   |/'\ ",
"          /'\|   |   |   |",
"         |   |   |   |   |\ ",
"         |   |   |   |   |  \ ",
"         | *   *   *   * |>  >",
"         |                  / ",
"          |               / ",
"           |            / ",
"            \          |",
"             | PLAYER2 |"]
    
    p2two = [
" ",
" ",
" ",
'         /"\ ',
"         \\./\ ",
"          \   \        /'\          _",
"           \>*<\   /'\|   |/'\    // \ ",
"            \   \ |   |   |   |  / \ /",
"             \   \|   |   |   | / >*/",
"              |   |   |   |   |/   /",
"              | *   *   *   * |>  >", 
"              |                  /",
"               |               /",
"                |            /",
"                 \          |",
"                  | PLAYER2 |"]

    p2three =['                  /"\ ', 
'              /"\|\./|/"\ ',
"             |\./|   |\./|",
"             |   |   |   |",
"             |   |>*<|>*<|",
"             |   |   |   |",
"             |   |   |   |",
"          /'\|   |   |   |",
"         |   |   |   |   |\ ",
"         |   |   |   |   |  \ ",
"         | *   *   *   * |>  >",   
"         |                  /",
"          |               /",
"           |            /",
"            \          |",
"             | PLAYER2 |"]
    
    p2four = [
'                  /"\ ',
'              /"\|\./|/"\ ',
"             |\./|   |\./|",
'          /"\|   |   |   |',
"         |\./|   |>*<|   |",
"         |   |>*<|   |>*<|",
"         |>*<|   |   |   |",
"         |   |   |   |   |",
"         |   |   |   |   |\ ",
"         |   |   |   |   |  \ ",
"         | *   *   *   * |>  >",   
"         |                  /",
"          |               /",
"           |            /",
"            \          |",
"             | PLAYER2 |"]
    
    p2five = ['                  /"\"',
'              /"\|\./|/"\ ',
"             |\./|   |\./|",
'          /"\|   |   |   |',
"         |\./|   |>*<|   |",
"         |   |>*<|   |>*<|    _",
'         |>*<|   |   |   |   // \ ',
"         |   |   |   |   |  / \ /",
"         |   |   |   |   | / >*/",
"         |   |   |   |   |/   /",
"         | *   *   *   * |>  >", 
"         |                  /",
"          |                /",
"           |             /",
"            \           |",
"             | PLAYER2  |"]
    
    p1options = [[], p1one, p1two, p1three, p1four, p1five]
    p2options = [[], p2one, p2two, p2three, p2four, p2five]

    final = ""
    hand1 = p1options[player1]
    hand2 = p2options[player2]

    counter = 0
    while counter <= 15:
        final = final + hand1[counter] + hand2[counter] + "\n"
        counter+=1
    print(final)

    
    
if __name__ == "__main__":
    main()
    
