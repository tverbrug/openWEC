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

def overwriteGraph(self,plotWindow=1):
    # Set the correct variables
    if plotWindow == 1:
        test = self.chooseX1.currentIndex() + 2*self.chooseY1.currentIndex()
        mpl = self.mpl1
        ntb = self.ntb1
    else:
        test = self.chooseX2.currentIndex() + 2*self.chooseY2.currentIndex()
        mpl = self.mpl2
        ntb = self.ntb2
    if test==0:
        xVar = self.freq
        yVar = self.Ma
        xlabel = 'Frequency [Hz]'
        ylabel = '$M_a$ [kg]'
    elif test==1:
        xVar = self.time
        yVar = self.wave
        xlabel = 'Time [s]'
        ylabel = '$\eta$ [m]'
    elif test==2:
        xVar = self.freq
        yVar = self.Bhyd
        xlabel = 'Frequency [Hz]'
        ylabel = '$B_{hyd}$ [kg/s]'
    elif test==3:
        xVar = self.time
        yVar = self.posZ
        xlabel = 'Time [s]'
        ylabel = '$z_{WEC}$ [m]'
    elif test==4:
        xVar = self.freq
        yVar = self.Fe
        xlabel = 'Frequency [Hz]'
        ylabel = '$F_{ex}$ [N]'
    elif test==5:
        xVar = self.time
        yVar = self.velZ
        xlabel = 'Time [s]'
        ylabel = '$v_{WEC}$ [m/s]'
    elif test==7:
        xVar = self.time
        yVar = self.Fpto
        xlabel = 'Time [s]'
        ylabel = '$F_{PTO}$ [N]'
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
        g.axes.plot_trisurf(triangul,y2,cmap = plt.get_cmap('Blues'),edgecolors='none')
        g.axes._axis3don = False
        # Create cubic bounding box to simulate equal aspect ratio
        max_range = np.array([x.max()-x.min(), y.max()-y.min(), y2.max()-y2.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x.max()+x.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y.max()+y.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(y2.max()+y2.min())
        # Comment or uncomment following both lines to test the fake bounding box:
        for xb, yb, zb in zip(Xb, Yb, Zb):
           g.axes.plot([xb], [yb], [zb], 'w')
        g.fig.patch.set_facecolor('white')
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
            g.axes.plot_trisurf(triangul,ob.Z,cmap = plt.get_cmap('Blues'),edgecolors='none')
        g.axes._axis3don = False
        g.fig.patch.set_facecolor('white')
        g.draw()
        
    else:
        t.update()
        g.fig.delaxes(g.axes)
        g.axes = g.fig.add_axes([0.20, 0.17, 0.75, 0.75])
        g.axes.plot(x,y)
        g.axes.hold(True)
        g.axes.plot(x2,y2)
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
            self.chooseY1.addItem(_fromUtf8(""))
            self.chooseY1.setItemText(3, _translate("MainWindow", "WEC PTO Force", None))
        if self.chooseX1.currentIndex()==0:
            self.chooseY1.removeItem(3)
            self.chooseY1.setItemText(0, _translate("MainWindow", "Added Mass", None))
            self.chooseY1.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
            self.chooseY1.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))
    else:
        if self.chooseX2.currentIndex()==1:
            self.chooseY2.setItemText(0, _translate("MainWindow", "Wave Signal", None))
            self.chooseY2.setItemText(1, _translate("MainWindow", "WEC Position", None))
            self.chooseY2.setItemText(2, _translate("MainWindow", "WEC Velocity", None))
            self.chooseY2.addItem(_fromUtf8(""))
            self.chooseY2.setItemText(3, _translate("MainWindow", "WEC PTO Force", None))
        if self.chooseX2.currentIndex()==0:
            self.chooseY2.removeItem(3)
            self.chooseY2.setItemText(0, _translate("MainWindow", "Added Mass", None))
            self.chooseY2.setItemText(1, _translate("MainWindow", "Hydrodynamic Damping", None))
            self.chooseY2.setItemText(2, _translate("MainWindow", "Wave Excitation Force", None))

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

