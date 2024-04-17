from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtGui


class UI(QMainWindow):
    buttonClicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
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
        self.text_field = QLabel()
        self.text_field.setFixedHeight(60)
        self.text_field.setStyleSheet("background-color: #F2ECFF; font: 22pt Ubuntu; padding-left: 10px")
        self.__layout.addWidget(self.text_field, 0, 0, 1, 4)

        num_buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("1", 3, 0),
                       ("2", 3, 1), ("3", 3, 2), ("0", 4, 0)]
        special_buttons = [("/", 1, 3), ("*", 2, 3), ("-", 3, 3), (".", 4, 2), ("C", 4, 1), ("+", 4, 3), ("=", 5, 3)]

        for btn_text, row, col in num_buttons + special_buttons:
            button = QPushButton(btn_text)
            button.setFixedHeight(60)
            self.__layout.addWidget(button, row, col)
            button.setStyleSheet("background-color: #767587; border: none; font: bold 32px Ubuntu; color: #1E1E1E")
            button.clicked.connect(lambda ch, btn_text=btn_text: self.button_clicked(btn_text))

    def button_clicked(self, button_text):
        self.buttonClicked.emit(button_text)


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

        button.clicked.connect(button_clicked)


class Logic:
    def __init__(self):
        self.current_result = 0
        self.current_operation = None
        self.new_number = True

    def calculate(self, operand, operator):
        if operator == '+':
            self.current_result += operand
        elif operator == '-':
            self.current_result -= operand
        elif operator == '*':
            self.current_result *= operand
        elif operator == '/':
            if operand != 0:
                self.current_result /= operand
            else:
                print("Moron")
                return None
        self.current_operation = None
        return self.current_result

    def clear(self):
        self.current_result = 0
        self.current_operation = None
        self.new_number = True


class MainApp:
    def __init__(self):
        self.__app = QApplication([])
        self.__ui = UI()
        self.__logic = Logic()

        # Connect UI's buttonClicked signal to Logic's method
        self.__ui.buttonClicked.connect(self.logic_operation)

    def logic_operation(self, button_text):
        if button_text.isdigit() or button_text == '.':
            if self.__logic.new_number:
                self.__ui.text_field.setText(button_text)
            else:
                self.__ui.text_field.setText(self.__ui.text_field.text() + button_text)
            self.__logic.new_number = False
        elif button_text in "+-*/":
            if not self.__logic.new_number:
                if self.__logic.current_operation is not None:
                    self.__logic.calculate(float(self.__ui.text_field.text()), self.__logic.current_operation)
                else:
                    self.__logic.current_result = float(self.__ui.text_field.text())
                self.__logic.current_operation = button_text
                self.__logic.new_number = True
            self.__ui.text_field.setText('0')
        elif button_text == '=':
            if self.__logic.current_operation:
                result = self.__logic.calculate(float(self.__ui.text_field.text()), self.__logic.current_operation)
                self.__ui.text_field.setText(str(result))
                self.__logic.clear()
        elif button_text == 'C':
            self.__logic.clear()
            self.__ui.text_field.setText('0')

    def run(self):
        self.__ui.show()
        self.__app.exec()


if __name__ == '__main__':
    calc_app = MainApp()
    calc_app.run()

