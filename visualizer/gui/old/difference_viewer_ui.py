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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QRadioButton, QSizePolicy, QToolBar,
    QVBoxLayout, QWidget)
from .resources import resources_rc

class Ui_DifferenceViewer(object):
    def setupUi(self, DifferenceViewer):
        if not DifferenceViewer.objectName():
            DifferenceViewer.setObjectName(u"DifferenceViewer")
        DifferenceViewer.resize(959, 705)
        self.action_zoom_in = QAction(DifferenceViewer)
        self.action_zoom_in.setObjectName(u"action_zoom_in")
        icon = QIcon()
        icon.addFile(u":/icons/zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zoom_in.setIcon(icon)
        self.action_zoom_in.setMenuRole(QAction.NoRole)
        self.action_zoom_out = QAction(DifferenceViewer)
        self.action_zoom_out.setObjectName(u"action_zoom_out")
        icon1 = QIcon()
        icon1.addFile(u":/icons/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zoom_out.setIcon(icon1)
        self.action_zoom_out.setMenuRole(QAction.NoRole)
        self.action_zoom_reset = QAction(DifferenceViewer)
        self.action_zoom_reset.setObjectName(u"action_zoom_reset")
        icon2 = QIcon()
        icon2.addFile(u":/icons/zoom-reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_zoom_reset.setIcon(icon2)
        self.action_zoom_reset.setMenuRole(QAction.NoRole)
        self.action_export = QAction(DifferenceViewer)
        self.action_export.setObjectName(u"action_export")
        icon3 = QIcon()
        icon3.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_export.setIcon(icon3)
        self.action_export.setMenuRole(QAction.NoRole)
        self.action_load_img_a = QAction(DifferenceViewer)
        self.action_load_img_a.setObjectName(u"action_load_img_a")
        icon4 = QIcon()
        icon4.addFile(u":/icons/letter-a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_load_img_a.setIcon(icon4)
        self.action_load_img_a.setMenuRole(QAction.NoRole)
        self.action_load_img_b = QAction(DifferenceViewer)
        self.action_load_img_b.setObjectName(u"action_load_img_b")
        icon5 = QIcon()
        icon5.addFile(u":/icons/letter-b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_load_img_b.setIcon(icon5)
        self.action_load_img_b.setMenuRole(QAction.NoRole)
        self.action_show_img_a = QAction(DifferenceViewer)
        self.action_show_img_a.setObjectName(u"action_show_img_a")
        self.action_show_img_a.setMenuRole(QAction.NoRole)
        self.action_show_img_b = QAction(DifferenceViewer)
        self.action_show_img_b.setObjectName(u"action_show_img_b")
        self.action_show_img_b.setMenuRole(QAction.NoRole)
        self.action_show_diff = QAction(DifferenceViewer)
        self.action_show_diff.setObjectName(u"action_show_diff")
        self.action_show_diff.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(DifferenceViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_img_a = QLabel(self.centralwidget)
        self.label_img_a.setObjectName(u"label_img_a")

        self.verticalLayout.addWidget(self.label_img_a)

        self.edit_img_a = QLineEdit(self.centralwidget)
        self.edit_img_a.setObjectName(u"edit_img_a")
        self.edit_img_a.setEnabled(False)
        self.edit_img_a.setFrame(False)

        self.verticalLayout.addWidget(self.edit_img_a)

        self.label_img_b = QLabel(self.centralwidget)
        self.label_img_b.setObjectName(u"label_img_b")

        self.verticalLayout.addWidget(self.label_img_b)

        self.edit_img_b = QLineEdit(self.centralwidget)
        self.edit_img_b.setObjectName(u"edit_img_b")
        self.edit_img_b.setEnabled(False)
        self.edit_img_b.setFrame(False)

        self.verticalLayout.addWidget(self.edit_img_b)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_show_img_a = QRadioButton(self.groupBox)
        self.radio_show_img_a.setObjectName(u"radio_show_img_a")

        self.horizontalLayout.addWidget(self.radio_show_img_a)

        self.radio_show_img_b = QRadioButton(self.groupBox)
        self.radio_show_img_b.setObjectName(u"radio_show_img_b")

        self.horizontalLayout.addWidget(self.radio_show_img_b)

        self.radio_show_diff = QRadioButton(self.groupBox)
        self.radio_show_diff.setObjectName(u"radio_show_diff")

        self.horizontalLayout.addWidget(self.radio_show_diff)


        self.verticalLayout.addWidget(self.groupBox)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.view = QGraphicsView(self.centralwidget)
        self.view.setObjectName(u"view")

        self.verticalLayout.addWidget(self.view)

        DifferenceViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DifferenceViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
        DifferenceViewer.setMenuBar(self.menubar)
        self.toolBar_2 = QToolBar(DifferenceViewer)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setIconSize(QSize(24, 24))
        DifferenceViewer.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)
        self.toolBar = QToolBar(DifferenceViewer)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        DifferenceViewer.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar_2.addAction(self.action_zoom_in)
        self.toolBar_2.addAction(self.action_zoom_out)
        self.toolBar_2.addAction(self.action_zoom_reset)
        self.toolBar_2.addSeparator()
        self.toolBar.addAction(self.action_export)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_load_img_a)
        self.toolBar.addAction(self.action_load_img_b)

        self.retranslateUi(DifferenceViewer)

        QMetaObject.connectSlotsByName(DifferenceViewer)
    # setupUi

    def retranslateUi(self, DifferenceViewer):
        DifferenceViewer.setWindowTitle(QCoreApplication.translate("DifferenceViewer", u"Visualizador de Diferen\u00e7as v0.1", None))
        self.action_zoom_in.setText(QCoreApplication.translate("DifferenceViewer", u"Zoom +", None))
#if QT_CONFIG(tooltip)
        self.action_zoom_in.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Zoom + (Ctrl++)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_zoom_in.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+=", None))
#endif // QT_CONFIG(shortcut)
        self.action_zoom_out.setText(QCoreApplication.translate("DifferenceViewer", u"Zoom -", None))
#if QT_CONFIG(tooltip)
        self.action_zoom_out.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Zoom - (Ctrl+-)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_zoom_out.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.action_zoom_reset.setText(QCoreApplication.translate("DifferenceViewer", u"Zoom 1:1", None))
#if QT_CONFIG(tooltip)
        self.action_zoom_reset.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Zoom 1:1 (Ctrl+0)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_zoom_reset.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.action_export.setText(QCoreApplication.translate("DifferenceViewer", u"Exportar", None))
#if QT_CONFIG(tooltip)
        self.action_export.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Exportar (Ctrl+A)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_export.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_load_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Carregar Imagem A", None))
#if QT_CONFIG(tooltip)
        self.action_load_img_a.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Carregar Imagem A (Ctrl+A)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_load_img_a.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_load_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Carregar Imagem B", None))
#if QT_CONFIG(tooltip)
        self.action_load_img_b.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Carregar Imagem B (Ctrl+B)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_load_img_b.setShortcut(QCoreApplication.translate("DifferenceViewer", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_show_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Show Image A", None))
#if QT_CONFIG(shortcut)
        self.action_show_img_a.setShortcut(QCoreApplication.translate("DifferenceViewer", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.action_show_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Show Image B", None))
#if QT_CONFIG(tooltip)
        self.action_show_img_b.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Show Image B", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_show_img_b.setShortcut(QCoreApplication.translate("DifferenceViewer", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.action_show_diff.setText(QCoreApplication.translate("DifferenceViewer", u"Show Differences", None))
#if QT_CONFIG(tooltip)
        self.action_show_diff.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Show Differences", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_show_diff.setShortcut(QCoreApplication.translate("DifferenceViewer", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.label_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem A:", None))
        self.label_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem B:", None))
        self.groupBox.setTitle(QCoreApplication.translate("DifferenceViewer", u"Visualiza\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.radio_show_img_a.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Exibir Imagem A (1)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_show_img_a.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem A (1)", None))
#if QT_CONFIG(shortcut)
        self.radio_show_img_a.setShortcut(QCoreApplication.translate("DifferenceViewer", u"1", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.radio_show_img_b.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Exibir Imagem B (2)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_show_img_b.setText(QCoreApplication.translate("DifferenceViewer", u"Imagem B (2)", None))
#if QT_CONFIG(shortcut)
        self.radio_show_img_b.setShortcut(QCoreApplication.translate("DifferenceViewer", u"2", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.radio_show_diff.setToolTip(QCoreApplication.translate("DifferenceViewer", u"Exibir Diferen\u00e7as (3)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_show_diff.setText(QCoreApplication.translate("DifferenceViewer", u"Diferen\u00e7as (3)", None))
#if QT_CONFIG(shortcut)
        self.radio_show_diff.setShortcut(QCoreApplication.translate("DifferenceViewer", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("DifferenceViewer", u"toolBar_2", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("DifferenceViewer", u"toolBar", None))
    # retranslateUi

