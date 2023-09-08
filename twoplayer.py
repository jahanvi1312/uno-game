import random
import tkinter.messagebox as tmsg
from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

ws = Tk()
ws.state('zoomed')
ws.title('2 PLAYER - UNO GAME')
ws.geometry("1550x850")
ws.resizable(height=None, width=None)


can_widght = Canvas(ws, width=1550, height=850)
can_widght.pack()
can_widght.create_oval(556, 190, 976, 610, fill='#bf4040', width=5)

l5 = Label(ws, text="Player 1", font="georgia 25 bold", fg="blue").place(x=690, y=640)
l6 = Label(ws, text="Player 2", font="georgia 25 bold", fg="blue").place(x=690, y=125)
l7 = Label(ws, text="UNO DECK", font="georgia 16 bold", fg="blue").place(x=55, y=659)
Button(ws, text="Exit", font="georgia 14 bold", padx=30, borderwidth=5, bg="red", fg="white",
       activebackground="red", activeforeground="white", command=quit).place(x=1400, y=8)
sec = StringVar()
Entry(ws, textvariable=sec, width=2, font='Helvetica 14', bg="black", fg="white").place(x=220, y=120)
sec.set('17')
Label(ws, text="Timer", font="georgia 25 bold", fg="blue").place(x=180, y=175)
can_widght.create_oval(195, 95, 270, 170, fill="black", width=2, outline="red")


def click(event):
    global l5
    global playerTurn
    global playDirection
    global currentColour
    global cardVal
    global photos3
    global photos4
    global players
    global discards

    cardChosen = event.widget.cget("text")
    print(f"Which card do u want to play ? : {cardChosen}")
    print("")
    if canPlay(currentColour, cardVal, [players[playerTurn][cardChosen - 1]]):
        print("You played {}".format(players[playerTurn][cardChosen - 1]))
        print("")
        var5 = players[playerTurn][cardChosen - 1]
        players[playerTurn].pop(cardChosen - 1)
        discards.append(var5)
        print("card on top of discard pile: {}".format(discards[-1]))
        print("")
        var3 = discards[-1]
        img2 = Image.open(f"images/{var3}.png")
        img2 = img2.resize((200, 300), Image.ANTIALIAS)
        photos3.append(ImageTk.PhotoImage(img2))
        l5.configure(image=photos3[-1])
        if len(players[playerTurn]) == 0:
            # ac = tmsg.showinfo("Instruction", f"Player {playerTurn + 1} is Winner")
            if playerTurn == 1:
                ws.destroy()
                import player2win
            else:
                ws.destroy()
                import player1win
        else:
            splitCard = discards[-1].split('_', 1)
            currentColour = splitCard[0]
            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]
            if currentColour == "wild":
                print("")
                currentColour = simpledialog.askstring(title="Enter Color Name", prompt="Enter Colour which You Want :")
            if cardVal == "reverse":
                playerTurn = playerTurn
            elif cardVal == "skip":
                playerTurn = playerTurn
            elif cardVal == "drawtwo":
                playerTurn = playerTurn + 1
                if playerTurn >= numPlayers:
                    playerTurn = 0
                players[playerTurn].extend(drawCards(2))
                playerTurn = playerTurn + 1
                if playerTurn >= numPlayers:
                    playerTurn = 0
            elif cardVal == "drawfour":
                playerTurn = playerTurn + 1
                if playerTurn >= numPlayers:
                    playerTurn = 0
                players[playerTurn].extend(drawCards(4))
                playerTurn = playerTurn + 1
                if playerTurn >= numPlayers:
                    playerTurn = 0
            else:
                playerTurn = playerTurn + 1
                if playerTurn >= numPlayers:
                    playerTurn = 0
            print("")
    else:
        print("You played {}".format(players[playerTurn][cardChosen - 1]))
        print("Not a Valid Card!, Please enter Another Card : ")
        ac = tmsg.showinfo("Instruction", "You can,t play this Card! Please Choose Another Card.")

    ws.update()
    # showHands(playerTurn, players[playerTurn])
    display()
    # print("card on top of discard pile: {}".format(discards[-1]))
    print("")


def draw():
    global playerTurn
    global photos4
    aa = tmsg.showinfo("Instruction", "You have to draw a card")
    players[playerTurn].extend(drawCards(1))
    if canPlay(currentColour, cardVal, players[playerTurn]):
        display()
    else:
        playerTurn = playerTurn + 1
        if playerTurn >= numPlayers:
            playerTurn = 0
        display()


def BuildDeck():
    deck = []
    colours = ["red", "green", "yellow", "blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "drawtwo", "skip", "reverse"]
    wilds = ['wild_change', 'wild_drawfour']
    for colour in colours:
        for value in values:
            cardValue = "{}_{}".format(colour, value)
            deck.append(cardValue)
            if value != 0:
                deck.append(cardValue)

    for i in range(4):
        deck.append(wilds[0])
    for i in range(4):
        deck.append(wilds[1])
    return deck


def halfShuffleDeck(deck):
    firstHalf = []
    secondHalf = []

    for i in range(len(deck)):
        if i < int(((len(deck)) / 2)):
            firstHalf.append(deck[i])
        else:
            secondHalf.append(deck[i])

    shuffleDeckbyHalf = []
    halflength = int((len(deck)) / 2)

    for i in range(halflength):
        shuffleDeckbyHalf.append(secondHalf[i])
        shuffleDeckbyHalf.append(firstHalf[i])
    if len(firstHalf) != len(secondHalf):
        shuffleDeckbyHalf.append(secondHalf[len(secondHalf) - 1])

    return shuffleDeckbyHalf


def randomShuffleDeck(deck):
    randomlyShuffleDeck = deck
    for cardPosition in range(len(randomlyShuffleDeck)):
        randomPosition = random.randint(0, 107)
        randomlyShuffleDeck[randomPosition], randomlyShuffleDeck[cardPosition] = \
            randomlyShuffleDeck[cardPosition], randomlyShuffleDeck[randomPosition]
    return randomlyShuffleDeck


def ultimateShuffledeck(deck):
    usd = halfShuffleDeck(randomShuffleDeck(deck))
    return usd


freshUnoDeck = BuildDeck()
UnoDeck = BuildDeck()
halfshuffleUnoDeck = halfShuffleDeck(UnoDeck)
randomshuffleUnoDeck = randomShuffleDeck(UnoDeck)
ultimateShuffleUnodeck = ultimateShuffledeck(UnoDeck)
print(UnoDeck)
print("")


def drawCards(numCards):
    cardsDrawn = []

    for x in range(numCards):
        cardsDrawn.append(UnoDeck.pop(0))
    return cardsDrawn


def showHands(player, plyerHand):
    print("")
    print("     player {}".format(player + 1))
    print("")
    print("your hand")
    print("---------------------------")
    y = 1
    for card in plyerHand:
        print("{}) {}".format(y, card))
        y += 1
    print("")


def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


discards = []
colours = ["red", "green", "yellow", "blue"]
players = []
numPlayers = 2
for player in range(numPlayers):
    players.append(drawCards(7))
print(players)
print("")

playerTurn = 0
playDirection = 1
discards.append(UnoDeck.pop(0))
splitCard = discards[-1].split('_', 1)
currentColour = splitCard[0]
cardVal = splitCard[1]


def check():
    global cardVal
    global currentColour
    # global UnoDeck
    # global discards
    global splitCard
    if currentColour != "wild":
        cardVal = splitCard[1]
    else:
        discards.pop(0)
        discards.append(UnoDeck.pop(0))
        splitCard = discards[-1].split('_', 1)
        currentColour = splitCard[0]
        cardVal = splitCard[1]
        check()


check()
photos3 = []
photos4 = []


def display():
    global l5
    global playerTurn
    global playDirection
    global currentColour
    global cardVal
    global photos1
    global photos2
    global photos3
    global photos4
    global players
    global discards
    photos1 = []
    photos2 = []
    if playerTurn == 0:
        for i in range(len(players[0])):
            var = players[0][i]
            image = Image.open(f"images/{var}.png")
            image = image.resize((74, 100), Image.ANTIALIAS)
            photos1.append(ImageTk.PhotoImage(image))

        ab = len(players[0])
        a = (1534 - (74 * ab + 3 * (ab - 1))) / 2
        for i in range(len(players[0])):
            b = 700
            btn = Button(ws, text=i + 1, image=photos1[i], borderwidth=0)
            btn.place(x=a, y=b)
            a = a + 77
    else:
        for i in range(len(players[0])):
            image = Image.open("images/back.png")
            image = image.resize((74, 100), Image.ANTIALIAS)
            photos1.append(ImageTk.PhotoImage(image))

        ab = len(players[0])
        a = (1534 - (30 * ab + 44)) / 2
        for i in range(len(players[0])):
            b = 700
            l1 = Label(ws, text=i + 1, image=photos1[i], borderwidth=0)
            l1.place(x=a, y=b)
            a = a + 30

    if playerTurn == 1:
        for i in range(len(players[playerTurn])):
            var = players[playerTurn][i]
            image = Image.open(f"images/{var}.png")
            image = image.resize((74, 100), Image.ANTIALIAS)
            photos2.append(ImageTk.PhotoImage(image))

        ab = len(players[playerTurn])
        a = (1534 - (74 * ab + 3 * (ab - 1))) / 2
        for i in range(len(players[playerTurn])):
            b = 10
            btn = Button(ws, text=i + 1, image=photos2[i], borderwidth=0)
            btn.place(x=a, y=b)
            a = a + 77
    else:
        for i in range(len(players[1])):
            image = Image.open("images/back.png")
            image = image.resize((74, 100), Image.ANTIALIAS)
            photos2.append(ImageTk.PhotoImage(image))

        ab = len(players[1])
        a = (1534 - (30 * ab + 44)) / 2
        for i in range(len(players[1])):
            b = 10
            l2 = Label(ws, text=i + 1, image=photos2[i], borderwidth=0)
            l2.place(x=a, y=b)
            a = a + 30

    var2 = discards[-1]
    discard = Image.open(f"images/{var2}.png")
    discard = discard.resize((200, 300), Image.ANTIALIAS)
    photos3.append(ImageTk.PhotoImage(discard))
    l5 = Label(ws, image=photos3[-1])
    l5.place(x=666, y=249)
    # label = Label(ws, text=f"Color on Discard Pile is : {currentColour}").place(x=600, y=)

    re_deck = Image.open("images/back.png")
    re_deck = re_deck.resize((140, 200), Image.ANTIALIAS)
    photos4.append(ImageTk.PhotoImage(re_deck))
    Label(ws, image=photos4[0]).place(x=50, y=450)

    showHands(playerTurn, players[playerTurn])
    print("card on top of discard pile: {}".format(discards[-1]))

    if canPlay(currentColour, cardVal, players[playerTurn]):
        if playerTurn == 0:
            ab = len(players[playerTurn])
            a = (1534 - (74 * ab + 3 * (ab - 1))) / 2
            for i in range(len(players[playerTurn])):
                b = 700
                btn = Button(ws, text=i + 1, image=photos1[i], borderwidth=0)
                btn.place(x=a, y=b)
                btn.bind("<Button-1>", click)
                a = a + 77

        else:
            ab = len(players[playerTurn])
            a = (1534 - (74 * ab + 3 * (ab - 1))) / 2
            for i in range(len(players[playerTurn])):
                b = 10
                btn = Button(ws, text=i + 1, image=photos2[i], borderwidth=0)
                btn.place(x=a, y=b)
                btn.bind("<Button-1>", click)
                a = a + 77
    else:
        draw()


display()
ws.mainloop()
