from PySide6.QtWidgets import QWidget


from views.add_edit_window import AddEditWindow
from views.general_custom_ui import GeneralCustomUi

from db import recipes

class AddWindowForm(QWidget, AddEditWindow):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
    #esta funcion viene de QWidget no es creada por nosotros es de la clase QWidget, se debe poner para poder arrastrar la ventana
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
        
    def add_recipe(self):
        # se obtiene el valor del titulo por medio de la funcion text
        title = self.title_line_edit.text()
        # se obtiene el valor seleccionado de la funcion curentText del combo box
        category = self.category_combo_box.currentText()
        # Para obetener el valor de url se hace con la funcion text
        url = self.url_line_edit.text()
        # Para obetener el valor de budget se hace con la funcion text
        budget = self.budget_line_edit.text()
        # para obtener el valor de un text edit se debe llamar la funcion toPlainText
        ingredients = self.ingredients_text_edit.toPlainText()
        directions = self.directions_text_edit.toPlainText()
        
        data = (
            title,
            category,
            url,
            budget,
            ingredients,
            directions
        )
        
        if recipes.insert(data):
            print("Recipe Added")