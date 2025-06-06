from PySide6.QtWidgets import QMainWindow

from src.Ui.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.txtBorrar.clicked.connect(self.borrar)


    def guardar(self):
        print('se hizo clic')
        print(self.ui.txtNombre.text())
        print(self.ui.txtApellido.text())
        print(self.ui.txtCedula.text())
        print(self.ui.cbSexo.currentText())
        print(self.ui.txtEmail.text())

    def borrar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtCedula.setText('')
        self.ui.txtEmail.setText('')
        self.ui.cbSexo.setCurrentText('seleccionar')

