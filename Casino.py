#Casino program featuring the choice between multiple games, as well as the option to put money onto a casino card and check balances if necessary.
import random
from time import sleep

def main():
    #Display the name of the casino
    print("-----Welcome to the COVID-19 Style Casino and Virtual Resort-----")
    print("\n\n\n")

    #Initialize variables and take input to verify age
    print("To access this casino and take full advantage of what we offer, you must be 21 years of age or older! \n\n")

    age = 0

    while True:
        try:
            age = int(input("Please enter your age: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    #Ensure the user is indeed 21
    if age >= 21:
        print("You may now proceed to access our casino. \n\n")
        print("----------------------------------------------------------------------------")
        card()
    elif age < 21:
        print("You have been denied access to our casino. I would suggest the virtual Chuck E. Cheese for your entertainment.")


#-------------------Begin Casino Card Code Block--------------------

#Function to accept a deposit for a card
def card():
    print("It is necessary for you to deposit money onto our casino card in order to play our games. \n")

    while True:
        try:
            casinoCard = int(input("How much money would you like to deposit onto your card ($100 is the recommended amount): \n"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    writeFile(casinoCard)
    print("Your card balance is currently",casinoCard,"dollars and the balance will be displayed after each game played. You will also be able to access the ATM at this time. \n")
    gameSelectionMenu()

#Function to write the card balance to a file
def writeFile(balance):
    inFile = open("balance.dat" , "w")

    inFile.write(str(balance))

    inFile.close()

#Function to check the card balance before each game to ensure that you can play the game
def checkCardBalance():
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    if int(currentBalance) == 0:
        print("\nYou must visit the ATM before playing this game as your card balance is zero.\n")
        atm()

#Function to read the card balance fron the file
def checkBalance():
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    while True:
        if int(currentBalance) <= 100:
            print("\nYour card balance is too low. You need to visit an ATM before playing this game.\n")
            atm()
        elif int(currentBalance) > 0:
            print("\nYou currently have",currentBalance,"dollars on your casino card.\n")
            print("----------------------------------------------------------------------------")
            break
    gameSelectionMenu()

#ATM  machine to add money onto the card
def atm():
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Write bet to file
    inFile = open("balance.dat" , "w")

    while True:
        try:
            deposit = int(input("\nHow much money would you like to deposit to your card: \n"))
        except ValueError:
            print("\nInvalid input.\n")
            continue
        else:
            break

    if deposit > 0:
        print("\nThank you for your deposit of",deposit,"dollars. Play on!")
        newBalance = int(currentBalance) + deposit
        inFile.write(str(newBalance))
        inFile.close()
        gameSelectionMenu()

#Function to compute a bet and write that new amount to a file
def writeBet(betValue):
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Write bet to file
    inFile = open("balance.dat" , "w")

    newBalance = int(currentBalance) - betValue

    inFile.write(str(newBalance))

    inFile.close()


def writeWinnings(winnings):
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Write winnings to file
    inFile = open("balance.dat" , "w")

    newBalance = int(currentBalance) + winnings

    inFile.write(str(newBalance))

    inFile.close()


#Menu to choose which game to play
def gameSelectionMenu():
    print("\nOur casino offers a slot machine, blackjack table, and a mouse wheel. Please select which game you would like to play! \n")
    userChoice = 0
    confirmation = 0

    print(" 1. Slot Machine")
    print(" 2. BlackJack")
    print(" 3. Mouse Wheel")
    print(" 4. Cup Game")
    print(" 5. Check Card Balance")
    print(" 6. Access ATM")
    print(" 7. Leave the casino")

    while True:
        try:
            userChoice = int(input("What would you like to do? "))
        except ValueError:
            print("\nInvalid input.\n")
            continue
        else:
            break

    print("----------------------------------------------------------------------------")

    if userChoice == 1:
        slotMachine()
    elif userChoice == 2:
        blackjackGame()
    elif userChoice == 3:
        mouseWheel()
    elif userChoice == 4:
        cups()
    elif userChoice == 5:
        checkBalance()
    elif userChoice == 6:
        atm()
    elif userChoice == 7:

        while True:
            try:
                confirmation = input("Are you sure you want to leave?(Type Y for yes and N for no): ")
            except ValueError:
                print("Invalid input.")
                continue
            else:
                break

        if confirmation == 'Y':
            print("\n\n---Thank you for visiting the COVID-19 Style Casino and Virtual Resort. We hope to see you again soon!---")
        elif confirmation == 'N':
            gameSelectionMenu()
        else:
            print("\n\nInvalid input. You have been returned to the game selection menu.\n")
            gameSelectionMenu()

#----------------Begin slot machine code block----------------------
def slotMachine():
    checkCardBalance()

    print("Slot Machine")
    print("Pull the lever to play and win up to $1000 dollars! Hit the jackpot by revealing three aliens. \n\n")

    print("First, place your bet.")
    symbolLibrary = ["Apple", "Ball", "Coin", "Stick", "Alien", "Jester"]

    while True:
        try:
            bet = int(input("How much would you like to bet: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    checkSlotBet(bet)
    writeBet(bet)

    position1 = random.sample(["Apple", "Ball", "Coin", "Stick", "Alien", "Jester"],1)
    position2 = random.sample(["Apple", "Ball", "Coin", "Stick", "Alien", "Jester"],1)
    position3 = random.sample(["Apple", "Ball", "Coin", "Stick", "Alien", "Jester"],1)

    spinPosition = [position1, position2, position3]
    print("\n",spinPosition,"\n")
    spin = onSpin(spinPosition)

def onSpin(spinPosition):
    position1 = spinPosition[0]
    position2 = spinPosition[1]
    position3 = spinPosition[2]

    if position1[0] == "Apple" and position2[0] == "Apple" and position3[0] == "Apple":
        print("You have won a whopping $50! Keep your streak of luck going.\n")
        writeWinnings(50)
        confirmSlot()

    elif position1[0] == "Coin" and position2[0] == "Coin" and position3[0] == "Coin":
        print("Someone just became 100 dollars richer. Want to make it $200? Play again.\n")
        writeWinnings(100)
        confirmSlot()

    elif position1[0] == "Alien" and position2[0] == "Alien" and position3[0] == "Alien":
        print("JACKPOT! JACKPOT! JACKPOT! You just won 1000 dollars! Dare to test your luck again?\n")
        writeWinnings(1000)
        confirmSlot()

    else:
        print("Not everyone is born to win. You can always keep trying, though.")
        confirmSlot()

def confirmSlot():
    confirmSlot = input("Would you like to play again?(Type Y for yes and N for no): ")

    if confirmSlot == 'Y':
        slotMachine()
    elif confirmSlot == 'N':
        gameSelectionMenu()
    else:
        print("Invalid input. You have been returned to the game selection menu.\n\n")
        gameSelectionMenu()


#Function to test if the bet will exceed the amount of money on the card
def checkSlotBet(bet):
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Check the bet
    while True:
        if bet > int(currentBalance):
            print("\nYou will exceed your balance if you bet this much.\n")
            slotMachine()
        if bet > 0:
            break
#----------------End slot machine code block----------------------


#----------------Begin blackjack code block----------------------

firstAceOne = 0
firstAceEleven = 0
secondAceOne = 0
secondAceEleven = 0

Jack = 10
Queen = 10
King = 10
Ace = 0
dealerAceOne = 1
dealerAceEleven = 11

possibleCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace]
possibleDealerCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, dealerAceOne, dealerAceEleven]

#Main code block to run blackjack game
def blackjackGame():
    checkCardBalance()

    userCard1 = 0
    userCard2 = 0
    cpuCard1 = 0
    cpuCard2 = 0
    userCardTotal = 0
    cpuCardTotal = 0

    print("\n\nBlackjack! Test your luck against our dealer and win big!")
    print("----------------------------------------------------------------------------")
    print("\n")

    while True:
        try:
            beginBlackjack = int(input("To begin, press 1 "))
        except ValueError:
            print("\nPlease press 1.")
            continue
        if beginBlackjack == 1:
            break
            blackjackGame()
        else:
            blackjackGame()

    while True:
        try:
            bet = int(input("How much would you like to bet (Minimum bet of 100): "))
        except ValueError:
            print("Invalid input.")
            continue
        if bet < 100:
            print("Your bet must be at least 100.")
            continue
        else:
            break

    checkBlackjackBet(bet)
    writeBet(bet)

    userCard1 = random.choice(possibleCards)
    checkFace1(userCard1)

    if userCard1 == Ace:
        userCard1 = checkCard1(userCard1)

    cpuCard1 = random.choice(possibleDealerCards)
    print("\nThe dealer has drawn their first card.")

    userCard2 = random.choice(possibleCards)
    checkFace2(userCard2)

    if userCard2 == Ace:
        userCard2 = checkCard2(userCard2)

    cpuCard2 = random.choice(possibleDealerCards)
    print("\nThe dealer has drawn their second card.")

    userCardTotal = userCard1 + userCard2
    cpuCardTotal = cpuCard1 + cpuCard2

    print("Your card total is",userCardTotal)

    newUserCardValue = random.choice(possibleCards)

    while True:
        newUserCard = input("\nWould you like another card? Yes or No: ")

        if newUserCard == 'Yes':
            userCardTotal = userCardTotal + newUserCardValue
            print("\n\nYour new card total is",userCardTotal)
            break
        elif newUserCard == 'No':
            print("\n\nYour card total is",userCardTotal)
            break
        else:
            print("You must type either Yes or No.")
            continue

    blackjackWins = 0

    if userCardTotal > 21:
        print("Bust! Better luck next time\n")
        playJackAgain()

    elif (userCard1 == 10 or userCard1 == Jack or userCard1 == Queen or userCard1 == King) and (userCard2 == secondAceEleven):
        blackjackWins = bet * 2.25
        print("Blackjack! You have won!\n")
        writeWinnings(blackjackWins)
        playJackAgain()

    elif (userCard2 == 10 or userCard2 == Jack or userCard2 == Queen or userCard2 == King) and (userCard1 == firstAceEleven):
        blackjackWins = bet * 2.25
        print("Blackjack! You have won!\n")
        writeWinnings(blackjackWins)
        playJackAgain()

    elif (cpuCard1 == 10 or cpuCard1 == Jack or cpuCard1 == Queen or cpuCard1 == King) and (cpuCard2 == dealerAceEleven):
        print("Blackjack! The dealer has won!\n")
        playJackAgain()

    elif (cpuCard2 == 10 or cpuCard2 == Jack or cpuCard2 == Queen or cpuCard2 == King) and (cpuCard1 == dealerAceEleven):
        print("Blackjack! the dealer has won!\n")
        playJackAgain()

    elif userCardTotal < cpuCardTotal:
        print("The dealer has won. Test your skills again.\n")
        playJackAgain()

    elif userCardTotal > cpuCardTotal:
        blackjackWins = bet * 2
        print("You have won. Continue your streak of luck!\n")
        writeWinnings(blackjackWins)
        playJackAgain()

    elif userCardTotal == cpuCardTotal:
        print("You and the dealer have the same hand. No winners this time!\n")
        playJackAgain()

#Check to see if the first user card is an ace and directs accordingly
def checkCard1(userCard1):
    aceValOne = 0

    while True:
        try:
            aceValOne = int(input("What value would you like the ace to have (1 or 11): "))
        except ValueError:
            print("You must type either 1 or 11.")
            continue
        else:
            break

    if aceValOne == 1:
        firstAceOne = aceValOne
        userCard1 = firstAceOne
        return userCard1

    if aceValOne == 11:
        firstAceEleven = aceValOne
        userCard1 = firstAceEleven
        return userCard1

    if aceValOne != 1 or 11:
        print("You must select either a 1 or 11.")
        checkCard1(userCard1)

#Check to see if the second user card is an ace and directs path accordingly
def checkCard2(userCard2):
    aceValTwo = 0

    while True:
        try:
            aceValTwo = int(input("What value would you like the ace to have (1 or 11): "))
        except ValueError:
            print("You must type either 1 or 11.")
            continue
        else:
            break

    if aceValTwo == 1:
        secondAceOne = aceValTwo
        userCard2 = secondAceOne
        return userCard2

    if aceValTwo == 11:
        secondAceEleven = aceValTwo
        userCard2 = secondAceEleven
        return userCard2

    if aceValTwo != 1 or 11:
        print("You must select either a 1 or 11.")
        checkCard2(userCard2)

#Check to see if first drawn user card is a face card
def checkFace1(userCard1):
    if userCard1 == possibleCards[9]:
        print("\n\nYour first card is a Jack.")
    elif userCard1 == possibleCards[10]:
        print("\n\nYour first card is a Queen.")
    elif userCard1 == possibleCards[11]:
        print("\n\nYour first card is a King.")
    elif userCard1 == possibleCards[12]:
        print("\n\nYour first card is an Ace.")
    else:
        print("\n\nYour first card is a",userCard1)

#Check to see if second drawn user card is a face card
def checkFace2(userCard2):
    if userCard2 == possibleCards[9]:
        print("\n\nYour second card is a Jack.")
    elif userCard2 == possibleCards[10]:
        print("\n\nYour second card is a Queen.")
    elif userCard2 == possibleCards[11]:
        print("\n\nYour second card is a King.")
    elif userCard2 == possibleCards[12]:
        print("\n\nYour second card is an Ace.")
    else:
        print("\n\nYour second card is a",userCard2)

#Check to see if user wishes to play Blackjack again and directs them accordingly
def playJackAgain():

    while True:
        try:
            playAgain = input("Would you like to play again? Type Y for yes and N for no: ")
        except ValueError:
            print("You must type either Y or N.")
            continue
        else:
            break

    if playAgain == 'Y':
        blackjackGame()
    elif playAgain == 'N':
        print("----------------------------------------------------------------------------")
        print("We hope to see you back again soon!\n\n")
        gameSelectionMenu()
    else:
        print("Invalid input. Try again.\n")
        playJackAgain()

#Function to verify the bet will not exceed the amount on card
def checkBlackjackBet(bet):
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Check the bet
    while True:
        if bet > int(currentBalance):
            print("\nYou will exceed your balance if you bet this much.\n")
            blackjackGame()
        if bet > 0:
            break

#----------------End Blackjack Code Block-------------------------


#----------------Begin Mouse Wheel Code Block------------------

betPosition = []
bets = 0
wheelPositions = list(range(1,80))

def mouseWheel():
    checkCardBalance()

    print("Mouse Wheel Game: This game is simple: wherever the mice go, the money goes as well!")
    print("----------------------------------------------------------------------------\n\n")

    print("Pick a position on the wheel 1 through 80. Each position you choose will cost you $5, but if you win, all money down will be doubled!\nChoose wisely!\n\n")

    betPositioning()

    bets = len(betPosition) * 5
    writeBet(bets)

    winningPosition = random.choice(wheelPositions)

    print("\nThe mouse has ran off into position",winningPosition,"\n\n")

    mouseWheelWins = len(betPosition) * 10

    if (winningPosition in betPosition):
        print("You have won! The mouse was very generous to you.\n")
        writeWinnings(mouseWheelWins)
    else:
        print("Darn! The mouse ran off to someone else. Maybe next time!\n\n")
        playMouseAgain()

#Confirm whether the user wishes to play the mouse wheel game again and directs them accordingly
def playMouseAgain():
    while True:
        try:
            playMouse = input("Would you like to play again? Type Y for yes and N for no: \n")
        except ValueError:
            print("You must type either Y or N.")
            continue
        else:
            break

    if playMouse == 'Y':
        mouseWheel()
    elif playMouse == 'N':
        print("----------------------------------------------------------------------------")
        print("We hope to see you back again soon!\n\n")
        gameSelectionMenu()
    else:
        print("Invalid input. Try again.\n")
        playMouseAgain()

#Take user input and create a list of bets to be used for the mouse wheel
def betPositioning():
    bets = 0

    print("Choose your betting positions. Once you are satisfied, type 0 to begin the game.\n\n")
    while True:
        try:
            bets = int(input("Where would you like to place your chips: "))

            if bets != 0 and bets <= 80:
                betPosition.append(bets)
                continue
            elif bets > 80:
                print("\nYou can only bet a number 1 through 80\n")
                continue
            elif bets == 0:
                break
                mouseWheel()
        except ValueError:
            print("\n\nYou must keep betting or type 0 to begin the game.\n\n")
            continue
        else:
            break
#--------------------End Mouse Wheel Code Block-------------------


#-------------------Cup Guessing Game--------------------------

def cups():
    checkCardBalance()

    print("In this game, there are three cups and you have to select which cup you believe has the ball underneath. This game is all or nothing so make every bet count.")
    print("-------------------------------------------------------\n\n")

    possibleCup = list(range(1,3))
    winningCup = random.choice(possibleCup)

    while True:
        try:
            bet = int(input("How much would you like to bet: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    checkCupsBet(bet)
    writeBet(bet)

    while True:
        try:
             choice = int(input("Choose a number 1 through 3 to pick a cup: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    cupWins = 0

    print("\n\n The winning cup was...cup " + str(winningCup) + "!")
    sleep(1)
    
    if choice == winningCup:
        cupWins = bet * 2
        writeWinnings(cupWins)
        print("You took the risk... and you won\n!")
        playCupsAgain()
    else:
        print("Don't take risks if you can't guess well..\n")
        playCupsAgain()
    
def checkCupsBet(bet):
    #Read file in to circumvent global scope
    outFile = open("balance.dat" , "r")

    readBalance = outFile.readlines()

    currentBalance = readBalance[0]

    outFile.close()

    #Check the bet
    while True:
        if bet > int(currentBalance):
            print("\nYou will exceed your balance if you bet this much.\n")
            cups()
        if bet > 0:
            break    

def playCupsAgain():
    while True:
        try:
            playCups = input("Would you like to play again? Type Y for yes and N for no: \n")
        except ValueError:
            print("You must type either Y or N.")
            continue
        else:
            break

    if playCups == 'Y':
        cups()
    elif playCups == 'N':
        print("----------------------------------------------------------------------------")
        print("We hope to see you back again soon!\n\n")
        gameSelectionMenu()
    else:
        print("Invalid input. Try again.\n")
        playCupsAgain()
        
main()




