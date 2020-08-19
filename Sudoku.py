import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class App(QtWidgets.QMainWindow):

    def __init__(self, board):
        super().__init__()
        self.left = 560
        self.top = 140
        self.width = 800
        self.height = 800
        self.board = list(board)
        self.mapToTextGrid = [[] for x in range(len(board))]
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Sudoku using PyQt5 by Bruno Thuma')
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        self.textGrid()
        self.fillInitialValues()

        self.draw()

    def verTxtBoxRow(self, textBox):
        n = -1
        for row in self.mapToTextGrid:
            if textBox in row:
                n = mapToTextGrid.index(row)
                break

        if n == -1:
            return "textBox not found on textGrid"
        # If there are any 0's return message of empty tile
        if not all(self.board[n]):
            return "row still got empty places"
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(self.board[n]) > len(set(self.board[n])):
            return "duplicated values in row"
        return "OK"
    
    def verTxtBoxCol(self, textBox):
        n = -1
        for row in self.mapToTextGrid:
            if textBox in row:
                n = row.index(textBox)
                break

        if n == -1:
            return "textBox not found on textGrid"
        temp = [i[position] for i in self.board]
        # If there are any 0's return message of empty tile
        if not all(temp):
            return "Col still got empty places"
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(temp) > len(set(temp)):
            return "Repeated values on col"
        return "Ok"

    def verTxtBoxSquare(self, textBox):
        xPos = -1
        for row in self.mapToTextGrid:
            if textBox in row:
                xPos = row.index(textBox)
                yPos = self.mapToTextGrid.index(row)
                break

        if xPos == -1:
            return "textBox not found on textGrid"
        temp = [
            self.board[row + (yPos - yPos%3)][col + (xPos - xPos%3)]
            for row in range(3)
            for col in range(3)
        ]
        print(temp)
        # If there are any 0's return message of empty tile
        if not all(temp):
            return False
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(temp) > len(set(temp)):
            return False
        return True
    
    def verPosRow(self, position):
        temp = self.board[position]
        print("Row ", temp)
        while 0 in temp:
            temp.remove(0)
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(temp) > len(set(temp)):
            return False
        return True
    
    def verPosCol(self, position):
        temp = [i[position] for i in self.board]
        print("Col ",temp)
        while 0 in temp:
            temp.remove(0)
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        while 0 in temp:
            temp.remove(0)
        if len(temp) > len(set(temp)):
            return False
        return True

    def verPosSquare(self, xPos, yPos):
        temp = [
            self.board[row + (yPos - yPos%3)][col + (xPos - xPos%3)]
            for row in range(3)
            for col in range(3)
        ]
        print("Square ",temp)
        while 0 in temp:
            temp.remove(0)
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(temp) > len(set(temp)):
            return False
        return True

    # Fill the textBoxes of the window 
    # with the values on the self.board matrix
    def fillValues(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                value = self.board[row][col]
                if value != 0:
                    self.mapToTextGrid[row][col].setText(str(value))
        self.draw()
        return

    # Same as self.fillValues() but set the non-0 tiles as read-only
    def fillInitialValues(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                value = self.board[row][col]
                if value != 0:
                    self.mapToTextGrid[row][col].setText(str(value))
                    self.mapToTextGrid[row][col].setReadOnly(True)
        self.draw()
        print("len(self.board) ", len(self.board))
        print("len(self.mapToTextGrid) ", len(self.mapToTextGrid))
        print("initialValues OK")
        return
    
    def readTextGrid(self):
        result = []
        for row in range(len(self.mapToTextGrid)):
            result.append([])
            for col in range(len(self.mapToTextGrid)):
                textBox = self.mapToTextGrid[row][col]
                if textBox.text() != '':
                    result[row].append(int(textBox.text()))
                else:
                    result[row].append(0)
        if len(result) < 9 or len(result[0]) < 9:
            print("error reading GUI")
        return result


    def textGrid(self):
        ymodifier = 0
        # For each row in the map
        for row in range(len(self.board)):
            xmodifier = 0
            
            # If we already filled 3 rows increase
            # ymodifier so we have some space
            if row%3 == 0 and row != 0:
                ymodifier += 5

            # For each col in each row
            for col in range(len(self.board)):

                # If we already filled 3 squares
                # increase xmodifier so we have some space
                if col%3 == 0 and col != 0:
                    xmodifier += 5
                
                newTextBox = QtWidgets.QLineEdit(self)
                # Concat a new QLineEdit in the variable that will 
                # translate textBoxes to values in board
                self.mapToTextGrid[row].append(newTextBox)
                # Set text alignment to center
                newTextBox.setAlignment(QtCore.Qt.AlignCenter)
                # Set max text length to 1 character
                newTextBox.setMaxLength(1)
                # Set font size to 27
                fs = newTextBox.font()
                fs.setPointSize(27) 
                newTextBox.setFont(fs)
                # Positions the textBox based on size of the textBoxes and modifiers
                newTextBox.move(35 + 80*col + xmodifier, 30 + 80*row + ymodifier)
                # Set textBox size
                newTextBox.resize(80,80)
        return

    # Just a call of self.show() but we rewrite the buttons on the screen first
    def draw(self):
         # Create a button in the window
        self.button = QtWidgets.QPushButton('Button 1', self)
        self.button.move(400,760)

        # Create a button in the window
        self.button2 = QtWidgets.QPushButton('Verify Row', self)
        self.button2.move(300,760)
        
        # Connect button to function changeBgRed
        self.button.clicked.connect(self.changeBgRed)
        # Connect button to function changeBgWhite
        self.button2.clicked.connect(self.verify)
        self.show()

    def changeBgColor(self, textBox, color = "white"):
        textBox.setStyleSheet(f"background-color: {color};")
        self.draw()

    def popupMessage(self, message):
        QtWidgets.QMessageBox.question(self, 'Sudoku says', message, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def changeBgRed(self):
        # textboxValue = self.mapToTextGrid[0][0].text()
        # QtWidgets.QMessageBox.question(self, 'Message Box says', "You typed: " + textboxValue, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        self.changeBgColor(self.mapToTextGrid[0][0], "red")
        self.mapToTextGrid[0][0].setText("")

    @QtCore.pyqtSlot()
    def changeBgWhite(self):
        # textboxValue = self.mapToTextGrid[0][0].text()
        # QtWidgets.QMessageBox.question(self, 'Message Box says', "You typed: " + textboxValue, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        self.changeBgColor(self.mapToTextGrid[0][0])
        self.mapToTextGrid[0][0].setText("")
    
    @QtCore.pyqtSlot()
    def verify(self):
        self.board = self.readTextGrid()
        # self.popupMessage("".join([self.verTxtBoxRow(self.mapToTextGrid[i][0]) for i in range(len(self.board))]))
        self.popupMessage(str(self.verPosSquare(4, 4) and self.verPosCol(4) and self.verPosRow(4)))
    

# initialBoard = [[0 for i in range(10)] for i in range(10)]
# initialBoard = [[0] * 9] * 9

initialBoard = [
    [0,0,6,8,7,1,0,0,3],
    [0,7,3,0,5,6,1,9,0],
    [0,0,0,3,4,9,0,2,7],
    [3,4,2,0,0,0,0,8,0],
    [0,6,0,0,2,0,0,0,0],
    [0,0,0,0,0,3,0,5,2],
    [0,1,0,7,0,4,8,0,0],
    [7,0,0,5,9,8,2,6,1],
    [0,0,5,0,0,0,3,0,0],
]

app = QtWidgets.QApplication(sys.argv)
ex = App(initialBoard)
# ex.board[0][0] = int(input("value for board test: "))
# input("enter to fill: ")
# ex.fillValues()
sys.exit(app.exec_())