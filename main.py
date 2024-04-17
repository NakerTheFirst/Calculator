from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__central_widget = None
        self.__layout = None
        self.setWindowTitle("Calculator")
        self.__setup_ui()

    def __setup_ui(self):
        self.__central_widget = QWidget()
        self.setCentralWidget(self.__central_widget)
        self.__layout = QGridLayout()
        self.__central_widget.setLayout(self.__layout)
        self.__central_widget.setStyleSheet("background-color: #04092E")
        self.setFixedSize(400, 400)

        num_buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("0", 4, 0)
        ]

        special_buttons = [
            ("/", 1, 3),
            ("*", 2, 3),
            ("-", 3, 3),
            (".", 4, 2),
            ("C", 4, 1),
            ("+", 4, 3),
            ("=", 5, 3)
        ]

        # Make the buttons come to life!
        for btn_text, row, col in num_buttons:
            Button(self.__layout, btn_text, row, col, "#767587")

        for btn_text, row, col in special_buttons:
            Button(self.__layout, btn_text, row, col, "#5C292B")

        # Make the text field come to life!
        text_field = QLabel("Lorem")
        text_field.setFixedHeight(60)
        text_field.setStyleSheet("background-color: #AAA9BC")
        self.__layout.addWidget(text_field, 0, 0, 1, 4)


class Button:
    # TODO: Add a slot argument - consider doing it in Logic class
    def __init__(self, layout, caption: str, row: int, col: int, colour: str) -> None:
        self.caption = caption
        self.row = row
        self.col = col
        self.colour = colour

        button = QPushButton(caption)
        button.setFixedHeight(60)
        layout.addWidget(button, row, col)
        button.setStyleSheet(f"background-color: {colour}; border: none")


class Logic:
    def __add(self, a, b):
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
