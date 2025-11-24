import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circle = None
        
    def add_circle(self, diameter):
        max_x = self.width() - diameter
        max_y = self.height() - diameter
        
        if max_x > 0 and max_y > 0:
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            self.circle = (x, y, diameter)
            self.update()

    def paintEvent(self, event):
        if self.circle is not None:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            x, y, diameter = self.circle
            painter.setPen(QPen(QColor('yellow'), 2))
            painter.setBrush(QColor('yellow'))
            painter.drawEllipse(x, y, diameter, diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.button = QPushButton("Добавить круг")
        self.button.clicked.connect(self.add_circle)
        layout.addWidget(self.button)
        
        self.circle_widget = CircleWidget()
        self.circle_widget.setStyleSheet("background-color: white;")
        layout.addWidget(self.circle_widget)
        
    def add_circle(self):
        diameter = random.randint(20, 200)
        self.circle_widget.add_circle(diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())