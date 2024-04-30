import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QWidget,
    QListWidgetItem,
    QListWidget,
)

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 600

class ContactsAppWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Contacts")
        self.setFixedWidth(WINDOW_WIDTH)
        self.setFixedHeight(WINDOW_HEIGHT)
        self._setLayout()

    def _setLayout(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # set outer layout 
        outer_layout = QHBoxLayout()
        
        list_pane_layout = QVBoxLayout()
        list_widget = QListWidget()
        QListWidgetItem("Alex Hakesley", list_widget)
        QListWidgetItem("John Smith", list_widget)
        QListWidgetItem("Jane Doe", list_widget)
        list_pane_layout.addWidget(list_widget)

        details_pane_layout = QFormLayout()
        details_pane_layout.addRow("First Name:", QLineEdit())
        details_pane_layout.addRow("Last Name:", QLineEdit())
        details_pane_layout.addRow("Telephone:", QLineEdit())
        details_pane_layout.addRow("Email:", QLineEdit())

        outer_layout.addLayout(list_pane_layout, 1)
        outer_layout.addLayout(details_pane_layout, 2)
        central_widget.setLayout(outer_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = ContactsAppWindow()
    window.show()
    sys.exit(app.exec())