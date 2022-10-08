from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("All Convertor")
        self.setWindowIcon(QIcon())
        self.setFixedSize(500, 300)
        self.setWindowIcon(QIcon(r'images\convert.png'))
        self.show()

        # Length button and icon
        self.length_button = QPushButton(self)
        self.length_button.setText("Length")
        self.length_button.setGeometry(30, 10, 90, 40)
        self.ruler_icon = QLabel(self)
        self.ruler_icon.setGeometry(130, 15, 90, 40)
        self.ruler = QPixmap(r'images/ruler.png')
        self.ruler_icon.setPixmap(self.ruler)
        self.length_button.show()
        self.ruler_icon.show()
    
        # Temperature button and icon
        self.temperature_button = QPushButton(self)
        self.temperature_button.setText("Temperature")
        self.temperature_button.setGeometry(30, 70, 90, 40)
        self.temp_icon = QLabel(self)
        self.temp_icon.setGeometry(130, 75, 90, 40)
        self.temp = QPixmap(r'images/thermometer.png')
        self.temp_icon.setPixmap(self.temp)
        self.temperature_button.show()
        self.temp_icon.show()

        # Area button and icon
        self.area_button = QPushButton(self)
        self.area_button.setText("Area")
        self.area_button.setGeometry(30, 130, 90, 40)
        self.area_icon = QLabel(self)
        self.area_icon.setGeometry(130, 135, 90, 40)
        self.area_image = QPixmap(r'images/area-graph.png')
        self.area_icon.setPixmap(self.area_image)
        self.area_button.show()
        self.area_icon.show()
    
        # Volume button and icon
        self.volume_button = QPushButton(self)
        self.volume_button.setText("Volume")
        self.volume_button.setGeometry(300, 10, 90, 40)
        self.volume_icon = QLabel(self)
        self.volume_icon.setGeometry(400, 11, 90, 40)
        self.volume_image = QPixmap(r'images/volume.png')
        self.volume_icon.setPixmap(self.volume_image)
        self.volume_button.show()
        self.volume_icon.show()
    
        # Weight button and icon
        self.weight_button = QPushButton(self)
        self.weight_button.setText("Weight")
        self.weight_button.setGeometry(300, 70, 90, 40)
        self.weight_icon = QLabel(self)
        self.weight_icon.setGeometry(400, 72, 90, 40)
        self.weight_image = QPixmap(r'images/weight-scale.png')
        self.weight_icon.setPixmap(self.weight_image)
        self.weight_button.show()
        self.weight_icon.show()
    

        self.time_button = QPushButton(self)
        self.time_button.setText("Time")
        self.time_button.setGeometry(300, 130, 90, 40)
        self.time_icon = QLabel(self)
        self.time_icon.setGeometry(400, 135, 90, 40)
        self.time_image = QPixmap(r'images/time.png')
        self.time_icon.setPixmap(self.time_image)
        self.time_button.show()
        self.time_icon.show()
        
if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    app.exec_()
        