from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtGui


class UI(QMainWindow):
    textChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__central_widget = None
        self.__layout = None
        self.__displayed_value = 0
        self.text_field = None
        self.setWindowTitle("Calculator")
        self.__setup_ui()

    def __setup_ui(self):
        self.__central_widget = QWidget()
        self.setCentralWidget(self.__central_widget)
        self.__layout = QGridLayout()
        self.__central_widget.setLayout(self.__layout)
        self.__central_widget.setStyleSheet("background-color: #1E1E1E; color: #1E1E1E")
        self.setFixedSize(400, 400)
        self.setWindowIcon(QtGui.QIcon('icon.svg'))
        self.text_field = QLabel("0")
        self.text_field.setFixedHeight(60)
        self.text_field.setStyleSheet("background-color: #F2ECFF; font: 22pt Ubuntu")
        self.__layout.addWidget(self.text_field, 0, 0, 1, 4)

        num_buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("1", 3, 0),
                       ("2", 3, 1), ("3", 3, 2), ("0", 4, 0)]
        special_buttons = [("/", 1, 3), ("*", 2, 3), ("-", 3, 3), (".", 4, 2), ("C", 4, 1), ("+", 4, 3), ("=", 5, 3)]

        # Buttons
        # for btn_text, row, col in num_buttons:
        #     Button(self.__layout, btn_text, row, col, "#945968")

        # for btn_text, row, col in special_buttons:
        #     Button(self.__layout, btn_text, row, col, "#D47E6C")

        # Create buttons and connect to a method that handles the click
        for btn_text, row, col in num_buttons + special_buttons:
            Button(self.__layout, btn_text, row, col, "#767587", lambda text=btn_text: self.button_clicked(text))

    def button_clicked(self, button_text):
        # Update the text field with button text
        current_text = self.text_field.text()
        new_text = current_text + button_text
        self.text_field.setText(new_text)
        self.textChanged.emit(new_text)


class Button:
    def __init__(self, layout, caption: str, row: int, col: int, colour: str, button_clicked) -> None:
        self.caption = caption
        self.row = row
        self.col = col
        self.colour = colour

        button = QPushButton(caption)
        button.setFixedHeight(60)
        layout.addWidget(button, row, col)
        button.setStyleSheet(f"background-color: {colour}; border: none; font: bold 32px Ubuntu; color: #1E1E1E")

        # Connect the button click to a passed function
        button.clicked.connect(lambda: button_clicked())


class Logic:
    def __init__(self):
        self.__output = 0

    @staticmethod
    def __add(a, b):
        return a + b


class MainApp:
    def __init__(self):
        self.__app = QApplication([])
        self.__ui = UI()
        self.__logic = Logic()

    def run(self):
        self.__ui.show()
        self.__app.exec()


if __name__ == '__main__':
    calc_app = MainApp()
    calc_app.run()
