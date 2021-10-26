import random

valeur ={"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Valet":11, "Dame":12, "Roi":13, "As":14}

couleur = ["Coeur", "Pique","Carreau","Trefle"]
deck = []
playerdeck = []
computerdeck = []
stock =[]
valuelist = {}
a = 0

def createdeck ():  
    global valuelist
    for c in couleur: 
        for k, v in valeur.items():
            valuelist[k +" de "+ c] = v
            deck.append(k +" de "+ c)
                 
    random.shuffle(deck)

def distributecard():
    global playerdeck
    global computerdeck
    global deck
    while len(deck) > 0:
        playerdeck.append(deck[0])
        computerdeck.append(deck[1])
        deck = deck[2:]
    

def createstock():
    global stock
    global playerdeck
    global computerdeck
    pC = playerdeck[0]
    cC = computerdeck[0]
    stock.append(pC)
    stock.append(cC)
    playerdeck.pop(0)
    computerdeck.pop(0)
    
def compare():
    global stock
    global playerdeck
    global computerdeck
    global valuelist
    global a
    a += 1
    playercard = stock[-2]
    computercard = stock[-1]
    Vp = valuelist[playercard]
    Vc = valuelist[computercard]
    print ("round "+  str(a)) 
    print ("You draw a {}, the computer draw a {}".format(playercard,computercard) + " you have {} cards".format(len(playerdeck)))
    if Vp > Vc :
        playerdeck = playerdeck + stock
        print ("You win this round")
        stock.clear()
        
    elif Vc > Vp :
        computerdeck = computerdeck + stock
        print("you loose this round")
        stock.clear()
    elif Vp == Vc and len(computerdeck) > 2 and len(playerdeck) > 2 :
        stock = stock + playerdeck[:2] + computerdeck[:2]
        playerdeck = playerdeck[2:]
        computerdeck = computerdeck[2:] 
        print ("Bataille !")
    elif Vp == Vc and len(computerdeck) < 2 :
        computerdeck.clear()
    elif Vp == Vc and len(playerdeck) < 2 :
        playerdeck.clear()
       
        
def game():
    global computerdeck
    global playerdeck
    global a
     
    while len(computerdeck) > 0 and len(playerdeck) > 0:
        createstock()
        compare()
        if len(computerdeck) == 0 and len(playerdeck) >= 1 :
            print ("You win the game of WAR !")
        elif len(playerdeck) == 0 and len(computerdeck) >= 1  :
            print ("You loose the game of WAR !")
        
        
createdeck()
distributecard()
game()
