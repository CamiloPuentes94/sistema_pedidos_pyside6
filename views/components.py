from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

class RecipeImg(QLabel):
    
    def __init__(self, img_path):
        super().__init__()
        
        # con esta variable cargamos la imgen con el path y le damos el tamaño a la imagen
        self.img = QPixmap(img_path).scaledToWidth(200)
        #con esta funcion ponemos visualizar la imagen
        self.setPixmap(self.img)