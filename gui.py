import sys
from PySide6 import QtCore, QtWidgets
from passwordGenerator import passwordGenerator


class passwordGeneratorGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.passwordLenght = QtWidgets.QLineEdit("Password Lenght")
        self.lowerCases = QtWidgets.QCheckBox("Lowercases 🔡")
        self.upperCases = QtWidgets.QCheckBox("Uppercases 🔠")
        self.numbers = QtWidgets.QCheckBox("Numbers 🔢")
        self.symbols = QtWidgets.QCheckBox("Symbols 🔣")
        self.password = QtWidgets.QLineEdit("Password")
        self.passwordLenght.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordGeneratorButton = QtWidgets.QPushButton("Generate Password 🔑")
        self.upperCases.setChecked(True)
        self.lowerCases.setChecked(True)
        self.numbers.setChecked(True)
        self.symbols.setChecked(True)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layoutCheckBox1 = QtWidgets.QHBoxLayout()
        self.layoutCheckBox2 = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.passwordLenght)
        self.layoutCheckBox1.addWidget(self.upperCases)
        self.layoutCheckBox1.addWidget(self.lowerCases)
        self.layoutCheckBox2.addWidget(self.numbers)
        self.layoutCheckBox2.addWidget(self.symbols)
        self.layout.addLayout(self.layoutCheckBox1)
        self.layout.addLayout(self.layoutCheckBox2)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.passwordGeneratorButton)
        self.passwordGeneratorButton.clicked.connect(self.passwordGenerator)

    @QtCore.Slot()
    def passwordGenerator(self):
        self.password.setText(
            passwordGenerator(
                int(self.passwordLenght.text()),
                self.lowerCases.isChecked(),
                self.upperCases.isChecked(),
                self.numbers.isChecked(),
                self.symbols.isChecked(),
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet(
        ".QLabel,.QCheckBox,.QPushButton { font-size: 12pt;} QLineEdit { font-size: 12pt;}"
    )
    widget = passwordGeneratorGUI()
    widget.resize(300, 200)
    widget.setWindowTitle("Password Generator")
    widget.show()
    sys.exit(app.exec())
