# CRUD: create, read, update y delete
# ABM: altas, bajas, modificaciones
from PyQt5 import uic
from PyQt5.uic.uiparser import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import os
from entities.persona import persona


def getpersonas():
    personas=[]
    personas.append(persona("per1", "Gabriel", "71902732", "Peruana"))
    personas.append(persona("per2", "Maffeo", "12345678", "Español"))
    personas.append(persona("per3", "Christian", "87654321", "Argentino"))
    personas.append(persona("per4", "Jose", "12345678", "Israel"))
    personas.append(persona("PER05", "Bertha Castillo", "43293902", "Ecuatoriana"))
    personas.append(persona("PER06", "Rosa Valdez", "43293902", "Ecuatoriana"))
    return personas

def crear_tabla():
    personas=getpersonas()
    print(form_main.twpersonas)
    form_main.twpersonas.setRowCount(len(personas))
    #form_main.twpersonas.setColumnCount(4)
    for i in range(len(personas)):
        form_main.twpersonas.setItem(i,0, QTableWidgetItem(personas[i].id))
        form_main.twpersonas.setItem(i,1, QTableWidgetItem(personas[i].dni))
        form_main.twpersonas.setItem(i,2, QTableWidgetItem(personas[i].nombre))
        form_main.twpersonas.setItem(i,3, QTableWidgetItem(personas[i].nacionalidad))

ui_path=os.path.dirname(os.path.abspath(__file__))
Form, Window = uic.loadUiType(os.path.join(ui_path, "ui", "crud-main.ui"))

app_crud= QApplication([])
window_main= Window()
form_main=Form()
form_main.setupUi(window_main)
window_main.show()
crear_tabla()
app_crud.exec()