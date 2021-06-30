# pyTranslate

> PeiwenJi 2021.04.23

## 1. 问题

参考在线软件https://web.expasy.org/translate/编写把DNA翻译成蛋白质序列的程序。

## 2. 代码说明

* <u>main.py</u>: 主要逻辑代码
* <u>main_ui.py</u>: “主界面”代码（由<u>pyTranslate.ui</u>转化而来）
* <u>results5_ui.py</u>: “结果界面”代码（由<u>results5.ui</u>转化而来）

### 步骤

**（1）用pyqt5绘制界面。**

分别完成主界面、结果界面的绘制后，保存为pyTranslate.ui和results5.ui文件。

**（2） 将.ui文件转化为.py文件。**

win+R，打开cmd，进入控制台界面。切换到ui文件所在路径，使用pyuic5命令。

```
cd C:\Users\20181\Desktop\code
pyuic5 -o main_ui.py pyTranslate.ui
pyuic5 -o results5_ui.py results5.ui
```

**（3） 新建main.py文件，编写主要逻辑代码。**

使用以下代码实现界面和逻辑代码的分离。

``` python
from PyQt5 import QtWidgets,QtGui,QtCore
from py文件名 import 类名
import sys

class MainWindow(QtWidgets.QMainWindow, 类名):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    # 此处编写业务逻辑代码
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

### 主要函数说明

**（1）mainTranslate(self, seq): 将DNA转成氨基酸序列。**

每次读三个碱基，如果在gencode中，返回对应的氨基酸；如果不在，记为<UNKNOWN>，并继续读下去。最后返回翻译的序列。

``` python
def mainTranslate(self, seq):
    translate = ''.join([self.gencode.get(seq[3*i:3*i+3],'<UNKNOWN>') for i in range(len(seq)//3)])
    return translate
```

注：gencode（标准密码表——根据NCBI Genetic Codes [Standard Code](https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1)绘制）

**（2） complement(self, s): 返回互补链。**

查询basecomplement字典返回对应的互补链。

``` python
def complement(self, s):
    letters = list(s)
    letters = [self.basecomplement[base] for base in letters]
    return ''.join(letters)
```

注：basecomplement（碱基对应表）

**（3） popWindow(self): 展示结果**

弹出结果窗口。

```python
# 创建一个QMainWindow，用来装载你需要的各种组件、控件
self.resultMainWindow = QtWidgets.QMainWindow() 
# ui是Ui_MainWindow()类的实例化对象
self.ui = Ui_MainWindow()
# 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
self.ui.setupUi(self.resultMainWindow) 
self.resultMainWindow.show()
```

预处理输入的DNA序列：去除空格、换行符、数字，并将所有字母大写。

```python
str = self.plainTextEdit.toPlainText() # 获取文本
seq = filter(lambda ch: ch not in ' \t\n1234567890', str) # 去除空格、换行符、数字
seq = list(seq)
seq = "".join(seq)
seq = seq.upper() # 字母变大写
```

输出正向和反向翻译结果。

```python
# 5'->3'
self.ui.textBrowser.setText(self.mainTranslate(seq[0:])) # 第一个阅读框
self.ui.textBrowser_2.setText(self.mainTranslate(seq[1:])) # 第二个阅读框
self.ui.textBrowser_3.setText(self.mainTranslate(seq[2:])) # 第三个阅读框

# 3'->5'
seq = self.complement(seq) # 获取互补链
self.ui.textBrowser_4.setText(self.mainTranslate(seq[::-1][0:])) # 反向第一个阅读框
self.ui.textBrowser_5.setText(self.mainTranslate(seq[::-1][1:])) # 反向第二个阅读框
self.ui.textBrowser_6.setText(self.mainTranslate(seq[::-1][2:])) # 反向第三个阅读框
```
