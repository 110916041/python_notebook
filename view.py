from tkinter import *
from tkinter.messagebox import *


class InputFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='藥品名稱: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text='進價 /元: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(
            row=2, column=1, stick=E)
        Label(self, text='售價 /元: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text='優惠 /元: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(
            row=4, column=1, stick=E)
        Button(self, text='錄入').grid(row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變量root
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查詢界面').pack()


class CountFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變量root
        self.createPage()

    def createPage(self):
        Label(self, text='統計界面').pack()


class AboutFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變量root
        self.createPage()

    def createPage(self):
        Label(self, text='關於界面').pack()
