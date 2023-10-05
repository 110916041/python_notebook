from tkinter import *
from tkinter import filedialog
import tkinter.messagebox


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
        about_menu.add_command(label="作者")
        menu.add_cascade(label="編輯", menu=about_menu)

        status_srt_var = StringVar()
        status_srt_var.set('字數{}'.format(0))
        status_label = Label(self.root, textvariable=status_srt_var,
                             bd=1, relief=SUNKEN, anchor=W)
        status_label.pack(side=BOTTOM, fill=X)

        var_line = StringVar()
        line_label = Label(self.root, textvariable=var_line, width=1,
                           bg='#faebd7', anchor=N, font=18)
        line_label.pack(side=LEFT, fill=Y)

        self.text_pad = Text(self.root, font=18)
        self.text_pad.pack(fill=BOTH, expand=True)

        scroll = Scrollbar(self.text_pad)
        self.text_pad.config(yscrollcommand=scroll.set)
        scroll.config(command=self.text_pad.yview)
        scroll.pack(side=RIGHT, fill=Y)

        self.root.config(menu=menu)

    def cut(self):
        self.copy()
        self.text_pad.delete(SEL_FIRST, SEL_LAST)

    def copy(self):
        self.text_pad.clipboard_clear()
        copy_text = self.text_pad.get(SEL_FIRST, SEL_LAST)
        self.text_pad.clipboard_append(copy_text)

    def paste(self):
        copy_text = self.text_pad.selection_get(selection="CLIPBOARD")
        self.text_pad.insert(INSERT, copy_text)

    def open_file(self):
        global filename
        filename = filedialog.askopenfilename()
        if filename == "":
            return
        with open(filename, "r", encoding="utf-8") as fileobj:
            content = fileobj.read()
            self.text_pad.delete("1.0", END)
            self.text_pad.insert(END, content)
            self.root.title(filename)

    def save_file(self):
        global filename
        textcontent = self.text_pad.get("1.0", END)
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename == "":
            return
        with open(filename, "w", encoding="utf-8") as file:
            file.write(textcontent)
            self.root.title(filename)

    def new_file(self):
        self.text_pad.delete("1.0", END)
        self.root.title("Untitled")

    def clean(self):
        self.text_pad.delete("1.0", "end")

    def rightClick(self, event):
        self.edit_menu.post(event.x_root, event.y_root)
