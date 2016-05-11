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
import matplotlib.pyplot as plt
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

class MoorDynPopup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1032, 849)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.LineTypeTable = QtGui.QTableWidget(Form)
        self.LineTypeTable.setObjectName(_fromUtf8("LineTypeTable"))
        self.LineTypeTable.setColumnCount(9)
        self.LineTypeTable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.LineTypeTable.setHorizontalHeaderItem(8, item)
        self.verticalLayout_3.addWidget(self.LineTypeTable)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.NodeTable = QtGui.QTableWidget(Form)
        self.NodeTable.setObjectName(_fromUtf8("NodeTable"))
        self.NodeTable.setColumnCount(11)
        self.NodeTable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.NodeTable.setHorizontalHeaderItem(10, item)
        self.verticalLayout_3.addWidget(self.NodeTable)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.LinesTable = QtGui.QTableWidget(Form)
        self.LinesTable.setObjectName(_fromUtf8("LinesTable"))
        self.LinesTable.setColumnCount(6)
        self.LinesTable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.LinesTable.setItem(0, 1, item)
        self.verticalLayout_3.addWidget(self.LinesTable)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_10 = QtGui.QPushButton(Form)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MoorDyn Configuration", None))
        self.label.setText(_translate("Form", "Line Type", None))
        self.pushButton_5.setText(_translate("Form", "Add Line Type", None))
        self.pushButton_5.clicked.connect(lambda: self.addremLine(self.LineTypeTable,1))
        self.pushButton.setText(_translate("Form", "Remove Line Type", None))
        self.pushButton.clicked.connect(lambda: self.addremLine(self.LineTypeTable,-1))
        item = self.LineTypeTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.LineTypeTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name", None))
        item = self.LineTypeTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Diameter", None))
        item = self.LineTypeTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mass Density", None))
        item = self.LineTypeTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Line Stifness", None))
        item = self.LineTypeTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Internal Damping", None))
        item = self.LineTypeTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Can", None))
        item = self.LineTypeTable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Cat", None))
        item = self.LineTypeTable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Cdn", None))
        item = self.LineTypeTable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Cdt", None))
        self.label_2.setText(_translate("Form", "Nodes", None))
        self.pushButton_7.setText(_translate("Form", "Add Node", None))
        self.pushButton_7.clicked.connect(lambda: self.addremLine(self.NodeTable,1))
        self.pushButton_6.setText(_translate("Form", "Remove Node", None))
        self.pushButton_6.clicked.connect(lambda: self.addremLine(self.NodeTable,-1))
        item = self.NodeTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.NodeTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.NodeTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "X", None))
        item = self.NodeTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Y", None))
        item = self.NodeTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Z", None))
        item = self.NodeTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Mass", None))
        item = self.NodeTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Volume", None))
        item = self.NodeTable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Fx", None))
        item = self.NodeTable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Fy", None))
        item = self.NodeTable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Fz", None))
        item = self.NodeTable.horizontalHeaderItem(9)
        item.setText(_translate("Form", "CdA", None))
        item = self.NodeTable.horizontalHeaderItem(10)
        item.setText(_translate("Form", "CA", None))
        self.label_3.setText(_translate("Form", "Lines", None))
        self.pushButton_9.setText(_translate("Form", "Add Line", None))
        self.pushButton_9.clicked.connect(lambda: self.addremLine(self.LinesTable,1))
        self.pushButton_8.setText(_translate("Form", "Remove Line", None))
        self.pushButton_8.clicked.connect(lambda: self.addremLine(self.LinesTable,-1))
        item = self.LinesTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.LinesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.LinesTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Unstretched Length", None))
        item = self.LinesTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "# Segments", None))
        item = self.LinesTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Anchor Node", None))
        item = self.LinesTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Vessel Node", None))
        item = self.LinesTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Output?", None))
        __sortingEnabled = self.LinesTable.isSortingEnabled()
        self.LinesTable.setSortingEnabled(False)
        self.LinesTable.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "Open Lines File", None))
        self.pushButton_2.clicked.connect(self.openLinesFile)
        self.pushButton_3.setText(_translate("Form", "Save Lines File", None))
        self.pushButton_3.clicked.connect(self.saveLinesFile)
        self.pushButton_10.setText(_translate("Form", "Manual", None))
        self.pushButton_10.clicked.connect(self.openMdManual)
        self.pushButton_4.setText(_translate("Form", "Cancel", None))
        self.pushButton_4.clicked.connect(self.close)
        
    def addremLine(self,table,ltype):
        rowC = table.rowCount()
        if ltype > 0:
            table.setRowCount(rowC+1)
        else:
            if table.currentRow() > -1:
                row = table.currentRow()
                table.removeRow(row)
            else:
                table.setRowCount(rowC-1)
        
    def openMdManual(self):
        os.chdir('Mooring')
        if sys.platform == 'linux2':
            os.system('xdg-open','MoorDyn_Manual.pdf')
        else:
            os.startfile('MoorDyn_Manual.pdf')
        os.chdir('..')
        
    def openLinesFile(self):
        sys.path.insert(0, './Run')
        import moorSim as ms        
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                        './Mooring','*.txt')
        mdLines = ms.openLines(fname)
        # Line types
        self.LineTypeTable.setRowCount(mdLines['nrLineTypes'])
        for iL in range(mdLines['nrLineTypes']):
            for iC in range(len(mdLines['linetype_{:d}'.format(iL+1)])):
                text = mdLines['linetype_{:d}'.format(iL+1)][iC]
                self.LineTypeTable.setItem(iL, iC, QtGui.QTableWidgetItem(text))
                
        # Nodes
        self.NodeTable.setRowCount(mdLines['nrNodes'])
        for iL in range(mdLines['nrNodes']):
            for iC in range(len(mdLines['node_{:d}'.format(iL+1)])):
                text = mdLines['node_{:d}'.format(iL+1)][iC]
                self.NodeTable.setItem(iL, iC, QtGui.QTableWidgetItem(text))
                
        # Lines
        self.LinesTable.setRowCount(mdLines['nrLines'])
        for iL in range(mdLines['nrLines']):
            for iC in range(len(mdLines['line_{:d}'.format(iL+1)])):
                text = mdLines['line_{:d}'.format(iL+1)][iC]
                self.LinesTable.setItem(iL, iC, QtGui.QTableWidgetItem(text))
                
    def saveLinesFile(self):
        linesFile = ['']
        depth = 0.0
        
        # Header
        linesFile.append('MoorDyn input file for OpenWEC mooring system\n')
        
        # Line Dictionary
        linesFile.append('---------------------- LINE DICTIONARY -----------------------------------------------------\n')
        linesFile.append('LineType  Diam    MassDenInAir    EA        BA/-zeta     Can     Cat    Cdn     Cdt\n')
        linesFile.append('(-)       (m)       (kg/m)        (N)       (Pa-s/-)     (-)     (-)    (-)     (-)\n')
        for iR in range(self.LineTypeTable.rowCount()):
            line = ''
            for iC in range(self.LineTypeTable.columnCount()):
                line = line + self.LineTypeTable.item(iR,iC).text() + '\t'
            line = line + '\n'
            linesFile.append(line)
            
        # Nodes
        linesFile.append('---------------------- NODE PROPERTIES -----------------------------------------------------\n')
        linesFile.append('Node      Type      X        Y         Z        M        V        FX       FY      FZ     CdA   CA\n')
        linesFile.append('(-)       (-)      (m)      (m)       (m)      (kg)     (m^3)    (kN)     (kN)    (kN)   (m^2)  (-)\n')
        for iR in range(self.NodeTable.rowCount()):
            line = '{:d}\t'.format(iR+1)
            for iC in range(self.NodeTable.columnCount()):
                line = line + self.NodeTable.item(iR,iC).text() + '\t'
                if iC==3:
                    depthT = -1.0*float(self.NodeTable.item(iR,iC).text())
                    if depthT > depth:
                        depth = depthT
            line = line + '\n'
            linesFile.append(line)
            
        # Lines
        linesFile.append('---------------------- LINE PROPERTIES -----------------------------------------------------\n')
        linesFile.append('Line     LineType  UnstrLen  NumSegs   NodeAnch  NodeFair  Flags/Outputs\n')
        linesFile.append('(-)      (-)       (m)         (-)       (-)       (-)       (-)\n')
        for iR in range(self.LinesTable.rowCount()):
            line = '{:d}\t'.format(iR+1)
            for iC in range(self.LinesTable.columnCount()):
                line = line + self.LinesTable.item(iR,iC).text() + '\t'
            line = line + '\n'
            linesFile.append(line)
        
        # Solver Options
        linesFile.append('---------------------- SOLVER OPTIONS-----------------------------------------\n')
        linesFile.append('0.002    dtM          - time step to use in mooring integration\n')
        linesFile.append('0        WaveKin      - wave kinematics flag (0=neglect, the only option currently supported)\n')
        linesFile.append('3.0e0    kBot         - bottom stiffness\n')
        linesFile.append('3.0e0    cBot         - bottom damping\n')
        linesFile.append('{:f}      WtrDpth      - water depth\n'.format(depth))
        linesFile.append('5.0      CdScaleIC    - factor by which to scale drag coefficients during dynamic relaxation IC gen\n')
        linesFile.append('0.001    threshIC     - threshold for IC convergence\n')
        linesFile.append('-------------------------- OUTPUTS --------------------------------\n')
        linesFile.append('FairTen1 FairTen2 FairTen3\n')
        linesFile.append('--------------------- need this line ------------------\n')
        
        # Write file
        with open('Mooring/lines.txt','w') as f:
            f.writelines(linesFile)
        print('Lines file succesfully written!\n')
        
    def close(self):
        self.hide()
        
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
        self.meshMethodLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.meshMethodLabel.setFont(font)
        self.meshMethodLabel.setObjectName(_fromUtf8("meshMethodLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.meshMethodLabel)
        self.meshMethod = QtGui.QComboBox(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.meshMethod.setFont(font)
        self.meshMethod.setObjectName(_fromUtf8("meshMethod"))
        self.meshMethod.addItem(_fromUtf8(""))
        self.meshMethod.addItem(_fromUtf8(""))
        self.meshMethod.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.meshMethod)
        self.geoProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.geoProp.setFont(font)
        self.geoProp.setObjectName(_fromUtf8("geoProp"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.geoProp)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.comboBox = QtGui.QComboBox(self.tabMesh)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_7.addWidget(self.comboBox)
        self.sketchShape = QtGui.QLabel(self.tabMesh)
        self.sketchShape.setText(_fromUtf8(""))
        self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/box.png")))
        self.sketchShape.setObjectName(_fromUtf8("sketchShape"))
        self.verticalLayout_7.addWidget(self.sketchShape)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.LabelRole, self.verticalLayout_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.propForm = QtGui.QFormLayout()
        self.propForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.propForm.setObjectName(_fromUtf8("propForm"))
        self.propLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.propLabel.setFont(font)
        self.propLabel.setObjectName(_fromUtf8("propLabel"))
        self.propForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.propLabel)
        self.prop1Label = QtGui.QLabel(self.tabMesh)
        self.prop1Label.setObjectName(_fromUtf8("prop1Label"))
        self.propForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.prop1Label)
        self.prop1 = QtGui.QLineEdit(self.tabMesh)
        self.prop1.setObjectName(_fromUtf8("prop1"))
        self.propForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.prop1)
        self.prop2Label = QtGui.QLabel(self.tabMesh)
        self.prop2Label.setObjectName(_fromUtf8("prop2Label"))
        self.propForm.setWidget(2, QtGui.QFormLayout.LabelRole, self.prop2Label)
        self.prop2 = QtGui.QLineEdit(self.tabMesh)
        self.prop2.setObjectName(_fromUtf8("prop2"))
        self.propForm.setWidget(2, QtGui.QFormLayout.FieldRole, self.prop2)
        self.prop3Label = QtGui.QLabel(self.tabMesh)
        self.prop3Label.setObjectName(_fromUtf8("prop3Label"))
        self.propForm.setWidget(3, QtGui.QFormLayout.LabelRole, self.prop3Label)
        self.prop3 = QtGui.QLineEdit(self.tabMesh)
        self.prop3.setObjectName(_fromUtf8("prop3"))
        self.propForm.setWidget(3, QtGui.QFormLayout.FieldRole, self.prop3)
        self.XinsLabel = QtGui.QLabel(self.tabMesh)
        self.XinsLabel.setObjectName(_fromUtf8("XinsLabel"))
        self.propForm.setWidget(4, QtGui.QFormLayout.LabelRole, self.XinsLabel)
        self.Xins = QtGui.QLineEdit(self.tabMesh)
        self.Xins.setObjectName(_fromUtf8("Xins"))
        self.propForm.setWidget(4, QtGui.QFormLayout.FieldRole, self.Xins)
        self.YinsLabel = QtGui.QLabel(self.tabMesh)
        self.YinsLabel.setObjectName(_fromUtf8("YinsLabel"))
        self.propForm.setWidget(5, QtGui.QFormLayout.LabelRole, self.YinsLabel)
        self.Yins = QtGui.QLineEdit(self.tabMesh)
        self.Yins.setObjectName(_fromUtf8("Yins"))
        self.propForm.setWidget(5, QtGui.QFormLayout.FieldRole, self.Yins)
        self.ZinsLabel = QtGui.QLabel(self.tabMesh)
        self.ZinsLabel.setObjectName(_fromUtf8("ZinsLabel"))
        self.propForm.setWidget(6, QtGui.QFormLayout.LabelRole, self.ZinsLabel)
        self.Zins = QtGui.QLineEdit(self.tabMesh)
        self.Zins.setObjectName(_fromUtf8("Zins"))
        self.propForm.setWidget(6, QtGui.QFormLayout.FieldRole, self.Zins)
        self.createObj = QtGui.QPushButton(self.tabMesh)
        self.createObj.setObjectName(_fromUtf8("createObj"))
        self.propForm.setWidget(7, QtGui.QFormLayout.FieldRole, self.createObj)
        self.horizontalLayout.addLayout(self.propForm)
        self.transForm = QtGui.QFormLayout()
        self.transForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.transForm.setObjectName(_fromUtf8("transForm"))
        self.transLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.transLabel.setFont(font)
        self.transLabel.setObjectName(_fromUtf8("transLabel"))
        self.transForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.transLabel)
        self.label_3 = QtGui.QLabel(self.tabMesh)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.transForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.transForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtGui.QLabel(self.tabMesh)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.transForm.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.transForm.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtGui.QLabel(self.tabMesh)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.transForm.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_3 = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.transForm.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtGui.QPushButton(self.tabMesh)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.transForm.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.horizontalLayout.addLayout(self.transForm)
        self.rotForm = QtGui.QFormLayout()
        self.rotForm.setObjectName(_fromUtf8("rotForm"))
        self.label_4 = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.rotForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_7 = QtGui.QLabel(self.tabMesh)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.rotForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_4 = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.rotForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_8 = QtGui.QLabel(self.tabMesh)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rotForm.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.rotForm.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_9 = QtGui.QLabel(self.tabMesh)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.rotForm.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_6 = QtGui.QLineEdit(self.tabMesh)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.rotForm.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.pushButton_2 = QtGui.QPushButton(self.tabMesh)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.rotForm.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.horizontalLayout.addLayout(self.rotForm)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_10 = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_10)
        self.listWidget = QtGui.QListWidget(self.tabMesh)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.listWidget)
        self.waterDepthLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.waterDepthLabel.setFont(font)
        self.waterDepthLabel.setObjectName(_fromUtf8("waterDepthLabel"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.waterDepthLabel)
        self.waterDepthBox = QtGui.QLineEdit(self.tabMesh)
        self.waterDepthBox.setObjectName(_fromUtf8("waterDepthBox"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.waterDepthBox)
        self.zGLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.zGLabel.setFont(font)
        self.zGLabel.setObjectName(_fromUtf8("zGLabel"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.zGLabel)
        self.zGBox = QtGui.QLineEdit(self.tabMesh)
        self.zGBox.setObjectName(_fromUtf8("zGBox"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.zGBox)
        self.rhoLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.rhoLabel.setFont(font)
        self.rhoLabel.setObjectName(_fromUtf8("rhoLabel"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.rhoLabel)
        self.rhoBox = QtGui.QLineEdit(self.tabMesh)
        self.rhoBox.setObjectName(_fromUtf8("rhoBox"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.FieldRole, self.rhoBox)
        self.MeshProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.MeshProp.setFont(font)
        self.MeshProp.setObjectName(_fromUtf8("MeshProp"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.LabelRole, self.MeshProp)
        self.nPanelLabel = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.nPanelLabel.setFont(font)
        self.nPanelLabel.setObjectName(_fromUtf8("nPanelLabel"))
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.LabelRole, self.nPanelLabel)
        self.nPanelBox = QtGui.QLineEdit(self.tabMesh)
        self.nPanelBox.setObjectName(_fromUtf8("nPanelBox"))
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.FieldRole, self.nPanelBox)
        self.meshButton = QtGui.QPushButton(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.meshButton.setFont(font)
        self.meshButton.setObjectName(_fromUtf8("meshButton"))
        self.formLayout_3.setWidget(12, QtGui.QFormLayout.FieldRole, self.meshButton)
        self.pushButton_3 = QtGui.QPushButton(self.tabMesh)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButton_3)
        self.genProp = QtGui.QLabel(self.tabMesh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.genProp.setFont(font)
        self.genProp.setObjectName(_fromUtf8("genProp"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.genProp)
        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabMesh, _fromUtf8(""))

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
        self.dofLabel = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.dofLabel.setFont(font)
        self.dofLabel.setObjectName(_fromUtf8("dofLabel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.dofLabel)
        self.dofImage = QtGui.QLabel(self.tabNemoh)
        self.dofImage.setText(_fromUtf8(""))
        self.dofImage.setPixmap(QtGui.QPixmap(_fromUtf8("src/dof.PNG")))
        self.dofImage.setScaledContents(False)
        self.dofImage.setObjectName(_fromUtf8("dofImage"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.dofImage)        
        self.dofLayout = QtGui.QGridLayout()
        self.dofLayout.setObjectName(_fromUtf8("dofLayout"))
        self.checkRoll = QtGui.QCheckBox(self.tabNemoh)
        self.checkRoll.setObjectName(_fromUtf8("checkRoll"))
        self.dofLayout.addWidget(self.checkRoll, 0, 1, 1, 1)
        self.checkHeave = QtGui.QCheckBox(self.tabNemoh)
        self.checkHeave.setObjectName(_fromUtf8("checkHeave"))
        self.dofLayout.addWidget(self.checkHeave, 2, 0, 1, 1)
        self.checkYaw = QtGui.QCheckBox(self.tabNemoh)
        self.checkYaw.setObjectName(_fromUtf8("checkYaw"))
        self.dofLayout.addWidget(self.checkYaw, 2, 1, 1, 1)
        self.checkPitch = QtGui.QCheckBox(self.tabNemoh)
        self.checkPitch.setObjectName(_fromUtf8("checkPitch"))
        self.dofLayout.addWidget(self.checkPitch, 1, 1, 1, 1)
        self.checkSurge = QtGui.QCheckBox(self.tabNemoh)
        self.checkSurge.setObjectName(_fromUtf8("checkSurge"))
        self.dofLayout.addWidget(self.checkSurge, 0, 0, 1, 1)
        self.checkSway = QtGui.QCheckBox(self.tabNemoh)
        self.checkSway.setObjectName(_fromUtf8("checkSway"))
        self.dofLayout.addWidget(self.checkSway, 1, 0, 1, 1)
        self.formLayout_2.setLayout(6, QtGui.QFormLayout.FieldRole, self.dofLayout)
        self.label_2 = QtGui.QLabel(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_2)
        self.wavDirStart = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStart.setObjectName(_fromUtf8("wavDirStart"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.wavDirStart)
        self.wavDirStop = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStop.setObjectName(_fromUtf8("wavDirStop"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.wavDirStop)
        self.wavDirStep = QtGui.QLineEdit(self.tabNemoh)
        self.wavDirStep.setObjectName(_fromUtf8("wavDirStep"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.FieldRole, self.wavDirStep)
        self.irfLabel = QtGui.QLabel(self.tabNemoh)
        self.irfLabel.setObjectName(_fromUtf8("irfLabel"))
        self.formLayout_2.setWidget(12, QtGui.QFormLayout.LabelRole, self.irfLabel)
        self.irfCheck = QtGui.QCheckBox(self.tabNemoh)
        self.irfCheck.setText(_fromUtf8(""))
        self.irfCheck.setObjectName(_fromUtf8("irfCheck"))
        self.formLayout_2.setWidget(12, QtGui.QFormLayout.FieldRole, self.irfCheck)
        self.irfDur = QtGui.QLineEdit(self.tabNemoh)
        self.irfDur.setObjectName(_fromUtf8("irfDur"))
        self.formLayout_2.setWidget(13, QtGui.QFormLayout.FieldRole, self.irfDur)
        self.irfStep = QtGui.QLineEdit(self.tabNemoh)
        self.irfStep.setObjectName(_fromUtf8("irfStep"))
        self.formLayout_2.setWidget(14, QtGui.QFormLayout.FieldRole, self.irfStep)
        self.kochinLabel = QtGui.QLabel(self.tabNemoh)
        self.kochinLabel.setObjectName(_fromUtf8("kochinLabel"))
        self.formLayout_2.setWidget(15, QtGui.QFormLayout.LabelRole, self.kochinLabel)
        self.kochinCheck = QtGui.QCheckBox(self.tabNemoh)
        self.kochinCheck.setText(_fromUtf8(""))
        self.kochinCheck.setObjectName(_fromUtf8("kochinCheck"))
        self.formLayout_2.setWidget(15, QtGui.QFormLayout.FieldRole, self.kochinCheck)
        self.kochinStart = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStart.setObjectName(_fromUtf8("kochinStart"))
        self.formLayout_2.setWidget(16, QtGui.QFormLayout.FieldRole, self.kochinStart)
        self.kochinStop = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStop.setObjectName(_fromUtf8("kochinStop"))
        self.formLayout_2.setWidget(17, QtGui.QFormLayout.FieldRole, self.kochinStop)
        self.kochinStep = QtGui.QLineEdit(self.tabNemoh)
        self.kochinStep.setObjectName(_fromUtf8("kochinStep"))
        self.formLayout_2.setWidget(18, QtGui.QFormLayout.FieldRole, self.kochinStep)
        self.nemohButton = QtGui.QPushButton(self.tabNemoh)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.nemohButton.setFont(font)
        self.nemohButton.setObjectName(_fromUtf8("nemohButton"))
        self.formLayout_2.setWidget(24, QtGui.QFormLayout.FieldRole, self.nemohButton)
        self.wavDirCheck = QtGui.QCheckBox(self.tabNemoh)
        self.wavDirCheck.setText(_fromUtf8(""))
        self.wavDirCheck.setObjectName(_fromUtf8("wavDirCheck"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.wavDirCheck)
        self.wavDirLabel = QtGui.QLabel(self.tabNemoh)
        self.wavDirLabel.setObjectName(_fromUtf8("wavDirLabel"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.wavDirLabel)
        self.fsCheck = QtGui.QCheckBox(self.tabNemoh)
        self.fsCheck.setText(_fromUtf8(""))
        self.fsCheck.setObjectName(_fromUtf8("fsCheck"))
        self.formLayout_2.setWidget(19, QtGui.QFormLayout.FieldRole, self.fsCheck)
        self.fsLabel = QtGui.QLabel(self.tabNemoh)
        self.fsLabel.setObjectName(_fromUtf8("fsLabel"))
        self.formLayout_2.setWidget(19, QtGui.QFormLayout.LabelRole, self.fsLabel)
        self.fsDeltaX = QtGui.QLineEdit(self.tabNemoh)
        self.fsDeltaX.setObjectName(_fromUtf8("fsDeltaX"))
        self.formLayout_2.setWidget(20, QtGui.QFormLayout.FieldRole, self.fsDeltaX)
        self.fsDeltaY = QtGui.QLineEdit(self.tabNemoh)
        self.fsDeltaY.setObjectName(_fromUtf8("fsDeltaY"))
        self.formLayout_2.setWidget(21, QtGui.QFormLayout.FieldRole, self.fsDeltaY)
        self.fsLengthX = QtGui.QLineEdit(self.tabNemoh)
        self.fsLengthX.setObjectName(_fromUtf8("fsLengthX"))
        self.formLayout_2.setWidget(22, QtGui.QFormLayout.FieldRole, self.fsLengthX)
        self.fsLengthY = QtGui.QLineEdit(self.tabNemoh)
        self.fsLengthY.setObjectName(_fromUtf8("fsLengthY"))
        self.formLayout_2.setWidget(23, QtGui.QFormLayout.FieldRole, self.fsLengthY)
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
        self.fdampBox = QtGui.QLineEdit(self.tabSim)
        self.fdampBox.setObjectName(_fromUtf8("fdampBox"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.fdampBox)
        
        verticalSpacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.LabelRole, verticalSpacer)        
        self.moorPropLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.moorPropLabel.setFont(font)
        self.moorPropLabel.setObjectName(_fromUtf8("moorPropLabel"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.moorPropLabel)
        self.moorCheck = QtGui.QCheckBox(self.tabSim)
        self.moorCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.moorCheck.setObjectName(_fromUtf8("moorCheck"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.moorCheck)
        self.moorConfig = QtGui.QPushButton(self.tabSim)
        self.moorConfig.setObjectName(_fromUtf8("moorConfig"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.moorConfig)
        
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.simProp = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.simProp.setFont(font)
        self.simProp.setObjectName(_fromUtf8("simProp"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.simProp)
        self.simTimeLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.simTimeLabel.setFont(font)
        self.simTimeLabel.setObjectName(_fromUtf8("simTimeLabel"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.simTimeLabel)
        self.simTimeBox = QtGui.QLineEdit(self.tabSim)
        self.simTimeBox.setObjectName(_fromUtf8("simTimeBox"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.simTimeBox)
        self.dtLabel = QtGui.QLabel(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.dtLabel.setFont(font)
        self.dtLabel.setObjectName(_fromUtf8("dtLabel"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.LabelRole, self.dtLabel)
        self.dtBox = QtGui.QLineEdit(self.tabSim)
        self.dtBox.setObjectName(_fromUtf8("dtBox"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.dtBox)
        self.simButton = QtGui.QPushButton(self.tabSim)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Raleway"))
        self.simButton.setFont(font)
        self.simButton.setObjectName(_fromUtf8("simButton"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.simButton)
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
        # Postprocessing tab
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
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.FieldRole, self.makePlot1)
        self.lowPlotTitle = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lowPlotTitle.setFont(font)
        self.lowPlotTitle.setObjectName(_fromUtf8("lowPlotTitle"))
        self.formLayout_5.setWidget(9, QtGui.QFormLayout.LabelRole, self.lowPlotTitle)
        self.plotX2 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotX2.setFont(font)
        self.plotX2.setObjectName(_fromUtf8("plotX2"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.LabelRole, self.plotX2)
        self.plotY2 = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.plotY2.setFont(font)
        self.plotY2.setObjectName(_fromUtf8("plotY2"))
        self.formLayout_5.setWidget(11, QtGui.QFormLayout.LabelRole, self.plotY2)
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
        self.formLayout_5.setWidget(11, QtGui.QFormLayout.FieldRole, self.chooseY2)
        self.chooseX2 = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.chooseX2.setFont(font)
        self.chooseX2.setObjectName(_fromUtf8("chooseX2"))
        self.chooseX2.addItem(_fromUtf8(""))
        self.chooseX2.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.FieldRole, self.chooseX2)
        self.makePlot2 = QtGui.QPushButton(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.makePlot2.setFont(font)
        self.makePlot2.setObjectName(_fromUtf8("makePlot2"))
        self.formLayout_5.setWidget(13, QtGui.QFormLayout.FieldRole, self.makePlot2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_5.setItem(8, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.dofPlotU = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.dofPlotU.setFont(font)
        self.dofPlotU.setObjectName(_fromUtf8("dofPlotU"))
        self.dofPlotU.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.FieldRole, self.dofPlotU)
        self.dofPlotLabelU = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.dofPlotLabelU.setFont(font)
        self.dofPlotLabelU.setObjectName(_fromUtf8("dofPlotLabelU"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.dofPlotLabelU)
        self.dofPlotL = QtGui.QComboBox(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.dofPlotL.setFont(font)
        self.dofPlotL.setObjectName(_fromUtf8("dofPlotL"))
        self.dofPlotL.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(12, QtGui.QFormLayout.FieldRole, self.dofPlotL)
        self.dofLabelL = QtGui.QLabel(self.tabPost)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.dofLabelL.setFont(font)
        self.dofLabelL.setObjectName(_fromUtf8("dofLabelL"))
        self.formLayout_5.setWidget(12, QtGui.QFormLayout.LabelRole, self.dofLabelL)        
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
        # Set GUI
        # Mesh Tab
        MainWindow.setWindowTitle(_translate("openWEC", "openWEC", None))
        self.infoConsoleLabel.setText(_translate("openWEC", "Information Console", None))
        self.visualisationLabel.setText(_translate("openWEC", "Visualisation", None))
        self.meshMethodLabel.setText(_translate("openWEC", "Mesh method:", None))
        self.meshMethod.setItemText(0, _translate("openWEC", "Generate new", None))
        self.meshMethod.setItemText(1, _translate("openWEC", "Import Nemoh mesh", None))
        self.meshMethod.setItemText(2, _translate("openWEC", "Convert .stl mesh", None))
        self.meshMethod.currentIndexChanged.connect(self.displayMessage)
        self.geoProp.setText(_translate("openWEC", "Mesh Creator", None))
        self.comboBox.setItemText(0, _translate("openWEC", "Box", None))
        self.comboBox.setItemText(1, _translate("openWEC", "Cylinder", None))
        self.comboBox.setItemText(2, _translate("openWEC", "Cone", None))
        self.comboBox.setItemText(3, _translate("openWEC", "Sphere", None))
        self.comboBox.setItemText(4, _translate("openWEC", "Pyramid", None))
        self.comboBox.setItemText(5, _translate("openWEC", "Wedge", None))
        self.comboBox.setItemText(6, _translate("openWEC", "Hemisphere", None))
        self.comboBox.setItemText(7, _translate("openWEC", "Hemicylinder", None))
        self.comboBox.currentIndexChanged.connect(self.meshTypeFig)
        self.propLabel.setText(_translate("openWEC", "Properties", None))
        self.prop1Label.setText(_translate("openWEC", "Length", None))
        self.prop2Label.setText(_translate("openWEC", "Width", None))
        self.prop3Label.setText(_translate("openWEC", "Height", None))
        self.XinsLabel.setText(_translate("openWEC", "Xinsert", None))
        self.YinsLabel.setText(_translate("openWEC", "Yinsert", None))
        self.ZinsLabel.setText(_translate("openWEC", "Zinsert", None))
        self.createObj.setText(_translate("openWEC", "Create", None))
        self.transLabel.setText(_translate("openWEC", "Translation", None))
        self.label_3.setText(_translate("openWEC", "tX", None))
        self.label_5.setText(_translate("openWEC", "tY", None))
        self.label_6.setText(_translate("openWEC", "tZ", None))
        self.pushButton.setText(_translate("openWEC", "Translate", None))
        self.label_4.setText(_translate("openWEC", "Rotation", None))
        self.label_7.setText(_translate("openWEC", "theta", None))
        self.label_8.setText(_translate("openWEC", "axis (x1,y1,z1)", None))
        self.label_9.setText(_translate("openWEC", "axis (x2,y2,z2)", None))
        self.pushButton_2.setText(_translate("openWEC", "Rotate", None))
        self.label_10.setText(_translate("openWEC", "Object List", None))
        self.waterDepthLabel.setText(_translate("openWEC", "Water Depth:", None))
        self.waterDepthBox.setPlaceholderText(_translate("openWEC", "in meter; 0 for infinite depth", None))
        self.zGLabel.setText(_translate("openWEC", "Position of COG:", None))
        self.zGBox.setPlaceholderText(_translate("openWEC", "in meter; negative below WL", None))
        self.rhoLabel.setText(_translate("openWEC", "Density:", None))
        self.rhoBox.setPlaceholderText(_translate("openWEC", "in kg/m³", None))
        self.MeshProp.setText(_translate("openWEC", "Mesh Properties:", None))
        self.nPanelLabel.setText(_translate("openWEC", "Number of mesh panels: ", None))
        self.nPanelBox.setPlaceholderText(_translate("openWEC", "integer (>100)", None))
        self.meshButton.setText(_translate("openWEC", "Mesh!", None))
        self.pushButton_3.setText(_translate("openWEC", "Delete selected object", None))
        self.genProp.setText(_translate("openWEC", "General properties", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMesh), _translate("openWEC", "Mesh Tool", None))
        self.nemConsLabel.setText(_translate("openWEC", "Information Console", None))
        self.nemVisualisation.setText(_translate("openWEC", "Visualisation", None))
        self.createObj.clicked.connect(self.drawObj)
        self.meshButton.clicked.connect(self.makeMesh)
        self.pushButton.clicked.connect(self.transObj)
        self.pushButton_2.clicked.connect(self.rotObj)
        self.pushButton_3.clicked.connect(self.delObj)
        # Nemoh Tab
        self.labelBEM.setText(_translate("MainWindow", "BEM Solver Options", None))
        self.label.setText(_translate("MainWindow", "Basic", None))
        self.omegaLabel.setText(_translate("MainWindow", "Frequency range:", None))
        self.omegaStart.setPlaceholderText(_translate("MainWindow", "start in rad/s (0.2)", None))
        self.omegaStop.setPlaceholderText(_translate("MainWindow", "stop in rad/s (2.5)", None))
        self.omegaStep.setPlaceholderText(_translate("MainWindow", "number of steps in between (50)", None))
        self.dofLabel.setText(_translate("openWEC", "Degrees of Freedom", None))
        self.checkRoll.setText(_translate("openWEC", "Roll (X-rotation)", None))
        self.checkHeave.setText(_translate("openWEC", "Heave (Z-translation)", None))
        self.checkHeave.setChecked(True)
        self.checkYaw.setText(_translate("openWEC", "Yaw (Z-rotation)", None))
        self.checkPitch.setText(_translate("openWEC", "Pitch (Y-rotation)", None))
        self.checkSurge.setText(_translate("openWEC", "Surge (X-translation)", None))
        self.checkSway.setText(_translate("openWEC", "Sway (Y-translation)", None))        
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
        self.fdampLabel.setText(_translate("MainWindow", "Damping Value:", None))
        self.dampTypeLabel.setText(_translate("openWEC", "Damping Type:", None))
        self.dampSelect.setItemText(0, _translate("openWEC", "Linear", None))
        self.dampSelect.setItemText(1, _translate("openWEC", "Coulomb", None))
        self.fdampBox.setPlaceholderText(_translate("MainWindow", "in N for Coulomb, in kg/s for Linear", None))
        self.moorPropLabel.setText(_translate("openWEC", "Mooring Properties", None))
        self.moorCheck.setText(_translate("openWEC", "Enable Mooring Lines", None))
        self.moorCheck.clicked.connect(self.changeMoorDyn)
        self.moorConfig.setText(_translate("openWEC", "Configure...", None))
        self.moorConfig.clicked.connect(self.runMoorDynConfig)
        self.moorConfig.setEnabled(False)
        self.simProp.setText(_translate("MainWindow", "Simulation", None))
        self.simTimeLabel.setText(_translate("MainWindow", "Time:", None))
        self.simTimeBox.setPlaceholderText(_translate("MainWindow", "in seconds", None))
        self.dtLabel.setText(_translate("MainWindow", "Time Step:", None))
        self.dtBox.setPlaceholderText(_translate("MainWindow", "in seconds", None))
        self.simButton.setText(_translate("MainWindow", "Simulate!", None))
        self.simButton.clicked.connect(self.runSimulation)
        self.nemConsLabel_2.setText(_translate("MainWindow", "Information Console", None))
        self.nemVisualisation_2.setText(_translate("MainWindow", "Visualisation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSim), _translate("MainWindow", "Simulation", None))
        # Post Processor
        self.plotToolTitle.setText(_translate("MainWindow", "Plotting Tool", None))
        self.upPlotTitle.setText(_translate("MainWindow", "Upper Plot", None))
        self.plotX1.setText(_translate("MainWindow", "Variable for X-axis                                                                  ", None))
        self.chooseX1.setItemText(0, _translate("MainWindow", "Frequency                                                                   ", None))
        self.chooseX1.setItemText(1, _translate("MainWindow", "Time", None))
        self.chooseX1.currentIndexChanged.connect(partial(self.plotVariables,plotWindow=1))
        self.plotY1.setText(_translate("MainWindow", "Variable for Y-axis", None))
        self.chooseY1.setItemText(0, _translate("MainWindow", "Added Mass", None))
        self.chooseY1.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
        self.chooseY1.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
        self.chooseY1.setItemText(3, _translate("MainWindow", "Response Amplitude Operator", None))
        self.dofPlotU.setItemText(0, _translate("openWEC", "-", None))
        self.dofPlotLabelU.setText(_translate("openWEC", "Degree of Freedom", None))        
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
        self.chooseX2.currentIndexChanged.connect(partial(self.plotVariables,plotWindow=2))
        self.dofPlotL.setItemText(0, _translate("openWEC", "-", None))
        self.dofLabelL.setText(_translate("openWEC", "Degree of Freedom", None))        
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
        # Get the correct dof data        
        import processNemoh as pn
        nameDof = ['Surge','Sway','Heave','Roll','Pitch','Yaw']
            
        # Set the correct variables
        if plotWindow == 1:
            dofSel = [0,0,0,0,0,0]
            test = self.chooseX1.currentIndex() + 2*self.chooseY1.currentIndex()
            iSel = nameDof.index(self.dofPlotU.currentText())
            dofSel[iSel] = 1
            mpl = self.mpl1
            ntb = self.ntb1
        else:
            dofSel = [0,0,0,0,0,0]
            test = self.chooseX2.currentIndex() + 2*self.chooseY2.currentIndex()
            iSel = nameDof.index(self.dofPlotL.currentText())
            dofSel[iSel] = 1
            mpl = self.mpl2
            ntb = self.ntb2
         
        (self.Ma,self.Bhyd,omeg) = pn.getAB(self.dof,sel=iSel)
        self.freq = omeg/(2*np.pi)
        (self.Fe,self.Fpha) = pn.getFe(self.dof,sel=iSel)
        (Mass,KH) = pn.calcM(rho=1025.0,dof=dofSel)
        self.RAO = (self.Fe)/np.abs(-omeg**2.0*(Mass+self.Ma)-1j*omeg*self.Bhyd+KH)
        
        if test % 2 == 1:
            if sum(self.dof) > 1:
                posZ = self.posZ[iSel,:]  
                velZ = self.velZ[iSel,:]       
                Fpto = self.Fpto[iSel,:]
            else:
                posZ = self.posZ 
                velZ = self.velZ       
                Fpto = self.Fpto
            
        if test==0:
            xVar = self.freq
            yVar = self.Ma
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Added Mass/Inertia$'
        elif test==1:
            xVar = self.time
            yVar = self.wave
            xlabel = '$Time [s]$'
            ylabel = '$\eta [m]$'
        elif test==2:
            xVar = self.freq
            yVar = self.Bhyd
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Hydrodynamic Damping$'
        elif test==3:
            xVar = self.time
            yVar = posZ
            xlabel = '$Time [s]$'
            ylabel = '$WEC Response$'
        elif test==4:
            xVar = self.freq
            yVar = self.Fe
            xlabel = '$Frequency [Hz]$'
            ylabel = '$Excitation Force/Torque$'
        elif test==5:
            xVar = self.time
            yVar = velZ
            xlabel = '$Time [s]$'
            ylabel = '$WEC Velocity$'
        elif test==6:
            xVar = self.freq
            yVar = self.RAO
            xlabel = '$Frequency [s]$'
            ylabel = '$RAO$'
        elif test==7:
            xVar = self.time
            yVar = Fpto
            xlabel = '$Time [s]$'
            ylabel = '$PTO Force/Torque$'
        # Plot the variables
        self.updateGraph(x=xVar,y=yVar,g=mpl,t=ntb,xlab=xlabel,ylab=ylabel)

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
            
        elif plotType == "Obj":
            g = self.mplMesh
            t = self.ntbMesh
            g.fig.delaxes(g.axes)
            t.update()
            g.axes = g.fig.add_subplot(111, projection='3d')
            for iO in range(len(self.meshObj)):
                ob = self.meshObj[iO]
                triangul = tri.Triangulation(ob.X,ob.Y,triangles=ob.trii)
                g.axes.plot_trisurf(triangul,ob.Z,color = '#468499',edgecolors='None')
            g.axes._axis3don = False
            g.draw()
            
        else:
            t.update()
            g.fig.delaxes(g.axes)
            g.axes = g.fig.add_axes([0.20, 0.17, 0.75, 0.75])
            g.axes.plot(x,y,color = '#468499')
            g.axes.hold(True)
            g.axes.plot(x2,y2,color = '#FF6666')
            g.axes.set_xlabel(xlab)
            g.axes.set_ylabel(ylab)
            g.draw()
            g.axes.hold(False)

    def displayMessage(self):
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

    def meshTypeFig(self):
        if self.comboBox.currentIndex()==0:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/box.png")))
            self.prop1Label.setText(_translate("openWEC", "Length", None))
            self.prop2Label.setText(_translate("openWEC", "Width", None))
            self.prop3Label.setText(_translate("openWEC", "Height", None))
        if self.comboBox.currentIndex()==1:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/cylinder.png")))
            self.prop1Label.setText(_translate("openWEC", "Diameter", None))
            self.prop2Label.setText(_translate("openWEC", "Height", None))
            self.prop3Label.setText(_translate("openWEC", "None", None))
        if self.comboBox.currentIndex()==2:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/cone.png")))
            self.prop1Label.setText(_translate("openWEC", "Diameter", None))
            self.prop2Label.setText(_translate("openWEC", "Height", None))
            self.prop3Label.setText(_translate("openWEC", "None", None))            
        if self.comboBox.currentIndex()==3:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/sphere.png")))
            self.prop1Label.setText(_translate("openWEC", "Diameter", None))
            self.prop2Label.setText(_translate("openWEC", "None", None))
            self.prop3Label.setText(_translate("openWEC", "None", None))            
        if self.comboBox.currentIndex()==4:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/pyramid.png")))
            self.prop1Label.setText(_translate("openWEC", "Length", None))
            self.prop2Label.setText(_translate("openWEC", "Width", None))
            self.prop3Label.setText(_translate("openWEC", "Height", None))            
        if self.comboBox.currentIndex()==5:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/wedge.png")))
            self.prop1Label.setText(_translate("openWEC", "Length", None))
            self.prop2Label.setText(_translate("openWEC", "Width", None))
            self.prop3Label.setText(_translate("openWEC", "Height", None))                        
        if self.comboBox.currentIndex()==6:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/hemisphere.png")))
            self.prop1Label.setText(_translate("openWEC", "Diameter", None))
            self.prop2Label.setText(_translate("openWEC", "None", None))
            self.prop3Label.setText(_translate("openWEC", "None", None))                        
        if self.comboBox.currentIndex()==7:
            self.sketchShape.setPixmap(QtGui.QPixmap(_fromUtf8("src/hemicylinder.png")))
            self.prop1Label.setText(_translate("openWEC", "Diameter", None))
            self.prop2Label.setText(_translate("openWEC", "Length", None))
            self.prop3Label.setText(_translate("openWEC", "None", None))            

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

    def drawObj(self,MainWindow):
        
        sys.path.insert(0, './Run')
        import meshTypes as mt
        
        if self.comboBox.currentIndex()==0:
            # Box
            length = float(self.prop1.text())
            width = float(self.prop2.text())
            height = float(self.prop3.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())
            ob = mt.box(length,width,height,[xC,yC,zC])
        elif self.comboBox.currentIndex()==1:
            # Cylinder
            diameter = float(self.prop1.text())
            height = float(self.prop2.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())
            ob = mt.cylinder(diameter,height,[xC,yC,zC])
        elif self.comboBox.currentIndex()==2:
            # Cone
            diameter = float(self.prop1.text())
            height = float(self.prop2.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())            
            ob = mt.cone(diameter,height,[xC,yC,zC])
        elif self.comboBox.currentIndex()==3:
            # Sphere
            diameter = float(self.prop1.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())            
            ob = mt.sphere(diameter,[xC,yC,zC])
        elif self.comboBox.currentIndex()==4:
            # Pyramid
            length = float(self.prop1.text())
            width = float(self.prop2.text())
            height = float(self.prop3.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())
            ob = mt.pyramid(length,width,height,[xC,yC,zC])
        elif self.comboBox.currentIndex()==5:
            # Wedge
            length = float(self.prop1.text())
            width = float(self.prop2.text())
            height = float(self.prop3.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())        
            ob = mt.wedge(length,width,height,[xC,yC,zC])
        elif self.comboBox.currentIndex()==6:
            # Hemisphere
            diameter = float(self.prop1.text())  
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())        
            ob = mt.hemisphere(diameter,[xC,yC,zC])
        elif self.comboBox.currentIndex()==7:
            # Hemicylinder
            diameter = float(self.prop1.text())  
            height = float(self.prop2.text())
            xC = float(self.Xins.text())
            yC = float(self.Yins.text())
            zC = float(self.Zins.text())        
            ob = mt.hemicylinder(diameter,height,[xC,yC,zC])
        
        # Add object to list        
        self.meshObj.append(ob)
        self.nrObj += 1
        item = QtGui.QListWidgetItem(ob.name + "-mesh-" + str(self.nrObj))        
        self.listWidget.addItem(item)      
        
        # Update graph
        self.updateGraph(plotType="Obj")

    def delObj(self):
        if len(self.meshObj) > 0:
            iDel = self.listWidget.currentRow()
            self.meshObj.remove(self.meshObj[iDel])
            self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem()))
            self.updateGraph(plotType="Obj")
        else:
            None
            
    def transObj(self):
        xT = float(self.lineEdit.text())
        yT = float(self.lineEdit_2.text())
        zT = float(self.lineEdit_3.text())
        self.meshObj[self.listWidget.currentRow()].translate(xT,yT,zT)
        self.updateGraph(plotType="Obj")
    def rotObj(self):
        theta = float(self.lineEdit_4.text())*np.pi/180.0
        U1 = [float(x) for x in self.lineEdit_5.text().split(',')]
        U2 = [float(x) for x in self.lineEdit_6.text().split(',')]
        self.meshObj[self.listWidget.currentRow()].rotate(U1,U2,theta)
        self.updateGraph(plotType="Obj")

    def makeMesh(self,MainWindow):
        
        sys.path.insert(0, './Run')
        import meshTypes as mt
        
        if self.meshMethod.currentIndex()==0:
            zG = float(self.zGBox.text())
            nPanels = int(self.nPanelBox.text())
            if(len(self.meshObj)>1):
                startMesh = self.meshObj[0]
                for iM in range(len(self.meshObj)-1):
                    comMesh = mt.Mesh()
                    comMesh.combineMesh(startMesh,self.meshObj[iM+1])
                    startMesh = comMesh
                mt.writeMesh(comMesh,'./Calculation/mesh/axisym')
                ne.createMeshOpt(zG,nPanels,int(0),rho=float(self.rhoBox.text()))
            elif(len(self.meshObj)==1):
                mt.writeMesh(self.meshObj[0],'./Calculation/mesh/axisym')
                ne.createMeshOpt(zG,nPanels,int(0),rho=float(self.rhoBox.text()))
            else:
                print('WARNING: Cannot create mesh when no mesh parts are created!')
            print('Mesh succesfully created!')

        elif self.meshMethod.currentIndex()==2:
            zG = float(self.zGBox.text())
            nPanels = self.convertMesh()
            ne.createMeshOpt(zG,nPanels,int(0),rho=float(self.rhoBox.text()))
            print('Mesh succesfully created!')

        elif self.meshMethod.currentIndex()==1:
            zG = float(self.zGBox.text())
            nPanels = self.convertMesh()
            ne.createMeshOpt(zG,nPanels,int(0),rho=float(self.rhoBox.text()))
            print('Mesh succesfully created!')
        
        # Mesh visualisation
        
        sys.path.insert(0, './Run')
        import processNemoh as pn
        
        (X,Y,Z,trian) = pn.getMesh()
        self.updateGraph(x=X,y=Y,x2=trian,y2=Z,plotType="Mesh")

    def runNemohCode(self):
        # Delete previous results
        folder = './Calculation/results'
        for fil in os.listdir(folder):
            filPath = os.path.join(folder,fil)
            if os.path.isfile(filPath):
                os.unlink(filPath)

        # Basic Options
        waterDepth = float(self.waterDepthBox.text())
        o2 = float(self.omegaStart.text())
        o3 = float(self.omegaStop.text())
        o1 = int(float(self.omegaStep.text()))
        omega = [o1,o2,o3]
        rhoW = 1025.0
        zG = float(self.zGBox.text())
        
        # DOF        
        self.dof = [1,1,1,1,1,1]
        self.dof[0] = int(self.checkSurge.isChecked())        
        self.dof[1] = int(self.checkSway.isChecked())        
        self.dof[2] = int(self.checkHeave.isChecked())        
        self.dof[3] = int(self.checkRoll.isChecked())        
        self.dof[4] = int(self.checkPitch.isChecked())        
        self.dof[5] = int(self.checkYaw.isChecked())        
        
        # Advanced Options
        advOps = {}
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
        ne.writeCalFile(rhoW,waterDepth,omega,zG,self.dof,aO=advOps)
        ne.runNemoh()

        # Delete content of destination folder
        folder = './Run/Nemoh'
        for fil in os.listdir(folder):
            filPath = os.path.join(folder,fil)
            if os.path.isfile(filPath):
                os.unlink(filPath)
        
        # Copy Result files to Simulation directory
        pathName = './Calculation/results'
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,"./Run/Nemoh")
        pathName = './Calculation/mesh'
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,"./Run/Nemoh")

        # Display results on matplotlib widgets
        sys.path.insert(0, './Run')
        import processNemoh as pn
        
        xlabel = 'Frequency [Hz]'
        ylabel = '$M_a$ and $B_{hyd}$'
        
        (self.Ma,self.Bhyd,omeg) = pn.getAB(self.dof,sel=self.dof.index(1))
        self.freq = omeg/(2*np.pi)
        (self.Fe,self.Fpha) = pn.getFe(self.dof,sel=self.dof.index(1))
        self.updateGraph(x=self.freq,y=self.Ma,x2=self.freq,y2=self.Bhyd,g=self.mplNem,
        t=self.ntbNem,xlab=xlabel,ylab=ylabel)
        
        # Change DOF labels in postprocessing window
        self.changeDofLabels()
            
        print ('Program Finished!')

    def openDialog(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
        "Open Nemoh File","./Calculation","Nemoh File (*.cal)")
        fileName = str(fileName)
        # Copy result files
        pathName = os.path.dirname(fileName)
        pathName = os.path.join(pathName,'results')
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,"./Run/Nemoh")
        # Copy mesh files
        pathName = os.path.dirname(fileName)
        pathName = os.path.join(pathName,'mesh')
        srcFiles = os.listdir(pathName)
        for iFile in srcFiles:
            fullFile = os.path.join(pathName,iFile)
            if(os.path.isfile(fullFile)):
                sh.copy(fullFile,"./Run/Nemoh")

    def convertMesh(self):
        if self.meshMethod.currentIndex()==2:
            fileName = QtGui.QFileDialog.getOpenFileName(self,
            "Open STL Mesh","./","Nemoh File (*.stl)")
            fileName = str(fileName)
            print(fileName)
            
            # convert to Nemoh format
            V,F = self.load_STL(fileName)
            nrNodes = len(V)
            nrPanels = len(F)
            self.write_MAR(V, F, nrNodes, nrPanels)
        elif self.meshMethod.currentIndex()==1:
            nrPanels = int(self.nPanelBox.text())
            fileName = QtGui.QFileDialog.getOpenFileName(self,
            "Open Nemoh Mesh","./","Nemoh Mesh File (*)")
            fileName = str(fileName)
            print(fileName)
            # copy to mesh directory
            sh.copyfile(fileName,"./Calculation/mesh/axisym")
        return nrPanels

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
        rho = 1025.0

        # DOF        
        self.dof = [1,1,1,1,1,1]
        self.dof[0] = int(self.checkSurge.isChecked())        
        self.dof[1] = int(self.checkSway.isChecked())        
        self.dof[2] = int(self.checkHeave.isChecked())        
        self.dof[3] = int(self.checkRoll.isChecked())        
        self.dof[4] = int(self.checkPitch.isChecked())        
        self.dof[5] = int(self.checkYaw.isChecked())        
        dof = self.dof
        
        # Get degrees of freedom
        indList = []
        dof2 = [a for a in dof]
        for iD in range(sum(dof)):
            indList.append(dof2.index(1))
            dof2[dof2.index(1)] = 0

        
        # Get Damping force
        dampType = self.dampSelect.currentIndex()
        Fdamp = float(self.fdampBox.text())

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
        
        # Calculate Exciting wave and wave force
        
        time,self.wave,Fex,specSS = wav.makeWaveFex(Hs,Tm,time,dof,wavName,Sout=True)

        # Preprocessing: calculate body parameters
        
        M,c = pn.calcM(rho=rho,dof=dof)
        if (wavType==0):
            Ma,Bhyd,omega = pn.getAB(dof)
            if sum(dof)<2:
                Ma = np.interp(2*np.pi/Tm,omega,Ma)
                Bhyd = np.interp(2*np.pi/Tm,omega,Bhyd)
            else:
                oI = np.interp(2*np.pi/Tm,omega,omega)
                mask = [a > 0 for a in omega - oI]
                iS,iE = (mask.index(True)-1,mask.index(True))
                Ma = Ma[:,:,iS] + (Ma[:,:,iE]-Ma[:,:,iS])*(oI-omega[iS])/(omega[iE]-omega[iS])
                Bhyd = Bhyd[:,:,iS] + (Bhyd[:,:,iE]-Bhyd[:,:,iS])*(oI-omega[iS])/(omega[iE]-omega[iS])
        else:
            alpha,beta,errorE,Mainf = pn.calcAlphaBeta(10,rho,dof)
            if sum(dof)>2:
                Ma,Bhyd,omega = pn.getAB(dof)
                MaS,BhydS = pn.irregAB(Ma,Bhyd,omega,M,c,dof,specSS)
                MaS[2,2] = Mainf
                np.savetxt('./Output/M.dat',M)
                np.savetxt('./Output/c.dat',c)
                np.savetxt('./Output/MaS.dat',MaS)
                np.savetxt('./Output/BhydS.dat',BhydS)
                np.savetxt('./Output/Fex.dat',Fex)

        #---------------------------------------------------------------------------
        # MODEL SIMULATION
        #---------------------------------------------------------------------------

        # First Run

        print('Wave height: ' + str(Hs) + ' m')
        print('Wave period: ' + str(Tm) + ' s')
        print('Simulation Start!')
        
        
        if (wavType==0):
            if sum(dof)<2:
                self.time,self.posZ,self.velZ,self.Fpto = wc.simBodyReg1DOF(time,Fex,Fdamp,dampType,M,c,Ma,Bhyd,moor=self.moorCheck.isChecked(),dof=dof)
            else:
                self.time,self.posZ,self.velZ = wc.simBodyReg(time,Fex,Fdamp,dampType,M,c,Ma,Bhyd,moor=self.moorCheck.isChecked(),dof=dof)
                self.Fpto = self.velZ*0.0
        else:
            if sum(dof)<2:
                self.time,self.posZ,self.velZ,self.Fpto = wc.simBody1DOF(time,Fex,Fdamp,dampType,M,Mainf,c,alpha,beta,moor=self.moorCheck.isChecked(),dof=dof)
            else:
                self.Fpto = self.velZ*0.0
        
        print('Simulation Finished!')

        # Output to matplotlib widgets

        xlabel = 'Time [s]'
        ylabel = '$z$ and $v$'

        if sum(dof)<2:        
            diff = len(self.time)-len(self.posZ)
            if diff>0.5:
                self.time = np.delete(self.time,0)
            elif diff <-0.5:
                self.posZ = np.delete(self.posZ,-1)
                self.velZ = np.delete(self.velZ,-1)
                self.Fpto = np.delete(self.Fpto,-1)
                
            self.updateGraph(x=self.time,y=self.posZ,x2=self.time,y2=self.velZ,g=self.mplSim,
            t=self.ntbSim,xlab=xlabel,ylab=ylabel)
            
        else:
            
            self.updateGraph(x=self.time,y=self.posZ[indList[0],:],x2=self.time,y2=self.velZ[indList[0],:],g=self.mplSim,
            t=self.ntbSim,xlab=xlabel,ylab=ylabel)

        # Change DOF labels in postprocessing window
        self.changeDofLabels()
        
        # Save Results
        saveName = QtGui.QFileDialog.getSaveFileName(self,
        "Save Simulation Results","./Output","Text File (*.txt)")
        wc.saveResults(saveName,self.time,self.posZ,self.velZ,self.Fpto,li=indList)        
        
        # Calculate Produced Power

        Pabs = self.Fpto*self.velZ
        Pabs_mean = np.mean(Pabs)
        print('Mean Absorbed Power: ' + str(Pabs_mean) + ' Watt')

    def merge_duplicates(self,V,F,verbose=True, tol=1e-8):

        nv, nbdim = V.shape

        levels = [0, nv]
        Vtmp = []
        iperm = np.array([i for i in xrange(nv)])

        for dim in range(nbdim):
            # Sorting the first dimension
            values = V[:, dim].copy()
            if dim > 0:
                values = values[iperm]
            levels_tmp = []
            for (ilevel, istart) in enumerate(levels[:-1]):
                istop = levels[ilevel+1]

                if istop-istart > 1:
                    level_values = values[istart:istop]
                    iperm_view = iperm[istart:istop]

                    iperm_tmp = level_values.argsort()

                    level_values[:] = level_values[iperm_tmp]
                    iperm_view[:] = iperm_view[iperm_tmp]

                    levels_tmp.append(istart)
                    vref = values[istart]

                    for idx in xrange(istart, istop):
                        cur_val = values[idx]
                        if np.abs(cur_val - vref) > tol:
                            levels_tmp.append(idx)
                            vref = cur_val

                else:
                    levels_tmp.append(levels[ilevel])
            if len(levels_tmp) == nv:
                # No duplicate vertices
                if verbose:  
                    print "The mesh has no duplicate vertices"
                break

            levels_tmp.append(nv)
            levels = levels_tmp

        else:
            # Building the new merged node list
            Vtmp = []
            newID = np.array([i for i in xrange(nv)])
            for (ilevel, istart) in enumerate(levels[:-1]):
                istop = levels[ilevel+1]

                Vtmp.append(V[iperm[istart]])
                newID[iperm[range(istart, istop)]] = ilevel
            V = np.array(Vtmp, dtype=float, order='F')
            # Applying renumbering to cells
            for cell in F:
                cell[:] = newID[cell-1]+1

            if verbose:
                nv_new = V.shape[0]
                print "Initial number of nodes : {:d}".format(nv)
                print "New number of nodes     : {:d}".format(nv_new)
                print "{:d} nodes have been merged".format(nv-nv_new)

        return V, F

    def load_STL(self,fileName):
        
        from vtk import vtkSTLReader        
        
        reader = vtkSTLReader()
        reader.SetFileName(fileName)
        reader.Update()

        data = reader.GetOutputDataObject(0)

        nv = data.GetNumberOfPoints()
        V = np.zeros((nv, 3), dtype=float, order='F')
        for k in range(nv):
            V[k] = np.array(data.GetPoint(k))
        nf = data.GetNumberOfCells()
        F = np.zeros((nf, 4), dtype=np.int32, order='F')
        for k in range(nf):
            cell = data.GetCell(k)
            if cell is not None:
                for l in range(3):
                    F[k][l] = cell.GetPointId(l)
                    F[k][3] = F[k][0]  # always repeating the first node as stl is triangle only
        F += 1

        V,F = self.merge_duplicates(V, F)

        return V,F

    def write_MAR(self,V, F, nv, nf):
        ofile = open('./Calculation/mesh/axisym', 'w')

        ofile.write('{0:d}\n{1:d}\n'.format(nv, nf))

        for (idx, vertex) in enumerate(V):
            ofile.write('{0:f}\t{1:f}\t{2:f}\n'.format(vertex[0], vertex[1], vertex[2]))

        cell_block = '\n'.join(
            ''.join(u'{0:d}\t'.format(elt) for elt in cell)
            for cell in F
        ) + '\n'
        ofile.write(cell_block)

        ofile.close()
        print 'File %s written' % 'axisym'
        
    def changeDofLabels(self):
        
        nameDof = ['Surge','Sway','Heave','Roll','Pitch','Yaw']        
        if self.dofPlotU.count() < sum(self.dof):
            for iC in range(sum(self.dof)-self.dofPlotU.count()):
                self.dofPlotU.addItem(_fromUtf8(""))
                self.dofPlotL.addItem(_fromUtf8(""))
        elif self.dofPlotU.count() > sum(self.dof):
            for iC in range(self.dofPlotU.count()-sum(self.dof)):
                self.dofPlotU.removeItem(0)
                self.dofPlotL.removeItem(0)
                
        count = 0
        for iD in range(sum(self.dof)):
            indDof = self.dof.index(1,count)
            count = indDof+1
            self.dofPlotU.setItemText(iD,nameDof[indDof])
            self.dofPlotL.setItemText(iD,nameDof[indDof])


    def openFile(self):
        
        sys.path.insert(0, './Run')
        import meshTypes as mt        
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                        './','*.cu')
                
        with open(fname,'r') as f:
            inData = f.readlines()
        
        # Set Mesh properties
        self.meshMethod.setCurrentIndex(int(inData[1].split('\t')[0]))
        self.comboBox.setCurrentIndex(int(inData[2].split('\t')[0]))
        self.prop1.setText(inData[3].split('\t')[0])
        self.prop2.setText(inData[4].split('\t')[0])
        self.prop3.setText(inData[5].split('\t')[0])
        self.Xins.setText(inData[6].split('\t')[0])
        self.Yins.setText(inData[7].split('\t')[0])
        self.Zins.setText(inData[8].split('\t')[0])
        self.lineEdit.setText(inData[9].split('\t')[0])
        self.lineEdit_2.setText(inData[10].split('\t')[0])
        self.lineEdit_3.setText(inData[11].split('\t')[0])
        self.lineEdit_4.setText(inData[12].split('\t')[0])
        self.lineEdit_5.setText(inData[13].split('\t')[0])
        self.lineEdit_6.setText(inData[14].split('\t')[0])
        self.waterDepthBox.setText(inData[15].split('\t')[0])
        self.zGBox.setText(inData[16].split('\t')[0])
        self.rhoBox.setText(inData[17].split('\t')[0])        
        self.nPanelBox.setText(inData[18].split('\t')[0])
        # Set Nemoh Properties
        self.omegaStart.setText(inData[20].split('\t')[0])        
        self.omegaStop.setText(inData[21].split('\t')[0])        
        self.omegaStep.setText(inData[22].split('\t')[0])
        self.checkSurge.setChecked(inData[23].split('\t')[0]=='True')
        self.checkSway.setChecked(inData[24].split('\t')[0]=='True')
        self.checkHeave.setChecked(inData[25].split('\t')[0]=='True')
        self.checkRoll.setChecked(inData[26].split('\t')[0]=='True')
        self.checkPitch.setChecked(inData[27].split('\t')[0]=='True')
        self.checkYaw.setChecked(inData[28].split('\t')[0]=='True')
        self.wavDirCheck.setChecked(inData[29].split('\t')[0]=='True')
        self.wavDirStart.setText(inData[30].split('\t')[0])        
        self.wavDirStop.setText(inData[31].split('\t')[0])        
        self.wavDirStep.setText(inData[32].split('\t')[0])
        self.irfCheck.setChecked(inData[33].split('\t')[0]=='True')
        self.irfDur.setText(inData[34].split('\t')[0])        
        self.irfStep.setText(inData[35].split('\t')[0])
        self.kochinCheck.setChecked(inData[36].split('\t')[0]=='True')
        self.kochinStart.setText(inData[37].split('\t')[0])        
        self.kochinStop.setText(inData[38].split('\t')[0])        
        self.kochinStep.setText(inData[39].split('\t')[0])
        self.fsCheck.setChecked(inData[40].split('\t')[0]=='True')
        self.fsDeltaX.setText(inData[41].split('\t')[0])        
        self.fsDeltaY.setText(inData[42].split('\t')[0])        
        self.fsLengthX.setText(inData[43].split('\t')[0])        
        self.fsLengthY.setText(inData[44].split('\t')[0])
        # Time Domain Properties
        self.wavType.setCurrentIndex(int(inData[46].split('\t')[0]))
        self.wavHBox.setText(inData[47].split('\t')[0])
        self.wavTBox.setText(inData[48].split('\t')[0])
        self.dampSelect.setCurrentIndex(int(inData[49].split('\t')[0]))
        self.fdampBox.setText(inData[50].split('\t')[0])
        self.simTimeBox.setText(inData[51].split('\t')[0])
        self.dtBox.setText(inData[52].split('\t')[0])
        # Mesh Objects
        self.meshObj = []
        self.nrObj = 0
        self.listWidget.clear()
        iL = 55
        for iO in range(int(inData[54].split('\t')[0])):
            meshType = inData[iL].split('\t')[0]
            if any(meshType in s for s in ['box','wedge','pyramid']):
                length = float(inData[iL+1].split('\t')[0])
                width = float(inData[iL+2].split('\t')[0])
                height = float(inData[iL+3].split('\t')[0])
                cCor = [float(a) for a in inData[iL+4].split('\t')[0].split(',')]
                ob = eval('mt.' + meshType + '(length,width,height,cCor)')
                self.meshObj.append(ob)
                self.nrObj += 1
                item = QtGui.QListWidgetItem(ob.name + "-mesh-" + str(self.nrObj))        
                self.listWidget.addItem(item)
                self.updateGraph(plotType="Obj")
                iL += 5
            elif any(meshType in s for s in ['cone','cylinder','hemicylinder']):
                diameter = float(inData[iL+1].split('\t')[0])
                height = float(inData[iL+2].split('\t')[0])
                cCor = [float(a) for a in inData[iL+3].split('\t')[0].split(',')]
                ob = eval('mt.' + meshType + '(diameter,height,cCor)')
                self.meshObj.append(ob)
                self.nrObj += 1
                item = QtGui.QListWidgetItem(ob.name + "-mesh-" + str(self.nrObj))        
                self.listWidget.addItem(item)
                self.updateGraph(plotType="Obj")
                iL += 4
            elif any(meshType in s for s in ['sphere','hemisphere']):
                diameter = float(inData[iL+1].split('\t')[0])
                cCor = [float(a) for a in inData[iL+2].split('\t')[0].split(',')]
                ob = eval('mt.' + meshType + '(diameter,cCor)')
                self.meshObj.append(ob)
                self.nrObj += 1
                item = QtGui.QListWidgetItem(ob.name + "-mesh-" + str(self.nrObj))        
                self.listWidget.addItem(item)
                self.updateGraph(plotType="Obj")
                iL += 3
                
        print(fname + " successfully opened!")
        
    def saveFile(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', 
                        './','*.cu')
                
        with open(fname,'w') as f:
            # Write Mesh Tab properties
            f.write('------------------------------------- Mesh Properties -------------------------------------\n')            
            f.write(str(self.meshMethod.currentIndex()) + "\t Mesh Method\n")
            f.write(str(self.comboBox.currentIndex()) + "\t Mesh Item\n")
            f.write(self.prop1.text() + "\t 1st Property\n")
            f.write(self.prop2.text() + "\t 2nd Property\n")
            f.write(self.prop3.text() + "\t 3rd Property\n")
            f.write(self.Xins.text() + "\t X insertion\n")
            f.write(self.Yins.text() + "\t Y insertion\n")
            f.write(self.Zins.text() + "\t Z insertion\n")
            f.write(self.lineEdit.text() + "\t X translation\n")
            f.write(self.lineEdit_2.text() + "\t Y translation\n")
            f.write(self.lineEdit_3.text() + "\t Z translation\n")
            f.write(self.lineEdit_4.text() + "\t Angle of Rotation\n")
            f.write(self.lineEdit_5.text() + "\t Rotation axis 1\n")
            f.write(self.lineEdit_6.text() + "\t Rotation axis 2\n")
            f.write(self.waterDepthBox.text() + "\t Water Depth\n")
            f.write(self.zGBox.text() + "\t Centre of Gravity Location\n")
            f.write(self.rhoBox.text() + "\t Density\n")
            f.write(self.nPanelBox.text() + "\t Number of Mesh Panels\n")
            # Write Nemoh Tab properties
            f.write('------------------------------------- Nemoh Properties -------------------------------------\n')
            f.write(self.omegaStart.text() + "\t Starting Frequency\n")
            f.write(self.omegaStop.text() + "\t Ending Frequency\n")
            f.write(self.omegaStep.text() + "\t Number of Frequency Steps\n")
            f.write(str(self.checkSurge.isChecked()) + "\t Surge\n")
            f.write(str(self.checkSway.isChecked()) + "\t Surge\n")
            f.write(str(self.checkHeave.isChecked()) + "\t Surge\n")
            f.write(str(self.checkRoll.isChecked()) + "\t Surge\n")
            f.write(str(self.checkPitch.isChecked()) + "\t Surge\n")
            f.write(str(self.checkYaw.isChecked()) + "\t Surge\n")
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
            f.write('------------------------------------- Time Domain Properties -------------------------------------\n')
            f.write(str(self.wavType.currentIndex()) + "\t Wave Type\n")
            f.write(self.wavHBox.text() + "\t Wave Height\n")
            f.write(self.wavTBox.text() + "\t Wave Period\n")
            f.write(str(self.dampSelect.currentIndex()) + "\t Damping Type\n")
            f.write(self.fdampBox.text() + "\t Damping Value\n")
            f.write(self.simTimeBox.text() + "\t Simulation Time\n")
            f.write(self.dtBox.text() + "\t Simulation Time Step\n")
            # Save Mesh Parts
            f.write('------------------------------------- Mesh Objects -------------------------------------\n')
            f.write(str(len(self.meshObj)) + "\t Number of mesh objects\n")
            for iO in range(len(self.meshObj)):
                f.write(self.meshObj[iO].name + "\t Mesh type\n")
                if any(self.meshObj[iO].name in s for s in ['box','wedge','pyramid']):
                    f.write("{:.2f} \t Length\n".format(self.meshObj[iO].length))
                    f.write("{:.2f} \t Width\n".format(self.meshObj[iO].width))
                    f.write("{:.2f} \t Height\n".format(self.meshObj[iO].height))
                    f.write("{0:.2f},{1:.2f},{2:.2f} \t Length\n".format(self.meshObj[iO].xC,self.meshObj[iO].yC,self.meshObj[iO].zC))
                elif any(self.meshObj[iO].name in s for s in ['cone','cylinder','hemicylinder']):
                    f.write("{:.2f} \t Diameter\n".format(self.meshObj[iO].diameter))
                    f.write("{:.2f} \t Height\n".format(self.meshObj[iO].height))
                    f.write("{0:.2f},{1:.2f},{2:.2f} \t Length\n".format(self.meshObj[iO].xC,self.meshObj[iO].yC,self.meshObj[iO].zC))
                elif any(self.meshObj[iO].name in s for s in ['sphere','hemisphere']):
                    f.write("{:.2f} \t Diameter\n".format(self.meshObj[iO].diameter))
                    f.write("{0:.2f},{1:.2f},{2:.2f} \t Length\n".format(self.meshObj[iO].xC,self.meshObj[iO].yC,self.meshObj[iO].zC))
        
        
        
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

    def runMoorDynConfig(self):
        print "Opening MoorDyn Configuration Tool..."
        self.w = MoorDynPopup()
        self.w.show()
        
    def changeMoorDyn(self):
        if self.moorCheck.isChecked():
            self.moorConfig.setEnabled(True)
        else:
            self.moorConfig.setEnabled(False)

def openCustom():
    ex2 = Ui_MainWindow()
    return ex2    

