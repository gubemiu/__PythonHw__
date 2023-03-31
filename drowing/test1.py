
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):  # *args沒有限定數量的引數名稱呼叫，但這個引數沒多少所以*args也可以不用打，也可以打**kwargs(也可以不打)
        super().__init__(**kwargs)  # 同上(上面打**kwargs下面要跟著改)
        ttkStyle=ttk.Style()
        #print(ttkStyle.theme_usenames())  # 檢查有哪些theme，加了這行後面才能找到write.TLabelFrame
        ttkStyle.theme_use('default')
        ttkStyle.configure('write.TLabelframe',background='white',bd=0) #bd=0好像可以不用加結果也一樣
        ttkStyle.configure('write.TLabelframe.Label', background='white',foreground='red')#write.TLabelframe.Label=>f要小寫，後面要加.Label

        # 這是要用的字形
        f1 = tkFont.Font(family='Helvetica', size=16, weight='bold') 

        drawingFrame = ttk.LabelFrame(self,text="這裏是畫圖區",style='write.TLabelframe')
        drawingFrame.pack(padx=50,pady=50)


        lineCanvas = tk.Canvas(drawingFrame,width=100,height=30,bd=0,highlightthickness=0,background='white')
        lineCanvas.create_line((0,0),(100,0),width=30,fill='#deafc7') #座標是往下
        lineCanvas.pack()

        ovalCanvas = tk.Canvas(drawingFrame,width=110,height=110,bd=0,highlightthickness=0,background='white')
        ovalCanvas.create_oval((10, 10), (100, 100),width=10,outline='pink',fill='#afded7')
        ovalCanvas.pack()

        textCanvas=tk.Canvas(drawingFrame,width=110,height=50,bd=0,highlightthickness=0,background='white')
        textCanvas.create_text(0,0,text='ABC_中文',font=f1,fill='green',anchor='nw')  #anchor='nw'對齊左上角
        textCanvas.pack()

        #tk.Button(drawingFrame,text="Press Me",padx=10,pady=10).pack(padx=30,pady=20)  # Button放在drawingFrame裡面
        #ttk.Button(drawingFrame,text="Press Me",padding=(50,20)).pack(padx=30,pady=20) # 這樣寫也可以(因為ttk沒有支援padx和pady，但可以用padding；tk可以用padx和pady)；pack(padx=30,pady=20)是按鈕和外面那層的距離

        mapCanvas = tk.Canvas(drawingFrame,width=300,height=300,bd=0,highlightthickness=0,background='white')
        taiwanImage = Image.open("map.png")
        newImage = taiwanImage.resize((300, 300),Image.LANCZOS)
        self.taiwanImageTk = ImageTk.PhotoImage(newImage)
        mapCanvas.create_image(0,0,image=self.taiwanImageTk,anchor=tk.NW)
        mapCanvas.create_text(100,100,text="ABC_中文",font=tkFont.Font(family='Helvetica', size=12),anchor='nw')
        mapCanvas.pack()


def main():
    window = Window()    # 用window去接，控制 Window()這個class實體；ScreenName是Tk的副類別?(滑鼠移到Tk,右鍵,移至類型定義)
    window.title('畫圖')  # window.title(method)
    window.mainloop()


if __name__ == "__main__":
    main()

