from PyQt5 import QtWidgets
import sys
from gui import Ui_MainWindow
import sqlite3


class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

        #Button settings
        self.ui.insert_data_btn.clicked.connect(self.insert_data)
        self.ui.update_data_btn.clicked.connect(self.update_data)
        self.ui.delete_data_btn.clicked.connect(self.delete_data)
        self.ui.tableWidget.clicked.connect(self.on_treeView_clicked)

        #connection to sqlite3
        try:
            self.ui.label_4.setText("Connected to the database!")
            self.conn = sqlite3.connect("mydatabase.db")
            self.c = self.conn.cursor()
        except Error:
            self.ui.label_4.setText("Error with connection.")
         
        #Put everything into the table  
    def show_table(self):
        query = 'SELECT * FROM kids'
        result = self.conn.execute(query)
        
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def insert_data(self):
        self.first_name = self.ui.FirstName_entry.text()
        self.last_name = self.ui.LastName_entry.text()
        self.grade = self.ui.Grade_entry.text()
        self.c.execute("INSERT INTO kids(First_Name, Last_Name, Grade) VALUES ('"+self.first_name+"','"+self.last_name+"','"+self.grade+"');")
        self.conn.commit()
        self.show_table()

    def update_data(self):
        pass
       
    def on_treeView_clicked(self, index):
        x = str(index.data())

        query = 'SELECT * FROM kids WHERE ID = 696'
        result = self.conn.execute(query)




        # mam = self.c.execute('SELECT First_Name FROM kids WHERE ID='+x+';')
        # mam2 = self.c.execute('SELECT Last_Name FROM kids WHERE ID='+x+';')
        # mam3 = self.c.execute('SELECT Grade FROM kids WHERE ID='+x+';')
        # bruh = self.conn.commit()

        # query = 'SELECT First_Name FROM kids WHERE ID='+x+''
        # result = self.conn.execute(query)
        # self.first_name = self.ui.FirstName_entry.setText(result)
        # self.last_name = self.ui.LastName_entry.setText("ds")
        # self.grade = self.ui.Grade_entry.setText("f")
        
        

    def delete_data(self):
        self.c.execute('DELETE FROM kids;')
        self.show_table()
        self.conn.commit()
        
# Shows the window
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = myWindow()
    application.show_table()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


