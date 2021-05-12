# ************************************
# *编码: utf-8
# *作者: 周俊
# *文件名: Main.py
# *创建时间: 2021-04-28 16:42
# *功能说明: 与PLC通讯 获取数据 并在主界面显示数据和调看曲线
# *版本: V1.0
# *更新时间:
# ************************************
import sys
import time
import PyQt5  # 导入PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QBrush, QFont, QIcon
from PyQt5.QtNetwork import QLocalSocket, QLocalServer
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QInputDialog, QLineEdit, QApplication, \
    QMainWindow
from PyQt5.QtCore import QTimer, QDateTime, QThread, pyqtSignal, Qt, QDate, QBasicTimer, QWaitCondition, QMutex
import pyqtgraph as pg  # 导入曲线库
import serial  # 导入串口
import serial.tools.list_ports
from view.pressDataView import Ui_MainWindow  # 导入程序主界面
from view.changePWD import Ui_Form_PWD  # 导入更改密码界面
from view.about import Ui_Form_About  # 导入关于界面
from view.pressCurve import Ui_Form  # 导入曲线显示界面
from kneed import KneeLocator  # 导入拐点算法
from view.serialPort import Ui_Form_SerialPort  # 导入串口设置界面
from database.mysql import mysql  # 导入数据库操作
from view.ui_Splash import Ui_Form_load  # 导入程序加载界面


# 数据更新到主界面线程
class SerialThread(QThread):
    update_data = pyqtSignal(tuple)
    port_open_status = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(SerialThread, self).__init__(parent)
        self.mysql = mysql()
        self.mysql.open_mysql()
        self.ser = serial.Serial()
        self.port_open()

        self._isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    # 打开串口
    def port_open(self):
        self.ser.port = 'COM3'
        self.ser.baudrate = 115200
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.parity = "O"  # 奇校验
        try:
            self.ser.open()
        except:
            QMessageBox.about(self, "Port Error", "此串口不能被打开！")
            return None

    # 关闭串口
    def port_close(self):
        try:
            self.ser.close()
        except:
            pass

    # DT78写入1 '%01#WDD00078000780100'  DT472写入0 '%01#WDD00472004720000'
    def DT_write(self, command):
        data = self.command_Data(command)
        self.data_send(data)

    # 将松下指令加上BCC校验位，并转成16进制
    def command_Data(self, Command):
        lit = []
        Command_hex = ''
        # 计算BCC校验码
        for i in range(len(Command)):
            PCD_Command_int = ord(Command[i])
            lit.append(PCD_Command_int)
        BCC = None
        for i in range(len(lit)):
            if i:
                BCC ^= lit[i]
            else:
                BCC = lit[i] ^ 0
        Command = Command + hex(BCC)[2:]  # 在指令中加入BCC校验码
        # 将松下指令转成16进制
        for i in range(len(Command)):
            Command_hex = Command_hex + hex(ord(Command[i]))[2:] + " "
        Command_hex = Command_hex + '0d'  # 加入松下指令的终止位CR
        # 返回将松下完整指令转成16进制数据
        return Command_hex

    # 串口发送数据
    def data_send(self, send_data):
        if self.ser.isOpen():
            if send_data != "":  # 非空字符串
                # hex发送
                send_data = send_data.strip()
                send_list = []
                while send_data != '':
                    num = int(send_data[0:2], 16)
                    send_data = send_data[2:].strip()
                    send_list.append(num)
                send_data = bytes(send_list)
                self.ser.write(send_data)
        else:
            pass

    # 处理单个数据  flag 质量状态
    def one_data(self, data):
        read_data = data.decode('utf-8')
        # 去掉前面无用响应码
        u8_data = read_data[6:]
        # 切取有效数据
        u8_data = u8_data[:4]
        # 将数据前后两位反序 得到正确数据
        H_Data = u8_data[:2]
        L_Data = u8_data[2:]
        data = L_Data + H_Data
        try:
            data = int(data, 16)
        except Exception as e:
            print("错误def_one_data:" + str(e))
        return data

    # 处理两个数据  最大压力等
    def two_data(self, data):
        read_data = data.decode('utf-8')
        if read_data != '':
            # 去掉前面无用响应码
            u8_data = read_data[6:]
            # 切取有效数据
            u8_data = u8_data[:8]
            data1 = u8_data[:4]
            data2 = u8_data[4:]
            # 将数据前后两位反序 得到正确数据
            H1_Data = data1[:2]
            L1_Data = data1[2:]
            data1 = L1_Data + H1_Data
            H2_Data = data2[:2]
            L2_Data = data2[2:]
            data2 = L2_Data + H2_Data
            data = data2 + data1
            try:
                data = int(data, 16)
            except Exception as e:
                print("错误one_data:" + str(e))
            return data

    # 处理多个数据  压力和位置采样
    def many_data(self, data):
        PLC_Data = data.decode('utf-8')
        if PLC_Data != None:
            PLC_Data = PLC_Data[6:]
            # 循环切片数据 调换高低位  并写入data_list
            data_list = []
            for i in range(0, len(PLC_Data), 4):
                data = PLC_Data[:4]
                H_Data = data[:2]
                L_Data = data[2:]
                data = L_Data + H_Data
                # 将位置数据转换为10进制 单位为mm
                if data == 0x00:
                    break
                try:
                    data = int(data, 16)
                    if data == 0:
                        break
                except Exception as e:
                    print("错误many_data:" + str(e))
                data_list.append(data)
                PLC_Data = PLC_Data[4:]
        else:
            pass
        return data_list

    # 发送falg 指令并接收数据
    def send_falg(self, command):
        import time
        if self.ser.isOpen():
            data = self.command_Data(command)
            self.data_send(data)
            try:
                while 1:
                    time.sleep(0.2)
                    num = self.ser.inWaiting()
                    if num != 0:
                        break
            except:
                self.port_close()
                return None
            if num > 0:
                data = self.ser.read(num)
                # print(data)
                data1 = self.one_data(data)
                return data1

    # 发送指令 接收数据
    def send_command(self, command, len):
        one_data = self.command_Data(command)
        self.data_send(one_data)
        while 1:
            num = self.ser.inWaiting()
            if num == len:
                break
        # print(num)
        data = self.ser.read(num)
        if num == 17:
            data1 = self.one_data(data)
        else:
            data1 = self.many_data(data)
        return data1

    # 读取数据 第一个参数 指令 第二个参数 读取数据长度
    def read_data(self, command):
        # 发送接收最大压力值 存入列表
        xy = []
        press_data_list = []
        # 最大压力，终止压力，终止位置，作业时间，压力采样数据，位置采样数据
        command_list_2 = ['<01#RDD2000220502', '<01#RDD2050321003', '<01#RDD2200222502', '<01#RDD2250323003']
        command3 = '<01#RDD0090000920'
        # 询环获取 最大压力，终止压力，终止位置，作业时间，质量状态
        for i in command:
            data1 = self.send_command(i, 17)
            press_data_list.append(data1)
        for j in command_list_2:
            data2 = self.send_command(j, 2013)
            xy.append(data2)
            press_data_list.append(data2)
        data3 = self.send_command(command3, 93)  # 接收长度待确认**********************
        press_data_list.append(data3)
        return xy, press_data_list

    # 接收压装数据 并写入数据库
    def press_data_receive(self):
        # 发送指令 读取DT472的值,'%01#RDD0047200472'
        data1 = self.send_falg('%01#RDD0047200472')
        # 当DT472>0时  读取压装数据
        if data1 > 0:
            command_list = ['%01#RDD0051200513', '%01#RDD0051000511', '%01#RDD0050800509',
                            '%01#RDD0051600517']
            xy, self.press_data_list = self.read_data(command_list)
            # 计算拐点
            y1 = int(xy[0]) * 10
            x1 = float(xy[1]) / 100
            kneedle = KneeLocator(x1, y1, curve='concave', direction='decreasing', online=True)
            # x为位置
            x = kneedle.elbow
            # y为压力
            y = kneedle.elbow_y
            # 将x,y传给DT474 还未写  ******************************
            # 读取完成后
            inflection_point = [x, y]
            self.press_data_list.append(inflection_point)
            # DT472写0
            self.DT_write('%01#WDD00472004720000')
            # 等待DT78 为2 取质量状态
            # 发送指令 读取DT78的值,'%01#RDD0007800078'
            data1 = self.send_falg('%01#RDD0007800078')
            if data1 == 2:
                # 发送指令读取质量状态
                command = ('%01#RDD0050200503')
                data1 = self.send_command(command)
                # 将质量状态数据插入列表
                self.press_data_list.insert(4, data1)
                self.data = self.press_data_list
                # 读完后 DT78写1
                self.DT_write('%01#WDD00078000780100')
        # 当DT472=0时 为出错或报警状态 读取数据
        elif data1 == 0:
            # 发送指令 读取DT78的值,'%01#RDD0007800078'
            data1 = self.send_falg('%01#RDD0007800078')
            if data1 == 2:
                # 发送指令读取质量状态
                command_list = ['%01#RDD0051200513', '%01#RDD0051000511', '%01#RDD0050800509',
                                '%01#RDD0051600517', '%01#RDD0050200503']
                xy, self.press_data_list = self.read_data(command_list)
                # 报警或出错状态 不计算拐点 直接插入空值
                self.press_data_list = self.press_data_list.append([])
                self.data = self.press_data_list
                # # 读完后 DT78写1
                self.DT_write('%01#WDD00078000780100')
        # 将数据 写入数据库
        # 0最大压力 1终止压力 2 终止位置 3作业时间 4质量状态 5压力数据采样 6压力数据采样 7位置数据采样 8位置数据采样 9条码 10拐点
        try:
            barcode = self.data[9]
            inflection_point = self.data[10]
            qualified_data = self.data[4]
            qualified = '合格' if qualified_data == 1 else '不合格'
            maxPressure = str(self.data[0])
            endPressure = str(self.data[1])
            endLocation = str(format(self.data[2] / 1000, '.2f')) if self.data[2] != '' else str(self.data[2])
            workTime = str(format(self.data[3] / 1000, '.2f')) if self.data[3] != '' else str(self.data[3])
            pressureCurveData = str(self.data[5] + self.data[6])
            locationCurveData = str(self.data[7] + self.data[8])
            time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")  # 获取当前时间
            # SQL语句
            sql = 'INSERT INTO pressdata(barcode,inflectionPoint,qualified, maxPressure, endPressure, endLocation, workTime, pressureCurveData, locationCurveData,timer) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
            # 插入的压装数据
            value = (
                barcode, inflection_point, qualified, maxPressure, endPressure, endLocation, workTime,
                pressureCurveData,
                locationCurveData, time)
            self.mysql.add_mysql(sql, value)
        except Exception as e:
            # 错误信息
            print("press_data_receive:" + str(e))

    # 暂停和开始线程
    def stop_start_thread(self, bool):
        if bool == 1:
            self._isPause = True
        elif bool == 0:
            self._isPause = False
            self.cond.wakeAll()

    # 线程run
    def run(self):
        while 1:
            try:
                print("111")
                # if self.ser.isOpen() == True:
                #     self.port_open_status.emit(True)
                # else:
                #     self.port_open_status.emit(False)
                self.press_data_receive()
                sql = 'SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE to_days(pressdata.timer) = to_days(now()) ;'
                result = self.mysql.find_mysql(sql)
                self.update_data.emit(result)  # 将查询到的数据发送给槽函数
            except Exception as e:
                print("run" + str(e))


# 主界面
class press_Data_App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(press_Data_App, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("img/press.ico"))
        self.init()
        # 实例化密码修改窗口
        self.change_password = change_password()
        # 实例关于窗口
        self.about_us = about_us()
        # 实例化曲线窗口
        self.curve_ui = curve_ui()
        # 实例化数据库
        self.mysql = mysql()
        self.mysql.open_mysql()

    def init(self):
        # 查询按钮
        self.query_btn.clicked.connect(self.find_data)
        self.delete_data_btn.clicked.connect(self.delete_data)

        now_day = time.strftime("%Y-%m-%d", time.localtime())  # 获取当前日期
        # 设置初使值为当前日期
        self.start_date.setDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.end_date.setDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.start_delete_date.setDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.end_delete_date.setDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
        # 禁止编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 整行选择
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 列内容自适应
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 双击加载曲线
        self.tableWidget.cellDoubleClicked.connect(self.main_curve_show)
        self.tableWidget_2.cellDoubleClicked.connect(self.find_curve_show)
        # ****************菜单栏****************
        # 管理员密码
        self.admin_pwd.triggered.connect(self.change_pwd_show)
        # 关于
        self.about_us.triggered.connect(self.about_show)
        # 线程
        self.backend = SerialThread()
        self.backend.update_data.connect(self.show_data_tebleWidget)
        self.backend.start()
        self.stop.clicked.connect(self.stop_thread)
        self.start.clicked.connect(self.start_thread)

    # 暂停线程
    def stop_thread(self, ):
        self.backend.stop_start_thread(1)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)

    # 开始线程
    def start_thread(self):
        self.backend.stop_start_thread(0)
        self.stop.setEnabled(True)
        self.start.setEnabled(False)

    # 主界面 显示曲线
    def main_curve_show(self):
        # 获取点击的列数
        tableWidget_col = self.tableWidget.currentIndex().column()
        # 判断主窗口还是数据查询窗口被点击 只有点击曲线编号列时，能才显示曲线
        if tableWidget_col == 7:
            id = self.tableWidget.currentItem().text()
            self.curve_ui.curev_widget(id)
            self.curve_ui.show()
        else:
            pass

    # 查询界面显示曲线
    def find_curve_show(self):
        # 获取点击的列数
        tableWidget_2_col = self.tableWidget_2.currentIndex().column()
        # 只有点击曲线编号列时，能才显示曲线
        if tableWidget_2_col == 7:
            id = self.tableWidget_2.currentItem().text()
            self.curve_ui.curev_widget(id)
            self.curve_ui.show()
        else:
            pass

    # 显示修改密码窗口
    def change_pwd_show(self):
        self.change_password.show()

    # 显示关于窗口
    def about_show(self):
        self.about_us.show()

    # **************************数据库**********************************
    # 按选择 或 条件 查询数据 并显示在tableWidget_2上
    def find_data(self):
        if self.select_rbtn.isChecked():
            if self.select_date.currentText() == "本月":
                sql = "SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE MONTH(timer)=MONTH(NOW());"
                data = self.mysql.find_mysql(sql)
                self.show_data_tableWidget_2(data)
            if self.select_date.currentText() == "上月":
                sql = "SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE  PERIOD_DIFF( date_format( now( ) , '%Y%m' ) , date_format( timer, '%Y%m' ) ) =1;"
                data = self.mysql.find_mysql(sql)
                self.show_data_tableWidget_2(data)
            elif self.select_date.currentText() == "近半年":
                sql = 'SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE timer BETWEEN date_sub(now(),INTERVAL 6 MONTH ) AND now();'
                # sql = 'SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE QUARTER(timer)=QUARTER(DATE_SUB(now(),interval 1 QUARTER)) AND YEAR(timer)=YEAR(NOW();'
                data = self.mysql.find_mysql(sql)
                self.show_data_tableWidget_2(data)
            elif self.select_date.currentText() == "本年":
                sql = 'SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE YEAR(timer)=YEAR(NOW());'
                data = self.mysql.find_mysql(sql)
                self.show_data_tableWidget_2(data)
            else:
                pass
        if self.condition_rbtn.isChecked():
            start_date = self.start_date.text()
            end_date = self.end_date.text()
            sql = "SELECT qualified,maxPressure,endPressure,endLocation,workTime,timer,id FROM pressdata WHERE timer >= STR_TO_DATE(" + "'" + start_date + "'," + "'%Y-%m-%d %H:%M:%S') AND timer <= STR_TO_DATE(" + "'" + end_date + "'," + "'%Y-%m-%d %H:%M:%S');"
            data = self.mysql.find_mysql(sql)
            self.show_data_tableWidget_2(data)

    # 按选择 或 条件 删除数据
    def delete_data(self):
        if self.select_delete_rbtn.isChecked():
            warning = QMessageBox.warning(self, '提示', '确定要删除数据吗,删除后数据不可恢复', QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if warning == QMessageBox.Yes:
                pwd, bb = QInputDialog.getText(self, '密码验证', '请输入管理员密码', echo=QLineEdit.Password)
                try:
                    sql = "SELECT password FROM userName WHERE name='admin';"
                    password = self.mysql.find_mysql(sql)
                    password = password[0][0]
                    # 跟数据库数据对比
                    if pwd == password and bb:
                        if self.select_delete_date.currentText() == "全部删除":
                            sql = "DELETE FROM pressdata"
                            self.mysql.delete_mysql(sql)
                            QMessageBox.about(self, '提示', '数据已删除')
                        elif self.select_delete_date.currentText() == "超过一年":
                            sql = "DELETE FROM pressdata WHERE timer < DATE_SUB(NOW(), INTERVAL 1 YEAR)"
                            self.mysql.delete_mysql(sql)
                            QMessageBox.about(self, '提示', '数据已删除')
                        elif self.select_delete_date.currentText() == "超过三年":
                            sql = "DELETE FROM pressdata WHERE timer < DATE_SUB(NOW(), INTERVAL 3 YEAR)"
                            self.mysql.delete_mysql(sql)
                            QMessageBox.about(self, '提示', '数据已删除')
                        elif self.select_delete_date.currentText() == "超过五年":
                            sql = "DELETE FROM pressdata WHERE timer < DATE_SUB(NOW(), INTERVAL 5 YEAR)"
                            self.mysql.delete_mysql(sql)
                            QMessageBox.about(self, '提示', '数据已删除')
                        else:
                            QMessageBox.about(self, '提示', '删除数据不成功')
                    else:
                        QMessageBox.warning(self, '提示', '密码不正确')
                except Exception as e:
                    # 错误信息
                    print("select_find:" + str(e))
            else:
                pass

        if self.condition_delete_rbtn.isChecked():
            start_delete_date = self.start_delete_date.text()
            end_delete_date = self.end_delete_date.text()
            warning = QMessageBox.warning(self, '提示',
                                          f'确定要删除{start_delete_date}--{end_delete_date}的数据吗,删除后数据不可恢复',
                                          QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if warning == QMessageBox.Yes:
                pwd, bb = QInputDialog.getText(self, '密码验证', '请输入管理员密码', echo=QLineEdit.Password)
                try:
                    sql = "SELECT password FROM userName WHERE name='admin';"
                    password = self.mysql.find_mysql(sql)
                    password = password[0][0]
                    # 跟数据库数据对比
                    if pwd == password and bb:
                        sql = f"DELETE FROM pressdata WHERE timer >= STR_TO_DATE('{start_delete_date}','%Y-%m-%d %H:%M:%S') AND timer <= STR_TO_DATE('{end_delete_date}','%Y-%m-%d %H:%M:%S');"
                        self.mysql.delete_mysql(sql)
                        QMessageBox.about(self, '提示', '数据已删除')
                    else:
                        QMessageBox.warning(self, '提示', '密码不正确')
                except Exception as e:
                    print("错误def_select_find:" + str(e))
            else:
                pass

    # 数据写入 tableWidget_2
    def show_data_tableWidget_2(self, result):
        self.tableWidget_2.setRowCount(len(result))
        list_data = []
        # 将数据取出 遍历加入数组
        for data in result:
            list_data.append(data)
        # 数组反序 使显示时第一条显示数据库最后一条数据
        list_data.reverse()
        # 设置行数
        self.tableWidget_2.setRowCount(len(result))
        # 将数据
        for i in range(len(result)):
            data = list_data[i]
            for index in range(8):
                try:
                    newItem = (QTableWidgetItem('1') if i == 0 else QTableWidgetItem(
                        str(i + 1))) if index == 0 else QTableWidgetItem(str(data[index - 1]))
                    if str(data[index - 1]) == '合格':
                        newItem.setForeground(QBrush(QColor(11, 166, 120)))  # 合格绿色
                    elif str(data[index - 1]) == '不合格':
                        newItem.setForeground(QBrush(QColor(168, 28, 66)))  # 不合格红色
                    # 设置字体样式 大小
                    newItem.setFont(QFont('Microsoft YaHei', 12))
                    # 文本居中
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget_2.setItem(i, index, newItem)
                except Exception as e:
                    print('错误show_data_tebleWidget' + e)

    # 数据写入 tableWidget
    def show_data_tebleWidget(self, result):
        self.tableWidget.setRowCount(len(result))
        list_data = []
        # 将数据取出 遍历加入数组
        for data in result:
            list_data.append(data)
        # 数组反序 使显示时第一条显示数据库最后一条数据
        list_data.reverse()
        # 将数据
        for i in range(len(result)):
            data = list_data[i]
            for index in range(8):
                try:
                    if index == 0:
                        if i == 0:
                            newItem = QTableWidgetItem('当前')
                            newItem.setForeground(QBrush(QColor(168, 28, 66)))  # 红色
                        else:
                            newItem = QTableWidgetItem(str(i + 1))
                    else:
                        newItem = QTableWidgetItem(str(data[index - 1]))
                    if str(data[index - 1]) == '合格':
                        newItem.setForeground(QBrush(QColor(11, 166, 120)))  # 合格绿色
                    elif str(data[index - 1]) == '不合格':
                        newItem.setForeground(QBrush(QColor(168, 28, 66)))  # 不合格红色
                    # 设置字体样式 大小
                    newItem.setFont(QFont('Microsoft YaHei', 12))
                    # 文本居中
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i, index, newItem)
                except Exception as e:
                    print('错误show_data_tebleWidget' + e)

    #  ****************************曲线******************

    def windowShow(self):
        # 打开子窗口后 阻塞主界面
        self.change_password.setWindowModality(Qt.ApplicationModal)
        self.about_us.setWindowModality(Qt.ApplicationModal)
        self.curve_ui.setWindowModality(Qt.ApplicationModal)
        # 全屏开启，有关闭按钮
        # win_show.showMaximized()
        win_show.show()  # 显示主界面


# 曲线显示界面
class curve_ui(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        super(curve_ui, self).__init__()
        self.setupUi(self)
        # 禁用窗口最大化 和拉伸
        self.setFixedSize(self.width(), self.height())
        # 禁用最小和最大化按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.mysql = mysql()
        self.mysql.open_mysql()

    def curev_widget(self, id):
        try:
            sql = f"SELECT locationCurveData,pressureCurveData,timer,inflectionPoint  FROM pressdata WHERE id = {id}"
            result = self.mysql.find_mysql(sql)
            x, y = self.str_to_int_list(result[0][0], result[0][1])
            self.pw = self.widget
            # 清除上次的曲线
            self.pw.clear()
            # 设置图表标题、颜色、字体大小
            self.pw.setTitle(f"压装时间: {result[0][2]}", color='008080', size='12pt')
            # 背景色改为白色
            self.pw.setBackground('#f0f0f0')
            self.pw.setWindowTitle('压装曲线')
            # 显示表格线
            self.pw.showGrid(x=True, y=True)
            # 设置上下左右的label
            # 第一个参数 只能是 'left', 'bottom', 'right', or 'top'
            self.pw.setLabel("left", "压力(N)")
            self.pw.setLabel("bottom", "位置", units='mm')
            # 线条颜色 粗细
            curve = self.pw.plot(pen=pg.mkPen(color='#0055ff', width=2))
            # 数据写入x,y坐标
            curve.setData(x, y)
            self.press_coordinates = 0
            self.location_coordinates = 0
            # 计算拐点
            inflection_point = result[0][3]
            # 曲线内显示文本
            aa = f'{inflection_point[1]}/{inflection_point[0]}'
            x = float(inflection_point[0])
            y = int(inflection_point[1])
            text = pg.TextItem(
                html=f'<div style="text-align: center"><span style="color: #0d1042; font-size: 12pt;">{aa}</span></div>',
                anchor=(-0.2, -0.6), border='w', fill=(149, 225, 225))
            self.pw.addItem(text)
            text.setPos(x, y)

            # 箭头
            arrow = pg.ArrowItem(pos=(x, y), angle=45)
            self.pw.addItem(arrow)

            # 显示坐标值
            def mouseover(pos):
                # 参数pos 是像素坐标，需要 转化为  刻度坐标
                act_pos = curve.mapFromScene(pos)
                if type(act_pos) != PyQt5.QtCore.QPointF:
                    return
                self.press_coordinates = format(act_pos.y(), '.2f')
                self.location_coordinates = format(act_pos.x(), '.2f')
                self.pw.setTitle(
                    f"压装时间: {result[0][2]}       压力: {self.press_coordinates}N  位置: {self.location_coordinates}mm",
                    color='008080', size='12pt')

            curve.scene().sigMouseMoved.connect(mouseover)

        except Exception as e:
            print(str(e))

    # 如果压力和位置采样数据长度不一样，删除多出的数据
    def str_to_int_list(self, x, y):
        x_data = x
        x_data = x_data[1:]
        x_data = x_data[:-1]
        x_data = x_data.split(', ')
        y_data = y
        y_data = y_data[1:]
        y_data = y_data[:-1]
        y_data = y_data.split(', ')
        x = []
        y = []
        for i in x_data:
            data = float(i) / 100
            x.append(data)
        for j in y_data:
            data = int(j) * 10
            y.append(data)
        if len(x) > len(y):
            i = len(x) - len(y)
            x = x[0:-i]
        elif len(y) > len(x):
            j = len(y) - len(x)
            y = y[0:-j]
        return x, y


# 修改密码界面
class change_password(QMainWindow, Ui_Form_PWD):
    def __init__(self):
        super(change_password, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('修改密码')
        self.init()
        # 禁用窗口最大化 和拉伸
        self.setFixedSize(self.width(), self.height())
        # 禁用最小和最大化按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.mysql = mysql()
        self.mysql.open_mysql()

    def init(self):
        self.cancel_btn.clicked.connect(self.close)
        self.submit_btn.clicked.connect(self.submit_change_pwd)

    def submit_change_pwd(self):
        try:
            user_name = self.user_name.text()
            original_pwd = self.original_pwd.text()
            new_pwd = self.new_pwd.text()
            confirm_pwd = self.confirm_pwd.text()
            sql = f"SELECT name,password FROM userName WHERE name='{user_name}';"
            data = self.mysql.find_mysql(sql)
            name = data[0][0]
            password = data[0][1]
            if original_pwd == '' or new_pwd == '' or confirm_pwd == '':
                QMessageBox.about(self, '提示', '密码不能为空，请重新输入')
                self.original_pwd.clear()
                self.new_pwd.clear()
                self.confirm_pwd.clear()
            elif original_pwd != password:
                QMessageBox.about(self, '提示', '原密码输入错误，请重新输入')
                self.original_pwd.clear()
                self.original_pwd.setFocus()
            elif new_pwd != confirm_pwd:
                QMessageBox.about(self, '提示', '两次新密码输入不一致，请重新输入')
                self.new_pwd.clear()
                self.confirm_pwd.clear()
                self.new_pwd.setFocus()
            else:
                # 输入没问题时，更新数据库修改密码
                sql = 'UPDATE username SET password = %s where name = %s;'
                value = (new_pwd, name)
                self.mysql.add_mysql(sql, value)
                QMessageBox.about(self, '提示', '密码修改成功，请记住您的新密码')
                self.original_pwd.clear()
                self.new_pwd.clear()
                self.confirm_pwd.clear()
                self.close()

        except Exception as e:
            print("submit_change_pwd" + str(e))


# 关于界面
class about_us(QMainWindow, Ui_Form_About):
    def __init__(self):
        super(about_us, self).__init__()
        self.setupUi(self)
        # 禁用窗口拉伸
        self.setFixedSize(self.width(), self.height())
        # 禁用最小和最大化按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)


# 加载窗口
class Splash(QMainWindow, Ui_Form_load):
    # 自定义信号
    splashClose = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 设置无边框并置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 设置背景为透明色
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 计时开始
        self.timeRun()

    # 进度条逻辑
    def timeRun(self):
        self.timer = QBasicTimer()
        self.step = 0
        # 设置10超时时间 并开始计时
        self.timer.start(10, self)

    def timerEvent(self, evet):
        if self.step >= 100:
            self.timer.stop()
            # 发出信号，可打开其它界面
            self.splashClose.emit()
            # 关闭开机画面
            self.close()
            return
        else:
            self.step = self.step + 1
            self.prg.setValue(self.step)
            self.lab1.setText('正在加载...{}%'.format(self.step))
            return


# 运行
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        serverName = 'testServer'
        socket = QLocalSocket()
        socket.connectToServer(serverName)
        # 如果连接成功，表明server已经存在，当前已有实例在运行
        if socket.waitForConnected(500):
            press_Data_App()
            app.quit()
        else:
            localServer = QLocalServer()
            localServer.listen(serverName)
            win_show = press_Data_App()
            # win_show.show()
            # 开机界面
            UiSplash = Splash()
            UiSplash.show()
            # 开机界面关闭连接打开主界面
            UiSplash.splashClose.connect(win_show.windowShow)
            sys.exit(app.exec_())
    except Exception as e:
        print("程序启动异常：{}".format(e))
