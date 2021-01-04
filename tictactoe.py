# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:00:10 2021

@author: ThatsDekuu
"""

#
    
class Player(object):
    def ReferenceHub(self, userId, syncVarNickname, userUniqId):
        self.userId = userId
        self.syncVarNickname = syncVarNickname
        self.userUniqId = userUniqId
    
    def GetUserId(self):
        return self.userId
    def GetSyncVarNickname(self):
        return self.syncVarNickname
    def GetUserUniqId(self):
        return self.userUniqId    
   
print('TicTacToe Python Version')
print('\nGiocatore 1')
    
userId_Player1 = input("Per iniziare scrivi il tuo nome: ")

while True:
    if len(userId_Player1) < 30:
        break
    for c in userId_Player1:
        if not c.isdigit():
            break
        else:
            print("Nome non valido\n")
            continue
    else:
        print("Nome non valido\n")
        continue
    
        
syncVarNickname_Player1 = input("Scegli il tuo Username: ")
if syncVarNickname_Player1.len > 16:
    lenghtCheck = True
    while lenghtCheck == True:
        try:
            syncVarNickname_Player1 = input("Scegli il tuo Username: ")
        except ValueError:
            print("Username troppo lungo. Non deve superare i 16 caratteri")
            continue
        else:
            break
userUniqId_Player1 = input("Inserisci la tua età: ")

print('\nGiocatore 2')
userId_Player2 = input("Per iniziare scrivi il tuo nome: ")
syncVarNickname_Player2 = input("Scegli il tuo Username: ")
userUniqId_Player2 = input("Inserisci la tua età: ")

Player1 = Player()
Player1 = Player.ReferenceHub(Player1, userId_Player1, syncVarNickname_Player1, userUniqId_Player1)



boardGame = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []
for key in boardGame:
    boardKeys.append(key)


def backgroundBoard(board):
    print(board['7'] + '  |' + board['8'] + ' |' + board['9'])
    print('----------')
    print(board['4'] + '  |' + board['5'] + ' |' + board['6'])
    print('----------')
    print(board['1'] + '  |' + board['2'] + ' |' + board['3'])
    
def game():
    playerTurn = 'X'
    playersTurnCounter = 0
    
    for i in range(10):
        backgroundBoard(boardGame)
        print(f"Tuo turno: {playerTurn}. Dove vuoi muovere?" )
        
        move = input()
        
        if boardGame[move] == ' ':
            boardGame[move] = playerTurn
            playersTurnCounter += 1
        else:
            print("Quel posto è già occupato\nDove vuoi muovere?")
            continue
        
        if playersTurnCounter >= 4:
            if boardGame['7'] == boardGame['8'] == boardGame['9'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            elif boardGame['4'] == boardGame['5'] == boardGame['6'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            elif boardGame['1'] == boardGame['2'] == boardGame['3'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            if boardGame['1'] == boardGame['4'] == boardGame['7'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            elif boardGame['2'] == boardGame['5'] == boardGame['8'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            elif boardGame['3'] == boardGame['6'] == boardGame['9'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            if boardGame['1'] == boardGame['5'] == boardGame['9'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            elif boardGame['7'] == boardGame['5'] == boardGame['3'] != ' ':
                backgroundBoard(boardGame)
                print("\nFine del gioco\n")
                print("\nHai vinto\n")
                break
            
            if playersTurnCounter == 9:
                print("\nFine del gioco\n")
                print("\nParità\n")
                
            if playerTurn == 'X':
                playerTurn = 'O'
            else:
                playerTurn = 'X'
                
            restartGame = input("Vuoi giocare ancora? S/N")
            if restartGame == 'S' or restartGame == 's':
                for key in boardKeys:
                    boardGame[key] = ' '                  
                game()
                
if __name__ == "__main__":
    game()                          


