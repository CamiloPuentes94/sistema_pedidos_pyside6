from PySide6.QtWidgets import QWidget, QTableWidgetItem

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from controllers.add_window import AddWindowForm
from views import components

from db import recipes

class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        
        self.config_table()
        self.populate_table()
        
        self.new_recipe_button.clicked.connect(self.open_add_window)
        
    #esta funcion viene de QWidget no es creada por nosotros es de la clase QWidget
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
        
    def open_add_window(self):
        window = AddWindowForm()
        window.show()
     
    def config_table(self):
        # en esta variable colocamos el nombre de las columnas a visualizar
        colum_labels = ("ID", "IMG", "TITULO", "CATEGORIA")
        # Se envian la cantidad de columnas que va a tener
        self.recipes_table.setColumnCount(len(colum_labels))
        #Se envian lo labels de la columna
        self.recipes_table.setHorizontalHeaderLabels(colum_labels)
        #Se cambia el ancho de las columnas para visualizar bien las imagenes
        self.recipes_table.setColumnWidth(1, 200)
        self.recipes_table.verticalHeader().setDefaultSectionSize(200)
     
        
    def populate_table(self):
        data = recipes.select_all()
        
        self.recipes_table.setRowCount(len(data))
        
        # este for se capturan los datos de las filas
        for (index_row, row) in enumerate(data):
            # en este for se captura los datos de cada celda
            for (index_cell, cell) in enumerate(row):
                if index_cell == 1:
                    self.recipes_table.setCellWidget(
                        index_row,
                        index_cell,
                        components.RecipeImg(cell)
                    )
                else:
                    self.recipes_table.setItem(
                        index_row,
                        index_cell,
                        QTableWidgetItem(str(cell))
                    )