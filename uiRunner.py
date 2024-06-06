import time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import pyqtSignal
import irTempSensor.irRunner as ir
import pyqtgraph as pg
from pandas import DataFrame

class Ui_MainWindow(object):
    checker = False

    def setupUi(self, MainWindow):
                
        # Made by Qt designer
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 658)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 28))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.groupBox)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(200, 28))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(438, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.checkBox.setGeometry(QtCore.QRect(50, 50, 151, 17))
        self.checkBox.setObjectName("checkBox")
        self.textBrowser.setGeometry(QtCore.QRect(40, 80, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(MainWindow)

        # setting up the plot
        self.plot_graph = pg.PlotWidget()
        self.plot_graph
        self.gridLayout_4.addWidget(self.plot_graph,1,0,1,1) #replaces widget with plotgraph 

        self.time = []
        self.temperature = []

        self.obj = self.plot_graph.plot(       #plotting obj temp
            self.time,
            self.temperature,
            name = "Object Temprature",
            pen = pg.mkPen(color=(255, 0, 0))
        )
        font1 = {'family':'serif','color':'blue','size':2000}
        
        self.amb = self.plot_graph.plot(        #plotting amb temp 
            self.time,
            self.temperature,
            name = "Amb Temp",
            pen = pg.mkPen(color=(0, 255, 0))
        )
        
        self.checkBox.stateChanged.connect(lambda:self.startWorker()) #connecting to thread

        # Saving at end of program. to use comment out call in plotter and uncomment statement below
        # MainWindow.destroyed.connect(lambda : self.saveData()) 
    
    def saveData(self):
        self.obj_Temp = Ui_MainWindow.y_vals_obj 
        self.amb_Temp = Ui_MainWindow.y_vals_amb
        self.time = Ui_MainWindow.x_vals

        df = DataFrame({"Time (s)" : self.time, "Obj Temp (c)" : self.obj_Temp, "Amb Temp (c)" : self.amb_Temp}) #Adds data to dataframe

        df.to_excel('test.xlsx') #converts to excel file

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.checkBox.setText(_translate("MainWindow", "Off / On"))
        
        self.label_2.setText(_translate("MainWindow", "Object Temperature:"))
        self.label_3.setText(_translate("MainWindow", "Ambient Temperature:"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Object and ambient Temprature Graph</span></p></body></html>"))
    
    def startWorker(self): #Worker thread 
        Ui_MainWindow.checker = self.checkBox.isChecked()
        self.thread = ThreadClass(parent = None)    
        self.thread.start() 
        self.thread.dataSignal.connect(self.myfunction) 


    def myfunction(self, objTemp, ambTemp):
        self.textBrowser.setText(objTemp)
        self.textBrowser_2.setText(ambTemp)
        self.plotter(objTemp,ambTemp)
        
    x_vals = []
    y_vals_obj = []
    y_vals_amb = []
    count = 0

    def plotter(self,objTemp,ambTemp):
        objTemp = float(objTemp)
        ambTemp = float(ambTemp)

        # removing glitches 

        # if objTemp >= 300:
        #     objTemp = Ui_MainWindow.y_vals_obj[len(Ui_MainWindow.y_vals_obj)-1]
        # if ambTemp >= 300:
        #     ambTemp = Ui_MainWindow.y_vals_amb[len(Ui_MainWindow.y_vals_amb)-1]

        Ui_MainWindow.count+=1
        Ui_MainWindow.x_vals.append(Ui_MainWindow.count)
        Ui_MainWindow.y_vals_obj.append(objTemp)
        Ui_MainWindow.y_vals_amb.append(ambTemp)

        # scrolling graph

        # if len(Ui_MainWindow.y_vals_amb) > 30:
        #     Ui_MainWindow.y_vals_obj.pop(0)   
        #     Ui_MainWindow.y_vals_amb.pop(0)
        #     Ui_MainWindow.x_vals.pop(0)

        self.obj.setData(Ui_MainWindow.x_vals, Ui_MainWindow.y_vals_obj)
        self.amb.setData(Ui_MainWindow.x_vals, Ui_MainWindow.y_vals_amb)

        self.saveData()


       
class ThreadClass(QtCore.QThread):

    dataSignal = pyqtSignal(str,str)

    def __init__(self,parent = None):
        super(ThreadClass, self).__init__(parent)
        self.isRunning=True

    def run(self):
        while(Ui_MainWindow.checker == True):
            tup = ir.printer()
            self.dataSignal.emit(tup[0],tup[1])
            time.sleep(0.5)
