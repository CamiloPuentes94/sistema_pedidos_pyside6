from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame

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
        #Se cambia el valor vertical de las columnas
        self.recipes_table.verticalHeader().setDefaultSectionSize(200)
        # ocultar la columna id
        self.recipes_table.setColumnHidden(0, True)
        # Al pulsar una columna se seleccionara toda la fila
        self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
     
        
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
            self.recipes_table.setCellWidget(
                index_row, 4, self.build_action_buttons()
            )
                    
    def build_action_buttons(self):
        # Boton de visualizar
        view_button = components.Button("view", "#17A2BB")
        # boton de editar
        edit_button = components.Button("edit", "#007BFF")
        # boton de eliminar
        delete_button = components.Button("delete", "#DC3545")
        
        # layout horizontal de los botones
        buttons_layout = QHBoxLayout()
        #Se pone el orden como se quiere poner los botones
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)
        
        # Se deja los botones dentro de un frame
        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)
        
        return buttons_frame