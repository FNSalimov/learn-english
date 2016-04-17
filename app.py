from PyQt4 import QtGui, QtCore
import sys, words, random

class MyApp(QtGui.QMainWindow, words.Ui_MainWindow):
        def __init__(self):
            super(MyApp, self).__init__()
            self.setupUi(self)
            self.show()
            #self.russian = ''
            #self.english = ''
            self.my_dict = {1: self.pushButton, 2: self.pushButton_2, 3: self.pushButton_3, 4: self.pushButton_4, 5: self.pushButton_5, 6: self.pushButton_6, 7: self.pushButton_7, 8: self.pushButton_8, 9: self.pushButton_9, 10: self.pushButton_10}
            self.my_list = [1, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine, self.ten]
            for i in range(1, 11):
                self.my_dict[i].setVisible(True)
                self.my_dict[i].setEnabled(True)
                self.my_dict[i].clicked.connect(self.my_list[i])
            """QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.one)
            self.pushButton_2.clicked.connect(self.two)
            self.pushButton_3.clicked.connect(self.three)
            self.pushButton_4.clicked.connect(self.four)
            self.pushButton_5.clicked.connect(self.five)
            self.pushButton_6.clicked.connect(self.six)
            self.pushButton_7.clicked.connect(self.seven)
            self.pushButton_8.clicked.connect(self.eight)
            self.pushButton_9.clicked.connect(self.nine)
            self.pushButton_10.clicked.connect(self.ten)"""
            self.list_of_words = []
            self.my_file = open('text.txt', 'r')
            for line in self.my_file:
                if line != '\n':
                    line = line.strip()
                    self.list_of_words.append(line)
            self.my_file.close()
            self.five_words = []
            self.random_number = random.randint(5, len(self.list_of_words) - 1)
            for i in range(self.random_number - 5, self.random_number):
                self.five_words.append(self.list_of_words[i])
            self.pushButton.setText(self.list_of_words[self.random_number - 5][:self.list_of_words[self.random_number - 5].index('–')])
            self.pushButton_2.setText(self.list_of_words[self.random_number - 4][:self.list_of_words[self.random_number - 4].index('–')])
            self.pushButton_3.setText(self.list_of_words[self.random_number - 3][:self.list_of_words[self.random_number - 3].index('–')])
            self.pushButton_4.setText(self.list_of_words[self.random_number - 2][:self.list_of_words[self.random_number - 2].index('–')])
            self.pushButton_5.setText(self.list_of_words[self.random_number - 1][:self.list_of_words[self.random_number - 1].index('–')])
            self.ran = [6, 7, 8, 9, 10]
            random.shuffle(self.ran)
            self.my_dict[self.ran[0]].setText(self.list_of_words[self.random_number - 5][self.list_of_words[self.random_number - 5].index('–') + 1:])
            self.my_dict[self.ran[1]].setText(self.list_of_words[self.random_number - 4][self.list_of_words[self.random_number - 4].index('–') + 1:])
            self.my_dict[self.ran[2]].setText(self.list_of_words[self.random_number - 3][self.list_of_words[self.random_number - 3].index('–') + 1:])
            self.my_dict[self.ran[3]].setText(self.list_of_words[self.random_number - 2][self.list_of_words[self.random_number - 2].index('–') + 1:])
            self.my_dict[self.ran[4]].setText(self.list_of_words[self.random_number - 1][self.list_of_words[self.random_number - 1].index('–') + 1:])
            self.flag = 0
            self.result = 0
        def one(self):
            if self.flag in range(6, 11):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton.text()) == self.five_words[ind][:self.five_words[ind].find('–')]):
                    self.pushButton.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.english = str(self.pushButton.text())
                self.pushButton.setEnabled(False)
                self.flag = 1
        def two(self):
            if self.flag in range(6, 11):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_2.text()) == self.five_words[ind][:self.five_words[ind].find('–')]):
                    self.pushButton_2.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.english = str(self.pushButton_2.text())
                self.pushButton_2.setEnabled(False)
                self.flag = 2
        def three(self):
            if self.flag in range(6, 11):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_3.text()) == self.five_words[ind][:self.five_words[ind].find('–')]):
                    self.pushButton_3.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.english = str(self.pushButton_3.text())
                self.pushButton_3.setEnabled(False)
                self.flag = 3
        def four(self):
            if self.flag in range(6, 11):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_4.text()) == self.five_words[ind][:self.five_words[ind].find('–')]):
                    self.pushButton_4.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.english = str(self.pushButton_4.text())
                self.pushButton_4.setEnabled(False)
                self.flag = 4
        def five(self):
            if self.flag in range(6, 11):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_5.text()) == self.five_words[ind][:self.five_words[ind].find('–')]):
                    self.pushButton_5.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.english = str(self.pushButton_5.text())
                self.pushButton_5.setEnabled(False)
                self.flag = 5
        def six(self):
            if self.flag in range(1, 6):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_6.text()) == self.five_words[ind][self.five_words[ind].find('–') + 1:]):
                    self.pushButton_6.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.russian = str(self.pushButton_6.text())
                self.pushButton_6.setEnabled(False)
                self.flag = 6
        def seven(self):
            if self.flag in range(1, 6):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_7.text()) == self.five_words[ind][self.five_words[ind].find('–') + 1:]):
                    self.pushButton_7.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.russian = str(self.pushButton_7.text())
                self.pushButton_7.setEnabled(False)
                self.flag = 7
        def eight(self):
            if self.flag in range(1, 6):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_8.text()) == self.five_words[ind][self.five_words[ind].find('–') + 1:]):
                    self.pushButton_8.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.russian = str(self.pushButton_8.text())
                self.pushButton_8.setEnabled(False)
                self.flag = 8
        def nine(self):
            if self.flag in range(1, 6):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_9.text()) == self.five_words[ind][self.five_words[ind].find('–') + 1:]):
                    self.pushButton_9.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.russian = str(self.pushButton_9.text())
                self.pushButton_9.setEnabled(False)
                self.flag = 9
        def ten(self):
            if self.flag in range(1, 6):
                w = str(self.my_dict[self.flag].text())
                ind = -1
                for i in range(len(self.five_words)):
                    if (self.five_words[i].find(w) != -1):
                        ind = i
                        break
                if (str(self.pushButton_10.text()) == self.five_words[ind][self.five_words[ind].find('–') + 1:]):
                    self.pushButton_10.setVisible(False)
                    self.my_dict[self.flag].setVisible(False)
                    print("YES")
                    self.result += 1
                    self.flag = 0
                else:
                    print("NO")
            else:
                if self.flag != 0:
                    self.my_dict[self.flag].setEnabled(True)
                #self.russian = str(self.pushButton_10.text())
                self.pushButton_10.setEnabled(False)
                self.flag = 10
            
def main():
    app = QtGui.QApplication(sys.argv)
    form = MyApp()
    if form.result == 5:
        print("ROZIYA")
    sys.exit(app.exec_())

if __name__ == '__main__':  
    main()