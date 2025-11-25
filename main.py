import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circle = None
        
    def add_circle(self, diameter, color):
        max_x = self.width() - diameter
        max_y = self.height() - diameter
        
        if max_x > 0 and max_y > 0:
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            self.circle = (x, y, diameter, color)
            self.update()
            
    def paintEvent(self, event):
        if self.circle is not None:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            x, y, diameter, color = self.circle
            painter.setPen(QPen(color, 2))
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Генератор случайных окружностей")
        self.setGeometry(100, 100, 900, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        self.create_button = QPushButton("Создать окружность")
        self.create_button.clicked.connect(self.add_circle)
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border: 1px solid gray;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: silver;
            }
            QPushButton:pressed {
                background-color: darkgray;
            }
        """)
        main_layout.addWidget(self.create_button)
        
        self.circle_widget = CircleWidget()
        self.circle_widget.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        main_layout.addWidget(self.circle_widget)
        
    def add_circle(self):
        diameter = random.randint(30, 250)
        color = self.generate_random_color()
        self.circle_widget.add_circle(diameter, color)
    
    def generate_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return QColor(red, green, blue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())