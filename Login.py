from tkinter import *
from tkinter.messagebox import *


class Login(object):
    def __init__(self, master=None):
        self.root = master  # 定義內部變量root
        self.root.geometry('%dx%d' % (300, 150))  # 設置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 創建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='帳號: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(
            row=1, column=1, stick=E)
        Label(self.page, text='密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password,
              show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登入', command=self.loginCheck).grid(
            row=3, stick=W, pady=10)
        Button(self.page, text='離開', command=self.page.quit).grid(
            row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        answer = self.password.get()
        if name == '1' and answer == '1':
            self.page.destroy()

        else:
            showinfo(title='錯誤', message='帳號密碼輸入錯誤！')
