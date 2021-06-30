# pyTranslate PeiwenJi 2021.4.20
# Translate DNA sequence to protein and display results to users.
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from main_ui import Ui_pyTranslate
from results5_ui import Ui_MainWindow


class MyMainWindow(QtWidgets.QMainWindow, Ui_pyTranslate):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("pyTranslate")
        
        # 此处编写业务逻辑代码
        self.startCodon = 'ATG' # 开始密码子
        self.stopCodon = {'TAA', 'TAG', 'TGA'} # 终止密码子
        
        self.gencode = { # 标准密码表
            'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
            'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
            'TTA':'L', 'TCA':'S', 'TAA':'_', 'TGA':'_',
            'TTG':'L', 'TCG':'S', 'TAG':'_', 'TGG':'W',

            'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
            'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
            'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
            'CTG':'L', 'CCG':'P', 'CAG':'Q', 'CGG':'R',

            'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
            'ATC':'I', 'ACC':'T', 'AAC':'N', 'AGC':'S',
            'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',
            'ATG':'<MET>', 'ACG':'T', 'AAG':'K', 'AGG':'R',

            'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
            'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
            'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
            'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G'}

        self.basecomplement = { # 碱基对应表
            'A':'T',
            'T':'A',
            'G':'C',
            'C':'G',
            'a':'t',
            't':'a',
            'g':'c',
            'c':'g'}

        self.btSubmit.clicked.connect(self.popWindow) # 绑定信号槽

    # 将DNA转成氨基酸序列
    def mainTranslate(self, seq):
        translate= ''.join([self.gencode.get(seq[3*i:3*i+3],'<UNKNOWN>') for i in range(len(seq)//3)])
        return translate

    # 返回互补链
    def complement(self, s):
        letters = list(s)
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)
    
    # 展示结果
    def popWindow(self):
        # 弹出第二个窗口
        self.resultMainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
        self.ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
        self.ui.setupUi(self.resultMainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
        self.resultMainWindow.show()
        self.resultMainWindow.setWindowTitle("results")
        
        # 预处理输入DNA序列：去除空格、换行符、数字，并将字母大写
        str = self.plainTextEdit.toPlainText() # 获取文本
        seq = filter(lambda ch: ch not in ' \t\n1234567890', str) # 去除空格、换行符、数字
        seq = list(seq)
        seq = "".join(seq)
        seq = seq.upper() # 字母变大写

        # 5'->3'
        self.ui.textBrowser.setText(self.mainTranslate(seq[0:])) # 第一个阅读框
        self.ui.textBrowser_2.setText(self.mainTranslate(seq[1:])) # 第二个阅读框
        self.ui.textBrowser_3.setText(self.mainTranslate(seq[2:])) # 第三个阅读框

        # 3'->5'
        seq = self.complement(seq) # 获取互补链
        self.ui.textBrowser_4.setText(self.mainTranslate(seq[::-1][0:])) # 反向第一个阅读框
        self.ui.textBrowser_5.setText(self.mainTranslate(seq[::-1][1:])) # 反向第二个阅读框
        self.ui.textBrowser_6.setText(self.mainTranslate(seq[::-1][2:])) # 反向第三个阅读框


# 程序入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())