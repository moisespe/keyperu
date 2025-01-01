import tkinter as tk
from tkinter import messagebox, Menu, filedialog, DISABLED, ttk

class Info:

    def __init__(self, root):
        self.root = root
        self.root.title('KeyPeru')
        self.root.resizable(False, False)
        self.root.geometry('240x100+1000+400')

        self.layout()
        
    def layout(self):
        lbtitle = tk.Label(self.root, text="KeyPeru v 0.1.0").place(x=75,y=0)
        #imglogo = tk.PhotoImage(file="./../assets/img/keylogo.jpg")
        #lbimg = tk.Label(self.root, image=imglogo).pack()


if __name__=='__main__':
    root = tk.Tk()
    app  = Info(root)
    root.mainloop()