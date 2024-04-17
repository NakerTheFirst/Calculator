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
        self.setFixedSize(400, 400)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            ("C", 4, 1),
            (".", 4, 2),
            ("+", 4, 3),
            ("=", 5, 3)
        ]

        # Make the buttons come to life!
        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.setFixedHeight(60)
            self.__layout.addWidget(button, row, col)

        # Make the text field come to life!
        text_field = QLabel("Lorem")
        text_field.setFixedHeight(60)
        text_field.setStyleSheet("background-color: slategray")
        self.__layout.addWidget(text_field, 0, 0, 1, 4)

    def __button_clicked(self):
        # Signal handler
        print("Button clicked")


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
