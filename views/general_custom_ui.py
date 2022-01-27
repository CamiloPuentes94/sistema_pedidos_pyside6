from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GeneralCustomUi():
    def __init__(self,ui):
        self.ui = ui
        
        self.remove_default_title_bar()
        # Con la funcion mouseMoveEvent captura el moviento del mouse cuando pasa por widget
        self.ui.top_bar_grame.mouseMoveEvent = self.move_window
        self.set_window_shadow()
        
        
    def maximize_window(self):
        # con esta funcion maximizamos la ventana de la aplicacion
        self.ui.showMaximized()
        # con esta funcion ocultamos el boton de maximizar
        self.ui.maximize_button.setVisible(False)
        
        
        
        
    # con esta funcion removemos la parte     
    def remove_default_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
    
    # esta funcion muestra la posicion de la ventana arrastrada
    def mouse_press_event(self, event):
        self.drag_pos = event.globalPos()
    
    # Esta funcion se realiza el movimiento de la pantalla
    def move_window(self, event):
        # si se pulsa el click izquierdo en el widget
        if event.buttons() == Qt.LeftButton:
            # se obtiene la posicion actual de la ventana cuando tiene presionado el boton izquierdo, se resta la posicion que esta siendo arrastrada
            self.ui.move(self.ui.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()
    
    # con esta funcion le vamos a poder sombra a la ventana
    
    def set_window_shadow(self):
        # obtine el objeto de la clase, se pasa la venta parent 
        shadow = QGraphicsDropShadowEffect(self.ui)
        # se envia la propiedad para que tan borroso se vera la sombra
        shadow.setBlurRadius(25)
        # esto se pone para que la sombre se vea alrededor de la ventana
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        # Se indica el color de la sombra
        shadow.setColor("#000000")
        # Se indica en el frame backgroud el efecto de sombra
        self.ui.background_frane.setGraphicsEffect(shadow)