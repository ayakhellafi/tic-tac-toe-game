PlayBoard = {1: ' ' , 2: ' ' , 3: ' ',
            4: ' ' , 5: ' ' , 6: ' ' ,
            7: ' ' , 8: ' ' , 9: ' ' }
def printBoard(board):
    print(board[1] + '  |' + board[2] + '  |' + board[3])
    print('-----------')
    print(board[4] + '  |' + board[5] + '  |' + board[6])
    print('-----------')
    print(board[7] + '  |' + board[8] + '  |' + board[9])

def checkPlayBoard(board):
	# rows
    for x in range(1,4):
        row = set([board[x],board[x+3],board[x+6]])
        if len(row) == 1 and board[x] != ' ':
            return board[x]

	# columns
    for x in range(1,9,3):
        column= set([board[x],board[x+1],board[x+2]])
        if len(column) == 1 and board[x] != ' ':
             return board[x]


	# diagonals
    diag1 = set([board[1],board[5],board[9]])
    diag2 = set([board[3],board[5],board[7]])
    if (len(diag1) == 1 or len(diag2) == 1) and board[5] != ' ':
          return board[5]


    # No winner
    if all(v !=' ' for v in board.values()):
      return 'No Winner'


    return 0

turn = 'O'


while checkPlayBoard(PlayBoard)==0:
    printBoard(PlayBoard)
    print("It's your turn," + turn+"  "+ "Which place you want to move?")
    move =int(input())
    if PlayBoard[move] == ' ':
        PlayBoard[move] = turn
    else:
      print("That place has been filled.\n Which place you want to move?")
      continue
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'
else:
       if(checkPlayBoard(PlayBoard)!='No Winner'):
         print('The winner is:',checkPlayBoard(PlayBoard))
         print("\nGame Over.\n")
       else:
           print('No winner')