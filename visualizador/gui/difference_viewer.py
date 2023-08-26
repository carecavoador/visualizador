# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'difference_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DifferenceViewer(object):
    def setupUi(self, DifferenceViewer):
        if not DifferenceViewer.objectName():
            DifferenceViewer.setObjectName(u"DifferenceViewer")
        DifferenceViewer.resize(959, 705)
        self.centralwidget = QWidget(DifferenceViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_img_a = QGridLayout()
        self.layout_img_a.setObjectName(u"layout_img_a")
        self.edit_img_a = QLineEdit(self.centralwidget)
        self.edit_img_a.setObjectName(u"edit_img_a")

        self.layout_img_a.addWidget(self.edit_img_a, 1, 1, 1, 1)

        self.btn_img_a = QPushButton(self.centralwidget)
        self.btn_img_a.setObjectName(u"btn_img_a")

        self.layout_img_a.addWidget(self.btn_img_a, 1, 0, 1, 1)

        self.label_img_a = QLabel(self.centralwidget)
        self.label_img_a.setObjectName(u"label_img_a")

        self.layout_img_a.addWidget(self.label_img_a, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_img_a)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.layout_img_b = QGridLayout()
        self.layout_img_b.setObjectName(u"layout_img_b")
        self.btn_img_b = QPushButton(self.centralwidget)
        self.btn_img_b.setObjectName(u"btn_img_b")

        self.layout_img_b.addWidget(self.btn_img_b, 1, 0, 1, 1)

        self.edit_img_b = QLineEdit(self.centralwidget)
        self.edit_img_b.setObjectName(u"edit_img_b")

        self.layout_img_b.addWidget(self.edit_img_b, 1, 1, 1, 1)

        self.label_img_b = QLabel(self.centralwidget)
        self.label_img_b.setObjectName(u"label_img_b")

        self.layout_img_b.addWidget(self.label_img_b, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.layout_img_b)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.layout_zoom = QHBoxLayout()
        self.layout_zoom.setObjectName(u"layout_zoom")
        self.btn_zoom_in = QPushButton(self.centralwidget)
        self.btn_zoom_in.setObjectName(u"btn_zoom_in")

        self.layout_zoom.addWidget(self.btn_zoom_in)

        self.btn_zoom_out = QPushButton(self.centralwidget)
        self.btn_zoom_out.setObjectName(u"btn_zoom_out")

        self.layout_zoom.addWidget(self.btn_zoom_out)

        self.btn_zoom_reset = QPushButton(self.centralwidget)
        self.btn_zoom_reset.setObjectName(u"btn_zoom_reset")

        self.layout_zoom.addWidget(self.btn_zoom_reset)

        self.btn_export = QPushButton(self.centralwidget)
        self.btn_export.setObjectName(u"btn_export")

        self.layout_zoom.addWidget(self.btn_export)


        self.verticalLayout.addLayout(self.layout_zoom)

        self.view = QGraphicsView(self.centralwidget)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)

        DifferenceViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DifferenceViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
        DifferenceViewer.setMenuBar(self.menubar)

        self.retranslateUi(DifferenceViewer)

        QMetaObject.connectSlotsByName(DifferenceViewer)
    # setupUi

    def retranslateUi(self, DifferenceViewer):
        DifferenceViewer.setWindowTitle(QCoreApplication.translate("DifferenceViewer", u"Visualizador de Diferen\u00e7as v0.1", None))
        self.btn_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Carregar...", None))
        self.label_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem A:", None))
        self.btn_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Carregar...", None))
        self.label_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem B:", None))
        self.btn_zoom_in.setText(QCoreApplication.translate("DifferenceViewer", u"Zoom +", None))
        self.btn_zoom_out.setText(QCoreApplication.translate("DifferenceViewer", u"Zoom -", None))
        self.btn_zoom_reset.setText(QCoreApplication.translate("DifferenceViewer", u"Resetar Zoom", None))
        self.btn_export.setText(QCoreApplication.translate("DifferenceViewer", u"Exportar", None))
    # retranslateUi

