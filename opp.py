from PyQt4 import QtGui, QtCore
import sys, words, random

class MyApp(QtGui.QMainWindow, words.Ui_MainWindow):
        def __init__(self):
            super(MyApp, self).__init__()
            self.setupUi(self)
            self.show()

def func_for_file():
    global list_of_words, five_words, form, my_dict, flag, result, wrong_answers
    flag, result, wrong_answers, five_words = 0, 0, 0, []
    for i in range(1, 11):
        my_dict[i].setVisible(True)
        my_dict[i].setEnabled(True)
    my_file = open('text.txt', 'r')
    for line in my_file:
        line = line.strip()
        list_of_words.append(line)
    my_file.close()
    for i in range(5):
        random_number = random.randint(1, len(list_of_words) - 1)
        while list_of_words[random_number] in five_words:
            random_number = random.randint(1, len(list_of_words) - 1)
        five_words.append(list_of_words[random_number])
    for i in range(1, 6):
        my_dict[i].setText(five_words[i - 1][:five_words[i - 1].index('--')])
    """form.pushButton.setText(list_of_words[random_number - 5][:list_of_words[random_number - 5].index('--')])
    form.pushButton_2.setText(list_of_words[random_number - 4][:list_of_words[random_number - 4].index('--')])
    form.pushButton_3.setText(list_of_words[random_number - 3][:list_of_words[random_number - 3].index('--')])
    form.pushButton_4.setText(list_of_words[random_number - 2][:list_of_words[random_number - 2].index('--')])
    form.pushButton_5.setText(list_of_words[random_number - 1][:list_of_words[random_number - 1].index('--')])"""
    ran = [6, 7, 8, 9, 10]
    random.shuffle(ran)
    for i in range(5):
        my_dict[ran[i]].setText(five_words[i][five_words[i].index('--') + 2:])
    """my_dict[ran[0]].setText(list_of_words[random_number - 5][list_of_words[random_number - 5].index('--') + 2:])
    my_dict[ran[1]].setText(list_of_words[random_number - 4][list_of_words[random_number - 4].index('--') + 2:])
    my_dict[ran[2]].setText(list_of_words[random_number - 3][list_of_words[random_number - 3].index('--') + 2:])
    my_dict[ran[3]].setText(list_of_words[random_number - 2][list_of_words[random_number - 2].index('--') + 2:])
    my_dict[ran[4]].setText(list_of_words[random_number - 1][list_of_words[random_number - 1].index('--') + 2:])"""

def one():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(6, 11):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton.text()) == five_words[ind][:five_words[ind].find('--')]):
            form.pushButton.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton.setEnabled(False)
        flag = 1

def two():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(6, 11):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_2.text()) == five_words[ind][:five_words[ind].find('--')]):
            form.pushButton_2.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_2.setEnabled(False)
        flag = 2
def three():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(6, 11):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_3.text()) == five_words[ind][:five_words[ind].find('--')]):
            form.pushButton_3.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_3.setEnabled(False)
        flag = 3
def four():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(6, 11):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_4.text()) == five_words[ind][:five_words[ind].find('--')]):
            form.pushButton_4.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_4.setEnabled(False)
        flag = 4
def five():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(6, 11):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_5.text()) == five_words[ind][:five_words[ind].find('--')]):
            form.pushButton_5.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_5.setEnabled(False)
        flag = 5
def six():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(1, 6):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_6.text()) == five_words[ind][five_words[ind].find('--') + 2:]):
            form.pushButton_6.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_6.setEnabled(False)
        flag = 6
def seven():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(1, 6):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_7.text()) == five_words[ind][five_words[ind].find('--') + 2:]):
            form.pushButton_7.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_7.setEnabled(False)
        flag = 7
def eight():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(1, 6):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_8.text()) == five_words[ind][five_words[ind].find('--') + 2:]):
            form.pushButton_8.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_8.setEnabled(False)
        flag = 8
def nine():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(1, 6):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_9.text()) == five_words[ind][five_words[ind].find('--') + 2:]):
            form.pushButton_9.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_9.setEnabled(False)
        flag = 9
def ten():
    global flag, result, my_dict, five_words, form, wrong_answers
    if flag in range(1, 6):
        w = str(my_dict[flag].text())
        ind = -1
        for i in range(len(five_words)):
            if (five_words[i].find(w) != -1):
                ind = i
                break
        if (str(form.pushButton_10.text()) == five_words[ind][five_words[ind].find('--') + 2:]):
            form.pushButton_10.setVisible(False)
            my_dict[flag].setVisible(False)
            result += 1
            if result == 5:
                QtGui.QMessageBox.information(form, "Result", "Amount of wrong answers: " + str(wrong_answers), QtGui.QMessageBox.Ok)
                func_for_file()
            flag = 0
        else:
            wrong_answers += 1
    else:
        if flag != 0:
            my_dict[flag].setEnabled(True)
        form.pushButton_10.setEnabled(False)
        flag = 10

app = QtGui.QApplication(sys.argv)
form = MyApp()
my_dict = {1: form.pushButton, 2: form.pushButton_2, 3: form.pushButton_3, 4: form.pushButton_4, 5: form.pushButton_5, 6: form.pushButton_6, 7: form.pushButton_7, 8: form.pushButton_8, 9: form.pushButton_9, 10: form.pushButton_10}
my_list = [1, one, two, three, four, five, six, seven, eight, nine, ten]
for i in range(1, 11): my_dict[i].clicked.connect(my_list[i])
list_of_words, five_words, flag, result, wrong_answers = [], [], 0, 0, 0
func_for_file()
sys.exit(app.exec_())