import random
import math

def CPUNumber():
    return random.ranint(0, 5)

def CPUGuess(guess):
    return random.randint(guess, guess + 5)

class PVEGame():

    def PVEplay():
        pass
    
class PVPGame():

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
        
        
def main():
    pass
    
if __name__ == "__main__":
    main()
    
