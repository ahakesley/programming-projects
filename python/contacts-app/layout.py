from PyQt5.QtWidgets import (
    QMainWindow,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QWidget,
    QListWidgetItem,
    QListWidget,
    QPushButton,
    QGridLayout,
)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 600

class ContactsAppWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Contacts")
        self.setFixedWidth(WINDOW_WIDTH)
        self.setFixedHeight(WINDOW_HEIGHT)
        self._setLayout()

    def new_button_clicked(self):
        print("Clicked 'New' button")

    def edit_button_clicked(self):
        print("Clicked 'Edit' button")

    def save_button_clicked(self):
        print("Clicked 'Save' button")

    def delete_button_clicked(self):
        print("Clicked 'Delete' button")
    
    def first_name_updated(self):
        print("First name: " + self.first_name_line_edit.text())

    def last_name_updated(self):
        print("Last name: " + self.last_name_line_edit.text())

    def telephone_updated(self):
        print("Telephone: " + self.telephone_line_edit.text())

    def email_updated(self):
        print("Email: " + self.email_line_edit.text())

    def _setLayout(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # set outer layout 
        outer_layout = QHBoxLayout()
        
        # set list pane layout (left)
        list_pane_layout = QVBoxLayout()
        list_widget = QListWidget()
        QListWidgetItem("Alex Hakesley", list_widget)
        QListWidgetItem("John Smith", list_widget)
        QListWidgetItem("Jane Doe", list_widget)
        list_pane_layout.addWidget(list_widget)

        # set details pane layout (right)
        details_pane_layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.first_name_line_edit = QLineEdit(self)
        self.first_name_line_edit.returnPressed.connect(self.first_name_updated)
        self.last_name_line_edit = QLineEdit(self)
        self.last_name_line_edit.returnPressed.connect(self.last_name_updated)
        self.telephone_line_edit = QLineEdit(self)
        self.telephone_line_edit.returnPressed.connect(self.telephone_updated)
        self.email_line_edit = QLineEdit(self)
        self.email_line_edit.returnPressed.connect(self.email_updated)
        form_layout.addRow("First Name:", self.first_name_line_edit)
        form_layout.addRow("Last Name:", self.last_name_line_edit)
        form_layout.addRow("Telephone:", self.telephone_line_edit)
        form_layout.addRow("Email:", self.email_line_edit)
        details_pane_layout.addLayout(form_layout)

        # buttons
        new_button = QPushButton(self)
        new_button.setText("New")
        new_button.clicked.connect(self.new_button_clicked)
        edit_button = QPushButton(self)
        edit_button.setText("Edit")
        edit_button.clicked.connect(self.edit_button_clicked)
        save_button = QPushButton(self)
        save_button.setText("Save")
        save_button.clicked.connect(self.save_button_clicked)
        delete_button = QPushButton(self)
        delete_button.setText("Delete")
        delete_button.clicked.connect(self.delete_button_clicked)

        # set button layout
        button_layout = QGridLayout()
        button_layout.addWidget(new_button, 0, 0)
        button_layout.addWidget(edit_button, 0, 1)
        button_layout.addWidget(save_button, 1, 0)
        button_layout.addWidget(delete_button, 1, 1)
        details_pane_layout.addLayout(button_layout)

        # add inner layouts to outer layout
        outer_layout.addLayout(list_pane_layout, 1)
        outer_layout.addLayout(details_pane_layout, 2)
        central_widget.setLayout(outer_layout)