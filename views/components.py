from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon

class RecipeImg(QLabel):
    
    def __init__(self, img_path):
        super().__init__()
        
        # con esta variable cargamos la imgen con el path y le damos el tamaño a la imagen
        self.img = QPixmap(img_path).scaledToWidth(200)
        #con esta funcion ponemos visualizar la imagen
        self.setPixmap(self.img)
        

class Button(QPushButton):
    
    def __init__(self, icon, color):
        # funcion para tamaño de boton
        self.setMinimumSize(30, 30)
        # funcion para ponerles un icono
        self.setIcon(QIcon(f"assets/icons/{icon}.png"))
        # funcion para cambiar color o cambiar estilo
        self.setStyleSheet(f"border-radius: 15px; background-color {color};")
        
    
        