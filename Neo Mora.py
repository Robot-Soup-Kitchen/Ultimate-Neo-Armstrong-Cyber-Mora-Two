import random

def main():
    while(1):
        PVEGame()


class PVEGame():

    def PVEplay(self):

        print("Hello, you are playing NEO MORA!")
        print("PLAY YOUR HAND: ")
        pnumber = self.getPlayerNumber()
        print("YOUR OPPONENT HAS SELECTED A NUMBER")
        cnumber = self.CPUGuess()
        print("MAKE YOUR GUESS")
        pguess = self.getPlayerNumber()
        print("YOUR OPPONENT HAS MADE THEIR GUESS")
        cguess = self.getPlayerGuess(cnumber)

        total = pnumber + cnumber

        print("YOU GUESSED %d" % pguess)
        print("YOUR OPPONENT GUESSED %d" % cguess)
        print("THE TOTAL WAS %d" % total)
        if ((pguess == total) and(cguess == total)):
            print("DRAW")
        elif pguess == total:
            print("YOU WIN")
        elif cguess == total:
            print("YOUR OPPONENT WON")
            print("YOU LOSE")
        else:
            print("YOU BOTH LOSE")



    def getPlayerNumber(self):
        return input()
    
    def CPUNumber(self):
        return random.ranint(0, 5)

    def CPUGuess(self, guess):
        return random.randint(guess, guess + 5)

main()