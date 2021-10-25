import random

valeur ={"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Valet":11, "Dame":12, "Roi":13, "As":14}

couleur = ["Coeur", "Pique","Carreau","Trefle"]
a=0
b=0
c=0 
x = input ("Welcome to War ! What is your name ? ")
deck = []
valuelist = {}

def createdeck ():
        
    for c in couleur: 
        for k, v in valeur.items():
            valuelist[k +" de "+ c] = v
            deck.append(k +" de "+ c)
            random.shuffle(deck)
    return deck
    

def distributecard():
    
    global deck 
    playerdeck = deck[:26]
    computerdeck = deck[26:]
    return (playerdeck, computerdeck)


def draw(c):
    global a
    global b
    global x
    global valuelist
    playerdeck, computerdeck = distributecard()
    
    if c < 26 :
        input("Enter any key to play the next round ") 
        activePcard = playerdeck[c]  
        pv = valuelist[activePcard]
        activeCcard = computerdeck[c]
        cv = valuelist[activeCcard]
        print ("Vous avez tiré un {}, l' ordinateur a tiré un {} " .format(activePcard, activeCcard))
        if cv < pv:
            print ("You win this round !")
            playerdeck.pop(0)
            computerdeck.pop(0)
            a += 1
            return draw(c+1)
        elif cv > pv:
            print ("The computer win this round !")
            playerdeck.pop(0)
            computerdeck.pop(0)
            b += 1
            return draw(c+1)
        else :
            print ("It's a draw !")
            
            return draw(c+1)
    else: 
        if a < b:
            print ("Congratulations {} you won against the computer !".format(x))
        elif a > b :
            print ("Sorry {} you loose against the computer!".format(x))
        else :
            print ("No winner, the game was a draw !")


createdeck ()
distributecard()
draw(c)


