from tkinter import *

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("图形化转换界面")           #窗口名
        self.init_window_name.geometry('1068x681+10+10')
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)

        self.init_data_Text = Text(self.init_window_name, width=65, height=14)  #待处理数据
        self.init_data_Text.grid(row=1, column=0, rowspan=1, columnspan=10)



        self.txt_mess = Label(self.init_window_name, text="txt文件信息")
        self.txt_mess.grid(row=2, column=0)
        self.txt_mess = Text(self.init_window_name, width=65, height=14)  # txt统计图展示
        self.txt_mess.grid(row=3, column=0, columnspan=10)



        self.log_label = Label(self.init_window_name, text="txt统计图展示")
        self.log_label.grid(row=4, column=0)
        self.log_data_Text = Text(self.init_window_name, width=65, height=14)  # txt统计图展示
        self.log_data_Text.grid(row=5, column=0, columnspan=10)


        self.result_data_label = Label(self.init_window_name, text="txt数据")
        self.result_data_label.grid(row=0, column=20)
        self.result_data_Text = Text(self.init_window_name, width=65, height=47)  #txt数据
        self.result_data_Text.grid(row=1, column=20, rowspan=15, columnspan=10)


        #button = ttk.Button(win, text="Hello World!", command=ButtonClick)  # 创建一个 button 按钮
        #按钮
        self.button_open_txt = Button(self.init_window_name,text="打开文件",bg="lightblue", width=10)
        self.button_open_txt.grid(row=1, column=11)
        self.button_open_label = Button(self.init_window_name,text="生成标签",bg="lightblue", width=10)
        self.button_open_label.grid(row=2, column=11)
        self.button_open_data = Button(self.init_window_name,text="数据展示",bg="lightblue", width=10)
        self.button_open_data.grid(row=3, column=11)

        self.button_open_message = Button(self.init_window_name,text="文件信息编辑",bg="lightblue", width=10)
        self.button_open_message.grid(row=4, column=11)
        self.button_open_label = Button(self.init_window_name,text="清除",bg="lightblue", width=10)
        self.button_open_label.grid(row=5, column=11)

    # def do_something(self1):
    #     self1.init_window_name.title("图形化转换界面2")  # 窗口名
    #     self1.init_window_name.geometry('1068x681+10+10')



def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()