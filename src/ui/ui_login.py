# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 141, 571))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(660, 0, 141, 571))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 0, 521, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(140, 90, 521, 71))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(140, 160, 4, 4))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(220, 160, 61, 31))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 61, 31))

        self.verticalLayout_9.addWidget(self.frame_2)

        self.verticalLayoutWidget_9 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(520, 160, 61, 70))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.loginButton = QPushButton(self.verticalLayoutWidget_9)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(51, 0))
        self.loginButton.setMaximumSize(QSize(20, 100))
        self.loginButton.setIconSize(QSize(10, 30))

        self.verticalLayout_10.addWidget(self.loginButton)

        self.verticalLayoutWidget_10 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(220, 200, 61, 31))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.verticalLayoutWidget_10)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 61, 31))

        self.verticalLayout_11.addWidget(self.frame_3)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(220, 250, 351, 31))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(220, 280, 351, 31))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.verticalLayoutWidget_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.signUpButton = QPushButton(self.frame_4)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setGeometry(QRect(119, 0, 111, 32))

        self.verticalLayout_6.addWidget(self.frame_4)

        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(280, 200, 241, 31))
        self.password.setMaxLength(100)
        self.password.setEchoMode(QLineEdit.Password)
        self.id = QLineEdit(self.centralwidget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(280, 160, 241, 31))
        self.id.setEchoMode(QLineEdit.Normal)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">\ub85c\uadf8\uc778</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\">ID</p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"\ub85c\uadf8\uc778", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\">PW</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#777777;\">\uacc4\uc815\uc774 \uc5c6\uc73c\uc2e0\uac00\uc694?</span></p></body></html>", None))
        self.signUpButton.setText(QCoreApplication.translate("LoginWindow", u"\ud68c\uc6d0\uac00\uc785", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
        self.id.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud558\uc138\uc694.", None))
    # retranslateUi

