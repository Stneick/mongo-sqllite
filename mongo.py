import sys
import random
from PyQt5.QtWidgets import *
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client['student_db']
collection = db['students']


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

class StudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Manager")
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
        collection.delete_many({})
        for i in range(10):
            student = {
                "ID": str(i + 1),
                "Last Name": ch(LNames),
                "Name": ch(FNames),
                "Subject": ch(Subjects),
                "Grade": ch(Points)
            }
            collection.insert_one(student)
        QMessageBox.information(self, "Done", "10 random records added.")

    def search_record(self):
        query = {}
        if self.id_input.text(): query["ID"] = self.id_input.text()
        if self.lname_input.text(): query["Last Name"] = self.lname_input.text()
        if self.fname_input.text(): query["Name"] = self.fname_input.text()
        if self.subject_input.text(): query["Subject"] = self.subject_input.text()
        if self.grade_input.text(): query["Grade"] = self.grade_input.text()

        result = collection.find_one(query)
        if result:
            self.id_input.setText(result["ID"])
            self.lname_input.setText(result["Last Name"])
            self.fname_input.setText(result["Name"])
            self.subject_input.setText(result["Subject"])
            self.grade_input.setText(result["Grade"])
        else:
            QMessageBox.information(self, "Not Found", "No matching record.")

    def update_record(self):
        ident = self.id_input.text()
        if not ident:
            QMessageBox.warning(self, "Error", "Provide ID to update.")
            return
        new_data = {
            "Last Name": self.lname_input.text(),
            "Name": self.fname_input.text(),
            "Subject": self.subject_input.text(),
            "Grade": self.grade_input.text()
        }
        result = collection.update_one({"ID": ident}, {"$set": new_data})
        if result.modified_count > 0:
            QMessageBox.information(self, "Success", "Record updated.")
        else:
            QMessageBox.warning(self, "Error", "No record updated.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StudentApp()
    win.show()
    sys.exit(app.exec_())
