import tkinter as tk
<<<<<<< HEAD
#from tkinter import ttk
from parts import TopFrame,MedianFrame


class Window(tk.Tk): #class裡面的self代表的都是我自己的實體，所有東西都放在Window裡面
    def __init__(self):
        super().__init__()  # super代表父類別
        topFrame = TopFrame(self, borderwidth=0)  # TopFrame子類別繼承LabelFrame父類別，用topFrame實體子容器去接，裡面有一個borderwidth，所以這裡可以用
        #print(topFrame.flowerPhoto1)
        topFrame.pack()  # topFrame裡面有attribute、property、method
        medianFrame=MedianFrame(self,borderwidth=0)
        medianFrame.pack(fill=tk.X)  # 讓radioButton的畫布靠左對齊
    
    # 建了這個window的實體method，使用者按了按鈕windows才會知道
    def radioButtonEvenOfMedianFrame(self, radioButtonValue):
        print(radioButtonValue) 



#實體在main裡面(主程式)
def main():
    window=Window()
    window.title('widgets')
    window.mainloop() #要讓主程式一直執行


=======
from tkinter import ttk

def main():
    pass
>>>>>>> 47e2d7aa5e418c8c27e5de4eb8f63807b17601b3
if __name__=='__main__':
    main()