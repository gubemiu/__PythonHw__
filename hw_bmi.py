

import tkinter as tk
from tkinter import ttk
import re
from PIL import Image, ImageTk
from datetime import datetime


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('gridLabel.TLabel', font=('Helvetica', 16), foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry', font=('Helvetica', 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="BMI試算", font=('Helvetica', '20')).pack(pady=(80, 20))

        buttomFrame = ttk.Frame(mainFrame)
        buttomFrame.pack(expand=True, fill=tk.BOTH)
        buttomFrame.columnconfigure(0, weight=3, pad=20)
        buttomFrame.columnconfigure(1, weight=5, pad=20)
        buttomFrame.rowconfigure(0, weight=1, pad=20)
        buttomFrame.rowconfigure(3, weight=1, pad=20)
        buttomFrame.rowconfigure(4, weight=1, pad=20)
        buttomFrame.rowconfigure(5, weight=1, pad=20)
        buttomFrame.rowconfigure(6, weight=1, pad=20)

        self.nameStringVar = tk.StringVar()
        self.birthStringVar = tk.StringVar()
        self.heightIntVar = tk.IntVar()
        self.weightIntVar = tk.IntVar()

        ttk.Label(buttomFrame, text="姓名:", style='gridLabel.TLabel').grid(
            column=0, row=0, sticky=tk.E)
        nameEntry = ttk.Entry(
            buttomFrame, style='gridEntry.TEntry', textvariable=self.nameStringVar)
        nameEntry.grid(column=1, row=0, sticky=tk.W, padx=10)

        ttk.Label(buttomFrame, text='出生年月日:', style='gridLabel.TLabel').grid(
            column=0, row=1, sticky=tk.E)
        ttk.Label(buttomFrame, text='(2000/03/01)',
                  style='gridLabel.TLabel').grid(column=0, row=2, sticky=tk.E)
        birthEntry = ttk.Entry(
            buttomFrame, style='gridEntry.TEntry', textvariable=self.birthStringVar)
        birthEntry.grid(column=1, row=1, sticky=tk.W, padx=10, rowspan=2)

        ttk.Label(buttomFrame, text='身高(cm):', style='gridLabel.TLabel').grid(
            column=0, row=3, sticky=tk.E)
        heightEntry = ttk.Entry(
            buttomFrame, style='gridEntry.TEntry', textvariable=self.heightIntVar)
        heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)

        ttk.Label(buttomFrame, text='體重(kg):', style='gridLabel.TLabel').grid(
            column=0, row=4, sticky=tk.E)
        weightEntry = ttk.Entry(
            buttomFrame, style='gridEntry.TEntry', textvariable=self.weightIntVar)
        weightEntry.grid(column=1, row=4, sticky=tk.W, padx=10)

        self.messageText = tk.Text(
            buttomFrame, height=5, width=35, state=tk.DISABLED, takefocus=0, bd=0)
        self.messageText.grid(column=0, row=5, sticky=tk.N+tk.S, columnspan=2)

        # --------------commitFrame開始(有左右兩個按鈕)------------------------

        commitFrame = ttk.Frame(buttomFrame)
        commitFrame.grid(column=0, row=6, columnspan=2)
        commitFrame.columnconfigure(0, pad=10)

        commitBtn = ttk.Button(commitFrame, text="計算", command=self.check_data)
        commitBtn.grid(column=0, row=0, sticky=tk.W)

        ClearBtn = ttk.Button(commitFrame, text="清除", command=self.press_clear)
        ClearBtn.grid(column=1, row=0, sticky=tk.E)

        # --------------commitFrame結束---------------------------------------

        # --------------插入Logo---------------------------------------
        logoImage = Image.open('logo1.png')
        resizeImage = logoImage.resize((99, 108), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(self, image=self.logoTkimage, width=180)
        logoLabel.place(x=33, y=48)

    # 清除鈕
    def press_clear(self) -> None:
        self.nameStringVar.set('')
        self.birthStringVar.set('')
        self.heightIntVar.set(0)
        self.weightIntVar.set(0)
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
        self.messageText.configure(state=tk.DISABLED)
        print('清除')

    # bmi說明
    def BMI_Msg(self, bmi) -> None:
        if bmi < 18.5:
            bmimsg = '體重太輕'
        elif bmi < 24:
            bmimsg = '體重正常'
        elif bmi < 30:
            bmimsg = '體重過重'
        else:
            bmimsg = '體重異常'
        return bmimsg

    # 計算年齡

    def Age(self, birthValue):
        date_now = datetime.now()
        date_birth = datetime.strptime(birthValue, '%Y/%m/%d')
        age = date_now.year-date_birth.year -((date_now.month, date_now.day) <(date_birth.month, date_birth.day))  # 依據月日判斷是否+1歲
        return age

    # 判斷星座

    def get_zodiac(self,birthValue):
        month, day = int(birthValue[5:7]), int(birthValue[8:10])
        if month == 12:
            zodiac = '射手座' if (day < 22) else '摩羯座'
        elif month == 1:
            zodiac = '摩羯座' if (day < 20) else '水瓶座'
        elif month == 2:
            zodiac = '水瓶座' if (day < 19) else '雙魚座'
        elif month == 3:
            zodiac = '雙魚座' if (day < 21) else '白羊座'
        elif month == 4:
            zodiac = '白羊座' if (day < 20) else '金牛座'
        elif month == 5:
            zodiac = '金牛座' if (day < 21) else '雙子座'
        elif month == 6:
            zodiac = '雙子座' if (day < 21) else '巨蟹座'
        elif month == 7:
            zodiac = '巨蟹座' if (day < 23) else '獅子座'
        elif month == 8:
            zodiac = '獅子座' if (day < 23) else '處女座'
        elif month == 9:
            zodiac = '處女座' if (day < 23) else '天秤座'
        elif month == 10:
            zodiac = '天秤座' if (day < 23) else '天蠍座'
        elif month == 11:
            zodiac = '天蠍座' if (day < 22) else '射手座'
        return zodiac

    # 檢查資料
    def check_data(self) -> None:
        # r'^\d\d\d\d/\d\d/\d\d$'是固定寫法，日期格式"正規則寫法"
        dateRegex = re.compile(r"^\d\d\d\d/\d\d/\d\d$")
        nameValue = self.nameStringVar.get()
        birthValue = self.birthStringVar.get()
        birthMatch = re.match(dateRegex, birthValue)

        if birthMatch is None:
            birthValue = ""

        try:
            heightValue = self.heightIntVar.get()
        except:
            heightValue = 0

        try:
            weightValue = self.weightIntVar.get()
        except:
            weightValue = 0

        if nameValue == "" or birthValue == "" or heightValue == 0 or weightValue == 0:
            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0", tk.END)
            self.messageText.insert(tk.END, "有欄位沒填或格式不正確")
            self.messageText.configure(state=tk.DISABLED)

        else:
            bmi = weightValue / (heightValue / 100) ** 2
            bmimsg = self.BMI_Msg(bmi)
            age1 = self.Age(birthValue)
            zodiac1 = self.get_zodiac(birthValue)

            message = f"{nameValue}您好:\n"
            message += f"出生年月日:{birthValue}\n"
            message += f'您的歲數:{age1}\n'
            message += f'您的星座:{zodiac1}\n'
            message += f"BMI值是:{bmi:.2f}\n"
            message += f"狀態是:{bmimsg}"

            self.messageText.configure(state=tk.NORMAL)
            self.messageText.delete("1.0", tk.END)
            self.messageText.insert(tk.END, message)
            self.messageText.configure(state=tk.DISABLED)


def close_window(w):
    w.destroy()


def main():
    '''
    function說明：這是主程式的執行點
    '''
    window = Window()
    window.title('BMI計算')
    window.resizable(width=False, height=False)
    window.protocol('WM_DELETE_WINDOW', lambda: close_window(window))
    window.mainloop()


if __name__ == "__main__":
    main()
