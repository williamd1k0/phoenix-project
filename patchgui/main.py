
import sys, os.path
from subprocess import call as process_call
from PySide.QtGui import *

if 'python.exe' in sys.executable:
    PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
else:
    PATH = os.path.dirname(os.path.realpath(sys.executable))

if hasattr(sys, '_MEIPASS'):
    RES_PATH = sys._MEIPASS
else:
    RES_PATH = PATH

PATCH_FILE = os.path.join(RES_PATH, 'phoenix.dt')
XDELTA = os.path.join(RES_PATH, 'xdelta.exe')


class Window(QWidget):
 
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Phoenix Wright | PT-BR")
        self.setWindowIcon(QIcon(os.path.join(RES_PATH, 'icon.png')))
        self.fix_size(390, 355)
        
        app_group = QVBoxLayout()

        patchfile_g = QGroupBox()
        layout = QHBoxLayout()
        label = QLabel()
        label.setPixmap(QPixmap(os.path.join(RES_PATH, "please.jpg")))
        layout.addWidget(label)
        patchfile_g.setLayout(layout)

        ds_g = QGroupBox("Selecionar ROM")
        layout2 = QHBoxLayout()
        self.edit = QLineEdit()
        self.edit.textChanged.connect(self.check_file)
        self.button_ds = QPushButton("Selecionar...")
        self.button_ds.clicked.connect(self.get_ds_src)
        layout2.addWidget(self.edit)
        layout2.addWidget(self.button_ds)
        ds_g.setLayout(layout2)

        patch_g = QGroupBox()
        layout3 = QHBoxLayout()
        self.quit_button = QPushButton("Fechar")
        self.quit_button.clicked.connect(sys.exit)
        
        self.patch_button = QPushButton("Aplicar")
        self.patch_button.setEnabled(False)
        self.patch_button.clicked.connect(self.apply_patch)
        
        layout3.addWidget(self.quit_button)
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
    
    def check_file(self):
        if self.edit.text().endswith('.nds'):
            self.patch_button.setEnabled(True)
        else:
            self.patch_button.setEnabled(False)
    
    def get_ds_src(self):
        self.nds_file = QFileDialog.getOpenFileName(None, "Selecionar ROM", PATH, "Rom (*.*)")
        self.edit.setText(self.nds_file[0])
    
    def apply_patch(self):
        proc = process_call([XDELTA], creationflags=0x08000000)
        if proc == 0:
            msg = QMessageBox(QMessageBox.Information,
                'Phoenix Wright | PT-BR', 'Patch concluído com sucesso!',
                buttons=QMessageBox.Ok, parent=self)
        else:
            msg = QMessageBox(QMessageBox.Critical,
                'Phoenix Wright | PT-BR', 'Algum erro ocorreu!',
                buttons=QMessageBox.Ok, parent=self)
        space = ' ' * int(len(msg.text())/2)
        msg.setText(msg.text() + space)
        ret = msg.exec_()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())