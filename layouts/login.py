import tkinter as tk
from tkinter import messagebox, Menu, filedialog, DISABLED, ttk

class Login:

    def __init__(self, root):
        self.root = root
        self.root.title('KeyPeru')
        self.root.resizable(False, False)
        self.root.geometry('240x100+1000+400')

        self.layout()

    def layout(self):
        lbuser = tk.Label(self.root, text="Usuario").place(x=7,y=10)
        inuser = tk.Entry(self.root, width=20).place(x=80,y=10)
        #inuser.pack(pady=10)

        lbpwdr = tk.Label(self.root, text="Clave").place(x=7,y=35)
        inpwdr = tk.Entry(self.root, width=20, show="■").place(x=80,y=33)
        #inpwdr.pack(pady=13)

        btaccess = tk.Button(self.root, text="Acceder").place(x=80,y=60)
        btquit = tk.Button(self.root, text="Salir").place(x=140,y=60)




if __name__=='__main__':
    root = tk.Tk()
    app  = Login(root)
    root.mainloop()