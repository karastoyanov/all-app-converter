from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QComboBox)
from PyQt5.QtGui import (QIcon, QPixmap, QValidator, QIntValidator)
import sys


max_size = sys.maxsize
min_size = -sys.maxsize - 1

class LengthMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All Convertor - Lenght")
        self.setFixedSize(480, 300)
        self.setWindowIcon(QIcon(r'images\ruler.png'))
        self.show()
            
        # Left DropDown Menu
        self.left_side = QComboBox(self)
        self.left_side.addItems(['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Micrometer', 'Nanometer', 'Mile',
            'Yard', 'Foot', 'Inch', 'Light Year'])
        self.left_side.setGeometry(50, 50, 130, 30)
        self.left_side.show()

        # Right DropDown Menu
        self.right_side = QComboBox(self)
        self.right_side.addItems(['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Micrometer', 'Nanometer', 'Mile',
            'Yard', 'Foot', 'Inch', 'Light Year'])
        self.right_side.setGeometry(300, 50, 130, 30)
        self.right_side.show()

        # Left Input Value
        self.validator = QIntValidator(-2147483646, 2147483647)
        self.value = QLineEdit(self)
        self.value.setValidator(self.validator)
        self.value.setGeometry(50, 85, 130, 30)
        self.value.show()
        
        # Right Result Value
        self.right_side_text = QLineEdit(self)
        self.right_side_text.setReadOnly(True)
        self.right_side_text.setGeometry(300, 85, 130, 30)
        self.right_side_text.show()

        # Convert Button
        self.convert_button = QPushButton(self)
        self.convert_button.clicked.connect(self.convert)
        self.convert_button.setText("Convert")
        self.convert_button.setGeometry(190, 47, 100, 70)
        self.convert_button.show()
        
    def convert(self):
        self.l = self.left_side.currentText()
        self.r = self.right_side.currentText()
        self.v =self.value.displayText()
        from length_convertor import calculate
        self.right_side_text.setText(str(calculate(self.l, self.r, self.v)))
        self.right_side_text.show()  
        

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = LengthMenu()
    win.show()
    app.exec_()