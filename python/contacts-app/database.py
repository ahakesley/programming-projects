import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox

class Database():
    def __init__(self):
        super().__init__
        self.createConnection()
        self.connect()
        self.createMainTable()

    def createConnection(self):
        self.connection = QSqlDatabase.addDatabase("QSQLITE")
        self.connection.setDatabaseName("contacts.sqlite")

    def connect(self):
        if not self.connection.open():
            QMessageBox.critical(
                None, 
                "Database Error", 
                "Database Error: %s" % self.connection.lastError().databaseText())
            sys.exit(1)

    def createMainTable(self):
        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            CREATE TABLE contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                first_name VARCHAR(40) NOT NULL,
                last_name VARCHAR(40) NOT NULL,
                telephone VARCHAR(13),
                email VARCHAR(40)
            )
            """
        )
    
    def insert(self, first_name, last_name, telephone, email):
        insertQuery = QSqlQuery()
        insertQuery.prepare(
            """
            INSERT INTO contacts (
                first_name,
                last_name,
                telephone,
                email
            )
            VALUES (?, ?, ?, ?)
            """
        )
        insertQuery.addBindValue(first_name)
        insertQuery.addBindValue(last_name)
        insertQuery.addBindValue(telephone)
        insertQuery.addBindValue(email)
        insertQuery.exec()

    def read(self):
        read_query = QSqlQuery()
        read_query.exec(
            """
            SELECT * FROM contacts
            """
        )

    def delete(self, id):
        deleteQuery = QSqlQuery()
        deleteQuery.prepare(
            """
            DELETE FROM contacts WHERE id = ?
            """
        )
        deleteQuery.addBindValue(id)
        deleteQuery.exec()