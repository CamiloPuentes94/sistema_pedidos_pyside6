from PySide6.QtWidgets import QWidget


from views.add_edit_window import AddEditWindow
from views.general_custom_ui import GeneralCustomUi

class AddWindowForm(QWidget, AddEditWindow):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)