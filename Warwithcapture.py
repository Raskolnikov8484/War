import random
import sys
sys.setrecursionlimit(3000)

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
    

def distributecard(d):
    global playerdeck
    global computerdeck
    playerdeck = d[:26]
    computerdeck = d[26:]
  

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
    
    return compare()

def compare():
    global a
    a += 1
    global stock
    global playerdeck
    global computerdeck
    global valuelist
    playercard = stock[-2]
    computercard = stock[-1]
    Vp = valuelist[playercard]
    Vc = valuelist[computercard]
    print ("You draw a {}, the computer draw a {}".format(playercard,computercard))
   
   
    
    if Vp > Vc :
        playerdeck = playerdeck + stock
        return win()
    elif Vc > Vp :
        computerdeck = computerdeck + stock
        return loose()
    else :
        stock = playerdeck[:5] + computerdeck[:5]
        
        playerdeck = playerdeck[5:]
        computerdeck = computerdeck[5:] 
        print ("Bataille !")
        return createstock()

def win ():
    global stock
    print ("You win this round")
    stock.clear()
    if len(computerdeck) >= 6:
        return createstock()
    else :
        print ("Congratulation ! You win the game of war !")

def loose():
    global stock
    stock.clear()
    print("you loose this round")
    if len(playerdeck) >= 6:
        return createstock()
    else :
        print ("No luck ! You loose War this time !")         
    
createdeck()
distributecard(deck)
createstock()
