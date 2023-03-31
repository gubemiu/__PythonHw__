import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tools import Taiwan_AQI

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        aqi_data = Taiwan_AQI()  # 這是__init__，Taiwan_AQI()是建立AQI的實體，會傳出實體，用aqi_data接
        mainFrame = ttk.Frame(self)  
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)  # topFrame放在mainFrame裡面
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="台灣即時AQI資訊", font=('Helvetica', '20')).pack(pady=(20, 20))
        
        buttomFrame = ttk.Frame(mainFrame)
        buttomFrame.pack(expand=True, fill=tk.BOTH)

        self.messageText = tk.Text(buttomFrame, height=15, width=35, state=tk.DISABLED, takefocus=0, bd=0)
        self.messageText.pack()
        bad5=aqi_data.get_bad(n=5)
        good5=aqi_data.get_better(n=5)
        message=''
        message += '目前AQI最好的5個站點\n'
        for item in good5:
            siteString = f'{item.site_name},{item.county},aqi={item.aqi}\n'
            message += siteString
        message +='==============================\n'
        message += '\n目前AQI最差的5個站點\n'
        for item in bad5:
            siteString = f'{item.site_name},{item.county},aqi={item.aqi}\n'
            message += siteString

        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete("1.0", tk.END)
        self.messageText.insert(tk.END, message)
        self.messageText.configure(state=tk.DISABLED)

        bad5 = aqi_data.get_bad(n=5)  # get_bad_3()傳出list，裡面有n筆
        for item in bad5:
            print(item)

        good5 = aqi_data.get_better(n=5) #如果()會預設取出3個
        for item in good5:
            print(item)


def main():
    window = Window()    
    window.title('畫圖')  
    window.mainloop()


if __name__ == "__main__":
    main()
