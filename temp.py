from itertools import count
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *


class notebook(object):
    def __init__(self, master=None):
        self.root = master
        self.root.title("記事本")
        self.root.geometry("800x500+200+200")
        menu = Menu(self.root, tearoff=False)

        file_menu = Menu(menu, tearoff=False)
        file_menu.add_command(label="新增檔案", command=self.new_file)
        file_menu.add_command(label="開啟舊檔", command=self.open_file)
        file_menu.add_command(label="儲存")
        file_menu.add_command(label="另存新檔", command=self.save_file)
        menu.add_cascade(label="檔案", menu=file_menu)

        self.edit_menu = Menu(menu, tearoff=False)
        self.edit_menu.add_command(label="剪下", command=self.cut)
        self.edit_menu.add_command(label="清空", command=self.clean)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="複製", command=self.copy)
        self.edit_menu.add_command(label="貼上", command=self.paste)
        self.root.bind("<Button-3>", self.rightClick)
        menu.add_cascade(label="編輯", menu=self.edit_menu)

        about_menu = Menu(menu, tearoff=False)
        about_menu.add_command(label="作者", command=self.writer)
        menu.add_cascade(label="編輯", menu=about_menu)

        # status_srt_var1 = StringVar()
        # status_srt_var1.set('字數{}'.format(0))
        # status_label = Label(self.root, textvariable=status_srt_var1,
        #                     bd=1, relief=SUNKEN, anchor=W)
        # status_label.pack(side=BOTTOM, fill=X)

        # 記事本尋找單字
        self.find_word = StringVar()
        word = Frame(self.root)  # 創建Frame
        Label(word, text='查詢: ').grid(row=1, stick=W, pady=10)
        Entry(word, textvariable=self.find_word).grid(
            row=1, column=1, stick=W)
        Button(word, text='查詢', command=self.wordfind).grid(
            row=1, column=1, padx=150)
        word.pack(side=BOTTOM, fill=X)

        # 顯示行數
        var_line = StringVar()
        line_label = Label(self.root, textvariable=var_line, width=1,
                           bg='#faebd7', anchor=N, font=18)
        line_label.pack(side=LEFT, fill=Y)

        # 打字框
        self.text_pad = Text(self.root, font=18)
        self.text_pad.pack(fill=BOTH, expand=True)
        self.scrollbar()

        #

        self.root.config(menu=menu)

    # 下拉卷軸

    def scrollbar(self):
        scroll = Scrollbar(self.text_pad)
        self.text_pad.config(yscrollcommand=scroll.set)
        scroll.config(command=self.text_pad.yview)
        scroll.pack(side=RIGHT, fill=Y)
    # 剪下

    def cut(self):
        self.copy()
        self.text_pad.delete(SEL_FIRST, SEL_LAST)
    # 複製

    def copy(self):
        self.text_pad.clipboard_clear()
        copy_text = self.text_pad.get(SEL_FIRST, SEL_LAST)
        self.text_pad.clipboard_append(copy_text)
    # 貼上

    def paste(self):
        copy_text = self.text_pad.selection_get(selection="CLIPBOARD")
        self.text_pad.insert(INSERT, copy_text)
    # 打開檔案

    def open_file(self):
        global filename
        filename = filedialog.askopenfilename()
        if filename == "":
            return
        try:
            with open(filename, "r", encoding="utf-8") as fileobj:
                content = fileobj.read()
        except FileNotFoundError:
            print("cannot open the file !")
        else:
            self.text_pad.delete("1.0", END)
            self.text_pad.insert(END, content)
            self.root.title(filename)
    # 另存新檔

    def save_file(self):
        global filename
        textcontent = self.text_pad.get("1.0", END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename == "":
            return
        with open(filename, "w", encoding="utf-8") as file:
            file.write(textcontent)
            self.root.title(filename)
    # 新增檔案

    def new_file(self):
        self.text_pad.delete("1.0", END)
        self.root.title("Untitled")
    # 清除畫面

    def clean(self):
        self.text_pad.delete("1.0", "end")
    # 右鍵點擊

    def rightClick(self, event):
        self.edit_menu.post(event.x_root, event.y_root)

    def writer(self):
        self.text_pad.insert("insert", "作者： 許証曜")
        self.text_pad.insert("insert", "\n參考資料： ")
        self.text_pad.insert(
            "insert", "\nhttps://www.youtube.com/watch?v=Eo5got6NIQA")
        self.text_pad.insert(
            "insert", "\nhttps://www.796t.com/content/1547705544.html")
        self.text_pad.insert(
            "insert", "\nhttps://blog.csdn.net/RCHT1_Hideonbush/article/details/120402834")

    def wordfind(self):
        word = self.find_word.get()
        _text = self.text_pad.get("1.0", END)
        for everyword in _text:
            if word in everyword:
                showinfo(message='找到關鍵字【{0}】'.format(word))
                break
            else:
                continue
        count = 1
        for i in _text:
            if word in i:
                temp = self.place(word, i)
                showinfo(message='關鍵字出現在{0}行，第{1}個位置。'.format(count, temp))
                count += 1
            else:
                count += 1

    def place(self, zi, mu):
        # 查詢子字符串在大字符串中的所有位置
        self.len1 = len(zi)
        pl = []
        if zi == mu:
            pl.append(0)
        else:
            for each in range(len(mu)-self.len1):
                if mu[each:each+self.len1] == zi:       # 找出與子字符串首字符相同的字符位置
                    pl.append(each)
        return pl
