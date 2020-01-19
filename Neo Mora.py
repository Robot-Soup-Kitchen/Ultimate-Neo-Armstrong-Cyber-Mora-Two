import random
import math

def main():
    print("Hey welcome to neo mora\n1 - PVE (1 player)\n2 - PVP (2 players)")
    choice = input("what do you want to play? ")
    if choice == '1':
        game = PVEGame()
        try: 
            game.play()
        except:
            print("yo stop cheating")
    elif choice == '2':
        game = PVPgame()
        try: 
            game.PVPplay()
        except:
            print("yo stop cheating")
    else:
        print("wtf dude, u dumb?")
    
    print()
    print("bye!!!! thanks for playing!")
        


class PVEGame():

    def play(self):

        print("Hello, you are playing NEO MORA!")
        print()
        pnumber = self.getPlayerNumber()
        print("Your Opponent played a number")
        cnumber = self.CPUNumber()
    
        pguess = self.getPlayerGuess()
        print("Your Oppenent has guessed")
        cguess = self.CPUGuess(cnumber)

        total = pnumber + cnumber
        print()
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

    def PVPplay():
        print("Ultimate Neo Armstrong Cyber Mora 2: Duel Mode")
        
        print("Select a number of fingers between 0 and 5. Choose wisely. The goal is to guess the sum of both members' fingers.")
        
        selectScreen = 1
        while selectScreen == 1:
            InputP1 = input("Contestant 1, choose your fingers!!! Fingers: ")
            if InputP1 < 0 | InputP1 > 5:
                print("Wrong! The number must be between 0 and 5!!")
            else:
                selectScreen = 0
                
        selectScreen = 1
        print("\n")
        while selectScreen == 1:
            InputP2 = input("Contestant 2, choose your fingers!!! Fingers: ")
            if InputP2 < 0 | InputP2 > 5:
                print("Wrong! The number must be between 0 and 5!!")
            else:
                selectScreen = 0            
        
        actualSum = InputP1 + InputP2
        
        print("Contestants have given their fingers.")
        GuessP1 = input("Contestant 1, make your guess! Guessed sum: ")
        print("n")
        GuessP2 = input("Contestant 1, make your guess! Guessed sum: ")
        
        #Check which player was closer
        CheckP1 = abs(actualSum - GuessP1)
        CheckP2 = abs(actualSum - GuessP2)
        
        if CheckP1 < checkP2:
            win = "Looks like contestant 1 came out victorious!\nThe new champion of Ultimate Neo Armstrong Cyber Mora 2 is crowned!"
        elif CheckP1 > CheckP2:
            win = "Contestant 2 is the winner!"
        else:
            win = "It's a tie! Both contestants fought valiantly!\nThe new champion of Ultimate Neo Armstrong Cyber Mora 2 is crowned!"
            
        print(win)
        
        

    
if __name__ == "__main__":
    main()
    
