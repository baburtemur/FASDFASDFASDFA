def main():
    from PyQt6.QtGui import QPainter, QBrush, QPen
    from PyQt6.QtWidgets import QMainWindow
    from PyQt6 import uic
    class Problem(QMainWindow):
        def __init__(self):
            super.__init__()
            uic.loadUi('UI.ui')



if __name__ == '__main__':
    main()