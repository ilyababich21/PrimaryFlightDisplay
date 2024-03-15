import sys

from PyQt6.QtWidgets import QApplication




from view.poletView import PoletView
def main():
    app = QApplication(sys.argv)
    window = PoletView()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()