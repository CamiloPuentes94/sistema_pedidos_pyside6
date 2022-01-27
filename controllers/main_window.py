from PySide6.QtWidgets import QWidget

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from controllers.add_window import AddWindowForm


class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        self.new_recipe_button.clicked.connect(self.open_add_window)
        
    #esta funcion viene de QWidget no es creada por nosotros es de la clase QWidget
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
        
    def open_add_window(self):
        window = AddWindowForm()
        window.show()