# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pressDataView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 961)
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("#centralwidget{\n"
                                 "    background-color:#c8ddd1;\n"
                                 "}\n"
                                 "\n"
                                 "#query_btn{\n"
                                 "    background-color:#30b89a;\n"
                                 "    border-radius:13px;\n"
                                 "    font:10pt;\n"
                                 "    border:1px solid rgb(179,190,222)\n"
                                 "}\n"
                                 "#query_btn:hover{\n"
                                 "    background-color:#3debc5;\n"
                                 "    border-radius:13px;\n"
                                 "    border:1px solid rgb(179,190,222)\n"
                                 "}\n"
"#query_btn:checked{\n"
"    background-color:#30b89a;\n"
"    border-radius:13px;\n"
"    border:1px solid rgb(179,190,222)\n"
"}\n"
"#query_btn:pressed{\n"
"    background-color:#30b89a;\n"
"    border-radius:12px;\n"
"\n"
"}\n"
"\n"
"#delete_data_btn{\n"
"    background-color:#d0879d;\n"
"    border-radius:13px;\n"
"    font:10pt;\n"
"    border:1px solid rgb(179,190,222)\n"
"}\n"
"#delete_data_btn:hover{\n"
"    background-color:#ffa6c1;\n"
"    border-radius:13px;\n"
"    border:1px solid rgb(179,190,222)\n"
"}\n"
                                 "#delete_data_btn:checked{\n"
                                 "    background-color:#a66c7d;\n"
                                 "    border-radius:13px;\n"
                                 "    border:1px solid rgb(179,190,222)\n"
                                 "}\n"
                                 "#delete_data_btn:pressed{\n"
                                 "    background-color:#d0879d;\n"
                                 "    border-radius:12px;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 2048))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("QListWidget\n"
                                      "{\n"
                                      "    background-color:#c8ddd1;\n"
                                      "    border:1px solid gray;   /*边界线:宽度、颜色*/\n"
                                      "    /*background:gray;*/    /*表格背景色*/\n"
                                      "    color:black;        /*前景色：文字颜色*/\n"
                                      "    margin:10px,10px,0px,20px;   /*上、下、左、右，间距*/\n"
                                      "}\n"
                                      "QListWidget::item{\n"
                                      "    margin-top:20px;\n"
                                      "    padding:20px,20px,10px,10px\n"
                                      "}")
        self.listWidget.setLineWidth(1)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setGridSize(QtCore.QSize(0, 100))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setEnabled(True)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("QPushButton,QLineEdit,QComboBox{\n"
" background-color: azure;\n"
" color:deepskyblue;\n"
"}\n"
"QPushButton:pressed{\n"
" color:red;\n"
"}")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_rbtn = QtWidgets.QRadioButton(self.groupBox_3)
        self.select_rbtn.setCheckable(True)
        self.select_rbtn.setChecked(True)
        self.select_rbtn.setObjectName("select_rbtn")
        self.horizontalLayout_2.addWidget(self.select_rbtn)
        self.select_date = QtWidgets.QComboBox(self.groupBox_3)
        self.select_date.setEnabled(True)
        self.select_date.setObjectName("select_date")
        self.select_date.addItem("")
        self.select_date.addItem("")
        self.select_date.addItem("")
        self.select_date.addItem("")
        self.horizontalLayout_2.addWidget(self.select_date)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.condition_rbtn = QtWidgets.QRadioButton(self.groupBox_3)
        self.condition_rbtn.setObjectName("condition_rbtn")
        self.horizontalLayout_2.addWidget(self.condition_rbtn)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.start_date = QtWidgets.QDateEdit(self.groupBox_3)
        self.start_date.setEnabled(False)
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate(2021, 1, 1))
        self.start_date.setObjectName("start_date")
        self.horizontalLayout_2.addWidget(self.start_date)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.end_date = QtWidgets.QDateEdit(self.groupBox_3)
        self.end_date.setEnabled(False)
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QtCore.QDate(2021, 1, 1))
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_2.addWidget(self.end_date)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.query_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.query_btn.setMinimumSize(QtCore.QSize(80, 26))
        self.query_btn.setAutoFillBackground(False)
        self.query_btn.setStyleSheet("")
        self.query_btn.setObjectName("query_btn")
        self.horizontalLayout_2.addWidget(self.query_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableWidget_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_delete_rbtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.select_delete_rbtn.setChecked(True)
        self.select_delete_rbtn.setObjectName("select_delete_rbtn")
        self.horizontalLayout_4.addWidget(self.select_delete_rbtn)
        self.select_delete_date = QtWidgets.QComboBox(self.groupBox_2)
        self.select_delete_date.setEnabled(True)
        self.select_delete_date.setObjectName("select_delete_date")
        self.select_delete_date.addItem("")
        self.select_delete_date.addItem("")
        self.select_delete_date.addItem("")
        self.select_delete_date.addItem("")
        self.horizontalLayout_4.addWidget(self.select_delete_date)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.condition_delete_rbtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.condition_delete_rbtn.setObjectName("condition_delete_rbtn")
        self.horizontalLayout_4.addWidget(self.condition_delete_rbtn)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.start_delete_date = QtWidgets.QDateEdit(self.groupBox_2)
        self.start_delete_date.setEnabled(False)
        self.start_delete_date.setCalendarPopup(True)
        self.start_delete_date.setDate(QtCore.QDate(2021, 1, 1))
        self.start_delete_date.setObjectName("start_delete_date")
        self.horizontalLayout_4.addWidget(self.start_delete_date)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.end_delete_date = QtWidgets.QDateEdit(self.groupBox_2)
        self.end_delete_date.setEnabled(False)
        self.end_delete_date.setCalendarPopup(True)
        self.end_delete_date.setDate(QtCore.QDate(2021, 1, 1))
        self.end_delete_date.setObjectName("end_delete_date")
        self.horizontalLayout_4.addWidget(self.end_delete_date)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.delete_data_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_data_btn.setMinimumSize(QtCore.QSize(80, 26))
        self.delete_data_btn.setObjectName("delete_data_btn")
        self.horizontalLayout_4.addWidget(self.delete_data_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.groupBox = QtWidgets.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.stop = QtWidgets.QPushButton(self.groupBox)
        self.stop.setGeometry(QtCore.QRect(130, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.start = QtWidgets.QPushButton(self.groupBox)
        self.start.setEnabled(False)
        self.start.setGeometry(QtCore.QRect(10, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.stackedWidget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.admin_pwd = QtWidgets.QAction(MainWindow)
        self.admin_pwd.setObjectName("admin_pwd")
        self.serial_set = QtWidgets.QAction(MainWindow)
        self.serial_set.setObjectName("serial_set")
        self.about_us = QtWidgets.QAction(MainWindow)
        self.about_us.setObjectName("about_us")
        self.menu.addAction(self.admin_pwd)
        self.menu.addSeparator()
        self.menu_2.addAction(self.about_us)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.condition_rbtn.toggled['bool'].connect(self.start_date.setEnabled)
        self.condition_rbtn.toggled['bool'].connect(self.end_date.setEnabled)
        self.condition_rbtn.toggled['bool'].connect(self.select_date.setDisabled)
        self.condition_delete_rbtn.toggled['bool'].connect(self.start_delete_date.setEnabled)
        self.condition_delete_rbtn.toggled['bool'].connect(self.end_delete_date.setEnabled)
        self.condition_delete_rbtn.toggled['bool'].connect(self.select_delete_date.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "压装数据"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "实时数据"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "数据查询"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "系统设置"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "是否合格"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "最大压力(N)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "终止压力(N)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "终止位置(mm)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "压装用时(s)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "压装时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "曲线编号"))
        self.groupBox_3.setTitle(_translate("MainWindow", "查询数据"))
        self.select_rbtn.setText(_translate("MainWindow", "选择查询"))
        self.select_date.setItemText(0, _translate("MainWindow", "本月"))
        self.select_date.setItemText(1, _translate("MainWindow", "上月"))
        self.select_date.setItemText(2, _translate("MainWindow", "近半年"))
        self.select_date.setItemText(3, _translate("MainWindow", "本年"))
        self.condition_rbtn.setText(_translate("MainWindow", "条件查询"))
        self.label_11.setText(_translate("MainWindow", "开始时间:"))
        self.label_12.setText(_translate("MainWindow", "--结束时间:"))
        self.query_btn.setText(_translate("MainWindow", "查询"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "是否合格"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "最大压力(N)"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "终止压力(N)"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "终止位置(mm)"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "压装用时(s)"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "压装时间"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "曲线编号"))
        self.groupBox_2.setTitle(_translate("MainWindow", "删除数据"))
        self.select_delete_rbtn.setText(_translate("MainWindow", "选择删除"))
        self.select_delete_date.setItemText(0, _translate("MainWindow", "全部删除"))
        self.select_delete_date.setItemText(1, _translate("MainWindow", "超过五年"))
        self.select_delete_date.setItemText(2, _translate("MainWindow", "超过三年"))
        self.select_delete_date.setItemText(3, _translate("MainWindow", "超过一年"))
        self.condition_delete_rbtn.setText(_translate("MainWindow", "条件删除"))
        self.label_13.setText(_translate("MainWindow", "开始时间:"))
        self.label_14.setText(_translate("MainWindow", "--结束时间:"))
        self.delete_data_btn.setText(_translate("MainWindow", "删除数据"))
        self.groupBox.setTitle(_translate("MainWindow", "开启/关闭接收数据"))
        self.stop.setText(_translate("MainWindow", "关闭"))
        self.start.setText(_translate("MainWindow", "开启"))
        self.menu.setTitle(_translate("MainWindow", "系统设置"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.admin_pwd.setText(_translate("MainWindow", "管理员密码"))
        self.serial_set.setText(_translate("MainWindow", "串口设置"))
        self.about_us.setText(_translate("MainWindow", "关于我们"))
