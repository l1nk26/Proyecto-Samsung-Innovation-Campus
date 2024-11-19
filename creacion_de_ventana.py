import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
from tkinter import filedialog
#from PIL import ImageTk, Image

#Constantes
BACKGROUND = "#121212"
TEXT = "#84C9FB"


#Screens

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value="Normal")

        self.init_widgets()

    def move_to_game(self):
        self.controller.mode = self.gameMode.get()
        self.controller.show_frame(Usuario)


    def init_widgets(self):

        marco_principal = tk.Frame(self)
        #marco_principal.configure(bg=BACKGROUND)

        """ image = tk.PhotoImage(master=self,file="ponim_color.png",height=100,width=100)
        label_img = ttk.Label(self,image=image)
        label_img.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        ) """

        
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        button = ttk.Button(
            marco_principal, 
            text="Ingresar Datos Del Usuario", 
            command= self.move_to_game,
        )
        button.grid(row=1,column=1)

        button2 = ttk.Button(
            marco_principal, 
            text="Ingresar Varios Usuarios con CSV", 
            command=lambda : print("hacer algo")
        )
        button2.grid(row=2,column=1)

        button3 = ttk.Button(
            marco_principal, 
            text="Salir", 
            command=lambda : sys.exit()
        )
        button3.grid(row=3,column=1)


class Usuario(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="red")
        self.controller = controller
        self.init_widgets()

    def move_to_formulario(self):
        self.controller.show_frame(Formula)

    def move_to_dataPDF(self):
        self.controller.show_frame(DataPDF)

    def init_widgets(self):
        marco_principal = tk.Frame(self)
        marco_principal.configure(height=100,width=100)
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        ttk.Button(
            marco_principal, 
            text="Ingresar Datos Del Usuario", 
            command= self.move_to_formulario,
        ).pack(
            side=tk.RIGHT,
            #fill=tk.BOTH,
            expand=True,
        )

        ttk.Button(
            marco_principal, 
            text="Ingresar Examenes en PDF", 
            command=self.move_to_dataPDF,
        ).pack(
            side=tk.LEFT,
            #fill=tk.BOTH,
            expand=True,
        )


class Formula(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        marco_principal = tk.Frame(self)
        marco_principal.configure(height=100,width=100)
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        Label(marco_principal,text="essxee").pack()


class DataPDF(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller
        self.init_widgets()

    def get_file_path(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            print(f"Selected file path: {file_path}")
            # Puedes hacer algo con el path del archivo aquí
        else:
            print("No file selected")

    def init_widgets(self):
        marco_principal = tk.Frame(self)
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        button = tk.Button(marco_principal, text="Select PDF File", command=self.get_file_path)
        button.pack(pady=20)

class Resultados(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller
        self.init_widgets()

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Yo Nunca: The Game")
        conteiner = tk.Frame(self)
        self.mode = "Normal"
        conteiner.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
        )
        conteiner.configure(background= BACKGROUND)
        conteiner.grid_columnconfigure(0,weight=1)
        conteiner.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Usuario, Formula, DataPDF, Resultados):
            frame = F(conteiner, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky= tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


if __name__=="__main__":
    app = Manager()
    app.geometry("500x500")
    app.mainloop()