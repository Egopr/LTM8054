from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import time


app = QtWidgets.QApplication([])
ui = uic.loadUi('LTM8054.ui')

ui.setWindowTitle('LTM 8054')

serial = QSerialPort()
serial.setBaudRate(115200)
portList = []

def refCom():
    ui.cbox_b.clear()
    ports = QSerialPortInfo.availablePorts()
    for port in ports:
        portList.append(port.portName())
    print('REFRESH')
    current_row = ui.listWidget.currentRow()
    ui.listWidget.insertItem(current_row + 1, 'REFRESH')
    return ui.cbox_b.addItems(set(portList))

def onClean():
    ui.listWidget.clear()



def onOpen():
    com_my = ui.cbox_b.currentText()
    print(com_my, '<= PORT OPEN')
    current_row = ui.listWidget.currentRow()
    writePort = str(com_my) + ' Port OPEN'
    ui.listWidget.insertItem(current_row + 1, writePort)
    serial.setPortName(com_my)
    serial.open(QIODevice.ReadWrite)


def onClose():
    serial.close()
    com_my = ui.cbox_b.currentText()
    print(com_my, '<= PORT CLOSE')
    writePort = str(com_my) + ' Port CLOSE'
    current_row = ui.listWidget.currentRow()
    ui.listWidget.insertItem(current_row + 1, writePort)


def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    current_row = ui.listWidget.currentRow()
    ui.listWidget.insertItem(current_row + 1, rxs)
    print(rx)


def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[:-1]
    txs += ';'
    serial.write(txs.encode())


def relayOn(val):
    serialSend('1')
    ui.label_info.setText("Reley ON")



def relayOff(val):
    serialSend('2')
    ui.label_info.setText("Reley OFF")



serial.readyRead.connect(onRead)
ui.ref_b.clicked.connect(refCom)

ui.open_b.clicked.connect(onOpen)
ui.close_b.clicked.connect(onClose)

ui.on_b.clicked.connect(relayOn)
ui.off_b.clicked.connect(relayOff)

ui.connect_b.clicked.connect(onClean)



ui.show()
app.exec()
