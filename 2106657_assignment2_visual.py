# necessary libraries
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np

# generating an editible dataframe for players to input into
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()

# determining characteristics from choice of size of matrix
        self._data = data

# returning # of rows
    def rowCount(self, index):
        return len(self._data)

# returning # of columns
    def columnCount(self, index):
        return len(self._data[0])

# function which returns the value of the cell to ensure every edit is saved
    def data(self, index, role=Qt.DisplayRole):

# table can only be rendered if # rows = # cols 
        if index.isValid():

# the two potential cell values are initial and user added, these cases make sure most recent version always top
            if role == Qt.DisplayRole:
                value = self._data[index.row()][index.column()]
                return str(value)

# whenever a new user input is added, resetting value of cell
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            return True
        return False

# flags is the import PyQt function that allows for editing in a session state
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

# creating the pop up 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

# rendering the standard Qt table thats empty so users can easily see where they can place next move
        self.table = QTableView()
        matrix_entries = []
        for i in range(0, n**2):
            matrix_entries.append("")
        matrix_entries = np.reshape(matrix_entries,[n,n])
    
        data = matrix_entries
        
# the determinant button function, prints the determinant of any input matrix
        def button_clicked():
            data_reshape = np.reshape(data,[n**2,1])
            get_data = [int(x) for x in data_reshape]
            get_data = np.reshape(get_data,[n,n])
            print("The determinant is",np.linalg.det(get_data))
        
                
# adding the determinant button
        b = QPushButton()
        b.setText("Calculate Determinant")
        b.clicked.connect(button_clicked)

# setting up the layout of the window so button and matrix are next to each other
        widget = QWidget(self)
        layout = QHBoxLayout(widget)
        layout.addWidget(self.table)
        layout.addWidget(b)

# window title
        self.setWindowTitle("Matrix Determinant Game")

# using the pandas model defined above so the matrix is editable and adding it to the window
        self.model = PandasModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(widget)

# dimensions of matrix (always square)
n =int(input("Choose dimensions"))

# rendering the window
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()