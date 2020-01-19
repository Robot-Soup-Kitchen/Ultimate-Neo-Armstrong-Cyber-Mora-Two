import random

def main():
    game = PVEGame()
    while(1):
        try: 
            game.play()
        except:
            print("yo stop cheating")


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

main()