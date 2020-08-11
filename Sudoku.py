import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class App(QtWidgets.QMainWindow):

    def __init__(self, board):
        super().__init__()
        self.title = 'Sudoku using PyQt5 by Bruno Thuma'
        self.left = 560
        self.top = 140
        self.width = 800
        self.height = 800
        self.mapToTextGrid = [[] for x in range(10)]
        self.board = list(board)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        self.textGrid()
        self.fillInitialValues()

        self.draw()

    def verRow(self, textBox):
        n = -1
        for row in self.mapToTextGrid:
            if textBox in row:
                n = row.index(textBox)

        if n == -1:
            return "textBox not found on textGrid"
        # If there are any 0's return message of ampty tile
        if not all(self.board[n]):
            return "row still got empty places"
        # If length of array(can repeat values) is greater than
        # length of set(doesnt repeat values) return duplicated 
        # values message
        if len(self.board[n]) > len(set(self.board[n])):
            return "duplicated values in row"
        return "OK"

    # Fill the textBoxes of the window 
    # with the values on the self.board matrix
    def fillValues(self):
        print("debug")
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                value = self.board[row][col]
                if value != 0:
                    self.mapToTextGrid[row][col].setText(str(value))
        self.draw()
        return

    # Same as self.fillValues() but set the non-0 tiles as read-only
    def fillInitialValues(self):
        print("debug")
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                value = self.board[row][col]
                if value != 0:
                    self.mapToTextGrid[row][col].setText(str(value))
                    self.mapToTextGrid[row][col].setReadOnly(True)
        self.draw()
        return
    
    def readTextGrid(self):
        result = []
        print("len(self.mapToTextGrid) ", len(self.mapToTextGrid))
        for row in range(len(self.mapToTextGrid)):
            result.append([])
            print(f"len(self.mapToTextGrid[{row}]) ", len(self.mapToTextGrid[row]))
            for col in range(len(self.mapToTextGrid)):
                print("row, col", row, col)
                textBox = self.mapToTextGrid[row][col]
                if textBox.text() != '':
                    # self.board[row][col] = int(textBox.text())
                    result[row].append(int(textBox.text()))
                    print(textBox.text())
                else:
                    result[row].append(0)
        if len(result) < 9 or len(result[0]) < 9:
            print("erro no read")
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
        self.button2 = QtWidgets.QPushButton('Button 2', self)
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
        self.readTextGrid()
        self.popupMessage(self.verRow(self.mapToTextGrid[0][0]))
    

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