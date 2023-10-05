import tkinter as tk
from itertools import count
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import time
from Login import *


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        # text_widget與其他widget相關聯
        self.textwidget = text_widget

    # 顯示行號用
    def redraw(self, *args):
        # 更新顯示行號
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)  # 回傳該行起始和結束
            if dline is None:  # 該行無值存在
                break
            y = dline[1]
            lineno = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=lineno)
            i = self.textwidget.index("%s+1line" % i)


class Textpad(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._action)

        self.find_word = StringVar()
        word = Frame()  # 創建Frame
        Label(word, text='查詢: ').grid(row=1, stick=W, pady=10)
        Entry(word, textvariable=self.find_word).grid(row=1, column=1, stick=W)
        Button(word, text='查詢', command=self.findword).grid(
            row=1, column=1, padx=150)
        word.pack(side=BOTTOM, fill=X)

        # 添加檔案欄位
        menu = tk.Menu(root, tearoff=False)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="新增檔案", command=self.new_file)
        file_menu.add_command(label="開啟舊檔", command=self.open_file)
        file_menu.add_command(label="儲存", command=self.save_file)
        file_menu.add_command(label="另存新檔", command=self.savenew_file)
        menu.add_cascade(label="檔案", menu=file_menu)

        # 添加編輯欄位
        self.edit_menu = tk.Menu(menu, tearoff=False)
        self.edit_menu.add_command(label="剪下", command=self.cut)
        self.edit_menu.add_command(label="清空", command=self.clean)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="複製", command=self.copy)
        self.edit_menu.add_command(label="貼上", command=self.paste)
        root.bind("<Button-3>", self.rightClick)
        menu.add_cascade(label="編輯", menu=self.edit_menu)

        # 添加檢視欄位
        about_menu = tk.Menu(menu, tearoff=False)
        about_menu.add_command(label="作者", command=self.writer)
        about_menu.add_command(label="時間", command=self.showtime)
        menu.add_cascade(label="檢視", menu=about_menu)
        # 配置上述三個欄位
        root.config(menu=menu)

    def _action(self, *args):
        # 執行請求的動作
        _command = (self._orig,) + args
        result = self.tk.call(_command)

        # 當進行插入或刪除文本或滾動時執行
        if (args[0] in ("insert", "replace", "delete") or
                    args[0:3] == ("mark", "set", "insert") or
                    args[0:2] == ("yview", "moveto") or
                    args[0:2] == ("yview", "scroll")
                ):
            self.event_generate("<<Change>>", when="tail")

        # 返回widget內容
        return result

    # 顯示日期
    def showtime(self):
        now = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", now)
        self.insert("insert", result)

    # 參考資料
    def writer(self):
        self.insert("insert", "\n作者： 哈哈是我啦")
        self.insert("insert", "\n參考資料： ")
        self.insert(
            "insert", "\nhttps://www.youtube.com/watch?v=Eo5got6NIQA ------框架")
        self.insert(
            "insert", "\nhttps://www.796t.com/content/1547705544.html ------tkinter介紹")
        self.insert(
            "insert", "\nhttp://kaiching.org/pydoing/index.html ------指令")

    # text剪下
    def cut(self):
        self.copy()
        self.delete(SEL_FIRST, SEL_LAST)

    # text複製
    def copy(self):
        self.clipboard_clear()
        copy_text = self.get(SEL_FIRST, SEL_LAST)
        self.clipboard_append(copy_text)

    # 檢測右鍵是否被點擊
    def rightClick(self, event):
        self.edit_menu.post(event.x_root, event.y_root)

    # text清除
    def clean(self):
        self.delete("1.0", "end")

    # text貼上
    def paste(self):
        copy_text = self.selection_get(selection="CLIPBOARD")
        self.insert(INSERT, copy_text)

    # 開啟舊檔
    def open_file(self):
        global filename
        filename = filedialog.askopenfilename()  # 存檔案位置
        if filename == "":
            return
        try:
            with open(filename, "r", encoding='UTF-8') as fileobj:
                content = fileobj.read()
        except FileNotFoundError:
            print("cannot open the file !")
        else:
            self.delete("1.0", END)
            self.insert(END, content)
            self.tk.title(filename)

    # 另存新檔
    def savenew_file(self):
        global filename  # 存儲檔案位置
        textcontent = self.get("1.0", END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename == "":
            return
        with open(filename, "w", encoding='UTF-8') as file:
            file.write(textcontent)
            self.tk.title(filename)

    # 新增檔案
    def new_file(self):
        global filename
        filename = " "
        self.delete("1.0", END)
        self.tk.title("Untitled")

    # 儲存
    def save_file(self):
        global filename  # 存儲檔案位置
        textcontent = self.get("1.0", END)
        if filename == "":
            filename = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(filename, "w", encoding='UTF-8') as file:
            file.write(textcontent)
            self.tk.title(filename)

    # 尋找目標單字在第幾行
    def place(self, _name, _all):
        len1 = len(_name)
        pl = []
        if _name == _all:
            pl.append(0)
        else:
            for each in range(len(_all)-len1):
                if _all[each:each+len1] == _name:       # 找出與子字符串首字符相同的字符位置
                    pl.append(each)
        return pl

    # 找尋是否有目摽字
    def findword(self):
        name = self.find_word.get()
        address = filename
        with open(address, encoding='UTF-8') as file:  # 打開文件
            for eachword in file:
                if name in eachword:  # 判斷改文件內是否有待查字符
                    break
                else:
                    continue
            file.seek(0, 0)  # 讓file從最一開始讀取
            count = 1  # 計算行數
            for all in file:
                if name in all:  # 查看該行是否有待查字符
                    pl = self.place(name, all)  # 執行place函式
                    showinfo(message='查詢的字在{0}行，第{1}個位置。'.format(
                        count, pl))  # 顯示所在位置
                    count += 1
                else:
                    count += 1


class Textbook(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = Textpad(self)

        # 定義下拉卷軸
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.linenumbers = TextLineNumbers(self, width=25)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)  # 發生自定義的事件：插入 刪除等等
        self.text.bind("<Configure>", self._on_change)  # 視窗產生大小變化

    def _on_change(self, event):
        self.linenumbers.redraw()


# 啟動函式
if __name__ == "__main__":
    root = tk.Tk()
    root.title("記事本")
    Login(root)
    Textbook(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
