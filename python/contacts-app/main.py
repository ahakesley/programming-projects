from layout import ContactsAppWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication([])
    window = ContactsAppWindow()
    window.database.insert("Alex", "Hakesley", "12345678910", "alexhakesley@email.com")
    window.show()
    sys.exit(app.exec())