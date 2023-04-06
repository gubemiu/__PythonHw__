import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class TopFrame(ttk.LabelFrame):  # LabelFrame父類別，TopFrame子類別，topFrame是子容器，class Window是父容器(寫在main.py裡面)
    def __init__(self, master, **kwargs):  # 這裡的**kwargs是參數
        # 定義的時候要有self，要知道放在誰裡面，父類別加上一個master(master是參數名稱可以自己定義)?
        super().__init__(master,**kwargs)  # 這裡的**kwargs是引數，ttk.LabelFrame要呼叫父類別至少要有一個參數(自取名為master)，所以要在上面定義也加master，是人家傳進來，要放在master裡面的意思
        ttkStyle=ttk.Style()
        ttkStyle.theme_use('default') #畫布變白了
        # ttkStyle change ttk.LabelFrame border width
        ttkStyle.configure('TLabelframe', borderwidth=0)

        # 建立圖片1(放在canvas畫布裡面)
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)  # self.flowerPhoto1=>self.就是attribute
        self.canvas = tk.Canvas(self, width=173, height=200)  # 畫布
        self.canvas.pack()
        self.canvas.create_image(0, 5, image=self.flowerPhoto1, anchor='nw') #image要小寫
        self.canvas.create_text(0, 200, text='Flower', fill='pink', font=('verdana', 36), anchor='sw') 

        #建立圖片2
        diamondImage1 = Image.open("./images/diamond.png")
        self.diamondPhoto1 = ImageTk.PhotoImage(diamondImage1)
        self.canvas.create_image(175, 5, image=self.diamondPhoto1, anchor='nw')  # 看圖片寬度去定義座標

        # 建立圖片3
        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        self.canvas.create_image(280, 5, image=self.atomPhoto1, anchor='nw')

        # created ttk.scrollbar of tkinter in canvas 建立拉bar
        self.scrollbar=ttk.Scrollbar(self,orient='horizontal',command=self.canvas.xview) #以canvas的xview為基準
        self.scrollbar.pack(side='bottom', fill='x')  # fill占滿(沒有高度直接占滿)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)  # 因為canvas建在上面，如果不想把這寫在上面要寫下面，要用configure
        self.canvas.configure(scrollregion=(0,0,500,200)) #scrollregion=> tuple (w, n, e, s) 西北東南，(0,0,500,200)代表=>對齊左,對齊上,往右寬,往下高


class MedianFrame(ttk.LabelFrame):
    def __init__(self, master, **kwargs):  # master代表main的window class
        super().__init__(master, **kwargs)

        # 建立單選按鈕 create ttk.radiobuttons in self
        # 建一個radioFrame放所有的radiobutton
        self.w = master  # 自己建一個self.w去給main的window實體用，把master給self.window，把master給self.w，才能在下面一個radioEvent那裏使用
        ttkStyle=ttk.Style()
        ttkStyle.theme_use('clam') #把按鈕改成圓的 ttk.Style change ttk.Radiobutton shape
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=10, pady=10)  # 讓radiobuttons靠左
        self.radioStringVar = tk.StringVar()  # 管理radiobuttons
        self.radiobutton1 = ttk.Radiobutton(radionFrame, text='Option 1', variable=self.radioStringVar,value='Option 01',command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(radionFrame, text='Option 2', variable=self.radioStringVar,value='Option 02',command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(radionFrame, text='Option 3', variable=self.radioStringVar,value='Option 03',command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(radionFrame, text='Option 4', variable=self.radioStringVar,value='Option 04',command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set('Option 01')  # 用set設定預設值   

        # 建立多選按鈕 create ttk.checkbuttons in self
        checkFrames = ttk.LabelFrame(self, text='Check Buttons')
        checkFrames.pack(side=tk.RIGHT, padx=10, pady=10)  # 讓radiobuttons靠左
        self.checkStringVar1 = tk.StringVar()  # 管理radiobuttons
        self.checkStringVar2 = tk.StringVar()
        self.checkStringVar3 = tk.StringVar()
        self.checkStringVar4 = tk.StringVar()
        self.checkbutton1 = ttk.Checkbutton(checkFrames, text='Option 1', variable=self.checkStringVar1, command=self.checkEvent, onvalue='Opcheck01', offvalue='Opoff01')
        self.checkbutton1.pack()  # onvalue是點選回傳的值，offvalue是取消點選回傳的值
        self.checkbutton2 = ttk.Checkbutton(checkFrames, text='Option 2', variable=self.checkStringVar2, command=self.checkEvent,onvalue='Opcheck02', offvalue='Opoff02')
        self.checkbutton2.pack()
        self.checkbutton3 = ttk.Checkbutton(checkFrames, text='Option 3', variable=self.checkStringVar3, command=self.checkEvent,onvalue='Opcheck03', offvalue='Opoff03')
        self.checkbutton3.pack()
        self.checkbutton4 = ttk.Checkbutton(checkFrames, text='Option 4', variable=self.checkStringVar4, command=self.checkEvent,onvalue='Opcheck04', offvalue='Opoff03')
        self.checkbutton4.pack()

    # create even of ttk.radionbuttons=>點過哪個值後臺可以得知(後改成把點選給值事件傳到main.py的window class執行)
    def radioEvent(self):
        self.w.radioButtonEvenOfMedianFrame(self.radioStringVar.get()) #改成把點選給值事件傳到main.py的window class執行
        #print(self.radioStringVar.get()) 
    
    def checkEvent(self):
        print(self.checkStringVar1.get())
        print(self.checkStringVar2.get())
        print(self.checkStringVar3.get())
        print(self.checkStringVar4.get())
        #self.w.radioButtonEvenOfMedianFrame(self.radioStringVar.get())
        








