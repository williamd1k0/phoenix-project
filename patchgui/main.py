
import sys, os
# from PySide.QtCore import *
from PySide.QtGui import *

def get_ds_src():
    pass

def apply_patch():
    pass


def get_patch_button():
    buttonok = QPushButton("Aplicar")
    buttonok.setEnabled(False)
    buttonok.clicked.connect(apply_patch)
    return buttonok


class Form(QWidget):
 
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Phoenix Wright | PT-BR")
        self.fix_size(400, 200)
        
        app_group = QVBoxLayout()

        patchfile_g = QGroupBox("Arquivo do patch")
        layout = QHBoxLayout()
        edit = QLineEdit()
        button = QPushButton("Selecionar...")
        layout.addWidget(edit)
        layout.addWidget(button)
        patchfile_g.setLayout(layout)

        ds_g = QGroupBox("Arquivo DS")
        layout2 = QHBoxLayout()
        edit2 = QLineEdit()
        button2 = QPushButton("Selecionar...")
        layout2.addWidget(edit2)
        layout2.addWidget(button2)
        ds_g.setLayout(layout2)

        patch_g = QGroupBox()
        layout3 = QHBoxLayout()
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(sys.exit)
        self.patch_button = get_patch_button()
        
        layout3.addWidget(self.cancel_button)
        layout3.addWidget(self.patch_button)
        patch_g.setLayout(layout3)

        app_group.addWidget(patchfile_g)
        app_group.addWidget(ds_g)
        app_group.addWidget(patch_g)
        self.setLayout(app_group)
    

    def fix_size(self, w, h):
        self.resize(w, h)
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        


def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())