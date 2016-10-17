# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openWECv2.ui'
#
# Created: Wed May 06 10:39:04 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from matplotlib.backends import qt_compat
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from functools import partial
import matplotlib.tri as tri
from mpl_toolkits.mplot3d import Axes3D
import nemoh as ne
import sys
import os
import shutil as sh
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs
 
    def __del__(self):
        self.wait()
 
    def run(self):
        self.function(*self.args,**self.kwargs)
        return

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.fig.patch.set_facecolor('white')
        #
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def compute_initial_figure(self):
        t = [0,0]
        s = [0,0]
        self.axes.plot(t, s)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    def setupUi(self, MainWindow):
        MainWindow.resize(1556, 987)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./src/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        # Mesh tab
        self.tabMesh = QtGui.QWidget()
        self.tabMesh.setObjectName(_fromUtf8("tabMesh"))
        self.gridLayout = QtGui.QGridLayout(self.tabMesh)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.infoConsoleLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.infoConsoleLabel.setFont(font)
        self.infoConsoleLabel.setObjectName(_fromUtf8("infoConsoleLabel"))
        self.verticalLayout_2.addWidget(self.infoConsoleLabel)
        self.messageBox = QtGui.QTextEdit(self.tabMesh)
        self.messageBox.setEnabled(True)
        self.messageBox.setReadOnly(True)
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.verticalLayout_2.addWidget(self.messageBox)
        self.visualisationLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.visualisationLabel.setFont(font)
        self.visualisationLabel.setObjectName(_fromUtf8("visualisationLabel"))
        self.verticalLayout_2.addWidget(self.visualisationLabel)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.geoProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.geoProp.setFont(font)
        self.geoProp.setObjectName(_fromUtf8("geoProp"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.geoProp)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sketchShape = QtGui.QLabel(self.tabMesh)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sketchShape.sizePolicy().hasHeightForWidth())
        self.sketchShape.setSizePolicy(sizePolicy)
        self.sketchShape.setMaximumSize(QtCore.QSize(512, 384))
        self.sketchShape.setText(_fromUtf8(""))
        self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/pelamis_shape.png")))
        self.sketchShape.setScaledContents(True)
        self.sketchShape.setObjectName(_fromUtf8("sketchShape"))
        self.horizontalLayout.addWidget(self.sketchShape)
        self.formLayout_3.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.lengthLabel = QtGui.QLabel(self.tabMesh)
        self.lengthLabel.setObjectName(_fromUtf8("lengthLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.lengthLabel)
        self.lengthBox = QtGui.QLineEdit(self.tabMesh)
        self.lengthBox.setObjectName(_fromUtf8("lengthBox"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lengthBox)
        self.heightLabel = QtGui.QLabel(self.tabMesh)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.heightLabel)
        self.heightBox = QtGui.QLineEdit(self.tabMesh)
        self.heightBox.setObjectName(_fromUtf8("heightBox"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.heightBox)
        self.widthLabel = QtGui.QLabel(self.tabMesh)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.widthLabel)
        self.widthBox = QtGui.QLineEdit(self.tabMesh)
        self.widthBox.setObjectName(_fromUtf8("widthBox"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.widthBox)
        self.spacingLabel = QtGui.QLabel(self.tabMesh)
        self.spacingLabel.setObjectName(_fromUtf8("spacingLabel"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.spacingLabel)
        self.spacingBox = QtGui.QLineEdit(self.tabMesh)
        self.spacingBox.setObjectName(_fromUtf8("spacingBox"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.spacingBox)
        self.genProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.genProp.setFont(font)
        self.genProp.setObjectName(_fromUtf8("genProp"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.genProp)
        self.waterDepthLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.waterDepthLabel.setFont(font)
        self.waterDepthLabel.setObjectName(_fromUtf8("waterDepthLabel"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.waterDepthLabel)
        self.waterDepthBox = QtGui.QLineEdit(self.tabMesh)
        self.waterDepthBox.setObjectName(_fromUtf8("waterDepthBox"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.waterDepthBox)
        self.rhoLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.rhoLabel.setFont(font)
        self.rhoLabel.setObjectName(_fromUtf8("rhoLabel"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.rhoLabel)
        self.rhoBox = QtGui.QLineEdit(self.tabMesh)
        self.rhoBox.setObjectName(_fromUtf8("rhoBox"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.rhoBox)
        self.MeshProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.MeshProp.setFont(font)
        self.MeshProp.setObjectName(_fromUtf8("MeshProp"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.MeshProp)
        self.nPanelLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.nPanelLabel.setFont(font)
        self.nPanelLabel.setObjectName(_fromUtf8("nPanelLabel"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.LabelRole, self.nPanelLabel)
        self.nPanelBox = QtGui.QLineEdit(self.tabMesh)
        self.nPanelBox.setObjectName(_fromUtf8("nPanelBox"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.FieldRole, self.nPanelBox)
        self.meshButton = QtGui.QPushButton(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.meshButton.setFont(font)
        self.meshButton.setObjectName(_fromUtf8("meshButton"))
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.FieldRole, self.meshButton)
        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 1)

        self.mplMesh = MyStaticMplCanvas(self.tabMesh, width=5, height=4, dpi=100)
        self.ntbMesh = NavigationToolbar(self.mplMesh, self.tabMesh)
        self.verticalLayout_2.addWidget(self.mplMesh)
        self.verticalLayout_2.addWidget(self.ntbMesh)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabMesh, _fromUtf8(""))
        # Nemoh Tab
        self.tabNemoh = QtGui.QWidget()
        self.tabNemoh.setObjectName(_fromUtf8("tabNemoh"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabNemoh)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelBEM = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelBEM.setFont(font)
        self.labelBEM.setObjectName(_fromUtf8("labelBEM"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelBEM)
        self.label = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.omegaLabel = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.omegaLabel.setFont(font)
        self.omegaLabel.setObjectName(_fromUtf8("omegaLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.omegaLabel)
        self.omegaStart = QtGui.QLineEdit(self.tabNemoh)
        self.omegaStart.setObjectName(_fromUtf8("omegaStart"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.omegaStart)
        self.omegaStop = QtGui.QLineEdit(self.tabNemoh)
        self.omegaStop.setObjectName(_fromUtf8("omegaStop"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.omegaStop)
        self.omegaStep = QtGui.QLineEdit(self.tabNemoh)
        self.omegaStep.setObjectName(_fromUtf8("omegaStep"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.omegaStep)
        self.label_2 = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_2)
        self.wavDirStart = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStart.setObjectName(_fromUtf8("wavDirStart"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.wavDirStart)
        self.wavDirStop = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStop.setObjectName(_fromUtf8("wavDirStop"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.wavDirStop)
        self.wavDirStep = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStep.setObjectName(_fromUtf8("wavDirStep"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.wavDirStep)
        self.irfLabel = QtGui.QLabel(self.tabNemoh)
        self.irfLabel.setObjectName(_fromUtf8("irfLabel"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.irfLabel)
        self.irfCheck = QtGui.QCheckBox(self.tabNemoh)
        self.irfCheck.setText(_fromUtf8(""))
        self.irfCheck.setObjectName(_fromUtf8("irfCheck"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.irfCheck)
        self.irfDur = QtGui.QLineEdit(self.tabNemoh)
        self.irfDur.setObjectName(_fromUtf8("irfDur"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.FieldRole, self.irfDur)
        self.irfStep = QtGui.QLineEdit(self.tabNemoh)
        self.irfStep.setObjectName(_fromUtf8("irfStep"))
        self.formLayout_2.setWidget(12, QtGui.QFormLayout.FieldRole, self.irfStep)
        self.kochinLabel = QtGui.QLabel(self.tabNemoh)
        self.kochinLabel.setObjectName(_fromUtf8("kochinLabel"))
        self.formLayout_2.setWidget(13, QtGui.QFormLayout.LabelRole, self.kochinLabel)
        self.kochinCheck = QtGui.QCheckBox(self.tabNemoh)
        self.kochinCheck.setText(_fromUtf8(""))
        self.kochinCheck.setObjectName(_fromUtf8("kochinCheck"))
        self.formLayout_2.setWidget(13, QtGui.QFormLayout.FieldRole, self.kochinCheck)
        self.kochinStart = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStart.setObjectName(_fromUtf8("kochinStart"))
        self.formLayout_2.setWidget(14, QtGui.QFormLayout.FieldRole, self.kochinStart)
        self.kochinStop = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStop.setObjectName(_fromUtf8("kochinStop"))
        self.formLayout_2.setWidget(15, QtGui.QFormLayout.FieldRole, self.kochinStop)
        self.kochinStep = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStep.setObjectName(_fromUtf8("kochinStep"))
        self.formLayout_2.setWidget(16, QtGui.QFormLayout.FieldRole, self.kochinStep)
        self.nemohButton = QtGui.QPushButton(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.nemohButton.setFont(font)
        self.nemohButton.setObjectName(_fromUtf8("nemohButton"))
        self.formLayout_2.setWidget(22, QtGui.QFormLayout.FieldRole, self.nemohButton)
        self.wavDirCheck = QtGui.QCheckBox(self.tabNemoh)
        self.wavDirCheck.setText(_fromUtf8(""))
        self.wavDirCheck.setObjectName(_fromUtf8("wavDirCheck"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.wavDirCheck)
        self.wavDirLabel = QtGui.QLabel(self.tabNemoh)
        self.wavDirLabel.setObjectName(_fromUtf8("wavDirLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.wavDirLabel)
        self.fsCheck = QtGui.QCheckBox(self.tabNemoh)
        self.fsCheck.setText(_fromUtf8(""))
        self.fsCheck.setObjectName(_fromUtf8("fsCheck"))
        self.formLayout_2.setWidget(17, QtGui.QFormLayout.FieldRole, self.fsCheck)
        self.fsLabel = QtGui.QLabel(self.tabNemoh)
        self.fsLabel.setObjectName(_fromUtf8("fsLabel"))
        self.formLayout_2.setWidget(17, QtGui.QFormLayout.LabelRole, self.fsLabel)
        self.fsDeltaX = QtGui.QLineEdit(self.tabNemoh)
        self.fsDeltaX.setObjectName(_fromUtf8("fsDeltaX"))
        self.formLayout_2.setWidget(18, QtGui.QFormLayout.FieldRole, self.fsDeltaX)
        self.fsDeltaY = QtGui.QLineEdit(self.tabNemoh)
        self.fsDeltaY.setObjectName(_fromUtf8("fsDeltaY"))
        self.formLayout_2.setWidget(19, QtGui.QFormLayout.FieldRole, self.fsDeltaY)
        self.fsLengthX = QtGui.QLineEdit(self.tabNemoh)
        self.fsLengthX.setObjectName(_fromUtf8("fsLengthX"))
        self.formLayout_2.setWidget(20, QtGui.QFormLayout.FieldRole, self.fsLengthX)
        self.fsLengthY = QtGui.QLineEdit(self.tabNemoh)
        self.fsLengthY.setObjectName(_fromUtf8("fsLengthY"))
        self.formLayout_2.setWidget(21, QtGui.QFormLayout.FieldRole, self.fsLengthY)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.nemConsLabel = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemConsLabel.setFont(font)
        self.nemConsLabel.setObjectName(_fromUtf8("nemConsLabel"))
        self.verticalLayout_3.addWidget(self.nemConsLabel)
        self.nemMessBox = QtGui.QTextEdit(self.tabNemoh)
        self.nemMessBox.setEnabled(True)
        self.nemMessBox.setReadOnly(True)
        self.nemMessBox.setObjectName(_fromUtf8("nemMessBox"))
        self.verticalLayout_3.addWidget(self.nemMessBox)
        self.nemVisualisation = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemVisualisation.setFont(font)
        self.nemVisualisation.setObjectName(_fromUtf8("nemVisualisation"))
        self.verticalLayout_3.addWidget(self.nemVisualisation)
        
        self.mplNem = MyStaticMplCanvas(self.tabNemoh, width=5, height=4, dpi=100)
        self.ntbNem = NavigationToolbar(self.mplNem, self.tabNemoh)
        self.verticalLayout_3.addWidget(self.mplNem)
        self.verticalLayout_3.addWidget(self.ntbNem)

        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabNemoh, _fromUtf8(""))
        # Simulation tab
        self.tabSim = QtGui.QWidget()
        self.tabSim.setObjectName(_fromUtf8("tabSim"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabSim)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.wavProp = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.wavProp.setFont(font)
        self.wavProp.setObjectName(_fromUtf8("wavProp"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.wavProp)
        self.wavTypeLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.wavTypeLabel.setFont(font)
        self.wavTypeLabel.setObjectName(_fromUtf8("wavTypeLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.wavTypeLabel)
        self.wavType = QtGui.QComboBox(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.wavType.setFont(font)
        self.wavType.setObjectName(_fromUtf8("wavType"))
        self.wavType.addItem(_fromUtf8(""))
        self.wavType.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.wavType)
        self.wavHLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.wavHLabel.setFont(font)
        self.wavHLabel.setObjectName(_fromUtf8("wavHLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.wavHLabel)
        self.wavHBox = QtGui.QLineEdit(self.tabSim)
        self.wavHBox.setObjectName(_fromUtf8("wavHBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.wavHBox)
        self.wavTLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.wavTLabel.setFont(font)
        self.wavTLabel.setObjectName(_fromUtf8("wavTLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.wavTLabel)
        self.wavTBox = QtGui.QLineEdit(self.tabSim)
        self.wavTBox.setObjectName(_fromUtf8("wavTBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.wavTBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem)
        self.ptoProp = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ptoProp.setFont(font)
        self.ptoProp.setObjectName(_fromUtf8("ptoProp"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.ptoProp)
        self.dampTypeLabel = QtGui.QLabel(self.tabSim)
        self.dampTypeLabel.setObjectName(_fromUtf8("dampTypeLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.dampTypeLabel)
        self.dampSelect = QtGui.QComboBox(self.tabSim)
        self.dampSelect.setObjectName(_fromUtf8("dampSelect"))
        self.dampSelect.addItem(_fromUtf8(""))
        self.dampSelect.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.dampSelect)
        self.fdampLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.fdampLabel.setFont(font)
        self.fdampLabel.setObjectName(_fromUtf8("fdampLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.fdampLabel)
        self.fdampLayout = QtGui.QHBoxLayout()
        self.fdampLayout.setObjectName(_fromUtf8("fdampLayout"))
        self.msupLabel = QtGui.QLabel(self.tabSim)
        self.msupLabel.setObjectName(_fromUtf8("msupLabel"))
        self.fdampLayout.addWidget(self.msupLabel)
        self.msupEdit = QtGui.QLineEdit(self.tabSim)
        self.msupEdit.setObjectName(_fromUtf8("msupEdit"))
        self.fdampLayout.addWidget(self.msupEdit)
        self.bsupLabel = QtGui.QLabel(self.tabSim)
        self.bsupLabel.setObjectName(_fromUtf8("bsupLabel"))
        self.fdampLayout.addWidget(self.bsupLabel)
        self.bsupEdit = QtGui.QLineEdit(self.tabSim)
        self.bsupEdit.setObjectName(_fromUtf8("bsupEdit"))
        self.fdampLayout.addWidget(self.bsupEdit)
        self.csupLabel = QtGui.QLabel(self.tabSim)
        self.csupLabel.setObjectName(_fromUtf8("csupLabel"))
        self.fdampLayout.addWidget(self.csupLabel)
        self.csupEdit = QtGui.QLineEdit(self.tabSim)
        self.csupEdit.setObjectName(_fromUtf8("csupEdit"))
        self.fdampLayout.addWidget(self.csupEdit)
        self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.fdampLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.simProp = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.simProp.setFont(font)
        self.simProp.setObjectName(_fromUtf8("simProp"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.simProp)
        self.simTimeLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.simTimeLabel.setFont(font)
        self.simTimeLabel.setObjectName(_fromUtf8("simTimeLabel"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.simTimeLabel)
        self.simTimeBox = QtGui.QLineEdit(self.tabSim)
        self.simTimeBox.setObjectName(_fromUtf8("simTimeBox"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.simTimeBox)
        self.dtLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.dtLabel.setFont(font)
        self.dtLabel.setObjectName(_fromUtf8("dtLabel"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.dtLabel)
        self.dtBox = QtGui.QLineEdit(self.tabSim)
        self.dtBox.setObjectName(_fromUtf8("dtBox"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.dtBox)
        self.simButton = QtGui.QPushButton(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.simButton.setFont(font)
        self.simButton.setObjectName(_fromUtf8("simButton"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.simButton)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.nemConsLabel_2 = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemConsLabel_2.setFont(font)
        self.nemConsLabel_2.setObjectName(_fromUtf8("nemConsLabel_2"))
        self.verticalLayout_5.addWidget(self.nemConsLabel_2)
        self.simMessBox = QtGui.QTextEdit(self.tabSim)
        self.simMessBox.setEnabled(True)
        self.simMessBox.setReadOnly(True)
        self.simMessBox.setObjectName(_fromUtf8("simMessBox"))
        self.verticalLayout_5.addWidget(self.simMessBox)
        self.nemVisualisation_2 = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemVisualisation_2.setFont(font)
        self.nemVisualisation_2.setObjectName(_fromUtf8("nemVisualisation_2"))
        self.verticalLayout_5.addWidget(self.nemVisualisation_2)
        
        self.mplSim = MyStaticMplCanvas(self.tabSim, width=5, height=4, dpi=100)
        self.ntbSim = NavigationToolbar(self.mplSim, self.tabSim)
        self.verticalLayout_5.addWidget(self.mplSim)
        self.verticalLayout_5.addWidget(self.ntbSim)

        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabSim, _fromUtf8(""))
        self.tabPost = QtGui.QWidget()
        self.tabPost.setObjectName(_fromUtf8("tabPost"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabPost)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.plotToolTitle = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.plotToolTitle.setFont(font)
        self.plotToolTitle.setObjectName(_fromUtf8("plotToolTitle"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.plotToolTitle)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_5.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.upPlotTitle = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.upPlotTitle.setFont(font)
        self.upPlotTitle.setObjectName(_fromUtf8("upPlotTitle"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.upPlotTitle)
        self.plotX1 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotX1.setFont(font)
        self.plotX1.setObjectName(_fromUtf8("plotX1"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.plotX1)
        self.chooseX1 = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.chooseX1.setFont(font)
        self.chooseX1.setObjectName(_fromUtf8("chooseX1"))
        self.chooseX1.addItem(_fromUtf8(""))
        self.chooseX1.addItem(_fromUtf8(""))
        self.chooseX1.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.chooseX1)
        self.plotY1 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotY1.setFont(font)
        self.plotY1.setObjectName(_fromUtf8("plotY1"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.plotY1)
        self.chooseY1 = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.chooseY1.setFont(font)
        self.chooseY1.setObjectName(_fromUtf8("chooseY1"))
        self.chooseY1.addItem(_fromUtf8(""))
        self.chooseY1.addItem(_fromUtf8(""))
        self.chooseY1.addItem(_fromUtf8(""))
        self.chooseY1.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.chooseY1)
        self.makePlot1 = QtGui.QPushButton(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.makePlot1.setFont(font)
        self.makePlot1.setObjectName(_fromUtf8("makePlot1"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.makePlot1)
        self.lowPlotTitle = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lowPlotTitle.setFont(font)
        self.lowPlotTitle.setObjectName(_fromUtf8("lowPlotTitle"))
        self.formLayout_5.setWidget(8, QtGui.QFormLayout.LabelRole, self.lowPlotTitle)
        self.plotX2 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotX2.setFont(font)
        self.plotX2.setObjectName(_fromUtf8("plotX2"))
        self.formLayout_5.setWidget(9, QtGui.QFormLayout.LabelRole, self.plotX2)
        self.plotY2 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotY2.setFont(font)
        self.plotY2.setObjectName(_fromUtf8("plotY2"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.LabelRole, self.plotY2)
        self.chooseY2 = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.chooseY2.setFont(font)
        self.chooseY2.setObjectName(_fromUtf8("chooseY2"))
        self.chooseY2.addItem(_fromUtf8(""))
        self.chooseY2.addItem(_fromUtf8(""))
        self.chooseY2.addItem(_fromUtf8(""))
        self.chooseY2.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.FieldRole, self.chooseY2)
        self.chooseX2 = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.chooseX2.setFont(font)
        self.chooseX2.setObjectName(_fromUtf8("chooseX2"))
        self.chooseX2.addItem(_fromUtf8(""))
        self.chooseX2.addItem(_fromUtf8(""))
        self.chooseX2.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(9, QtGui.QFormLayout.FieldRole, self.chooseX2)
        self.makePlot2 = QtGui.QPushButton(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.makePlot2.setFont(font)
        self.makePlot2.setObjectName(_fromUtf8("makePlot2"))
        self.formLayout_5.setWidget(11, QtGui.QFormLayout.FieldRole, self.makePlot2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_5.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.gridLayout_5.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.nemConsLabel_3 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemConsLabel_3.setFont(font)
        self.nemConsLabel_3.setObjectName(_fromUtf8("nemConsLabel_3"))
        self.verticalLayout_6.addWidget(self.nemConsLabel_3)
        self.postMessBox = QtGui.QTextEdit(self.tabPost)
        self.postMessBox.setEnabled(True)
        self.postMessBox.setReadOnly(True)
        self.postMessBox.setObjectName(_fromUtf8("postMessBox"))
        self.verticalLayout_6.addWidget(self.postMessBox)
        self.nemVisualisation_3 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nemVisualisation_3.setFont(font)
        self.nemVisualisation_3.setObjectName(_fromUtf8("nemVisualisation_3"))
        self.verticalLayout_6.addWidget(self.nemVisualisation_3)
        
        self.mpl1 = MyStaticMplCanvas(self.tabPost, width=5, height=4, dpi=100)
        self.ntb1 = NavigationToolbar(self.mpl1, self.tabPost)
        self.mpl2 = MyStaticMplCanvas(self.tabPost, width=5, height=4, dpi=100)
        self.ntb2 = NavigationToolbar(self.mpl2, self.tabPost)
        self.verticalLayout_6.addWidget(self.mpl1)
        self.verticalLayout_6.addWidget(self.ntb1)
        self.verticalLayout_6.addWidget(self.mpl2)
        self.verticalLayout_6.addWidget(self.ntb2)

        self.gridLayout_5.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabPost, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1556, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionManual = QtGui.QAction(MainWindow)
        self.actionManual.setObjectName(_fromUtf8("actionManual"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.menuAbout.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionSave)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Initialize plot variables
        self.freq = np.array([0,1])
        self.time = np.array([0,1])
        self.Ma = np.array([0,1])
        self.Bhyd = np.array([0,1])
        self.Fe = np.array([0,1])
        self.RAO = np.array([0,1])
        self.posZ = np.array([0,1])
        self.velZ = np.array([0,1])
        self.wave = np.array([0,1])
        self.Fpto = np.array([0,1])
        self.nrObj = 0
        self.meshObj = []
        self.X = np.zeros((4,4))
        self.Y = np.zeros((4,4))
        self.etaDiff = np.zeros((4,4))
        self.etaRad = np.zeros((4,4))
        self.wDir = os.path.join(os.path.expanduser("~"),'openWEC')
        # Set GUI
        # Mesh Tab
        MainWindow.setWindowTitle(_translate("openWEC", "openWEC", None))
        
        self.infoConsoleLabel.setText(_translate("openWEC", "Information Console", None))
        self.visualisationLabel.setText(_translate("openWEC", "Visualisation", None))
        self.geoProp.setText(_translate("openWEC", "Mesh Creator", None))
        self.lengthLabel.setText(_translate("openWEC", "Length", None))
        self.lengthBox.setPlaceholderText(_translate("openWEC", "in meter", None))
        self.heightLabel.setText(_translate("openWEC", "Height", None))
        self.heightBox.setPlaceholderText(_translate("openWEC", "in meter", None))
        self.widthLabel.setText(_translate("openWEC", "Width", None))
        self.widthBox.setPlaceholderText(_translate("openWEC", "in meter", None))
        self.spacingLabel.setText(_translate("openWEC", "Spacing", None))
        self.spacingBox.setPlaceholderText(_translate("openWEC", "in meter", None))
        self.genProp.setText(_translate("openWEC", "General properties", None))
        self.waterDepthLabel.setText(_translate("openWEC", "Water Depth:", None))
        self.waterDepthBox.setPlaceholderText(_translate("openWEC", "in meter; 0 for infinite depth", None))
        self.rhoLabel.setText(_translate("openWEC", "Density:", None))
        self.rhoBox.setPlaceholderText(_translate("openWEC", "in kg/m³", None))
        self.MeshProp.setText(_translate("openWEC", "Mesh Properties:", None))
        self.nPanelLabel.setText(_translate("openWEC", "Number of mesh panels: ", None))
        self.nPanelBox.setPlaceholderText(_translate("openWEC", "integer (>100)", None))
        self.meshButton.setText(_translate("openWEC", "Mesh!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMesh), _translate("openWEC", "Mesh Tool", None))
        self.meshButton.clicked.connect(self.makeMesh)

        # Nemoh Tab
        self.nemConsLabel.setText(_translate("openWEC", "Information Console", None))
        self.nemVisualisation.setText(_translate("openWEC", "Visualisation", None))
        self.labelBEM.setText(_translate("MainWindow", "BEM Solver Options", None))
        self.label.setText(_translate("MainWindow", "Basic", None))
        self.omegaLabel.setText(_translate("MainWindow", "Frequency range:", None))
        self.omegaStart.setPlaceholderText(_translate("MainWindow", "start in rad/s (0.2)", None))
        self.omegaStop.setPlaceholderText(_translate("MainWindow", "stop in rad/s (2.5)", None))
        self.omegaStep.setPlaceholderText(_translate("MainWindow", "number of steps in between (50)", None))
        self.label_2.setText(_translate("MainWindow", "Advanced", None))
        self.wavDirStart.setPlaceholderText(_translate("MainWindow", "start in degrees (0.0)", None))
        self.wavDirStop.setPlaceholderText(_translate("MainWindow", "end in degrees (0.0)", None))
        self.wavDirStep.setPlaceholderText(_translate("MainWindow", "number of steps in between (1)", None))
        self.irfLabel.setText(_translate("MainWindow", "Calculate IRF:", None))
        self.irfDur.setPlaceholderText(_translate("MainWindow", "IRF Duration in seconds (20)", None))
        self.irfStep.setPlaceholderText(_translate("MainWindow", "IRF time step in seconds (0.01)", None))
        self.kochinLabel.setText(_translate("MainWindow", "Kochin function:", None))
        self.kochinStart.setPlaceholderText(_translate("MainWindow", "Kochin Start in degrees", None))
        self.kochinStop.setPlaceholderText(_translate("MainWindow", "Kochin Stop in degrees", None))
        self.kochinStep.setPlaceholderText(_translate("MainWindow", "Kochin steps in between", None))
        self.nemohButton.setText(_translate("MainWindow", "Simulate!", None))
        self.nemohButton.clicked.connect(self.runNemohCode)
        self.wavDirLabel.setText(_translate("MainWindow", "Wave directions:", None))
        self.fsLabel.setText(_translate("MainWindow", "Free Surface:", None))
        self.fsDeltaX.setPlaceholderText(_translate("MainWindow", "number of grid points in X-direction", None))
        self.fsDeltaY.setPlaceholderText(_translate("MainWindow", "number of grid points in Y-direction", None))
        self.fsLengthX.setPlaceholderText(_translate("MainWindow", "length of grid in X-direction", None))
        self.fsLengthY.setPlaceholderText(_translate("MainWindow", "length of grid in Y-direction", None))
        self.nemConsLabel.setText(_translate("MainWindow", "Information Console", None))
        self.nemVisualisation.setText(_translate("MainWindow", "Visualisation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNemoh), _translate("MainWindow", "Nemoh", None))
        # Time Solver
        self.wavProp.setText(_translate("MainWindow", "Wave climate", None))
        self.wavTypeLabel.setText(_translate("MainWindow", "Wave Type:", None))
        self.wavType.setItemText(0, _translate("MainWindow", "Regular", None))
        self.wavType.setItemText(1, _translate("MainWindow", "Irregular", None))
        self.wavType.currentIndexChanged.connect(self.displayMessageSim)
        self.wavHLabel.setText(_translate("MainWindow", "Wave Height:", None))
        self.wavHBox.setPlaceholderText(_translate("MainWindow", "in meter", None))
        self.wavTLabel.setText(_translate("MainWindow", "Wave Period:", None))
        self.wavTBox.setPlaceholderText(_translate("MainWindow", "in seconds", None))
        self.ptoProp.setText(_translate("MainWindow", "PTO Properties", None))
        self.dampTypeLabel.setText(_translate("openWEC", "Damping Type:", None))
        self.dampSelect.setItemText(0, _translate("openWEC", "Linear", None))
        self.dampSelect.setItemText(1, _translate("openWEC", "Coulomb", None))
        self.dampSelect.currentIndexChanged.connect(self.changePtoLabels)
        self.msupLabel.setText(_translate("openWEC", "Mpto: ", None))
        self.msupEdit.setPlaceholderText(_translate("openWEC", "Exernal Mass in kg", None))
        self.bsupLabel.setText(_translate("openWEC", "Bpto: ", None))
        self.bsupEdit.setPlaceholderText(_translate("openWEC", "External Damping in kg/s", None))
        self.csupLabel.setText(_translate("openWEC", "Cpto: ", None))
        self.csupEdit.setPlaceholderText(_translate("openWEC", "External Spring in kg/s²", None))
        self.fdampLabel.setText(_translate("MainWindow", "PTO values:", None))
        self.simProp.setText(_translate("MainWindow", "Simulation", None))
        self.simTimeLabel.setText(_translate("MainWindow", "Time:", None))
        self.simTimeBox.setPlaceholderText(_translate("MainWindow", "in seconds", None))
        self.dtLabel.setText(_translate("MainWindow", "Time Step:", None))
        self.dtBox.setPlaceholderText(_translate("MainWindow", "in seconds", None))
        self.simButton.setText(_translate("MainWindow", "Simulate!", None))
        self.simButton.clicked.connect(partial(self.runThread,pf=self.postSim,f=self.runSimulation))        
        self.nemConsLabel_2.setText(_translate("MainWindow", "Information Console", None))
        self.nemVisualisation_2.setText(_translate("MainWindow", "Visualisation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSim), _translate("MainWindow", "Simulation", None))
        # Post Processor
        self.plotToolTitle.setText(_translate("MainWindow", "Plotting Tool", None))
        self.upPlotTitle.setText(_translate("MainWindow", "Upper Plot", None))
        self.plotX1.setText(_translate("MainWindow", "Variable for X-axis                                                                  ", None))
        self.chooseX1.setItemText(0, _translate("MainWindow", "Frequency                                                                   ", None))
        self.chooseX1.setItemText(1, _translate("MainWindow", "Time", None))
        self.chooseX1.setItemText(2, _translate("MainWindow", "Grid", None))
        self.chooseX1.currentIndexChanged.connect(partial(self.plotVariables,plotWindow=1))
        self.plotY1.setText(_translate("MainWindow", "Variable for Y-axis", None))
        self.chooseY1.setItemText(0, _translate("MainWindow", "Added Mass", None))
        self.chooseY1.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
        self.chooseY1.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
        self.chooseY1.setItemText(3, _translate("MainWindow", "Response Amplitude Operator", None))
        self.makePlot1.setText(_translate("MainWindow", "Plot 1", None))
        self.makePlot1.clicked.connect(partial(self.overwriteGraph,plotWindow=1))
        self.lowPlotTitle.setText(_translate("MainWindow", "Lower Plot", None))
        self.plotX2.setText(_translate("MainWindow", "Variable for X-axis", None))
        self.plotY2.setText(_translate("MainWindow", "Variable for Y-axis", None))
        self.chooseY2.setItemText(0, _translate("MainWindow", "Added Mass", None))
        self.chooseY2.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
        self.chooseY2.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
        self.chooseY2.setItemText(3, _translate("MainWindow", "Response Amplitude Operator", None))
        self.chooseX2.setItemText(0, _translate("MainWindow", "Frequency", None))
        self.chooseX2.setItemText(1, _translate("MainWindow", "Time", None))
        self.chooseX2.setItemText(2, _translate("MainWindow", "Grid", None))
        self.chooseX2.currentIndexChanged.connect(partial(self.plotVariables,plotWindow=2))
        self.makePlot2.setText(_translate("MainWindow", "Plot 2", None))
        self.makePlot2.clicked.connect(partial(self.overwriteGraph,plotWindow=2))

        self.ntb1._views.clear()
        self.ntb2._views.clear()
        self.ntbMesh._views.clear()
        self.ntbNem._views.clear()
        self.ntbSim._views.clear()

        self.nemConsLabel_3.setText(_translate("MainWindow", "Information Console", None))
        self.nemVisualisation_3.setText(_translate("MainWindow", "Visualisation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPost), _translate("MainWindow", "Post-Processing", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Program", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open..", None))
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.setText(_translate("MainWindow", "Save..", None))
        self.actionSave.triggered.connect(self.saveFile)        
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.triggered.connect(self.about)
        self.actionManual.setText(_translate("MainWindow", "Manual", None))
        self.actionManual.triggered.connect(self.manual)
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionClose.triggered.connect(self.close)
        
        
    def overwriteGraph(self,plotWindow=1):
        # Set the correct variables
        if plotWindow == 1:
            test = 4*self.chooseX1.currentIndex() + self.chooseY1.currentIndex()
            mpl = self.mpl1
            ntb = self.ntb1
        else:
            test = 4*self.chooseX2.currentIndex() + self.chooseY2.currentIndex()
            mpl = self.mpl2
            ntb = self.ntb2
            
        pT = ""
        if test/4 == 2:
            pT = "Grid"
            fsFile = os.path.join(self.wDir,'Nemoh','freesurface.    1.dat')
            if(os.path.isfile(fsFile)):
                None
            else:
                print("Warning! No free surface was calculated with Nemoh! Plotting not possible!")

        if test==0:
            xVar = self.freq
            yVar = self.Ma
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Added Mass/Inertia$'
        elif test==1:
            xVar = self.freq
            yVar = self.Bhyd
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Hydrodynamic Damping$'
        elif test==2:
            xVar = self.freq
            yVar = self.Fe
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Excitation Force/Torque$'
        elif test==3:
            xVar = self.freq
            yVar = self.RAO
            xlabel = '$Frequency [Hz]$'
            ylabel = '$RAO$'
        elif test==4:
            xVar = self.time
            yVar = self.wave
            xlabel = '$Time [s]$'
            ylabel = '$\eta [m]$'
        elif test==5:
            xVar = self.time
            yVar = self.posZ
            xlabel = '$Time [s]$'
            ylabel = '$WEC Response$'
        elif test==6:
            xVar = self.time
            yVar = self.velZ
            xlabel = '$Time [s]$'
            ylabel = '$WEC Velocity$'
        elif test==7:
            xVar = self.time
            yVar = self.Fpto
            xlabel = '$Time [s]$'
            ylabel = '$PTO Force/Torque$'
        elif test==8:
            xVar = (self.X,self.Y)
            yVar = np.abs(self.etaDiff)
            xlabel = '$X [m]$'
            ylabel = '$Y [m]$'
        elif test==9:
            xVar = (self.X,self.Y)
            yVar = np.angle(self.etaDiff)
            xlabel = '$X [m]$'
            ylabel = '$Y [m]$'
        elif test==10:
            xVar = (self.X,self.Y)
            yVar = np.abs(self.etaRad)
            xlabel = '$X [m]$'
            ylabel = '$Y [m]$'
        elif test==11:
            xVar = (self.X,self.Y)
            yVar = np.angle(self.etaRad)
            xlabel = '$X [m]$'
            ylabel = '$Y [m]$'          
        # Plot the variables
        self.updateGraph(x=xVar,y=yVar,g=mpl,t=ntb,xlab=xlabel,ylab=ylabel,plotType=pT)

    def updateGraph(self,x=[0,1,2],y=[1,1,1],x2=[],y2=[],g=[],t=[],
    xlab = "", ylab = "", plotType=""):
        
        if plotType == "Mesh":
            g = self.mplMesh
            t = self.ntbMesh
            g.fig.delaxes(g.axes)
            t.update()
            g.axes = g.fig.add_subplot(111, projection='3d')
            triangul = tri.Triangulation(x,y,triangles=x2)
            g.axes.plot_trisurf(triangul,y2,color = '#468499',edgecolors='None')
            g.axes._axis3don = False
            # Create cubic bounding box to simulate equal aspect ratio
            max_range = np.array([x.max()-x.min(), y.max()-y.min(), y2.max()-y2.min()]).max()
            Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
            Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
            Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(y2.max()+y2.min())
            # Comment or uncomment following both lines to test the fake bounding box:
            for xb, yb, zb in zip(Xb, Yb, Zb):
               g.axes.plot([xb], [yb], [zb], 'w')
            # Plot axes
            xline=((-max(np.abs(x))/2.0,max(np.abs(x))/2.0),(0,0),(0,0))
            g.axes.plot(xline[0],xline[1],xline[2],'grey')
            yline=((0,0),(-max(np.abs(y))/2.0,max(np.abs(y))/2.0),(0,0))
            g.axes.plot(yline[0],yline[1],yline[2],'grey')
            zline=((0,0),(0,0),(-max(np.abs(y2))/2.0,max(np.abs(y2))/2.0))
            g.axes.plot(zline[0],zline[1],zline[2],'grey')
            g.draw()
            
        elif plotType == "Grid":
            t.update()
            g.fig.delaxes(g.axes)
            g.axes = g.fig.add_axes([0.1, 0.17, 0.7, 0.75])
            cax = g.fig.add_axes([0.85, 0.17, 0.05, 0.75])
            test = g.axes.pcolor(x[0],x[1],y)
            g.fig.colorbar(test, cax=cax, orientation='vertical')
            g.axes.set_xlabel(xlab)
            g.axes.set_ylabel(ylab)
            g.draw()
            g.axes.hold(False)
            
        else:
            t.update()
            g.fig.delaxes(g.axes)
            g.axes = g.fig.add_axes([0.20, 0.17, 0.75, 0.75])
            g.axes.plot(x,y,color = '#468499')
            g.axes.hold(True)
            g.axes.plot(x2,y2,color = '#FF6666')
            g.axes.set_xlabel(xlab)
            g.axes.set_ylabel(ylab)
            g.fig.patch.set_facecolor('white')
            g.draw()
            g.axes.hold(False)

    def displayMessage(self):
        if self.meshMethod.currentIndex()==3:
            print("ATTENTION!\n"+
                "You have chosen to import previous Nemoh results \n" + 
                "Please skip to the Simulations tab and fill in the time domain options, \n" +
                "you will be prompted to load the results when you press \n" + 
                "Simulate!")
        if self.meshMethod.currentIndex()==2:
            print("ATTENTION!\n"+
                  "You have chosen to import and convert a .stl mesh \n" +
                  "Please fill in the General Properties \n" +
                  "You will be prompted to load the .stl mesh when you press \n"+
                  "Mesh!")
        if self.meshMethod.currentIndex()==1:
            print("ATTENTION!\n"+
                  "You have chosen to import a Nemoh mesh \n" +
                  "Please fill in the General and Mesh Properties \n" +
                  "You will be prompted to load the Nemoh mesh when you press \n"+
                  "Mesh!")

    def displayMessageSim(self):
        if self.wavType.currentIndex()==1:
            print("ATTENTION!\n"+
                "When choosing irregular waves, you need to have selected the IRF calculation in the Nemoh tab!!")

    def plotVariables(self,plotWindow=1):
        if plotWindow==1:
            if self.chooseX1.currentIndex()==1:
                self.chooseY1.setItemText(0, _translate("MainWindow", "Wave Signal", None))
                self.chooseY1.setItemText(1, _translate("MainWindow", "WEC Position", None))
                self.chooseY1.setItemText(2, _translate("MainWindow", "WEC Velocity", None))
                self.chooseY1.setItemText(3, _translate("MainWindow", "WEC PTO Force", None))
            if self.chooseX1.currentIndex()==0:
                self.chooseY1.setItemText(0, _translate("MainWindow", "Added Mass", None))
                self.chooseY1.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
                self.chooseY1.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
                self.chooseY1.setItemText(3, _translate("MainWindow", "Response Amplitude Operator", None))
            if self.chooseX1.currentIndex()==2:
                self.chooseY1.setItemText(0, _translate("MainWindow", "Diffraction Amplitude", None))
                self.chooseY1.setItemText(1, _translate("MainWindow", "Diffraction Phase Angle", None))
                self.chooseY1.setItemText(2, _translate("MainWindow", "Radiation Amplitude", None))
                self.chooseY1.setItemText(3, _translate("MainWindow", "Radiation Phase Angle", None))
        else:
            if self.chooseX2.currentIndex()==1:
                self.chooseY2.setItemText(0, _translate("MainWindow", "Wave Signal", None))
                self.chooseY2.setItemText(1, _translate("MainWindow", "WEC Position", None))
                self.chooseY2.setItemText(2, _translate("MainWindow", "WEC Velocity", None))
                self.chooseY2.setItemText(3, _translate("MainWindow", "WEC PTO Force", None))
            if self.chooseX2.currentIndex()==0:
                self.chooseY2.setItemText(0, _translate("MainWindow", "Added Mass", None))
                self.chooseY2.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
                self.chooseY2.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
                self.chooseY2.setItemText(3, _translate("MainWindow", "Response Amplitude Operator", None))
            if self.chooseX2.currentIndex()==2:
                self.chooseY2.setItemText(0, _translate("MainWindow", "Diffraction Amplitude", None))
                self.chooseY2.setItemText(1, _translate("MainWindow", "Diffraction Phase Angle", None))
                self.chooseY2.setItemText(2, _translate("MainWindow", "Radiation Amplitude", None))
                self.chooseY2.setItemText(3, _translate("MainWindow", "Radiation Phase Angle", None))

    def makeMesh(self,MainWindow):
        
        sys.path.insert(0, './Run')
        import meshTypes as mt
        
        length = float(self.lengthBox.text())
        height = float(self.heightBox.text())
        nPanels = int(self.nPanelBox.text())
        zG = -height/4.0
        cG = [0.0,0.0,zG]

        
        width = float(self.widthBox.text())        
        spacing = float(self.spacingBox.text())       
        
        box1 = mt.box(length,width,height,[-(length+spacing)/2.0,0.0,0.0])
        box2 = mt.box(length,width,height,[(length+spacing)/2.0,0.0,0.0])
        
        boxFile1 = os.path.join(self.wDir,'Calculation','mesh','axisym1')
        boxFile2 = os.path.join(self.wDir,'Calculation','mesh','axisym2')
        mt.writeMesh(box1,boxFile1)
        mt.writeMesh(box2,boxFile2)
        print("Meshing...")
        self.genericThread = GenericThread(ne.createMeshOpt,cG,nPanels/2,int(0),rho=float(self.rhoBox.text()),nbody=2,xG=[-(length+spacing)/2.0,(length+spacing)/2.0])
        self.genericThread.start()
        self.genericThread.finished.connect(self.visualizeMesh)

    def visualizeMesh(self):
        # Mesh visualisation
        sys.path.insert(0, './Run')
        import processNemoh as pn
        
        (X,Y,Z,trian) = pn.getMesh(nbody=2)
        self.updateGraph(x=X,y=Y,x2=trian,y2=Z,plotType="Mesh")
        print('Mesh succesfully created!')

    def runNemohCode(self):
        # Delete previous results
        folder = os.path.join(self.wDir,'Calculation','results')
        for fil in os.listdir(folder):
            filPath = os.path.join(folder,fil)
            if os.path.isfile(filPath):
                os.unlink(filPath)

        # Basic Options
        self.dof = [0,0,0,0,1,0]
        dof = self.dof
        waterDepth = float(self.waterDepthBox.text())
        o2 = float(self.omegaStart.text())
        o3 = float(self.omegaStop.text())
        o1 = int(float(self.omegaStep.text()))
        omega = [o1,o2,o3]
        try:
            rhoW = float(self.rhoBox.text())
        except:
            rhoW = 1025.0
        spacing = float(self.spacingBox.text()) 
        height = float(self.heightBox.text())
        length = float(self.lengthBox.text())
        xG = [-(length+spacing)/2.0,(length+spacing)/2.0]
        zG = -height/4.0
        
        # Advanced Options
        advOps = {}
        advOps['parkCheck'] = False
        if self.wavDirCheck.isChecked():
            advOps['dirCheck'] =  True
            advOps['dirStart'] = float(self.wavDirStart.text())
            advOps['dirStop'] = float(self.wavDirStop.text())
            advOps['dirStep'] = int(float(self.wavDirStep.text()))
        else:
            advOps['dirCheck'] = False
        if self.irfCheck.isChecked():
            advOps['irfCheck']  = True
            advOps['irfDur'] = float(self.irfDur.text())
            advOps['irfStep'] = float(self.irfStep.text())
        else:
            advOps['irfCheck'] = False
        if self.kochinCheck.isChecked():
            advOps['kochCheck'] = True
            advOps['kochStart'] = float(self.kochinStart.text())
            advOps['kochStop'] = float(self.kochinStop.text())
            advOps['kochStep'] = int(float(self.kochinStep.text()))
        else:
            advOps['kochCheck'] = False
        if self.fsCheck.isChecked():
            advOps['fsCheck'] = True
            advOps['fsDeltaX'] = float(self.fsDeltaX.text())
            advOps['fsDeltaY'] = float(self.fsDeltaX.text())
            advOps['fsLengthX'] = float(self.fsLengthX.text())
            advOps['fsLengthY'] = float(self.fsLengthY.text())
        else:
            advOps['fsCheck'] = False

        # Write CAL file
        ne.writeCalFile(rhoW,waterDepth,omega,zG,dof,aO=advOps,nbody=2,xG=xG)
        self.genericThread = GenericThread(ne.runNemoh,nbody=2)
        self.genericThread.start()
        print("Nemoh Simulation Running...")
        self.genericThread.finished.connect(partial(self.postNemoh,advOps,rhoW,waterDepth))

    def postNemoh(self,advOps,rhoW,depth):
        # Delete content of destination folder
        folder = os.path.join(self.wDir,'Nemoh')
        for fil in os.listdir(folder):
            filPath = os.path.join(folder,fil)
            if os.path.isfile(filPath):
                os.unlink(filPath)
        
        # Copy Result files to Simulation directory
        pathName = os.path.join(self.wDir,'Calculation','results')
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,os.path.join(self.wDir,'Nemoh'))
        pathName = os.path.join(self.wDir,'Calculation','mesh')
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,os.path.join(self.wDir,'Nemoh'))

        # Display results on matplotlib widgets
        sys.path.insert(0, './Run')
        import processNemoh as pn
        
        xlabel = 'Frequency [Hz]'
        ylabel = '$M_a$ and $B_{hyd}$'

        (self.Ma,self.Bhyd,omeg) = pn.getAB(self.dof,nbody=2,sel=self.dof.index(1))
        self.freq = omeg/(2*np.pi)
        (self.Fe,self.Fpha) = pn.getFe(self.dof,nbody=2,sel=self.dof.index(1))
        (Mass,KH) = pn.calcM(rho=rhoW,dof = self.dof)
        self.RAO = (self.Fe)/np.abs(-omeg**2.0*(Mass+self.Ma)-1j*omeg*self.Bhyd+KH)
        self.updateGraph(x=self.freq,y=self.Ma,x2=self.freq,y2=self.Bhyd,g=self.mplNem,
        t=self.ntbNem,xlab=xlabel,ylab=ylabel)
        
        # Calculate FS/Kochin grids
        if self.fsCheck.isChecked():
            self.X,self.Y,self.etaDiff,self.etaRad = pn.getFS(advOps,depth,omeg,self.RAO)
        
        print ('Program Finished!')

    def runThread(self,pf=[],f=[],*args,**kwargs):
        self.genericThread = GenericThread(f,*args,**kwargs)
        self.genericThread.start()
        self.genericThread.finished.connect(pf)

    def runSimulation(self):
        
        # Set type of simulation        
        wavType = self.wavType.currentIndex()
        if (wavType==0):
            wavName = 'regular'            
        else:
            wavName = 'irregular'

        # Import necessary modules
        sys.path.insert(0, './Run')
        import makeWaveFex as wav
        import processNemoh as pn
        import wecSim as wc

        # Get Wave Parameters
        Hs = float(self.wavHBox.text())
        Tm = float(self.wavTBox.text())
        dof = [0,0,0,0,1,0]
        try:
            rho = float(self.rhoBox.text())
        except:
            rho = 1025.0
        
        # Get Damping force
        dampType = self.dampSelect.currentIndex()
        if dampType == 0:
            Fdamp = []
            Fdamp.append(float(self.msupEdit.text()))
            Fdamp.append(float(self.bsupEdit.text()))
            Fdamp.append(float(self.csupEdit.text()))
        else:
            Fdamp = float(self.fdampEdit.text())
        
        # Get Simulation Parameters
        tSim = int(self.simTimeBox.text())
        tStep = float(self.dtBox.text())
        time = np.linspace(0,tSim,tSim/tStep+1)
        
        #---------------------------------------------------------------------------
        # MODEL PREPARATION
        #---------------------------------------------------------------------------
        reload(wav)
        reload(pn)
        reload(wc)
        # Preprocessing: calculate body parameters
        
        M,c = pn.calcM(dof=dof)
        if (wavType==0):
            Ma,Bhyd,omega = pn.getAB(dof,sel=self.dof.index(1))
            Ma = np.interp(2*np.pi/Tm,omega,Ma)
            Bhyd = np.interp(2*np.pi/Tm,omega,Bhyd)
        else:
            alpha,beta,errorE,Mainf = pn.calcAlphaBeta(10,rho,dof)
        
        # Correct negative Ma
        Ma = np.abs(Ma)

        # Calculate Exciting wave and wave force
        
        time,self.wave,Fex = wav.makeWaveFex(Hs,Tm,time,dof,wavName)

        #---------------------------------------------------------------------------
        # MODEL SIMULATION
        #---------------------------------------------------------------------------

        # First Run

        print('Wave height: ' + str(Hs) + ' m')
        print('Wave period: ' + str(Tm) + ' s')
        print('Simulation Start!')
        
        if (wavType==0):
            self.time,self.posZ,self.velZ,self.Fpto = wc.simBodyReg1DOF(time,Fex,Fdamp,dampType,M,c,Ma,Bhyd)
        else:
             self.time,self.posZ,self.velZ,self.Fpto = wc.simBody1DOF(time,Fex,Fdamp,dampType,M,Mainf,c,alpha,beta)

        print('Simulation Finished!')

    def postSim(self):
        sys.path.insert(0, './Run')
        import wecSim as wc
        # Output to matplotlib widgets
        diff = len(self.time)-len(self.posZ)
        if diff>0.5:
            self.time = np.delete(self.time,0)
        elif diff <-0.5:
            self.posZ = np.delete(self.posZ,-1)
            self.velZ = np.delete(self.velZ,-1)
            self.Fpto = np.delete(self.Fpto,-1)
        
        xlabel = 'Time [s]'
        ylabel = '$z$ and $v$'

        self.updateGraph(x=self.time,y=self.posZ,x2=self.time,y2=self.velZ,g=self.mplSim,
        t=self.ntbSim,xlab=xlabel,ylab=ylabel)

        saveName = QtGui.QFileDialog.getSaveFileName(self,
        "Save Simulation Results",os.path.join(self.wDir,"Output"),"Text File (*.txt)")
        wc.saveResults(saveName,self.time,self.posZ,self.velZ,self.Fpto)        
        
        # Calculate Produced Power

        Pabs = self.Fpto*self.velZ
        Pabs_mean = np.mean(Pabs)
        print('Mean Absorbed Power: ' + str(Pabs_mean) + ' Watt')

    def changePtoLabels(self):
        if self.dampSelect.currentIndex() == 0:
            # Linear Damping with 3 options Mext, Bext, Cext
            self.fdampEdit.deleteLater()
            self.formLayout.removeItem(self.fdampLayout)
            # Set UI
            self.fdampLayout = QtGui.QHBoxLayout()
            self.fdampLayout.setObjectName(_fromUtf8("fdampLayout"))
            self.msupLabel = QtGui.QLabel(self.tabSim)
            self.msupLabel.setObjectName(_fromUtf8("msupLabel"))
            self.fdampLayout.addWidget(self.msupLabel)
            self.msupEdit = QtGui.QLineEdit(self.tabSim)
            self.msupEdit.setObjectName(_fromUtf8("msupEdit"))
            self.fdampLayout.addWidget(self.msupEdit)
            self.bsupLabel = QtGui.QLabel(self.tabSim)
            self.bsupLabel.setObjectName(_fromUtf8("bsupLabel"))
            self.fdampLayout.addWidget(self.bsupLabel)
            self.bsupEdit = QtGui.QLineEdit(self.tabSim)
            self.bsupEdit.setObjectName(_fromUtf8("bsupEdit"))
            self.fdampLayout.addWidget(self.bsupEdit)
            self.csupLabel = QtGui.QLabel(self.tabSim)
            self.csupLabel.setObjectName(_fromUtf8("csupLabel"))
            self.fdampLayout.addWidget(self.csupLabel)
            self.csupEdit = QtGui.QLineEdit(self.tabSim)
            self.csupEdit.setObjectName(_fromUtf8("csupEdit"))
            self.fdampLayout.addWidget(self.csupEdit)
            self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.fdampLayout)            
            # Retranslate UI
            self.fdampLabel.setText(_translate("openWEC", "PTO Values:", None))
            self.msupLabel.setText(_translate("openWEC", "Mpto: ", None))
            self.msupEdit.setPlaceholderText(_translate("openWEC", "Exernal Mass in kg", None))
            self.bsupLabel.setText(_translate("openWEC", "Bpto: ", None))
            self.bsupEdit.setPlaceholderText(_translate("openWEC", "External Damping in kg/s", None))
            self.csupLabel.setText(_translate("openWEC", "Cpto: ", None))
            self.csupEdit.setPlaceholderText(_translate("openWEC", "External Spring in kg/s²", None))        
        else:
            self.msupLabel.deleteLater()
            self.bsupLabel.deleteLater()
            self.csupLabel.deleteLater()
            self.msupEdit.deleteLater()
            self.bsupEdit.deleteLater()
            self.csupEdit.deleteLater()            
            self.formLayout.removeItem(self.fdampLayout)
            # Set UI
            self.fdampLayout = QtGui.QHBoxLayout()
            self.fdampLayout.setObjectName(_fromUtf8("fdampLayout"))
            self.fdampEdit = QtGui.QLineEdit(self.tabSim)
            self.fdampEdit.setObjectName(_fromUtf8("fdampEdit"))
            self.fdampLayout.addWidget(self.fdampEdit)
            self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.fdampLayout)            
            # Retranslate UI
            self.fdampLabel.setText(_translate("openWEC", "PTO Force:", None))
            self.fdampEdit.setPlaceholderText(_translate("openWEC", "PTO Force in Newton", None))        
            
    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                        './','*.pe')
                
        with open(fname,'r') as f:
            inData = f.readlines()
            
        self.lengthBox.setText(inData[1].split('\t')[0])
        self.heightBox.setText(inData[2].split('\t')[0])
        self.widthBox.setText(inData[3].split('\t')[0])
        self.spacingBox.setText(inData[4].split('\t')[0])
        self.waterDepthBox.setText(inData[5].split('\t')[0])        
        self.rhoBox.setText(inData[6].split('\t')[0])        
        self.nPanelBox.setText(inData[7].split('\t')[0])
        
        self.omegaStart.setText(inData[9].split('\t')[0])        
        self.omegaStop.setText(inData[10].split('\t')[0])        
        self.omegaStep.setText(inData[11].split('\t')[0])
        self.wavDirCheck.setChecked(inData[12].split('\t')[0]=='True')
        self.wavDirStart.setText(inData[13].split('\t')[0])        
        self.wavDirStop.setText(inData[14].split('\t')[0])        
        self.wavDirStep.setText(inData[15].split('\t')[0])
        self.irfCheck.setChecked(inData[16].split('\t')[0]=='True')
        self.irfDur.setText(inData[17].split('\t')[0])        
        self.irfStep.setText(inData[18].split('\t')[0])
        self.kochinCheck.setChecked(inData[19].split('\t')[0]=='True')
        self.kochinStart.setText(inData[20].split('\t')[0])        
        self.kochinStop.setText(inData[21].split('\t')[0])        
        self.kochinStep.setText(inData[22].split('\t')[0])
        self.fsCheck.setChecked(inData[23].split('\t')[0]=='True')
        self.fsDeltaX.setText(inData[24].split('\t')[0])        
        self.fsDeltaY.setText(inData[25].split('\t')[0])        
        self.fsLengthX.setText(inData[26].split('\t')[0])        
        self.fsLengthY.setText(inData[27].split('\t')[0])
        
        self.wavType.setCurrentIndex(int(inData[29].split('\t')[0]))
        self.wavHBox.setText(inData[30].split('\t')[0])
        self.wavTBox.setText(inData[31].split('\t')[0])
        self.dampSelect.setCurrentIndex(int(inData[32].split('\t')[0]))
        if int(inData[32].split('\t')[0])==0:
            self.msupEdit.setText(inData[33].split('\t')[0].split(';')[0])
            self.bsupEdit.setText(inData[33].split('\t')[0].split(';')[1])
            self.csupEdit.setText(inData[33].split('\t')[0].split(';')[2])
        else:
            self.fdampEdit.setText(inData[33].split('\t')[0])
        self.simTimeBox.setText(inData[34].split('\t')[0])
        self.dtBox.setText(inData[35].split('\t')[0])

        print(fname + " successfully opened!")
        
    def saveFile(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', 
                        os.path.join(self.wDir),'*.pe')
                
        with open(fname,'w') as f:
            # Write Mesh Tab properties
            f.write('Mesh Properties\n')            
            f.write(self.lengthBox.text() + "\t Float Length\n")
            f.write(self.heightBox.text() + "\t Float Height\n")
            f.write(self.widthBox.text() + "\t Float Width\n")
            f.write(self.spacingBox.text() + "\t Float Spacing\n")
            f.write(self.waterDepthBox.text() + "\t Water Depth\n")
            f.write(self.rhoBox.text() + "\t Density\n")
            f.write(self.nPanelBox.text() + "\t Number of Mesh Panels\n")
            # Write Nemoh Tab properties
            f.write('Nemoh Properties\n')
            f.write(self.omegaStart.text() + "\t Starting Frequency\n")
            f.write(self.omegaStop.text() + "\t Ending Frequency\n")
            f.write(self.omegaStep.text() + "\t Number of Frequency Steps\n")
            f.write(str(self.wavDirCheck.isChecked()) + "\t Include Wave direction?\n")
            f.write(self.wavDirStart.text() + "\t Starting wave direction\n")
            f.write(self.wavDirStop.text() + "\t Ending wave direction\n")
            f.write(self.wavDirStep.text() + "\t Number of wave direction steps\n")
            f.write(str(self.irfCheck.isChecked()) + "\t Include IRF?\n")
            f.write(self.irfDur.text() + "\t Duration of IRF\n")
            f.write(self.irfStep.text() + "\t Time step of IRF\n")
            f.write(str(self.kochinCheck.isChecked()) + "\t Include Kochin Function?\n")
            f.write(self.kochinStart.text() + "\t Start of Kochin Function\n")
            f.write(self.kochinStop.text() + "\t End of Kochin Function\n")
            f.write(self.kochinStep.text() + "\t Number of Kochin Steps\n")
            f.write(str(self.fsCheck.isChecked()) + "\t Include Wave Free Surface?\n")
            f.write(self.fsDeltaX.text() + "\t Free Surface DeltaX\n")
            f.write(self.fsDeltaY.text() + "\t Free Surface DeltaY\n")
            f.write(self.fsLengthX.text() + "\t Free Surface X-length\n")
            f.write(self.fsLengthY.text() + "\t Free Surface Y-length\n") 
            # Write Time Domain Properties
            f.write('Time Domain Properties\n')
            f.write(str(self.wavType.currentIndex()) + "\t Wave Type\n")
            f.write(self.wavHBox.text() + "\t Wave Height\n")
            f.write(self.wavTBox.text() + "\t Wave Period\n")
            f.write(str(self.dampSelect.currentIndex()) + "\t Damping Type\n")
            if self.dampSelect.currentIndex()==0:
                f.write(self.msupEdit.text()+";"+self.bsupEdit.text()+";"+self.csupEdit.text() + "\t Damping Value\n")
            else:
                f.write(self.fdampEdit.text() + "\t Damping Value\n")
            f.write(self.simTimeBox.text() + "\t Simulation Time\n")
            f.write(self.dtBox.text() + "\t Simulation Time Step\n") 
            
        print(fname + " successfully written!")

    def about(self):
        print('openWEC alpha v0.1 \nCreated by Tim Verbrugghe \ntiml.verbrugghe@ugent.be')

    def manual(self):
        if sys.platform == 'linux2':
            os.system('xdg-open','Manual.pdf')
        else:
            os.startfile('Manual.pdf')

    def close(self):
        QtGui.QApplication.quit()

    def normalOutputWritten(self,text):
        cursor = self.messageBox.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.messageBox.setTextCursor(cursor)
        self.messageBox.ensureCursorVisible()

        cursor = self.nemMessBox.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.nemMessBox.setTextCursor(cursor)
        self.nemMessBox.ensureCursorVisible()

        cursor = self.simMessBox.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.simMessBox.setTextCursor(cursor)
        self.simMessBox.ensureCursorVisible()

        cursor = self.postMessBox.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.postMessBox.setTextCursor(cursor)
        self.postMessBox.ensureCursorVisible()

def openPE():
    ex2 = Ui_MainWindow()
    return ex2    

