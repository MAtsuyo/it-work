# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:00:10 2021

@author: ThatsDekuu, Matsuyo the Dragon Summoner
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

# Player 1 { get; set;}
print('\nGiocatore 1')    
userId_Player1 = input("Per iniziare scrivi il tuo nome: ")         
syncVarNickname_Player1 = input("Scegli il tuo Username: ")
userUniqId_Player1 = input("Come stai uwu?: ")

# Player 2 { get; set;}
print('\nGiocatore 2')
userId_Player2 = input("Per iniziare scrivi il tuo nome: ")
syncVarNickname_Player2 = input("Scegli il tuo Username: ")
userUniqId_Player2 = input("Come stai uwu?: ")

Player1 = Player()
Player1 = Player.ReferenceHub(Player1, userId_Player1, syncVarNickname_Player1, userUniqId_Player1)
Player2 = Player()
Player2 = Player.ReferenceHub(Player2, userId_Player2, syncVarNickname_Player2, userUniqId_Player2)


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []
for key in theBoard:
    boardKeys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turno = 'X'
    counter = 0
    
    for i in range(10):
        printBoard(theBoard)
        print("E' il tuo turno," + turno + ".Dove muoi muovere?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turno
            counter += 1
        else:
            print("Questo posto è già occupato! non fare la sanguisuga.\nDove vuoi muovere?")
            continue

        if counter >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # in alto
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # in mezzo
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # sul fondo
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # lungo il lato sinistro
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # nel mezzo
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # lungo il lato destro
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonale
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonale
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turno + " ha vinto. ****")
                break 

        if counter == 9:
            print("\nGame Over.\n")                
            print("E' un pareggio, peggio di Civil War!!")

        # Ora c'è da cambiare il turno ai giocatori.
        if turno =='X':
            turno = 'O'
        else:
            turno = 'X'        
    
    # Ora chiederemo al player se vuole ricominciare o meno.
    restartGame = input("Vuoi giocare ancora? (s/n)")
    if restartGame == 'S' or restartGame == 's':
        for key in boardKeys:
            theBoard[key] = " "                  
        game()
                
if __name__ == "__main__":
    game()                          



