import tkinter as tk
from tkinter import ttk

# 產生BMI計算器視窗


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('gdLabel.TLabel', font=(
            'Helvetica', '16'), foreground="#666666")
        ttkStyle.configure('gdEntry.TEntry', font=('Helvetica', '16'))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)
        ttk.Label(topFrame, text="BMI試算", font=(
            'Helvetica', '20')).pack(pady=20)

        self.bottomFrame = ttk.Frame(mainFrame)
        self.bottomFrame.pack(expand=True, fill=tk.BOTH)
        self.bottomFrame.columnconfigure(0, weight=3, pad=20)
        self.bottomFrame.columnconfigure(1, weight=5, pad=20)
        self.bottomFrame.rowconfigure(0, weight=1, pad=20)
        self.bottomFrame.rowconfigure(3, weight=1, pad=20)
        self.bottomFrame.rowconfigure(4, weight=1, pad=20)
        self.bottomFrame.rowconfigure(5, weight=1, pad=20)
        self.bottomFrame.rowconfigure(6, weight=1, pad=20)

        # 輸入區域
        ttk.Label(self.bottomFrame, text="姓名:", style='gdLabel.TLabel').grid(
            row=0, column=0, sticky=tk.E)
        self.nameEntry = ttk.Entry(self.bottomFrame, style='gdEntry.TEntry')
        self.nameEntry.grid(row=0, column=1, sticky=tk.W, padx=10)

        ttk.Label(self.bottomFrame, text="出生年月日:", style='gdLabel.TLabel').grid(
            row=1, column=0, sticky=tk.E)
        ttk.Label(self.bottomFrame, text="(2000/03/01)",style='gdLabel.TLabel').grid(row=2, column=0, sticky=tk.E)
        birthEntry = ttk.Entry(self.bottomFrame, style='gdEntry.TEntry')
        birthEntry.grid(row=1, column=1, sticky=tk.W, rowspan=2, padx=10)

        ttk.Label(self.bottomFrame, text="身高(cm):", style='gdLabel.TLabel').grid(
            row=3, column=0, sticky=tk.E)
        self.heightVar = tk.StringVar()
        self.heightEntry = ttk.Entry(
            self.bottomFrame, textvariable=self.heightVar, style="gdEntry.TEntry")
        self.heightEntry.grid(row=3, column=1, sticky=tk.W, padx=10)

        ttk.Label(self.bottomFrame, text="體重(kg):", style='gdLabel.TLabel').grid(
            row=4, column=0, sticky=tk.E)
        self.weightVar = tk.StringVar()
        self.weightEntry = ttk.Entry(
            self.bottomFrame, textvariable=self.weightVar, style="gdEntry.TEntry")
        self.weightEntry.grid(row=4, column=1, sticky=tk.W, padx=10)

        # 顯示計算結果的label
        self.messageText = tk.Text(
            self.bottomFrame, height=5, width=38, state=tk.DISABLED)
        self.messageText.grid(row=5, column=0, sticky=tk.N+tk.S, columnspan=2)

        # 計算按鈕
        comitButton = ttk.Button(
            self.bottomFrame, text="計算", command=self.Data_click)
        comitButton.grid(row=6, column=1, sticky=tk.W)

    # 計算BMI
    def cal_BMI(self, height, weight):
        bmi_value = round(float(weight)/(float(height)/100)**2, 2)
        if bmi_value < 18.5:  # 使用邏輯判斷
            message = '體重太輕'
        elif bmi_value < 24:
            message = '體重正常'
        elif bmi_value < 30:
            message = '體重過重'
        else:
            message = '體重異常'
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
        self.messageText.insert("insert", f"BMI:{bmi_value: .5f}, {message}")
        self.messageText.configure(state=tk.DISABLED)

    def Data_wrong(self, height, weight):
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
        # if not height.isdigit():
        if not self.is_number(height):
            self.messageText.insert("insert", f"身高:'{height}', 輸入錯誤\n")
            self.heightVar.set('')
        # if not weight.isdigit():
        if not self.is_number(weight):
            self.messageText.insert("insert", f"體重:'{weight}', 輸入錯誤\n")
            self.weightVar.set('')
        self.messageText.configure(state=tk.DISABLED)

    def is_number(self, string):
        try:
            float(string)
            return True
        except Exception:
            return False

    def Data_click(self):
        # if self.heightVar.get().isdigit() and self.weightVar.get().isdigit():
        if self.is_number(self.heightVar.get()) and self.is_number(self.weightVar.get()):
            self.cal_BMI(self.heightVar.get(), self.weightVar.get())
        else:
            self.Data_wrong(self.heightVar.get(), self.weightVar.get())


def main():
    window = Window()
    window.title('BMI計算')
    window.mainloop()


if __name__ == "__main__":
    main()
