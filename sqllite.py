import sys
import random
import sqlite3
from PyQt5.QtWidgets import *


LNames = ['Abashidze', 'Gigauri', 'Archvadze', 'Akhalaya', 'Badzaghua', 'Berianidze', 'Berishvili', 'Gventsadze', 'Dalakishvili', 

'Antidze', 'Gyorgadze', 'Gogaladze', 'Gotsiridze', 'Vardidze', 'Zarandia', 'Tadumadze', 'Labadze', 'Kvaratskhelia', 

'Kusradze', 'Kveselava', 'Kapanadze', 'Kasradze', 'Kvinikadze', 'Kopadze', 'Kankia', 'Kordzaia', 'Mikava', 'Melia', 

'Monyava', 'Niauri', 'Latsabidze', 'Mikadze', 'Nemsitsveridze', 'Maisuradze', 'Matsaberidze', 'Tsavania', 'Machaladze', 

'Odisharia', 'Metreveli', 'Nefaridze', 'Modebadze', 'Marjanidze', 'Mumladze', 'Nasrashvili', 'Djanjghava', 'Mosia', 

'Nozadze', 'Nutsubidze', 'Oniani', 'Okruashvili', 'Pertia', 'Razmadze', 'Revazashvili', 'Saganelidze', 'Jakhaia', 

'Salukvadze', 'Samsonashvili', 'Samkharadze', 'Saralidze', 'Sartania', 'Sarishvili', 'Simonishvili', 'Skhiladze', 

'Khurtsidze', 'Sikharulidze', 'Tabatadze', 'Fatsatsia', 'Filauri', 'Fukhashvili', 'Kobalia', 'Kipshidze', 'Shainidze', 

'Fifia', 'Shengelia', 'Sherozia', 'Shvelidze', 'Chkheidze', 'Chaduneli', 'Chikvashvili', 'Tskitishvili', 'Chokoraya', 

'Tsaguria', 'Tsertsvadze', 'Tsukhishvili', 'Dzindzibadze', 'Tsereteli', 'Tsiklauri', 'Chavchanidze', 'Chiradze', 'Chelidze', 

'Chanturia', 'Siradze', 'Shonia', 'Khanjaladze', 'Kharazishvili', 'Kheladze', 'Khvingia', 'Khutishvili', 'Janelidze', 

'Jokhadze'] 

FNames = ['Anna', 'Anuki', 'Barbare', 'Gvantsa', 'Diana', 'Eka', 'Elene', 'Veronika', 'Viktoria', 'Tatia', 'Lamzira', 

'Tea', 'Tekle', 'Tiniko', 'Tamari', 'Isabella', 'Ia', 'Yamze', 'Lia', 'Lika', 'Lana', 'Marika', 'Manana', 

'Maya', 'Maka', 'Mariam', 'Nana', 'Nani', 'Nata', 'Nato', 'Nino', 'Nona', 'Oliko', 'Ketevani', 'Salome', 

'Sofiko', 'Nia', 'Christine', 'Shorena', 'Khatia', 'Aleko', 'Alika', 'Amiran', 'Andria', 'Archil', 'Aslan', 

'Bachuk', 'Beka', 'Giga', 'Gyorgi', 'David', 

'Gigi', 'Goga', 'Data', 'Erekle', 'Temur', 'Yakob', 'Ilia', 'Irakli', 'Lado', 'Lasha', 'Mikhail', 

'Nika', 'Otari', 'Paata', 'Ramaz', 'Ramini', 'Rati', 'Rauli', 'Revazi', 'Roma', 'Romani', 'Sandro', 

'Saba', 'Sergi', 'Simon', 'Shalva', 'Shota', 'Tsotne', 'Jaba'] 

Subjects = ['Basics of Programming', 'Calculus II', 'Introduction to Physics', 'Computer Skills', 

'Introduction to Chemistry', 'Introduction to Biology', 'Algorithms I', 'Introduction to Electronics', 

'Data Structures', 'Algorithms II'] 

Points = [str(i) for i in range(101)]
ch = random.choice


conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        ID TEXT PRIMARY KEY,
        last_name TEXT,
        first_name TEXT,
        subject TEXT,
        grade TEXT
    )
""")
conn.commit()

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Manager (SQLite)")
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.id_input = QLineEdit()
        self.lname_input = QLineEdit()
        self.fname_input = QLineEdit()
        self.subject_input = QLineEdit()
        self.grade_input = QLineEdit()

        grid.addWidget(QLabel("ID"), 0, 0)
        grid.addWidget(self.id_input, 0, 1)

        grid.addWidget(QLabel("Last Name"), 1, 0)
        grid.addWidget(self.lname_input, 1, 1)

        grid.addWidget(QLabel("Name"), 2, 0)
        grid.addWidget(self.fname_input, 2, 1)

        grid.addWidget(QLabel("Subject"), 3, 0)
        grid.addWidget(self.subject_input, 3, 1)

        grid.addWidget(QLabel("Grade"), 4, 0)
        grid.addWidget(self.grade_input, 4, 1)

        self.add_btn = QPushButton("Add all records")
        self.add_btn.clicked.connect(self.add_records)
        grid.addWidget(self.add_btn, 0, 2)

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.search_record)
        grid.addWidget(self.search_btn, 1, 2)

        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_record)
        grid.addWidget(self.update_btn, 2, 2)

        self.remove_btn = QPushButton("Remove")
        self.remove_btn.setEnabled(False)
        grid.addWidget(self.remove_btn, 3, 2)

        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close)
        grid.addWidget(self.close_btn, 5, 1)

        self.setLayout(grid)

    def add_records(self):
        cursor.execute("DELETE FROM students")
        for i in range(10):
            student = (
                str(i + 1),
                ch(LNames),
                ch(FNames),
                ch(Subjects),
                ch(Points)
            )
            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
        conn.commit()
        QMessageBox.information(self, "Done", "10 random records added.")

    def search_record(self):
        query = "SELECT * FROM students WHERE 1=1"
        params = []
        if self.id_input.text():
            query += " AND ID = ?"
            params.append(self.id_input.text())
        if self.lname_input.text():
            query += " AND last_name = ?"
            params.append(self.lname_input.text())
        if self.fname_input.text():
            query += " AND first_name = ?"
            params.append(self.fname_input.text())
        if self.subject_input.text():
            query += " AND subject = ?"
            params.append(self.subject_input.text())
        if self.grade_input.text():
            query += " AND grade = ?"
            params.append(self.grade_input.text())

        cursor.execute(query, params)
        result = cursor.fetchone()
        if result:
            self.id_input.setText(result[0])
            self.lname_input.setText(result[1])
            self.fname_input.setText(result[2])
            self.subject_input.setText(result[3])
            self.grade_input.setText(result[4])
        else:
            QMessageBox.information(self, "Not Found", "No matching record.")

    def update_record(self):
        ident = self.id_input.text()
        if not ident:
            QMessageBox.warning(self, "Error", "Provide ID to update.")
            return

        cursor.execute("""
            UPDATE students SET
                last_name = ?,
                first_name = ?,
                subject = ?,
                grade = ?
            WHERE ID = ?
        """, (
            self.lname_input.text(),
            self.fname_input.text(),
            self.subject_input.text(),
            self.grade_input.text(),
            ident
        ))
        conn.commit()
        if cursor.rowcount > 0:
            QMessageBox.information(self, "Success", "Record updated.")
        else:
            QMessageBox.warning(self, "Error", "No record updated.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StudentApp()
    win.show()
    sys.exit(app.exec_())
