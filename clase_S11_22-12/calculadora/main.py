from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
from aritmetica import operaciones


def sumar():
    val1, val2= obtener_operandos()
    form_calculadora.lbResult.setText((str)(operaciones.sumar(val1,val2)))

def restar():
    val1, val2= obtener_operandos()
    form_calculadora.lbResult.setText((str)(operaciones.restar(val1,val2)))    

def multiplicar():
    val1, val2= obtener_operandos()
    form_calculadora.lbResult.setText((str)(operaciones.multiplicar(val1,val2)))

def dividir():
    val1, val2= obtener_operandos()
    form_calculadora.lbResult.setText((str)(operaciones.dividir(val1,val2)))

def obtener_operandos():
    val1=int(form_calculadora.sbOperator1.text())
    val2=int(form_calculadora.sbOperator2.text())
    return(val1,val2)

ui_path=os.path.dirname(os.path.abspath(__file__))
Form, Window = uic.loadUiType(os.path.join(ui_path, "ui", "calculadora-basic.ui"))

app_calculadora= QApplication([])
window_calculadora= Window()
form_calculadora=Form()
form_calculadora.setupUi(window_calculadora)
window_calculadora.show()
form_calculadora.pbSum.clicked.connect(sumar)
form_calculadora.pbRes.clicked.connect(restar)
form_calculadora.pbMult.clicked.connect(multiplicar)
form_calculadora.pbDiv.clicked.connect(restar)
app_calculadora.exec()