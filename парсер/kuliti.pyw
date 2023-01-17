import sys
from PyQt5 import uic
from PyQt5 import  QtWidgets
import os
Form,Window =uic.loadUiType("ku1.ui")
app=QtWidgets.QApplication([])
window=Window()
form=Form()
form.setupUi(window)
window.show()
#filter="JPEG (*.jpg *.jpeg);;PNG (*.png)"

def xuy1(huy1):


     res = QtWidgets.QFileDialog.getOpenFileName(filter="JPEG (*.jpg *.jpeg) PNG (*.png)")

     print(res)

     huy1 = ''
     huy1 = huy1.join(res)
     print(huy1)
     huy1 = huy1.replace("JPEG (*.jpg *.jpeg) PNG (*.png)", '')
     huy1 = os.path.join(huy1)
     huy1 = huy1.replace("/", "\\")
     huy1 = os.path.join(huy1)
     file = open("name1.txt", "w+")
     file.write(huy1)
     print(huy1)
     return (huy1)


form.pushButton_2.clicked.connect(xuy1)
def da(ku4):
    global file1

    ku1=''
    ku1=form.lineEdit.text()
    ku1=ku1+"<br>"
    ku1=str(ku1)
    ku2=''
    ku2=form.lineEdit_2.text()
    ku2=ku2+"<br>"
    ku2=str(ku2)
    ku3=''
    ku3=form.lineEdit_3.text()
    ku3=ku3+"<br>"
    ku3=str(ku3)
    ku4=ku1+ku2+ku3
    print (ku4)
    file = open("name.txt", "w+")
    file.write(ku4)
    file.close()

    #file2=open('name.txt', 'w').close()

    #if not file2:
    #  print('пошел нахуй')


form.pushButton.clicked.connect(da)
app.exec()


