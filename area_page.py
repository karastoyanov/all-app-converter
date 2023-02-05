from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QComboBox)
from PyQt5.QtGui import (QIcon, QPixmap, QValidator, QIntValidator, QDoubleValidator)
import sys

class AreaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All Convertor - Area")
        self.setFixedSize(480, 300)
        self.setWindowIcon(QIcon(r'images\area-graph.png'))
        self.show()

        # Left DropDown Menu
        self.left_side = QComboBox(self)
        self.left_side.addItems(['Square Meter',
                                 'Square Kilometer',
                                 'Square Millimeter',
                                 'Square Micrometer',
                                 'Hectare',
                                 'Square Mile',
                                 'Square Yard',
                                 'Square Foot',
                                 'Square Inch',
                                 'Acre'])
        self.left_side.setGeometry(50, 50, 130, 30)
        self.left_side.show()

        # Right DropDown Menu
        self.right_side = QComboBox(self)
        self.right_side.addItems(['Square Meter',
                                 'Square Kilometer',
                                 'Square Millimeter',
                                 'Square Micrometer',
                                 'Hectare',
                                 'Square Mile',
                                 'Square Yard',
                                 'Square Foot',
                                 'Square Inch',
                                 'Acre'])
        self.right_side.setGeometry(300, 50, 130, 30)
        self.right_side.show()

        # Left Input Value
        self.validator = QDoubleValidator(-2147483646, 2147483647, 10)
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
        self.v = self.value.displayText()
        from area_convertor import calculate
        self.right_side_text.setText(str(calculate(self.l, self.r, self.v)))
        self.right_side_text.show()  


if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = AreaMenu()
    win.show()
    app.exec_()