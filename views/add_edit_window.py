# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class AddEditWindow(object):
    def setupUi(self, AddEditWindow):
        if not AddEditWindow.objectName():
            AddEditWindow.setObjectName(u"AddEditWindow")
        AddEditWindow.resize(1009, 491)
        AddEditWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(AddEditWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(AddEditWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_grame = QFrame(self.background_frame)
        self.top_bar_grame.setObjectName(u"top_bar_grame")
        self.top_bar_grame.setMinimumSize(QSize(0, 40))
        self.top_bar_grame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_grame.setStyleSheet(u"background-color: rgb(30, 61, 89);")
        self.top_bar_grame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_grame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_grame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tittle_label = QLabel(self.top_bar_grame)
        self.tittle_label.setObjectName(u"tittle_label")
        self.tittle_label.setStyleSheet(u"color:white\n"
"")

        self.horizontalLayout_3.addWidget(self.tittle_label)

        self.buttons_holder_frame = QFrame(self.top_bar_grame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(0, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(40, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(40, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(80, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_grame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setEnabled(True)
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 49, 16))
        self.tittle_lene_edit = QLineEdit(self.content_frame)
        self.tittle_lene_edit.setObjectName(u"tittle_lene_edit")
        self.tittle_lene_edit.setGeometry(QRect(10, 20, 291, 30))
        self.tittle_lene_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 71, 16))
        self.categoria_combo_box = QComboBox(self.content_frame)
        self.categoria_combo_box.setObjectName(u"categoria_combo_box")
        self.categoria_combo_box.setGeometry(QRect(10, 90, 291, 30))
        self.url_line_edit = QLineEdit(self.content_frame)
        self.url_line_edit.setObjectName(u"url_line_edit")
        self.url_line_edit.setGeometry(QRect(10, 150, 291, 30))
        self.url_line_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 141, 16))
        self.budhet_lene_edit = QLineEdit(self.content_frame)
        self.budhet_lene_edit.setObjectName(u"budhet_lene_edit")
        self.budhet_lene_edit.setGeometry(QRect(10, 210, 291, 30))
        self.budhet_lene_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.label_4 = QLabel(self.content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 81, 16))
        self.image_path_line_edit = QLineEdit(self.content_frame)
        self.image_path_line_edit.setObjectName(u"image_path_line_edit")
        self.image_path_line_edit.setGeometry(QRect(10, 280, 221, 30))
        self.image_path_line_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.label_5 = QLabel(self.content_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 260, 131, 16))
        self.select_img_button = QToolButton(self.content_frame)
        self.select_img_button.setObjectName(u"select_img_button")
        self.select_img_button.setGeometry(QRect(240, 280, 31, 31))
        self.select_img_button.setStyleSheet(u"QToolButton::hover{background-color: #ff640};")
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_img_button.setIcon(icon4)
        self.select_img_button.setIconSize(QSize(50, 50))
        self.add_edit_button = QPushButton(self.content_frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setGeometry(QRect(50, 320, 201, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.add_edit_button.setFont(font)
        self.add_edit_button.setStyleSheet(u"QPushButton{\n"
"background-color: #ff6e40;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton::hover {background-color: #ffc13b};")
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edit_button.setIcon(icon5)
        self.add_edit_button.setIconSize(QSize(20, 20))
        self.cancel_button = QPushButton(self.content_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(50, 360, 201, 30))
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
"background-color: #6b7b8c;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton::hover {background-color: #ffc13b};")
        icon6 = QIcon()
        icon6.addFile(u"../assets/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon6)
        self.cancel_button.setIconSize(QSize(20, 20))
        self.label_6 = QLabel(self.content_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 10, 131, 16))
        self.ingredients_text_edit = QPlainTextEdit(self.content_frame)
        self.ingredients_text_edit.setObjectName(u"ingredients_text_edit")
        self.ingredients_text_edit.setGeometry(QRect(320, 30, 311, 371))
        self.ingredients_text_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.directions_text_edit = QPlainTextEdit(self.content_frame)
        self.directions_text_edit.setObjectName(u"directions_text_edit")
        self.directions_text_edit.setGeometry(QRect(640, 30, 311, 371))
        self.directions_text_edit.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: 1px solid #ff6e40;")
        self.label_7 = QLabel(self.content_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(640, 10, 131, 16))

        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(AddEditWindow)

        QMetaObject.connectSlotsByName(AddEditWindow)
    # setupUi

    def retranslateUi(self, AddEditWindow):
        AddEditWindow.setWindowTitle(QCoreApplication.translate("AddEditWindow", u"Form", None))
        self.tittle_label.setText(QCoreApplication.translate("AddEditWindow", u"Recipes_Organizer", None))
        self.minimize_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("AddEditWindow", u"Titulo", None))
        self.label_2.setText(QCoreApplication.translate("AddEditWindow", u"Categoria", None))
        self.categoria_combo_box.setPlaceholderText(QCoreApplication.translate("AddEditWindow", u"Seleccione una categoria", None))
        self.label_3.setText(QCoreApplication.translate("AddEditWindow", u"URL de una Guia", None))
        self.label_4.setText(QCoreApplication.translate("AddEditWindow", u"presupuesto", None))
        self.label_5.setText(QCoreApplication.translate("AddEditWindow", u"Seleccione una imagen", None))
        self.select_img_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.add_edit_button.setText(QCoreApplication.translate("AddEditWindow", u"text", None))
        self.cancel_button.setText(QCoreApplication.translate("AddEditWindow", u"cancelar", None))
        self.label_6.setText(QCoreApplication.translate("AddEditWindow", u"Ingredientes", None))
        self.label_7.setText(QCoreApplication.translate("AddEditWindow", u"Pasos de realizacion", None))
    # retranslateUi
