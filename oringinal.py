import tkinter as tk


root = tk.Tk()
root.title("記事本")
root.geometry("800x600+200+200")
menu = tk.Menu(root, tearoff=False)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="新增檔案")
file_menu.add_command(label="開啟舊檔")
file_menu.add_command(label="儲存")
file_menu.add_command(label="另存新檔")
menu.add_cascade(label="檔案", menu=file_menu)

edit_menu = tk.Menu(menu, tearoff=False)
edit_menu.add_command(label="剪下")
edit_menu.add_command(label="清空")
edit_menu.add_command(label="複製")
edit_menu.add_command(label="貼上")
menu.add_cascade(label="編輯", menu=edit_menu)

about_menu = tk.Menu(menu, tearoff=False)
about_menu.add_command(label="關於")
menu.add_cascade(label="檢視", menu=about_menu)

status_srt_var = tk.StringVar()
status_srt_var.set('字數{}'.format(0))
status_label = tk.Label(root, textvariable=status_srt_var,
                        bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

var_line = tk.StringVar()
line_label = tk.Label(root, textvariable=var_line,
                      width=1, bg="#faebd7", anchor=tk.N, font=18)
line_label.pack(side=tk.LEFT, fill=tk.Y)

text_pad = tk.Text(root, font=18)
text_pad.pack(fill=tk.BOTH, expand=True)

scroll = tk.Scrollbar(text_pad)
text_pad.config(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)


root.config(menu=menu)
root.mainloop
