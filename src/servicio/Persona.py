from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.Ui.vtnPrincipal import Ui_vtnPrincipal
from src.datos.personaDao import PersonaDao
from src.dominio.persona import Persona


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.txtBorrar.clicked.connect(self.borrar)
        self.ui.txtCedula.setValidator(QIntValidator())


    def guardar(self):
        if (self.ui.txtNombre.text() == "" or self.ui.txtApellido.text() == "" or self.ui.txtCedula.text() == "" or len(self.ui.txtCedula.text()) < 10
                or self.ui.cbSexo.currentText() == "Seleccionar" or self.ui.txtEmail.text() == ""):
            QMessageBox.warning(self, "Advertencia", "Completar datos")

        else:
            sexo_completo = self.ui.cbSexo.currentText()
            sexo_para_db = sexo_completo[0].upper()
            persona = Persona(
                nombre = self.ui.txtNombre.text(),
                apellido = self.ui.txtApellido.text(),
               cedula = self.ui.txtCedula.text(),
                sexo = sexo_para_db,
                email = self.ui.txtEmail.text())
            #print(persona)
            if PersonaDao.insertar_persona(persona) == -1:
                QMessageBox.critical(self, "Error", "No se pudo guardar.")
            #PersonaDao.insertar_persona(persona)
            else:
                self.ui.statusbar.showMessage('Se guardo correctamente', 3000)
                self.borrar()





    def borrar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtCedula.setText('')
        self.ui.txtEmail.setText('')
        self.ui.cbSexo.setCurrentText('seleccionar')




