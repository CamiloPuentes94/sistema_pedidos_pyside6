from PySide6.QtWidgets import QWidget
from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi


class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
    #esta funcion viene de QWidget no es creada por nosotros es de la clase QWidget
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)