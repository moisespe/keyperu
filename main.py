import tkinter as tk
from tkinter import messagebox, Menu, filedialog, DISABLED, ttk
from datetime import datetime

from operations import Operation


class WindowMain:

    def __init__(self, root):
        self.root = root
        self.root.title('KeyPeru')
        self.root.resizable(False, False)
        self.root.geometry('350x500+1000+400')

        self.create_menu()
        self.layout()
        
        

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu, bg="#fff")

        archive_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Archivo', menu=archive_menu)
        archive_menu.add_cascade(label='Archive 1')
        archive_menu.add_cascade(label='Archive 2')
        archive_menu.add_cascade(label='Archive 3')

        tool_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Herramientas', menu=tool_menu)
        tool_menu.add_cascade(label='Tool 1')
        tool_menu.add_cascade(label='Tool 2')
        tool_menu.add_cascade(label='Tool 3')

        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Ayuda', menu=help_menu)
        help_menu.add_cascade(label='Ayuda 1')
        help_menu.add_cascade(label='Ayuda 2')
        help_menu.add_cascade(label='info', command=lambda:self.info())


    def get_datatime(self):
        now = datetime.now()
        fh = now.strftime("%Y-%m-%d %H:%M:%S")
        return fh        



    def push_genky(self):
        self.code_entry.delete(0, tk.END)

        ops = Operation()
        key = str(ops.generator_pw()) 
        self.code_entry.insert(0, key)
        


    def save_data(self):
        name = self.inname_entry.get()
        code = self.code_entry.get()
        desc = self.indesc_entry.get()
        url = self.inurl.get()
        now = self.get_datatime()

        if code != "" and code != "###########" :
            data = []
            data.append(name)
            data.append(code)
            data.append(desc)
            data.append(url)
            data.append(now)
            self.datalist.insert("", tk.END, values=(name, url, now))
            print(data)
        else:
            messagebox.showwarning("Advertencia", "No se ingresaron datos")

    def info(self):
                messagebox.showinfo("Keyperu v0.0.1", "Gracias por usar mi version gratuita para aumentar tu seguridad, recuerda que puedes revisar el codigo fuente https://github.com/moisespe/keyperu.")




    def layout(self):

        lbname = tk.Label(self.root, text="Name", bg="#fff").place(x=10, y=20)                                                                                                                                                                      
        self.inname_entry = tk.Entry(self.root, width=30)
        self.inname_entry.place(x=94, y=20)

        lbdesc = tk.Label(self.root, text="Description", bg="#fff").place(x=10, y=40)
        self.indesc_entry = tk.Entry(self.root, width=30)
        self.indesc_entry.place(x=94, y=40)

        lburl = tk.Label(self.root, text="Dominio", bg="#fff").place(x=10, y=60)
        self.inurl = tk.Entry(self.root, width=30)
        self.inurl.place(x=94, y=60)

        self.code = tk.Label(self.root, text="Code", bg="#fff").place(x= 10, y= 80)
        self.code_entry = tk.Entry(self.root, justify='center', width=38, font=("Arial 7"))
        self.code_entry.insert(0, "###########")
        self.code_entry.place(x=94, y=85)

        bt_gencode = tk.Button(self.root, text="Generar", command=lambda:self.push_genky(), width=7).place(x=275, y=83)
        btnadd = tk.Button(self.root, text="Agregar", command=lambda:self.save_data(), width=20).place(x=94, y=120)

        # data
        self.datalist = ttk.Treeview()
        self.datalist['columns'] = ('name', 'desc', 'email')

        #configurando columnas
        self.datalist.column("#0", width=0, minwidth=0) #quitando inicial
        self.datalist.column("name", width=100, minwidth=20)
        self.datalist.column("desc", width=120, minwidth=20)
        self.datalist.column("email", width=120, minwidth=20)

        #configurando cabeceras
        self.datalist.heading("#0", text="Main Col", anchor=tk.CENTER)
        self.datalist.heading("name", text="Nombre", anchor=tk.CENTER)
        self.datalist.heading("desc", text="Dominio", anchor=tk.CENTER)
        self.datalist.heading("email", text="Fecha", anchor=tk.CENTER)

        
        #Insertando data muestra
        #self.datalist.insert("", tk.END, values=("Dato 1", "Dato 2", "Dato 3"))


        self.datalist.place(x=5,y=170)


        btnsave = tk.Button(self.root, text="Guardar", command=lambda:self.save_data(), width=20).place(x=85, y=420)



if __name__ == "__main__":
    root = tk.Tk()
    app  = WindowMain(root)
    root.mainloop()


#window = tk.Tk()
#window.title('KeyPeru')
#window.geometry('350x500')
#window.mainloop()