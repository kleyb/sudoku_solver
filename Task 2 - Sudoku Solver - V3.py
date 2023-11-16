
import time
#Created by Kleybson Sousa

#Created a stack with a dictionary , this way I can record both values ( Move number and locations)
class Moves:
    #Creater a constructor 
    def __init__(self):
        self.moves = {}
    #Creates a string representation of the object
    def __str__(self):
        return str(self.moves)
    
    #Checks weather the stack is empty
    def is_empty(self):
        #returns a boolean 
        return self.moves == {}
    
    #Records the move by pushing it into the stack
    def push(self,moveNum,row,col):
        #Uses moveNum as a key , row and col as its values
        self.moves[moveNum] = row,col
        #Increments the counter (moveNum) by 1 
        counter()
    
    #Removes the last item of the stack
    def pop(self):
        #Uses the popitem function which removes the last entry into the dictionary
        self.moves.popitem()

    def peek(self):
        #Get the last key entry into the dictionary by reversing it's order and getting the first key
        key = next(reversed(self.moves.keys()))
        #returns the values of the postion of keys
        return self.moves[key]

#Sudoku class is where the board and its operations , such as update and display are located
class Sudoku:
    #Creates a list constructor 
    def __init__(self):
        self.box = []
    #String representantion of the object
    def __str__(self):
        return str(self.box)
    
    # Creates the board of the game
    def boxCreation(self,newboard):
        # Assigns into the object the board that is given 
        self.box = newboard
        #returns it 
        return self.box

    #Prints the board into the screen
    def print_board(self):
        #Create a temporary new 2d list 
        newbox = [[],[],[],[],[],[],[],[],[]]
        #Goes through the rows
        for i in range(len(self.box)):
            #Iterate through every item in the row
            for b in range(len(self.box[i])):
                # if it finds a 'x' , a empty space will be appended 
                if self.box[b][i] == "x":
                    newbox[b].append(" ")
                # else if its not a 'x' , it appends whatever value is found
                elif self.box[b][i] != "x":
                    newbox[b].append(self.box[b][i])                           
        # Iterates through the rows           
        for row in newbox:
            # Prints every item in the row , with 2 spaces between them. it repeates this process by the number of rows
            print("[ {: >2} {: >2} {: >2} | {: >2} {: >2} {: >2} | {: >2} {: >2} {: >2} ] ".format(*row))
            print("----------------------------------")
    
    #Updates the board
    def update_board(self, row, col, newValue):
        #Uses the global stack record
        global record
        #if the new value is an int , it records it 
        if type(newValue) == int:
            record.push(moveNum,row,col)
        # Assign a new value into the corresponding position
        self.box[row][col] = newValue
        
    #Finds an empty space in board
    def findEmpty(self):
        # Goes through every row
        for i in range(len(self.box)):
            #iterates through each item in the row
            for b in range(len(self.box[i])):
                #if equals to 'x' , returns the location
                if self.box[i][b] == "x":
                    return i , b
        #if there is no empty space ('x') returns None            
        return None
    
    #Checks weather the guess is valid or not, if not it returns false
    def is_valid(self,guess,row,col):
        #Check if guess in valid on the corresponding row 
        if guess in self.box[row]:
            return False
        #check if the guess is valid on the corresponding column
        for i in range(len(self.box)):
            if self.box[i][col] == guess:
                return False
        # This is important to check the right 3x3 Box , an integer division 
        #it works by dividing the first 3 indexes location by 3 , 0 - 2 divided by 3 will be 0 ,
        #  3 - 5 // 3 = 1 , 6-8 // 3 = 2, this allow to identify the first 3 locations of the rows and colomns as they all the same lengh

        rowStart = ( row // 3 ) * 3 # 0 // 3 * 3 = 0 , 5 // 3 = 1 * 3 = 3 , 7 // 3 = 2 * 3 = 6
        colStart = ( col // 3 ) * 3
        # Essencially creates a 3x3 range to be checked , when row start is equal to 0 , it must end on 3  
        for b in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                # if location b , j  example ( 0,2) contains the value guessed , it returns False , meaning its not a valid location 
                if self.box[b][j] == guess:
                    return False
        # If the value is not found on any of the relevant Row , columns and 3x3 Box , it returns True ; its a valid Value
        return True

    #Create a list of possible numbers that can entered into a specific place
    def avaliableNum(self,is_valid,findEmpty):
        #Creater a helper list
        avaliable = []
        #Find next empty space and get the locations
        row,col = findEmpty()
        #Tries every number from 1 to 9
        for i in range(1,10):
            #if that number is valid then append into the list
            if is_valid(i,row,col):
                avaliable.append(i)
        #if no number from 0 to 9 is possible into that position then it returns 'None'        
        if avaliable == []:
            return None
        #Return the list 
        return avaliable


def counter():
    #Uses the moveNum variable
    global moveNum
    #Increaments the variable by 1
    moveNum += 1

# This function is essentially where game happens for the user      
def human_play():
    #call of the global sudoku board
    global box
    #While there is empty spaces in the board 
    #if there is no empty spaces , it means that the sudoku has been solved
    while (box.findEmpty() != None):
        #display the status of the game
        gameStatus() 
        #Display the board
        box.print_board()
        #If avaliableNum returns None , it means that there is an empty space but there is no possible number that can go into that specific position 
        # that means that this game is unsolvable , the player has failed the game
        if box.avaliableNum(box.is_valid,box.findEmpty) == None :           
            break
        # Get the next empty locations and assign them into row and col
        row,col = box.findEmpty()
        #Takes the player guess , then it tries to convert it into an 'int' using the intTryParse function      
        # if inTryParse is not successful to convert the guess , it then returns the value that was used
        guess = intTryParse(input("The next empty position is at Row {0}, Column {1} , Please enter a number between 1 to 9, Enter B to reset the last guess or Enter 'H' for help: ".format(row,col)))
        #if the conversion is successful then guess will become and int
        if type(guess) == int:
            #Check if the guess is valid using the is_valid function of box and if the guess is between 1-9
            if box.is_valid(guess,row,col) and guess > 0 and guess < 10:
                #if valid , updates the board with the guess and records it 
                box.update_board(row, col, guess)               
            else:
                #If the guess is not valid or between 1-9 then it is not valid , prints this message to the user
                print("The number you have entered cannot be placed at this postion")
        #if the value is equal H , it means that the user needs a hint , a help from the game
        elif guess.upper() == "H":
            # Print a list of avaliable numbers that can be entered into the corresponding position 
            print("The following number(s) {0} are avaliable for the position {1} {2}".format(box.avaliableNum(box.is_valid,box.findEmpty),row,col))
            
        #if the user Enters B then he wants to reset the last guess 
        #if guess is equal to B and record stack is not empty then it perfomrs the reset
        elif guess.upper() == "B" and record.is_empty() == False:
            
            #gets from the stack the position of the last guess
            recordedRow,recordedCol = record.peek()
            #Uses a loop to confirm the change
            while True:
                #Tries to convert the user's choice  into a int
                choice2 = intTryParse(input("Please enter 1 to confirm you would like to reset the last guess, 2 to cancel: "))
                # if the user enters 1 , the user confirms the change
                if choice2 == 1:
                    # Updates the board with the value of 'x', taking the Row and Column from the stack
                    box.update_board(recordedRow,recordedCol,"x")
                    print("The guess placed at position {0} {1} has been reset ".format(recordedRow,recordedCol))
                    # Removes the last entry to the stack
                    record.pop()
                    #breaks the loop and goes back into the game
                    break
                #if the user enters 2 , then the move to reset is cancelled
                elif choice2 == 2:
                    print("The change has been cancelled")
                    # breaks the look and returns to the game
                    break
                #if the user enters anything else except 1 or 2 , then he entered a invalid value 
                else:
                    print("You have entered a invalid value ")
              
        else:
            #if the user did not enter a valid value or entered B in his first move , then an error message will be displayed
            #as there is no move to be reset
            print("You have entered a invalid value or selected B on your first move")
                 
    #Display the board
    box.print_board()
    #states the status of the game
    gameStatus()

def gameStatus():
    global box
    #if there is not empty space , it means that the sudoku has been solved
    if box.findEmpty() == None:
            print("Congratulations you have solved the SUDOKU! ")
    #if there are no possible numbers to be placed in a empty space, it means the puzzle is unsolvable
    elif box.avaliableNum(box.is_valid,box.findEmpty) == None :
        print("This puzzle has no avaliable solutions ")
        print("'You have failed me for the last time , Admiral!' ")
    else:
        #The only other possible status is that the game is still being played , there is no outcome yet
        print("No outcome, play continues")
        
       
# This fuction tries to parse a value into a int            
def intTryParse(value):

    try:
        #if it can be converted into a int , it converts and returns the value converted 
        return int(value)
        #if not possible to convert , returns the original value
    except ValueError:
        return value

#This function of the game uses recursion and backtracking to solve the puzzle
def computer_play():
    global box
    #if there are no empty spaces then it retruns True
    if box.findEmpty() == None :
        return  True
    #find the next empty space and assign them into row and col        
    row,col = box.findEmpty()
    # uses a loop to try a guess between 1-9
    for guess in range(1,10):
        #if guess is a valid number then updates the board with it and records it
        if box.is_valid(guess,row,col) :              
            #Places the guess and records it 
            box.update_board(row,col,guess)
            # Uses recursion to call this function from inside 
            # the recursive function will perfom this check and will keep calling itself 
            # until either there are not valid guesses or empty positon
            # if there is no empty space then the if statment below will be executed , as it will be true 
            if computer_play():
                #Returns true , a flag which breaks the recursive function
                return True   
            #when there are no empty numbers the function when called above will go through the loop , try all possible combinations ,
            # and at the end it will return to the previous step , it is at this point that the below function will be called
            #if there are no valid guesses , then it enters 'x' and back tracks  
            box.update_board(row,col,"x")

#The copy function is used only to copy effectively the board ( or 2d lists) in its entirety 
def copy(board):
    #Creates a new list
    boardCopy = []
    #for every list in board
    for i in board:
        #Append a copy of i
        boardCopy.append(i.copy())
    #Return the new copied list
    return boardCopy

#The board of the game , which remains unchanged during the game
board = [[8,'x','x','x','x','x','x','x','x'],
			['x','x',3,6,'x','x','x','x','x'],
			['x',7,'x','x',9,'x',2,'x','x'],
			['x',5,'x','x','x',7,'x','x','x'],
			['x','x','x','x',4,5,7,'x','x'],
			['x','x','x',1,'x','x','x',3,'x'],
			['x','x',1,'x','x','x','x',6,8],
			['x','x',8,5,'x','x','x',1,'x'],
			['x',9,'x','x','x','x',4,'x','x']
			]           
#Helper variable to start the game and give an option at the end 
playChoice = "1"

print("--------------------- Welcome to SUDOKU ---------------------")
#While playChoice = 1 , the game is executed
while playChoice == "1":
    #Copies the board of the game
    boardCopy = copy(board)
    #Declares moveNum as 0 at the begining of the game 
    moveNum = 0
    #Creater a new instance of the Moves object 
    record = Moves()
    #Creating of the game board
    box = Sudoku()
    #Gives a board to the box instance of the sudoku class
    box.boxCreation(boardCopy)
    #Display the board
    box.print_board()

    while True:
        #Asks the user in which mode the game is to be played   
        choice = intTryParse(input(" Please enter 1 to play the game or 2 to use our AI to solve the Soduko: "))
        # if the user chooses 1 or 2 , then it breaks the loop
        if choice == 1 or choice == 2:
            break
        else:
        #if the user enters anything else , the it is an invalid number/value
            print("Invalid number/value ")        
    #if the user entered 1 , then he selected to play the game    
    if choice == 1:
        #start the timer, this specific time module ( process_time) counts only the time the CPU is being used
        startTimer = time.process_time()
        #Starts the Human_play 
        human_play()
        #End timer
        endTimer = time.process_time()
        #Print the number of moves on this game and the time the CPU was used 
        print("This game took {0} moves and {1} second(s) of CPU processing time to be completed ".format(moveNum,endTimer-startTimer))
        
    #if the user entered 2 , he selected the AI to the play the game         
    elif choice == 2:
        #starts the CPU timer
        startTimer = time.process_time()
        #Starts the computer_play
        computer_play()
        #End CPU timer
        endTimer = time.process_time()
        #Print the number of moves the AI took and the CPU time that was used
        print("The puzzle has been solved, The AI took {0} moves and {1} second(s) of CPU time to solve this puzzle".format(moveNum,endTimer-startTimer))
        box.print_board()
    #Asks if the user wants to keep playing the game , if he enters 1 , a new game is started
    playChoice = input("Please enter 1 to play again or anything else to exit the game: ")
#if the user enters anything else , then the game is closed
raise SystemExit