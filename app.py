import random 
""" introducción a este desafío, el ganador del juego
estará determinado por tres reglas simples:

La Rock gana a las tijeras.
Las Scissors ganan al papel.
El Paper gana a la piedra.
"""

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    else:
        return None
    
if __name__ == '__main__':
    print("Comp Turn: Rock(r) Paper(p) or Scissors(s)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 'r'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 's'

    you = input()
    print(f"Computer chose {comp}")
    a = gameWin(comp, you)

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
        
    