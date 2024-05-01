from layout import ContactsAppWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication([])
    window = ContactsAppWindow()
    window.show()
    sys.exit(app.exec())