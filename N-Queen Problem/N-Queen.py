n = int(input("Enter the value of n: ")) # Gets the value of N from the user
board = [] # Represent the Chess Board

'''Use to define the board that is to be used for the N-Queen Problem'''
def Board():
    for i in range(n):
        nthList = []
        for j in range(n):
            nthList.append(0)
        board.append(nthList)

'''Prints the board after solving the N-Queen Problem to check the solution'''
def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print("")
 
'''Checks if the Queen is safe from row and column. It returns true if the Queen is safe, else it returns false'''       
def isSafe(row, col):
    
    '''Determines if there is a Queen at correspoding row'''
    for i in range(n):
        if board[row][i] == 1:
            return False
        
    '''Determines if there is a Queen at correspoding row'''    
    for j in range(n):
        if board[j][col] == 1:
            return False
   
    '''Determines if the Queen is positioned in any diagonal direction'''   
    '''Checks if the Queen appears at NW direction'''  
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j-1

    '''Checks if the Queen appears at NE direction'''  
    i = row-1
    j = col+1
    while(i>=0 and j<n):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j+1

    '''Checks if the Queen appears at SW direction'''  
    i = row+1
    j = col-1
    while(i<n and j>=0):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j-1

    '''Checks if the Queen appears at SE direction'''  
    i = row+1
    j = col+1
    while(i<n and j<n):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j+1
    return True

def main(n, count):
    if count == n:
        return True
    
    for i in range(n):
        for j in range(n):
            
            if isSafe(i, j):
                board[i][j] = 1
                count = count+1
                
                if main(n, count) == True:
                    return True
                board[i][j] = 0
                count = count-1
    return False

Board()
main(n, 0)
printBoard()









                   
            