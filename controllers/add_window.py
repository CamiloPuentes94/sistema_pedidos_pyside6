from PySide6.QtWidgets import QWidget,QFileDialog


from views.add_edit_window import AddEditWindow
from views.general_custom_ui import GeneralCustomUi

from db import recipes

import shutil

class AddWindowForm(QWidget, AddEditWindow):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # Se llama la funcion de rellenar combo box
        self.ui.fill_category_cb()
        
        # Se cambia el nombre del boton
        self.add_edit_button.setText("Agregar")
        # cuando se realice el click se conecta a la base de datos
        self.add_edit_button.clicked.connect(self.add_recipe)
        # se llama la funcion click para que selecione la imagen
        self.select_img_button.clicked.connect(self.select_img)
        
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
        img_path = self.img_path_to
        # para obtener el valor de un text edit se debe llamar la funcion toPlainText
        ingredients = self.ingredients_text_edit.toPlainText()
        directions = self.directions_text_edit.toPlainText()
        
        data = (
            title,
            category,
            url,
            budget,
            img_path,
            ingredients,
            directions
        )
        
        if recipes.insert(data):
            self.save_img()
            print("Recipe Added")
            self.clear_inputs()
            
    def select_img(self):
        
        # con esta funcion de QFileDialog abre ventana para selecionar retorna una lista con dos datos y el primer dato es la direccion del archivo
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        # se guarda la direccion del archivo y con la funcion split nos divide con un / y se pone -1 para tomar el ultimo numero de la lista
        img_name = self.img_path_from.split("/")[-1]
        # esta varible contiene el nombre de la carpeta donde tendremos las imagenes y el nombre del archivo
        self.img_path_to = f"recipe_images\{img_name}"
        # se envia el nombre del archivo
        self.image_path_line_edit.setText(img_name)
        
        
    def save_img(self):
        # de este modo se guarda en la carpeta de recipes y se deb importar de python shutil
        shutil.copy(self.img_path_from, "recipe_images")
        
        
    def  clear_inputs(self):
        # con la funcion clear se limpian todos los inputs de la pantalla
        self.title_line_edit.clear()
        self.category_combo_box.clear()
        self.url_line_edit.clear()
        self.budget_line_edit.clear()
        self.ingredients_text_edit.clear()
        self.directions_text_edit.clear()