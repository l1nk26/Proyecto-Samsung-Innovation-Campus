import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
from tkinter import filedialog
#from PIL import ImageTk, Image

import pdf_read


#Constantes
BACKGROUND = "#121212"
BG_SECOND = "#dcdcdc"
BG_TEXTINPUT = "#dadada"
TEXT = "#84C9FB"


#si tiene -1 no se, significa que no hay dato
DATA_USUARIO = {
    "glucosa": -1,
    "glucosa basal": -1,
    "glucosa postprandial": -1,
    "hemoglobina glicosilada": -1,
    "nombreCompleto" : "",
    "edad" : -1,
    "familia" : False,
    "peso" : -1,
    "orinaMucho" : False,
    "muchaSed" : False,
    "doleresCabeza": False,
}


#Screens
#ventana Home
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


        button3 = ttk.Button(
            marco_principal, 
            text="Salir", 
            command=lambda : sys.exit()
        )
        button3.grid(row=2,column=1)

#ventana de para dar la opcion de datos por pdf o por formulario
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

    def move_to_back_home(self):
        self.controller.show_frame(Home)

    def init_widgets(self):

        header = tk.Frame(self)
        header.configure(height=100)
        header.pack(
            side=tk.TOP,
            fill=tk.X,
        )
        ttk.Button(
            header,
            text="<=",
            command=self.move_to_back_home,
        ).pack(
            side=tk.LEFT,
        )


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

#ventana con todo el formulario 
class Formula(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller

        #variables
        self.data = {
            "glucosa": tk.IntVar(self, value=-1),
            "glucosa basal": tk.IntVar(self, value=-1),
            "glucosa postprandial": tk.IntVar(self, value=-1),
            "hemoglobina glicosilada": tk.IntVar(self, value=-1),
            "nombreCompleto" : tk.StringVar(self, value=""),
            "edad" : tk.IntVar(self, value=-1),
            "familia" : tk.BooleanVar(self, value=False),
            "peso" : tk.IntVar(self, value=-1),
            "orinaMucho" : tk.BooleanVar(self, value=False),
            "muchaSed" : tk.BooleanVar(self, value=False),
            "doleresCabeza": tk.BooleanVar(self, value=False),
        }

        self.init_widgets()

    def move_to_back_home(self):
        self.controller.show_frame(Usuario)

    def mostrar_data(self):
        for i, v in self.data.items():
            print(i,v.get())

    def init_widgets(self):

        header = tk.Frame(self)
        header.configure(height=100)
        header.pack(
            side=tk.TOP,
            fill=tk.X,
        )
        ttk.Button(
            header,
            text="<=",
            command=self.move_to_back_home,
        ).pack(
            side=tk.LEFT,
        )

        nombre_div = tk.Frame(self)
        nombre_div.configure(bg=BG_SECOND)
        nombre_div.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=30,
            pady=10,
        )

        ttk.Label(
            nombre_div, 
            text="Nombre Completo",
            background=BG_SECOND
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )

        tk.Entry(
            nombre_div,
            bg=BG_TEXTINPUT,
            justify="center",
            textvariable=self.data["nombreCompleto"],
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )


        edad_div = tk.Frame(self)
        edad_div.configure(bg=BG_SECOND)
        edad_div.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=30,
            pady=10,
        )

        ttk.Label(
            edad_div, 
            text="Edad",
            background=BG_SECOND
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )

        tk.Entry(
            edad_div,
            bg=BG_TEXTINPUT,
            justify="center",
            textvariable=self.data["edad"],
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )

        pregunta_glucosa_div = tk.Frame(self)
        pregunta_glucosa_div.configure(bg=BG_SECOND)
        pregunta_glucosa_div.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=30,
            pady=10,
        )

        ttk.Label(
            pregunta_glucosa_div, 
            text="¿Sabes tu valor de normal de glucosa en la sangren?",
            background=BG_SECOND
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )

        tk.Entry(
            pregunta_glucosa_div,
            bg=BG_TEXTINPUT,
            justify="center",
            textvariable=self.data["glucosa"],
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=20,
            pady=10,
        )


        ttk.Button(self, text="aa", command=self.mostrar_data).pack()


        
        

#ventana que pide el archivo .pdf
class DataPDF(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller
        self.init_widgets()

    def move_to_resul(self):
        self.controller.show_frame(Resultados)

    def get_file_path(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            print(f"Selected file path: {file_path}")
            # Puedes hacer algo con el path del archivo aquí
            print(pdf_read.pdf_read(file_path))
            self.move_to_resul()

        else:
            print("No file selected")

    def move_to_back_home(self):
        self.controller.show_frame(Usuario)

    def init_widgets(self):

        header = tk.Frame(self)
        header.configure(height=100)
        header.pack(
            side=tk.TOP,
            fill=tk.X,
        )
        ttk.Button(
            header,
            text="<=",
            command=self.move_to_back_home,
        ).pack(
            side=tk.LEFT,
        )


        marco_principal = tk.Frame(self)
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        button = tk.Button(marco_principal, text="Select PDF File", command=self.get_file_path)
        button.pack(pady=20)

#ventana que mostrara los resultados 
class Resultados(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure()
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        marco_principal = tk.Frame(self)
        marco_principal.configure(bg="#2611d5")
        marco_principal.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

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


def init():
    app = Manager()
    app.geometry("500x500")
    app.mainloop()