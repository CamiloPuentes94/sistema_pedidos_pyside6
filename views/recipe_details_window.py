# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_details_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(718, 728)
        DetailWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_widget_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout_3.addWidget(self.top_bar_grame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.recipe_pic_label = QLabel(self.frame)
        self.recipe_pic_label.setObjectName(u"recipe_pic_label")
        self.recipe_pic_label.setMaximumSize(QSize(170, 170))

        self.horizontalLayout.addWidget(self.recipe_pic_label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.recipe_tittle_label = QLabel(self.frame_3)
        self.recipe_tittle_label.setObjectName(u"recipe_tittle_label")
        self.recipe_tittle_label.setGeometry(QRect(30, 10, 331, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.recipe_tittle_label.setFont(font)
        self.recipe_tittle_label.setStyleSheet(u"color: #6b7b8c;")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 61, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.recipe_category_label = QLabel(self.frame_3)
        self.recipe_category_label.setObjectName(u"recipe_category_label")
        self.recipe_category_label.setGeometry(QRect(100, 50, 351, 20))
        self.recipe_url_label_ = QLabel(self.frame_3)
        self.recipe_url_label_.setObjectName(u"recipe_url_label_")
        self.recipe_url_label_.setGeometry(QRect(100, 80, 351, 20))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 61, 16))
        self.label_2.setFont(font1)
        self.recipe_budget_label_ = QLabel(self.frame_3)
        self.recipe_budget_label_.setObjectName(u"recipe_budget_label_")
        self.recipe_budget_label_.setGeometry(QRect(100, 110, 361, 16))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 16))
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.recipe_tittle_label_2 = QLabel(self.frame_2)
        self.recipe_tittle_label_2.setObjectName(u"recipe_tittle_label_2")
        self.recipe_tittle_label_2.setFont(font)
        self.recipe_tittle_label_2.setStyleSheet(u"color: #6b7b8c;")

        self.verticalLayout_5.addWidget(self.recipe_tittle_label_2)

        self.ingredients_text_edit = QPlainTextEdit(self.frame_2)
        self.ingredients_text_edit.setObjectName(u"ingredients_text_edit")

        self.verticalLayout_5.addWidget(self.ingredients_text_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.recipe_tittle_label_3 = QLabel(self.frame_2)
        self.recipe_tittle_label_3.setObjectName(u"recipe_tittle_label_3")
        self.recipe_tittle_label_3.setFont(font)
        self.recipe_tittle_label_3.setStyleSheet(u"color: #6b7b8c;")

        self.verticalLayout_6.addWidget(self.recipe_tittle_label_3)

        self.directions_text_edit = QPlainTextEdit(self.frame_2)
        self.directions_text_edit.setObjectName(u"directions_text_edit")

        self.verticalLayout_6.addWidget(self.directions_text_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.tittle_label.setText(QCoreApplication.translate("DetailWindow", u"Recipes_Organizer", None))
        self.minimize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("DetailWindow", u"...", None))
        self.recipe_pic_label.setText("")
        self.recipe_tittle_label.setText(QCoreApplication.translate("DetailWindow", u"Titulo", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"Categoria:", None))
        self.recipe_category_label.setText(QCoreApplication.translate("DetailWindow", u"Categoria", None))
        self.recipe_url_label_.setText(QCoreApplication.translate("DetailWindow", u"URL", None))
        self.label_2.setText(QCoreApplication.translate("DetailWindow", u"URL:", None))
        self.recipe_budget_label_.setText(QCoreApplication.translate("DetailWindow", u"Presupuesto", None))
        self.label_3.setText(QCoreApplication.translate("DetailWindow", u"Presupuesto:", None))
        self.recipe_tittle_label_2.setText(QCoreApplication.translate("DetailWindow", u"Ingredientes", None))
        self.recipe_tittle_label_3.setText(QCoreApplication.translate("DetailWindow", u"Proceso de realizacion", None))
    # retranslateUi

